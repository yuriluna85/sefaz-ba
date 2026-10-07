import os
import json
import re
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

MAX_POR_CONCURSO = 8
DIAS_MAXIMOS_DE_VIDA = 90  # notícias mais antigas que isso são descartadas mesmo sem substituto


def fetch_google_news(query, contest_tag):
    encoded_query = urllib.parse.quote(query)
    url = f"https://news.google.com/rss/search?q={encoded_query}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    print(f"Buscando notícias para: {query} (Tag: {contest_tag})")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            xml_data = response.read()

        root = ET.fromstring(xml_data)
        news_items = []

        for item in root.findall('.//item'):
            title = item.find('title').text if item.find('title') is not None else ""
            link = item.find('link').text if item.find('link') is not None else ""
            pub_date = item.find('pubDate').text if item.find('pubDate') is not None else ""
            source = item.find('source').text if item.find('source') is not None else "Google News"

            if " - " in title:
                title = title.rsplit(" - ", 1)[0]

            news_items.append({
                "title": title,
                "link": link,
                "pubDate": pub_date,
                "source": source,
                "tag": contest_tag,
                "fetchedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        return news_items
    except Exception as e:
        print(f"Erro ao buscar notícias para {query}: {e}")
        return []


def data_para_ordenacao(item):
    """Converte pubDate (RFC 822) em datetime real para ordenar por data de publicação, não por ordem de chegada."""
    try:
        dt = parsedate_to_datetime(item.get("pubDate", ""))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        # Sem data confiável: trata como muito antiga para não ficar no topo indevidamente
        return datetime.min.replace(tzinfo=timezone.utc)


def dias_desde_publicacao(item):
    dt = data_para_ordenacao(item)
    agora = datetime.now(timezone.utc)
    return (agora - dt).days


# O título precisa citar o órgão; evita listas genéricas ("18 editais previstos") e concursos vizinhos (SEPLAG-BA)
TERMOS_OBRIGATORIOS = {
    "SEFAZ-BA": ["sefaz"],
    "Receita Federal": ["receita federal", "rfb"],
    "Banco Central": ["banco central", "bacen"],
}


# Títulos terminados em código aleatório entre parênteses (letras e números, 8 ou mais), padrão de
# páginas de spam que o Google News às vezes indexa: "... Scotland Vs Usa (78ya9tBoMb)"
CODIGO_SPAM = re.compile(r"\((?=[A-Za-z0-9]*\d)(?=[A-Za-z0-9]*[A-Za-z])[A-Za-z0-9]{8,}\)\s*$")


def relevante(item):
    titulo_original = item.get("title", "")
    if CODIGO_SPAM.search(titulo_original):
        return False
    termos = TERMOS_OBRIGATORIOS.get(item.get("tag"), [])
    titulo = titulo_original.lower()
    return not termos or any(t in titulo for t in termos)


def sem_titulos_repetidos(itens):
    """Mantém só a primeira ocorrência de cada título (o mesmo texto replicado por vários portais)."""
    vistos = set()
    unicos = []
    for item in itens:
        chave = " ".join(item.get("title", "").lower().split())
        if chave not in vistos:
            vistos.add(chave)
            unicos.append(item)
    return unicos


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(base_dir, "static")

    os.makedirs(static_dir, exist_ok=True)
    news_file = os.path.join(static_dir, "news_data.json")

    existing_news = []
    if os.path.exists(news_file):
        try:
            with open(news_file, 'r', encoding='utf-8') as f:
                existing_news = json.load(f)
        except Exception:
            existing_news = []

    existing_links = {item['link'] for item in existing_news}

    # Várias buscas por concurso; a SEFAZ-BA inclui banca (Cesgranrio) e edital, fase atual do certame
    queries = {
        "SEFAZ-BA": [
            "concurso SEFAZ BA 2026",
            "SEFAZ BA Cesgranrio edital",
        ],
        "Receita Federal": ["concurso Receita Federal 2026"],
        "Banco Central": ["concurso Banco Central BACEN 2026"],
    }

    new_articles_count = 0
    novos_por_tag = {}

    for tag, lista_buscas in queries.items():
        novos = []
        for query in lista_buscas:
            for art in fetch_google_news(query, tag):
                if art['link'] not in existing_links:
                    existing_links.add(art['link'])
                    novos.append(art)
        novos_por_tag[tag] = novos
        new_articles_count += len(novos)

    # Descarta notícias antigas demais mesmo que não haja substituto novo (evita ficar preso a julho para sempre)
    pool_por_tag = {}
    for tag in queries:
        antigas_da_tag = [item for item in existing_news if item.get("tag") == tag]
        antigas_validas = [item for item in antigas_da_tag if dias_desde_publicacao(item) <= DIAS_MAXIMOS_DE_VIDA]
        pool_por_tag[tag] = [i for i in antigas_validas + novos_por_tag.get(tag, []) if relevante(i)]

    # Ordena cada concurso pela data real de publicação (mais recente primeiro) e limita por concurso,
    # garantindo que um concurso com muitas notícias novas não expulse os outros dois da lista.
    updated_news = []
    for tag in queries:
        ordenadas = sem_titulos_repetidos(sorted(pool_por_tag[tag], key=data_para_ordenacao, reverse=True))
        updated_news.extend(ordenadas[:MAX_POR_CONCURSO])

    try:
        with open(news_file, 'w', encoding='utf-8') as f:
            json.dump(updated_news, f, indent=4, ensure_ascii=False)
        print(f"Sucesso! Salvas {len(updated_news)} notícias (adicionadas {new_articles_count} novas) em {news_file}")
        for tag in queries:
            qtd = len([n for n in updated_news if n['tag'] == tag])
            print(f"  {tag}: {qtd} notícia(s)")
    except Exception as e:
        print(f"Erro ao salvar arquivo de notícias: {e}")


if __name__ == "__main__":
    main()
