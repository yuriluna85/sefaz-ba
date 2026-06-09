import os
import re
import urllib.request
from bs4 import BeautifulSoup

TARGET_DIR = r"G:\Meu Drive\ESPECIALIZAÇÕES\Concurso SEFAZ"
os.makedirs(TARGET_DIR, exist_ok=True)

URL_SEFAZ_BA = "https://www.pciconcursos.com.br/provas/sefaz-ba/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

def get_exam_links():
    print("Buscando links de provas no PCI Concursos...")
    try:
        req = urllib.request.Request(URL_SEFAZ_BA, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read()
        
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        
        # PCI Concursos lists exams in anchor tags with '/provas/download/' in the href
        for a in soup.find_all('a', href=True):
            href = a['href']
            if '/provas/download/' in href:
                # Resolve relative URL if necessary
                if href.startswith('/'):
                    href = "https://www.pciconcursos.com.br" + href
                title = a.get_text().strip()
                links.append((title, href))
                
        print(f"Encontrados {len(links)} links de provas.")
        return links
    except Exception as e:
        print(f"Erro ao buscar a lista de provas: {e}")
        return []

def download_pci_pdf(title, download_url):
    # Clean the title to use as filename
    clean_title = re.sub(r'[\\/*?:"<>|]', "", title)
    clean_title = clean_title.replace(" ", "_")[:60] + ".pdf"
    target_path = os.path.join(TARGET_DIR, clean_title)
    
    print(f"\nTentando baixar: {title}")
    print(f"URL: {download_url}")
    
    try:
        # First, request the download page to get the actual PDF redirection if any,
        # or download the file directly (PCI uses a download button that points to the PDF).
        req = urllib.request.Request(download_url, headers=headers)
        with urllib.request.urlopen(req) as response:
            content = response.read()
            
            # Check if we got a PDF or HTML
            if content.startswith(b'%PDF'):
                with open(target_path, 'wb') as f:
                    f.write(content)
                print(f"-> Salvo com sucesso em: {target_path}")
                return True
            else:
                # PCI might require a post request or have a button inside.
                # Let's parse the HTML of the download page to find the real PDF file.
                html_content = content.decode('utf-8', errors='ignore')
                sub_soup = BeautifulSoup(html_content, 'html.parser')
                
                # Look for the download button or link pointing to the PDF
                real_pdf_url = None
                for a_tag in sub_soup.find_all('a', href=True):
                    sub_href = a_tag['href']
                    if sub_href.endswith('.pdf'):
                        real_pdf_url = sub_href
                        break
                
                # Alternatively, search for the download form or javascript action
                if not real_pdf_url:
                    # Sometimes the link is inside a button or form.
                    # Let's search for a script or form redirection.
                    match = re.search(r"window\.open\('([^']+)'", html_content)
                    if match:
                        real_pdf_url = match.group(1)
                
                if real_pdf_url:
                    if real_pdf_url.startswith('/'):
                        real_pdf_url = "https://www.pciconcursos.com.br" + real_pdf_url
                    print(f"-> Real PDF URL encontrada: {real_pdf_url}")
                    
                    pdf_req = urllib.request.Request(real_pdf_url, headers=headers)
                    with urllib.request.urlopen(pdf_req) as pdf_response:
                        pdf_content = pdf_response.read()
                        if pdf_content.startswith(b'%PDF'):
                            with open(target_path, 'wb') as f:
                                f.write(pdf_content)
                            print(f"-> Salvo com sucesso em: {target_path}")
                            return True
                
                print("-> Não foi possível extrair o PDF desta página de download.")
                return False
    except Exception as e:
        print(f"-> Erro ao processar download: {e}")
        return False

if __name__ == "__main__":
    links = get_exam_links()
    
    # Download the first 3 exams found
    download_count = 0
    for title, href in links:
        if download_count >= 3:
            break
        if download_pci_pdf(title, href):
            download_count += 1
            
    print(f"\nDownload concluído! Total de provas baixadas: {download_count}")
