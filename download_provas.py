import os
import urllib.request

# Directory to save the downloaded exam PDFs
TARGET_DIR = r"G:\Meu Drive\ESPECIALIZAÇÕES\Concurso SEFAZ\Provas"
os.makedirs(TARGET_DIR, exist_ok=True)

# List of target SEFAZ exam PDFs (using stable public government and Cebraspe URLs)
PDF_URLS = {
    "SEFAZ_AL_2021_Edital_Auditor.pdf": "https://www.cebraspe.org.br/concursos/sefaz_al_21/arquivos/Edital_1_Sefaz_AL_2021.pdf",
    "SEFAZ_CE_2021_Edital_Auditor.pdf": "https://www.cebraspe.org.br/concursos/sefaz_ce_21/arquivos/ED_1_2021_SEFAZ_CE_ABERTURA.PDF",
}

def download_file(filename, url):
    target_path = os.path.join(TARGET_DIR, filename)
    print(f"Baixando: {filename}...")
    try:
        # Using a custom User-Agent to prevent 403 Forbidden from security firewalls
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
        )
        with urllib.request.urlopen(req) as response:
            with open(target_path, 'wb') as f:
                f.write(response.read())
        print(f"Salvo com sucesso em: {target_path}")
    except Exception as e:
        print(f"Erro ao baixar {filename}: {e}")

if __name__ == "__main__":
    for name, url in PDF_URLS.items():
        download_file(name, url)
    print("Processo de download concluído!")
