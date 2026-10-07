"""Teste ponta a ponta do simulado no padrão Cesgranrio (Chromium via Playwright), em porta separada.

Confere o filtro por banca, o modo prova cronometrada (sem gabarito durante a prova),
a entrega com questão em branco e o resultado por disciplina com gabarito comentado.
Uso: python testar_modo_prova.py
"""
import os
import subprocess
import sys
import time
import urllib.request

from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
PORTA = 5083


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
            page.goto(f"http://127.0.0.1:{PORTA}/")
            page.wait_for_timeout(1200)
            page.click('[data-tab="simulados"]')
            page.click('#btn-simulado-ti')
            page.wait_for_timeout(300)

            btn_cesg = page.locator('button.setup-opt-btn', has_text='Somente Cesgranrio')
            assert btn_cesg.count() == 1, 'botão de filtro Cesgranrio ausente'
            n_cesg = int(btn_cesg.inner_text().split('(')[-1].rstrip(')'))
            if n_cesg == 0:
                assert btn_cesg.is_disabled(), 'filtro Cesgranrio deveria estar desabilitado sem questões'
            print(f"OK: filtro por banca presente ({n_cesg} questões Cesgranrio)")

            if n_cesg > 0:
                btn_cesg.click()
                page.click('button.setup-opt-btn:has-text("Todas (")')
                page.click('.start-quiz-btn')
                page.wait_for_timeout(300)
                for _ in range(n_cesg):
                    fonte = page.locator('.quiz-meta-info').inner_text()
                    assert 'cesgranrio' in fonte.lower(),f'questão de outra banca no filtro Cesgranrio: {fonte}'
                    page.locator('.quiz-option').first.click()
                    page.click('#quiz-action-btn')
                    page.click('#quiz-action-btn')
                print(f"OK: filtro Cesgranrio trouxe somente as {n_cesg} questões da banca")
                page.click('button:has-text("Refazer Simulado")')
                page.click('button.setup-opt-btn:has-text("Todas as bancas")')
                page.click('button.setup-opt-btn:has-text("10 Questões")')

            page.click('button.setup-opt-btn:has-text("Prova cronometrada")')
            assert '34 minutos' in page.locator('.setup-nota').inner_text(), 'tempo de 10 questões deveria ser 34 min (3,4 por questão)'
            page.click('.start-quiz-btn')
            page.wait_for_timeout(1300)

            crono = page.locator('#prova-cronometro').inner_text()
            assert crono.startswith('33:') or crono == '34:00', f'cronômetro inesperado: {crono}'
            assert page.locator('#prova-cronometro').get_attribute('role') == 'timer', 'cronômetro sem role=timer'
            print(f"OK: cronômetro ativo e acessível ({crono})")

            enunciado = page.locator('#quiz-card .quiz-question-text').inner_text()
            page.click('#btn-quiz-disc')
            page.wait_for_timeout(300)
            page.click('#btn-quiz-mc')
            page.wait_for_timeout(300)
            assert page.locator('#prova-cronometro').count() == 1, 'prova não foi retomada após abrir as Discursivas'
            assert page.locator('#quiz-card .quiz-question-text').inner_text() == enunciado, 'prova retomada em outra questão'
            print("OK: prova retomada de onde parou depois de abrir as Discursivas")

            page.once('dialog', lambda d: d.dismiss())
            page.click('#btn-simulado-brother')
            page.wait_for_timeout(300)
            assert page.locator('#prova-cronometro').count() == 1, 'prova abandonada mesmo com confirmação negada'
            print("OK: trocar de cargo pede confirmação e, se negada, mantém a prova")

            page.click('button:has-text("Deixar em branco")')
            for i in range(9):
                n_opc = page.locator('.quiz-option').count()
                assert n_opc >= 5, f'modo prova trouxe questão com {n_opc} alternativas'
                page.locator('.quiz-option').first.click()
                assert page.locator('#explanation-box').is_hidden(), 'gabarito não pode aparecer no modo prova'
                page.click('#quiz-action-btn')
            print("OK: 10 questões percorridas sem revelar gabarito")

            resumo = page.locator('.prova-resumo')
            assert resumo.is_visible(), 'resumo da prova não apareceu'
            assert 'em branco ou não alcançadas: 1' in resumo.inner_text(), 'contagem de questão em branco errada'
            assert page.locator('.prova-item').count() == 10, 'gabarito comentado deveria ter 10 itens'
            assert page.locator('.prova-disciplinas li').count() >= 1
            primeiro = page.locator('.prova-item').nth(0)
            primeiro.locator('summary').click()
            texto = primeiro.inner_text()
            assert 'Sua resposta: em branco' in texto and 'Gabarito (' in texto, 'gabarito comentado sem texto das alternativas'
            segundo = page.locator('.prova-item').nth(1)
            segundo.locator('summary').click()
            assert 'Sua resposta (' in segundo.inner_text(), 'alternativa marcada não aparece no gabarito comentado'
            print("OK: resultado com desempenho por disciplina e gabarito comentado com texto das alternativas")

            page.click('button:has-text("Nova Prova")')
            page.click('button.setup-opt-btn:has-text("Estudo")')
            page.click('.start-quiz-btn')
            page.locator('.quiz-option').first.click()
            page.click('#quiz-action-btn')
            assert page.locator('#explanation-box').is_visible(), 'modo estudo deveria mostrar gabarito'
            assert page.locator('#prova-cronometro').count() == 0, 'cronômetro não deveria aparecer no modo estudo'
            print("OK: modo estudo segue mostrando gabarito a cada questão")

            print("\nTODOS OS TESTES DO MODO PROVA PASSARAM.")
            browser.close()
    finally:
        srv.terminate()


if __name__ == "__main__":
    main()
