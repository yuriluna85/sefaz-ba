import os
import urllib.request
import pypdf

PDF_URL = "https://cdn.cebraspe.org.br/concursos/sefaz_rn_25_auditor/arquivos/E8D7BE4C19CD39BFF1D87ECFBF92C0409AF35B178B8865C9534F17236D261200.pdf"
LOCAL_PDF = "sefaz_rn_edital.pdf"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

def download_pdf():
    print("Baixando edital da SEFAZ-RN...")
    req = urllib.request.Request(PDF_URL, headers=headers)
    with urllib.request.urlopen(req) as response:
        with open(LOCAL_PDF, 'wb') as f:
            f.write(response.read())
    print("Download concluído!")

def extract_content():
    if not os.path.exists(LOCAL_PDF):
        download_pdf()
        
    print("Extraindo texto do edital...")
    reader = pypdf.PdfReader(LOCAL_PDF)
    text_by_page = []
    
    # We look for where the "CONTEÚDO PROGRAMÁTICO" or "OBJETIVAS" starts
    found_start = False
    start_page = 0
    
    for idx, page in enumerate(reader.pages):
        page_text = page.extract_text()
        if "CONTEÚDO PROGRAMÁTICO" in page_text or "DOS CONHECIMENTOS" in page_text:
            if not found_start:
                found_start = True
                start_page = idx
                print(f"Encontrou início do conteúdo programático na página {idx + 1}")
        text_by_page.append(page_text)
        
    # Let's print pages from start_page onwards
    content_text = ""
    for idx in range(start_page, len(reader.pages)):
        content_text += f"\n--- PÁGINA {idx + 1} ---\n" + text_by_page[idx]
        
    # Write to a txt file for analysis
    with open("sefaz_rn_syllabus.txt", "w", encoding="utf-8") as f:
        f.write(content_text)
    print("Texto do conteúdo programático salvo em sefaz_rn_syllabus.txt")

if __name__ == "__main__":
    extract_content()
