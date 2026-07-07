import os
import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime

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
        
        # Parse RSS items
        for item in root.findall('.//item'):
            title = item.find('title').text if item.find('title') is not None else ""
            link = item.find('link').text if item.find('link') is not None else ""
            pub_date = item.find('pubDate').text if item.find('pubDate') is not None else ""
            source = item.find('source').text if item.find('source') is not None else "Google News"
            
            # Clean title (Google News titles often end with " - Source Name")
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

def main():
    # Relative path to support both Windows and GitHub Actions (Linux)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(base_dir, "static")
    
    os.makedirs(static_dir, exist_ok=True)
    news_file = os.path.join(static_dir, "news_data.json")
    
    # Load existing news to avoid duplicates
    existing_news = []
    if os.path.exists(news_file):
        try:
            with open(news_file, 'r', encoding='utf-8') as f:
                existing_news = json.load(f)
        except Exception:
            existing_news = []
            
    # Create a set of existing links for fast lookup
    existing_links = {item['link'] for item in existing_news}
    
    queries = {
        "SEFAZ-BA": "concurso SEFAZ BA 2026",
        "Receita Federal": "concurso Receita Federal 2026",
        "Banco Central": "concurso Banco Central BACEN 2026"
    }
    
    new_articles_count = 0
    
    for tag, query in queries.items():
        articles = fetch_google_news(query, tag)
        # Take the top 5 articles per query
        for art in articles[:5]:
            if art['link'] not in existing_links:
                existing_news.insert(0, art)  # Add new items to the front
                existing_links.add(art['link'])
                new_articles_count += 1
                
    # Limit the list to the 20 most recent news overall
    updated_news = existing_news[:20]
    
    # Save back to file
    try:
        with open(news_file, 'w', encoding='utf-8') as f:
            json.dump(updated_news, f, indent=4, ensure_ascii=False)
        print(f"Sucesso! Salvas {len(updated_news)} notícias (adicionadas {new_articles_count} novas) em {news_file}")
    except Exception as e:
        print(f"Erro ao salvar arquivo de notícias: {e}")

if __name__ == "__main__":
    main()
