import os
import urllib.request

TARGET_DIR = r"G:\Meu Drive\ESPECIALIZAÇÕES\Concurso SEFAZ"
os.makedirs(TARGET_DIR, exist_ok=True)

# Try downloading the actual SEFAZ-BA REDA 2026 opening notice PDF
url = "https://www.sefaz.ba.gov.br/concurso/reda_2026/Edital_Abertura_Reda_2026.pdf"
filename = "SEFAZ_BA_REDA_2026_Edital.pdf"
target_path = os.path.join(TARGET_DIR, filename)

print(f"Baixando: {filename} de {url}...")
try:
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
    )
    with urllib.request.urlopen(req) as response:
        content = response.read()
        if response.status == 200 and content.startswith(b'%PDF'):
            with open(target_path, 'wb') as f:
                f.write(content)
            print(f"Sucesso! Salvo em: {target_path}")
        else:
            print(f"Resposta de status {response.status} ou arquivo não é um PDF válido (Assinatura: {content[:10]}).")
except Exception as e:
    print(f"Erro ao baixar: {e}")
