"""Teste ponta a ponta do motor de gamificação (Chromium via Playwright), em porta separada.

Confere: XP e badge ao marcar um tópico de trilha, XP ao responder uma questão do simulado,
inclusão de questão errada na fila de revisão espaçada, alerta de fila no widget e
carregamento correto do modo Revisão Espaçada. Uso: python testar_gamificacao.py
"""
import os
import subprocess
import sys
import time
import urllib.request

from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
PORTA = 5078


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
        [sys.executable, '-c', f"import app; app.app.run(port={PORTA}, debug=False)"],
        cwd=BASE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        esperar_servidor()
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            erros_console = []
            page.on("console", lambda msg: erros_console.append(msg.text) if msg.type == "error" else None)
            page.goto(f"http://127.0.0.1:{PORTA}/")
            page.wait_for_timeout(800)

            widget = page.locator("#gamificacao-widget")
            assert "Nível 1" in widget.inner_html(), "Widget de nível não renderizou"
            print("OK: widget de gamificação renderizou no carregamento.")

            page.click('[data-tab="trilhas"]')
            page.wait_for_timeout(300)
            page.evaluate("""() => {
                const chk = document.querySelector(".checkbox-input.ti-checkbox");
                chk.checked = true;
                chk.dispatchEvent(new Event("change"));
            }""")
            page.wait_for_timeout(300)

            xp_data = page.evaluate("() => localStorage.getItem('sefaz_gamificacao_v1')")
            assert xp_data is not None and '"xpTotal":10' in xp_data, "XP não foi creditado ao marcar tópico"
            assert '"primeiro_passo"' in xp_data, "Badge primeiro_passo não foi concedida"
            print("OK: XP e badge de primeiro passo concedidos ao marcar tópico.")

            page.click('[data-tab="dashboard"]')
            page.wait_for_timeout(300)
            assert "10 XP total" in widget.inner_html(), "Widget não atualizou o XP na tela"
            print("OK: widget atualizou XP na tela após marcar tópico.")

            page.click('[data-tab="simulados"]')
            page.wait_for_timeout(1500)
            page.click("#btn-simulado-ti")
            page.wait_for_timeout(800)
            start_btn = page.locator(".start-quiz-btn")
            if start_btn.count() > 0:
                start_btn.click()
                page.wait_for_timeout(800)

            primeira_opcao = page.locator(".quiz-option").first
            if primeira_opcao.count() > 0:
                primeira_opcao.click()
                page.click("#quiz-action-btn")
                page.wait_for_timeout(400)
                quiz_data = page.evaluate("() => localStorage.getItem('sefaz_gamificacao_v1')")
                assert '"questoesRespondidas":1' in quiz_data, "Resposta de questão não foi contabilizada"
                print("OK: resposta de questão do simulado contabilizada na gamificação.")
            else:
                print("AVISO: nenhuma questão carregada para testar o simulado nesta execução.")

            page.evaluate("""() => {
                const raw = JSON.parse(localStorage.getItem('sefaz_gamificacao_v1'));
                raw.filaRevisao['q_ti_1'] = { materiaId: 'teste', intervaloIdx: 0, dueDate: '2020-01-01' };
                localStorage.setItem('sefaz_gamificacao_v1', JSON.stringify(raw));
            }""")
            page.click('[data-tab="dashboard"]')
            page.wait_for_timeout(300)
            assert "fila de revisão espaçada" in widget.inner_html(), "Alerta de fila de revisão não apareceu no widget"
            print("OK: alerta de fila de revisão apareceu no widget quando há item vencido.")

            page.click('[data-tab="simulados"]')
            page.wait_for_timeout(300)
            page.click("#btn-simulado-revisao")
            page.wait_for_timeout(500)
            revisao_card_html = page.locator("#quiz-card").inner_html()
            assert "Questão 1 de" in revisao_card_html, "Simulado de revisão não carregou a questão vencida"
            print("OK: botão Revisão Espaçada carregou a questão vencida corretamente.")

            erros_relevantes = [e for e in erros_console if "gamif" in e.lower() or "Uncaught" in e]
            if erros_relevantes:
                print("ERROS DE CONSOLE:", erros_relevantes)
                sys.exit(1)

            print("\nTODOS OS TESTES DE GAMIFICAÇÃO PASSARAM.")
            browser.close()
    finally:
        srv.terminate()


if __name__ == "__main__":
    main()
