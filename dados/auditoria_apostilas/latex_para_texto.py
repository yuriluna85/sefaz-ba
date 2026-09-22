"""Converte fórmulas em LaTeX ($...$) das apostilas em texto simples legível (o gerador de PDFs não interpreta LaTeX).

Protege o "R$" (reais), repara escapes corrompidos (tabulação + "imes" = \\times) e converte apenas os segmentos entre
cifrões. Uso: python latex_para_texto.py [--aplicar]   (sem argumentos, só mostra o antes e o depois)
"""
import json
import os
import re
import sys

APP = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARQ = os.path.join(APP, 'apostilas_conteudo.json')
PROT = '\u0001'

SIMBOLOS = [
    (r'\times', ' x '), (r'\cdot', ' x '), (r'\div', ' / '), (r'\leq', ' <= '), (r'\geq', ' >= '), (r'\le', ' <= '),
    (r'\ge', ' >= '), (r'\neq', ' != '), (r'\approx', ' ~ '), (r'\sim', ' ~ '), (r'\pm', ' +/- '), (r'\cup', ' U '),
    (r'\cap', ' inter '), (r'\emptyset', 'conjunto vazio'), (r'\rightarrow', ' -> '), (r'\to', ' -> '),
    (r'\sum', 'soma de '), (r'\sigma', 'sigma'), (r'\mu', 'mu'), (r'\lambda', 'lambda'), (r'\alpha', 'alfa'),
    (r'\beta', 'beta'), (r'\epsilon', 'epsilon'), (r'\chi', 'qui'), (r'\left', ''), (r'\right', ''),
]


def achar_grupo(s, i):
    """s[i] == '{'. Retorna (conteudo, indice_apos_fecha)."""
    nivel, j = 0, i
    while j < len(s):
        if s[j] == '{':
            nivel += 1
        elif s[j] == '}':
            nivel -= 1
            if nivel == 0:
                return s[i + 1:j], j + 1
        j += 1
    return s[i + 1:], len(s)


def simples(t):
    return re.fullmatch(r'[\w.,]+', t.strip()) is not None


def conv(s):
    # comandos com argumentos, de dentro para fora
    while True:
        m = re.search(r'\\(text|frac|binom|sqrt|bar)\b', s)
        if not m:
            break
        cmd, ini = m.group(1), m.end()
        # pular espaços
        while ini < len(s) and s[ini] == ' ':
            ini += 1
        if ini >= len(s) or s[ini] != '{':
            s = s[:m.start()] + s[m.end():]
            continue
        a, fim = achar_grupo(s, ini)
        if cmd == 'text':
            rep = a
        elif cmd == 'sqrt':
            rep = 'raiz(' + conv(a) + ')'
        elif cmd == 'bar':
            rep = conv(a) + ' barra'
        else:
            k = fim
            while k < len(s) and s[k] == ' ':
                k += 1
            b, fim2 = achar_grupo(s, k) if k < len(s) and s[k] == '{' else ('', fim)
            a2, b2 = conv(a), conv(b)
            if cmd == 'binom':
                rep = 'C(' + a2 + ', ' + b2 + ')'
            else:
                rep = (a2 if simples(a2) else '(' + a2 + ')') + ' / ' + (b2 if simples(b2) else '(' + b2 + ')')
            fim = fim2
        s = s[:m.start()] + rep + s[fim:]
    s = re.sub(r'\\sum_\{([^{}]*)\}\^\{([^{}]*)\}', lambda m: 'soma (' + m.group(1).replace('=', ' = ') + ' até ' + m.group(2) + ') de ', s)
    for cmd, rep in sorted(SIMBOLOS, key=lambda x: -len(x[0])):
        s = re.sub(re.escape(cmd) + r'(?![A-Za-z])', lambda _m, r=rep: r, s)
    s = s.replace('\\%', '%').replace('\\ ', ' ').replace('\\,', '').replace('\\;', ' ').replace('\\!', '')
    # subscritos e sobrescritos
    s = re.sub(r'_\{([^{}]*)\}', lambda m: '(' + m.group(1) + ')' if re.search(r'[ ,+\-/]', m.group(1)) else m.group(1), s)
    s = re.sub(r'(?<=[a-z]{3})_(\w)', '\u0002\\1', s)
    s = re.sub(r'_(\w)', r'\1', s)
    s = s.replace('\u0002', '_')
    s = re.sub(r'\^\{([^{}]*)\}', lambda m: '^(' + m.group(1) + ')' if re.search(r'[ ,+\-]', m.group(1)) else '^' + m.group(1), s)
    s = re.sub(r'(?<=\d)(sigma|mu|lambda|alfa|beta)', r' \1', s)
    s = s.replace('{', '').replace('}', '').replace('\\', '')
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def converter_texto(t):
    if not isinstance(t, str):
        return t
    t = t.replace('\t' + 'imes', '\\times')
    t = t.replace('R$', 'R' + PROT)
    if '$' in t:
        t = re.sub(r'\$([^$]+)\$', lambda m: conv(m.group(1)), t)
    return t.replace(PROT, '$')


def mapear(o, f):
    if isinstance(o, str):
        return f(o)
    if isinstance(o, list):
        return [mapear(x, f) for x in o]
    if isinstance(o, dict):
        return {k: mapear(x, f) for k, x in o.items()}
    return o


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    dados = json.load(open(ARQ, encoding='utf-8'))
    if '--aplicar' in sys.argv:
        novo = mapear(dados, converter_texto)
        json.dump(novo, open(ARQ, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        restos = sum(s.replace('R$', '').count('$') for s in _todas(novo))
        print('conversão aplicada; cifrões restantes (fora de R$):', restos)
        return
    n = 0
    for v in dados:
        for s in _todas(v):
            s2 = s.replace('\t' + 'imes', '\\times').replace('R$', 'R' + PROT)
            for m in re.finditer(r'\$([^$]+)\$', s2):
                n += 1
                print('%s | %s\n     => %s' % (v['filename'][10:24], m.group(1), conv(m.group(1))))
    print('segmentos:', n)


def _todas(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, list):
        for x in o:
            yield from _todas(x)
    elif isinstance(o, dict):
        for x in o.values():
            yield from _todas(x)


if __name__ == '__main__':
    main()
