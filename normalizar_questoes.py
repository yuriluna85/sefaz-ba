"""Normaliza questions.json para um esquema único e valida o resultado.

Esquema final: options = {"A": "...", ...} (Certo/Errado: {"C": "Certo", "E": "Errado"}),
correct sempre uma chave de options, option_explanations com as mesmas chaves.

Uso: python normalizar_questoes.py [--dry-run]
"""
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
ARQ = os.path.join(BASE, 'questions.json')

# Itens do TRF1 que são direito penal, não redes de computadores.
RECLASSIFICAR = {
    'q_trf1_fgv_tec_77': 'Direito Penal - Crimes contra a Administração Pública',
    'q_trf1_fgv_tec_80': 'Direito Penal - Abuso de Autoridade (Lei 13.869/2019)',
}

# Correções seguras de artefatos de OCR (sem regex genérico para não quebrar texto válido).
OCR = [
    (re.compile(r'\baf irm'), 'afirm'),
    (re.compile(r'\b(Lei|Decreto|LC|Lei Complementar) no (\d)'), r'\1 nº \2'),
    (re.compile(r'(\w) -(se|lo|la|los|las|lhe|lhes|me|te|nos)\b'), r'\1-\2'),
]


def limpar(txt):
    if not isinstance(txt, str):
        return txt
    for rx, sub in OCR:
        txt = rx.sub(sub, txt)
    return txt


def normalizar_opcoes(q):
    o = q['options']
    if isinstance(o, dict):
        return {k: limpar(v) for k, v in o.items()}
    if o and isinstance(o[0], dict):
        return {i['label']: limpar(i['text']) for i in o}
    return {'ABCDEFGH'[i]: limpar(t) for i, t in enumerate(o)}


def chave_dup(q):
    return re.sub(r'\s+', ' ', q['question']).strip().lower()


def validar(qs):
    erros = []
    ids = set()
    for q in qs:
        if q['id'] in ids:
            erros.append((q['id'], 'id duplicado'))
        ids.add(q['id'])
        o = q.get('options')
        if not isinstance(o, dict) or len(o) < 2:
            erros.append((q['id'], 'options fora do esquema'))
            continue
        if q.get('correct') not in o:
            erros.append((q['id'], 'correct não está em options'))
        oe = q.get('option_explanations')
        if oe is not None and set(oe) != set(o):
            erros.append((q['id'], 'option_explanations com chaves diferentes de options'))
        if not str(q.get('explanation', '')).strip():
            erros.append((q['id'], 'sem explicação'))
        if not str(q.get('question', '')).strip():
            erros.append((q['id'], 'enunciado vazio'))
        cg = q.get('cargos')
        if not isinstance(cg, list) or not set(cg) <= {'auditor_ti', 'agente'}:
            erros.append((q['id'], 'cargos ausente ou inválido'))
        if q.get('disponivel') is False and not q.get('motivo_indisponivel'):
            erros.append((q['id'], 'item oculto sem motivo_indisponivel'))
    vistos = {}
    for q in qs:
        k = chave_dup(q)
        if k in vistos:
            erros.append((q['id'], 'enunciado duplicado de ' + vistos[k]))
        vistos[k] = q['id']
    return erros


def main():
    dry = '--dry-run' in sys.argv
    with open(ARQ, encoding='utf-8') as f:
        qs = json.load(f)
    antes = len(qs)

    vistos = set()
    saida = []
    removidas = []
    for q in qs:
        k = chave_dup(q)
        if k in vistos:
            removidas.append(q['id'])
            continue
        vistos.add(k)
        q['options'] = normalizar_opcoes(q)
        q['question'] = limpar(q['question'])
        if isinstance(q.get('explanation'), str):
            q['explanation'] = limpar(q['explanation'])
        if isinstance(q.get('option_explanations'), dict):
            q['option_explanations'] = {k2: limpar(v) for k2, v in q['option_explanations'].items()}
        if q['id'] in RECLASSIFICAR:
            q['subject'] = RECLASSIFICAR[q['id']]
        saida.append(q)

    erros = validar(saida)
    print(f'questões: {antes} -> {len(saida)} ({len(removidas)} cópias exatas removidas)')
    print(f'erros de validação: {len(erros)}')
    for e in erros[:20]:
        print('  ', e)
    if erros:
        return 1
    if not dry:
        with open(ARQ, 'w', encoding='utf-8') as f:
            json.dump(saida, f, ensure_ascii=False, indent=2)
        print('questions.json gravado.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
