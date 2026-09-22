import os
import sys
import py_compile

def run_harness_tests():
    """Suíte de autoteste padronizada (Harness) do laboratório."""
    app_dir = os.path.dirname(os.path.abspath(__file__))
    app_name = os.path.basename(app_dir)
    print(f"=== [HARNESS TEST] Iniciando verificação de integridade em: {app_name} ===")
    
    passed = 0
    total = 0

    # Teste 1: Presença do README.md
    total += 1
    readme_path = os.path.join(app_dir, "README.md")
    if os.path.exists(readme_path):
        passed += 1
        print("  [PASS 1/4] Arquivo README.md presente e válido.")
    else:
        print("  [FAIL 1/4] Arquivo README.md ausente.")

    # Teste 2: Verificação de sintaxe Python nos scripts principais (se houver)
    total += 1
    py_files = [f for f in os.listdir(app_dir) if f.endswith(".py") and f != "harness.py"]
    py_success = True
    for pf in py_files:
        try:
            py_compile.compile(os.path.join(app_dir, pf), doraise=True)
        except Exception as e:
            py_success = False
            print(f"  [ERRO SINTAXE] Falha em {pf}: {e}")

    if py_success:
        passed += 1
        print("  [PASS 2/4] Sintaxe Python e integridade de arquivos validadas.")
    else:
        print("  [FAIL 2/4] Falha de compilação em scripts Python.")

    # Teste 3: Verificação de Favicon ou Ativos Web (se houver HTML)
    total += 1
    html_files = [f for f in os.listdir(app_dir) if f.endswith(".html")]
    if html_files:
        fav_exists = any(os.path.exists(os.path.join(app_dir, f)) for f in ["favicon.png", "favicon.ico", "favicon.svg"])
        if fav_exists:
            passed += 1
            print("  [PASS 3/4] Interface HTML acompanhada de Favicon oficial.")
        else:
            print("  [FAIL 3/4] Interface HTML sem Favicon.")
    else:
        passed += 1
        print("  [PASS 3/4] Aplicação autocontida validada.")

    # Teste 4: esquema do banco de questões (options em dict, correct válido, sem duplicatas)
    qfile = os.path.join(app_dir, "questions.json")
    if os.path.exists(qfile):
        total += 1
        sys.path.insert(0, app_dir)
        try:
            import json
            from normalizar_questoes import validar
            with open(qfile, encoding="utf-8") as f:
                erros = validar(json.load(f))
            if not erros:
                passed += 1
                print("  [PASS 4/4] questions.json no esquema único, gabaritos válidos e sem duplicatas.")
            else:
                print(f"  [FAIL 4/4] questions.json com {len(erros)} problema(s); primeiros: {erros[:5]}")
        except Exception as e:
            print(f"  [FAIL 4/4] Falha ao validar questions.json: {e}")

    print(f"Resultados: {passed}/{total} testes aprovados.")
    if passed == total:
        print(">>> RESULTADO FINAL: PASS (100% OK) <<<")
        return 0
    else:
        print(">>> RESULTADO FINAL: FAIL <<<")
        return 1

if __name__ == '__main__':
    sys.exit(run_harness_tests())
