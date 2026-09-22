"""Teste ponta a ponta do simulado (Chromium via Playwright), em porta separada.

Para cada questão dos dois simulados (TI e Agente de Tributos): responde certo e confere
"Resposta Correta!", responde errado e confere o gabarito; falha se aparecer [object Object]
ou opção vazia.  Uso: python testar_simulado.py
"""
import json
import os
import subprocess
import sys
import time
import urllib.request

from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
PORTA = 5077


def esperar_servidor():
    for _ in range(50):
        try:
            urllib.request.urlopen(f'http://127.0.0.1:{PORTA}/api/questions', timeout=1)
            return
        except Exception:
            time.sleep(0.2)
    raise RuntimeError('servidor não subiu')


def main():
    srv = subprocess.Popen(
        [sys.executable, '-c',
         f"import app; app.app.run(port={PORTA}, debug=False)"],
        cwd=BASE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    ORIG = json.load(open(os.path.join(BASE, 'questions.json'), encoding='utf-8'))
    ORIG_POR_ID = {o['id']: o for o in ORIG}
    CARGO = {'ti': 'auditor_ti', 'general': 'agente'}
    vistos_embaralhadas = set()
    embaralhadas = set()
    falhas = []
    total = 0
    try:
        esperar_servidor()
        with sync_playwright() as p:
            nav = p.chromium.launch()
            page = nav.new_page()
            erros_js = []
            page.on('pageerror', lambda e: erros_js.append(str(e)))
            page.goto(f'http://127.0.0.1:{PORTA}/')
            page.wait_for_function('typeof allQuestions !== "undefined" && allQuestions.length > 0')

            for cat in ('ti', 'general'):
                for modo in ('certo', 'errado'):
                    page.evaluate(
                        f"quizCategory='{cat}'; quizSize='all'; quizOrder='sequence'; startSimulado('{cat}'); launchSimuladoWithConfig();")
                    n = page.evaluate('activeQuizQuestions.length')
                    esperado_n = sum(1 for o in ORIG if o.get('disponivel', True) and CARGO[cat] in o['cargos'])
                    if n != esperado_n:
                        falhas.append((cat, 'quantidade de questões', n, esperado_n))
                    for i in range(n):
                        q = page.evaluate('activeQuizQuestions[currentQuestionIdx]')
                        chaves = list(q['options'].keys())
                        orig = ORIG_POR_ID[q['id']]
                        if orig['options'][orig['correct']] != q['options'][q['correct']]:
                            falhas.append((cat, q['id'], 'gabarito remapeado não aponta para o texto certo'))
                        if q['id'] in vistos_embaralhadas or list(orig['options']) == chaves and orig['options'] != q['options']:
                            embaralhadas.add(q['id'])
                        if q.get('disponivel') is False:
                            falhas.append((cat, q['id'], 'item oculto apareceu no simulado'))
                        escolha = q['correct'] if modo == 'certo' else next(k for k in chaves if k != q['correct'])
                        textos = page.eval_on_selector_all('.quiz-option .option-text', 'els => els.map(e => e.textContent.trim())')
                        if len(textos) != len(chaves) or any(not t or 'object Object' in t for t in textos):
                            falhas.append((cat, q['id'], 'alternativas mal renderizadas', textos))
                        page.evaluate(f"selectQuizOption('{escolha}'); checkQuizAnswer();")
                        titulo = page.inner_text('#explanation-title')
                        esperado = 'Resposta Correta!' if modo == 'certo' else f"Gabarito: {q['correct']}"
                        if esperado not in titulo:
                            falhas.append((cat, q['id'], modo, titulo))
                        if page.locator(f"#opt-{q['correct']}.correct-answer").count() != 1:
                            falhas.append((cat, q['id'], 'card do gabarito não destacado'))
                        total += 1
                        page.evaluate('checkQuizAnswer()')  # próxima / finalizar
            nav.close()
        if erros_js:
            falhas.append(('js', 'erros de página', erros_js[:3]))
    finally:
        srv.terminate()

    print(f'respostas verificadas: {total}; questões com alternativas embaralhadas: {len(embaralhadas)}; falhas: {len(falhas)}')
    for f in falhas[:15]:
        print('  ', f)
    return 1 if falhas else 0


if __name__ == '__main__':
    sys.exit(main())
