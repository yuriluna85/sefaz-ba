"""Teste offline (sem rede) dos filtros de notícias do fetch_news.py.

Confere o filtro de relevância por título, o descarte de títulos com código de spam
e a remoção de títulos repetidos entre portais.
Uso: python testar_fetch_news.py
"""
from fetch_news import relevante, sem_titulos_repetidos


def noticia(titulo, tag="SEFAZ-BA", link=None):
    return {"title": titulo, "tag": tag, "link": link or titulo}


def main():
    assert relevante(noticia("Concurso Sefaz BA define Cesgranrio como banca"))
    assert not relevante(noticia("Edital SEPLAG-BA 2026: Concurso abre 50 vagas de R$ 10,8 mil"))
    assert not relevante(noticia("Concurso público: 18 editais previstos para outubro; até R$ 33,8 mil!"))
    print("OK: filtro de relevância exige o órgão no título")

    assert relevante(noticia("Concurso Receita Federal 2026: veja as últimas atualizações", "Receita Federal"))
    assert not relevante(noticia("Receita Federal 2026: O Edital Pode Vir Com FGV De Novo? Scotland Vs Usa (78ya9tBoMb)", "Receita Federal"))
    assert relevante(noticia("Concurso Bacen: 170 vagas autorizadas (2026)", "Banco Central"))
    assert relevante(noticia("Concurso Sefaz BA (Cesgranrio) tem banca definida"))
    print("OK: títulos com código de spam são descartados; parênteses comuns passam")

    lista = [
        noticia("Concurso Sefaz BA define Cesgranrio como banca", link="a"),
        noticia("Concurso  Sefaz BA define Cesgranrio como banca", link="b"),
        noticia("Concurso Sefaz BA: Cesgranrio é escolhida banca; 200 vagas", link="c"),
    ]
    unicos = sem_titulos_repetidos(lista)
    assert [n["link"] for n in unicos] == ["a", "c"], unicos
    print("OK: títulos repetidos entre portais aparecem uma vez só")

    print("\nTODOS OS TESTES DO FETCH_NEWS PASSARAM.")


if __name__ == "__main__":
    main()
