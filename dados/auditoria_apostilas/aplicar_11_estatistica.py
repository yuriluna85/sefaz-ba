"""Aplica a auditoria da Apostila de Estatística e RLM (Fase 1) e acrescenta o que faltava do programa: SEFAZ-CE 2026
(Matemática Financeira, Estatística e Raciocínio Lógico) e SEFAZ-BA 2022 (RLM e Estatística). Todos os exemplos numéricos
foram recalculados. Idempotente. Relatório: dados/auditoria_apostilas/11_estatistica.md
Uso (na pasta do app): python dados/auditoria_apostilas/aplicar_11_estatistica.py
"""
import json
import os
import sys

APP = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARQ = os.path.join(APP, 'apostilas_conteudo.json')
dados = json.load(open(ARQ, encoding='utf-8'))
ap = next(a for a in dados if 'Estatistica' in a['filename'])
S = ap['sections']

if any(s['title'].startswith('11.') for s in S):
    print('Apostila de Estatística já atualizada; nada a fazer.')
    sys.exit(0)


def bul(sec, inicio):
    return next(b for b in sec['bullets'] if b[0].strip().startswith(inicio))


def trocar(txt, velho, novo):
    assert velho in txt, 'trecho não encontrado: ' + velho[:70]
    return txt.replace(velho, novo)


# ---- Seção 3: combinatória ----
b = bul(S[2], 'Permutação Simples')
b[1] = trocar(b[1], '(ex: cálculo de anagramas da palavra SEFAZ ou BANCO)',
              '(exemplo: os anagramas de BANANA, com A repetido 3 vezes e N 2 vezes, são 6! / (3! x 2!) = 60; SEFAZ e BANCO não têm letras '
              'repetidas, então seus anagramas são 5! = 120)')
b = bul(S[2], 'Arranjo Simples')
b[1] = b[1] + (' Se pode haver repetição de elementos (por exemplo, senha de 4 dígitos que aceita dígitos repetidos), o arranjo com '
               'repetição vale n elevado a p (10^4 = 10.000 senhas).')
b = bul(S[2], 'Combinação Simples')
b[1] = ('Agrupamentos em que a alteração da ordem dos elementos não gera novo resultado (comissões, equipes, sorteio de loteria, '
        'subconjuntos): C(n, p) = n! / (p! x (n - p)!). Exemplo: C(5, 2) = 10.')

# ---- Seção 5: descritiva ----
b = bul(S[4], 'Curvas de Assimetria')
b[1] = ('1. Distribuição simétrica: Média = Mediana = Moda. 2. Assimetria positiva (à direita, com cauda longa à direita, típica de '
        'renda e faturamento): em geral Média > Mediana > Moda. 3. Assimetria negativa (à esquerda): em geral Moda > Mediana > Média. '
        'A ordem é uma regra prática para distribuições unimodais; existem exceções.')

# ---- Seção 7: discretas ----
b = bul(S[6], 'Aproximação da Binomial')
b[1] = ('Quando o número de ensaios n é grande e a probabilidade de sucesso p é pequena (regra prática usual: n >= 100 e p <= 0,01, ou '
        'n x p pequeno), a Binomial pode ser aproximada por uma Poisson com lambda = n x p. Os limites variam entre autores.')
S[6]['tip'] = ['Alerta de Prova - Poisson',
               'Na Poisson, média e variância são iguais. Se uma questão disser que a variável tem distribuição de Poisson, use lambda como '
               'média e como variância. Média igual à variância é compatível com a Poisson, mas não a demonstra por si só.']

# ---- Seção 8: normal ----
b = bul(S[7], 'Propriedade da Distribuição Normal Padronizada')
b[0] = 'Regra Empírica (68-95-99,7) e Valores Críticos'
b[1] = ('Intervalo de mu - 1 sigma a mu + 1 sigma: cerca de 68,27% dos valores. De mu - 2 sigma a mu + 2 sigma: cerca de 95,45%. De '
        'mu - 3 sigma a mu + 3 sigma: cerca de 99,73%. Valores críticos usuais: Z = +/- 1,96 delimita 95% (bilateral); Z = +/- 2,576 '
        'delimita 99%; Z = +/- 1,645 delimita 90%. Não confunda 2 desvios-padrão (95,45%) com 1,96 desvio-padrão (95%).')
b = bul(S[7], 'O Teorema Central do Limite')
b[1] = trocar(b[1], '(n >= 30)', '(regra prática usual: n >= 30, dependendo da assimetria da população)')
S[7]['tip'] = ['O Poder do Teorema Central do Limite',
               'O TCL sustenta a inferência por amostragem: mesmo que a população seja assimétrica, a distribuição da média amostral é '
               'aproximadamente normal para amostras suficientemente grandes. É uma aproximação, não uma igualdade exata.']

# ---- Seção 9: inferência ----
b = bul(S[8], 'Intervalo de Confiança')
b[1] = trocar(b[1], 'Para 99% de confiança, Z(alfa/2) = 2,575.',
              'Para 99% de confiança, Z(alfa/2) = 2,576 (2,58 em aproximações). Exemplo: n = 36, média amostral 50 e sigma = 12 dão '
              'erro padrão 12 / 6 = 2 e IC de 95% igual a 50 +/- 1,96 x 2 = [46,08; 53,92].')

# ---- Seção 10: armadilhas ----
S[9]['title'] = '10. Armadilhas Conceituais Recorrentes em Estatística e RLM'
S[9]['content'] = ('Pontos conceituais que costumam gerar erro em questões de Raciocínio Lógico e Estatística. Servem de revisão rápida; a '
                   'base de cada ponto está nas seções anteriores.')
for i, bl in enumerate(S[9]['bullets']):
    if bl[0].startswith('Pegadinha 5'):
        S[9]['bullets'][i] = ['Pegadinha 5: Erro Tipo I versus Erro Tipo II',
                              'Erro Tipo I é rejeitar H0 quando ela é verdadeira (condenar o inocente). Erro Tipo II é não rejeitar H0 '
                              'quando ela é falsa (absolver o culpado).']
    if bl[0].startswith('Pegadinha 7'):
        S[9]['bullets'][i] = ['Pegadinha 7: Média versus Mediana na Assimetria à Direita',
                              'Na distribuição assimétrica à direita (típica de salários e faturamento), em geral a Média é maior que a '
                              'Mediana, porque os valores extremos puxam a média para cima.']


def sec(t, c, bl, tip):
    S.append({'title': t, 'content': c, 'bullets': bl, 'tip': tip})


sec('11. Lógica: Complementos, Argumentos e Conjuntos',
    'Complementa as seções 1 e 2 com equivalências completas, formas de argumento, falácias, problemas de verdade e mentira e conjuntos.',
    [['Tabela-verdade e quantidade de linhas',
      'Uma proposição composta com n proposições simples tem 2 elevado a n linhas: 2 proposições, 4 linhas; 3, 8 linhas; 4, 16 linhas.'],
     ['Recíproca, inversa e contrapositiva',
      'De "se p, então q": recíproca "se q, então p"; inversa "se não p, então não q"; contrapositiva "se não q, então não p". Só a '
      'contrapositiva é equivalente à condicional original. A recíproca e a inversa são equivalentes entre si.'],
     ['Bicondicional e disjunção exclusiva',
      'p <-> q equivale a (p -> q) e (q -> p). A negação de p <-> q é a disjunção exclusiva: p ou exclusivo q. A bicondicional é verdadeira '
      'quando p e q têm o mesmo valor.'],
     ['Formas de argumento válidas',
      'Modus ponens (p -> q, p, logo q), modus tollens (p -> q, não q, logo não p), silogismo hipotético (p -> q, q -> r, logo p -> r) e '
      'silogismo disjuntivo (p ou q, não p, logo q).'],
     ['Falácias comuns',
      'Afirmação do consequente (p -> q, q, logo p) e negação do antecedente (p -> q, não p, logo não q) são inválidas. Um argumento é '
      'válido quando é impossível ter premissas verdadeiras e conclusão falsa; validade não é verdade das premissas.'],
     ['Verdades e mentiras',
      'Estratégia: supor que uma declaração é verdadeira, deduzir as consequências e checar contradições; usar cada hipótese até '
      'restar uma única consistente. Em problemas com apenas um mentiroso, teste cada candidato.'],
     ['Conjuntos e contagem',
      'Operações: união, interseção, diferença e complemento. n(A união B) = n(A) + n(B) - n(A interseção B). Com três conjuntos: n(A) + n(B) + '
      'n(C) - n(A e B) - n(A e C) - n(B e C) + n(A e B e C). Nos diagramas de Venn, comece pela interseção tripla e volte para fora.']],
    ['Só a Contrapositiva é Equivalente',
     'A recíproca e a inversa não equivalem à condicional. Trocar "se p então q" por "se q então p" é erro clássico de argumentação.'])
sec('12. Porcentagem, Razão, Proporção, Regra de Três, PA e PG',
    'Fundamentos aritméticos e sequências, com exemplos conferidos.',
    [['Porcentagem',
      'x% de N = N x x/100. Aumento de x% multiplica por (1 + x/100); desconto de x% multiplica por (1 - x/100). Aumentos e descontos '
      'sucessivos multiplicam-se: aumento de 10% seguido de desconto de 10% dá 1,10 x 0,90 = 0,99, ou seja, queda de 1%.'],
     ['Razão e proporção',
      'Razão é a divisão de duas grandezas (a/b). Proporção é a igualdade de duas razões: a/b = c/d, e o produto dos meios é igual ao '
      'produto dos extremos (a x d = b x c).'],
     ['Regra de três',
      'Simples direta (grandezas que crescem juntas) e inversa (uma cresce enquanto a outra diminui). Composta: compare cada grandeza '
      'com a incógnita, direta ou inversamente. Exemplo inverso: 6 auditores concluem em 10 dias; 12 auditores concluem em 6 x 10 / 12 = 5 dias.'],
     ['Divisão proporcional',
      'Dividir N em partes diretamente proporcionais a a, b e c: cada parte é N x a/(a+b+c) etc. Inversamente proporcionais: use os '
      'inversos 1/a, 1/b e 1/c.'],
     ['Progressão aritmética (PA)',
      'Diferença constante r. Termo geral: a_n = a_1 + (n - 1) x r. Soma dos n primeiros: S_n = (a_1 + a_n) x n / 2. Exemplo: 5, 8, 11, ..., '
      'termo 10 = 5 + 9 x 3 = 32; soma = (5 + 32) x 10 / 2 = 185.'],
     ['Progressão geométrica (PG)',
      'Razão constante q. Termo geral: a_n = a_1 x q^(n - 1). Soma dos n primeiros: S_n = a_1 x (q^n - 1) / (q - 1). PG infinita com |q| < 1: '
      'S = a_1 / (1 - q). Exemplo: parcelas de 700, 770 e 847 formam PG de razão 1,1, com soma 2.317.'],
     ['Médias e problemas de idade e velocidade',
      'Velocidade média = distância total / tempo total (não é a média das velocidades). Conversão: 1 km/h = 1/3,6 m/s.']],
    ['Aumento e Desconto Não se Cancelam',
     'Aumento de 20% seguido de desconto de 20% dá 1,20 x 0,80 = 0,96: perda de 4%. Percentuais sucessivos multiplicam-se, e não se somam.'])
sec('13. Geometria Básica, Unidades e Medidas',
    'Geometria plana e espacial básica citada no edital, e conversões de medidas.',
    [['Ângulos e triângulos',
      'A soma dos ângulos internos de um triângulo é 180 graus. Teorema de Pitágoras no triângulo retângulo: hipotenusa ao quadrado é a '
      'soma dos quadrados dos catetos (3, 4 e 5 formam uma terna). Semelhança: lados proporcionais e ângulos iguais (teorema de Tales).'],
     ['Polígonos',
      'Soma dos ângulos internos de um polígono de n lados: (n - 2) x 180 graus (quadrilátero: 360 graus; hexágono: 720 graus). Número de '
      'diagonais: n x (n - 3) / 2.'],
     ['Perímetro e área',
      'Retângulo: área = base x altura. Triângulo: base x altura / 2. Trapézio: (base maior + base menor) x altura / 2. Losango: (diagonal '
      'maior x diagonal menor) / 2. Círculo: área = pi x r ao quadrado; comprimento da circunferência = 2 x pi x r.'],
     ['Volumes',
      'Paralelepípedo: comprimento x largura x altura. Cubo: aresta ao cubo. Cilindro: pi x r ao quadrado x altura. Pirâmide e cone: '
      'um terço da base vezes a altura.'],
     ['Unidades e conversões',
      'Comprimento: 1 km = 1000 m. Área: 1 m2 = 10.000 cm2 (o fator é o quadrado do de comprimento). Volume: 1 m3 = 1000 litros = 1.000.000 '
      'cm3. Massa: 1 t = 1000 kg. Tempo: 1 h = 60 min = 3600 s.']],
    ['Área Muda pelo Quadrado, Volume pelo Cubo',
     'Dobrar o lado de um quadrado quadruplica a área (2 ao quadrado). Dobrar a aresta de um cubo multiplica o volume por 8 (2 ao '
     'cubo).'])
sec('14. Matemática Financeira: Juros, Descontos, Amortização, VPL e TIR',
    'Conteúdo do programa SEFAZ-CE 2026 (Matemática Financeira). Os exemplos numéricos foram recalculados.',
    [['Juros simples',
      'J = C x i x t; M = C x (1 + i x t). Os juros incidem só sobre o capital inicial. Exemplo: C = 1.000, i = 10% ao ano, 2 anos: J = 200 e '
      'M = 1.200.'],
     ['Juros compostos',
      'M = C x (1 + i) elevado a t. Os juros incidem sobre o montante anterior. Mesmo exemplo: M = 1.000 x 1,10 ao quadrado = 1.210.'],
     ['Taxas equivalentes, proporcionais e nominais',
      'Taxas equivalentes produzem o mesmo montante no mesmo prazo: 1 + i_anual = (1 + i_mensal) elevado a 12. Exemplo: 1% ao mês equivale a '
      '1,01 elevado a 12 menos 1 = 12,68% ao ano (e não 12%). Taxa nominal é a declarada com capitalização em outro período: 12% ao ano '
      'com capitalização mensal significa 1% ao mês, que dá taxa efetiva de 12,68% ao ano.'],
     ['Taxa real',
      '1 + i_aparente = (1 + i_real) x (1 + inflação). Exemplo: 10% de taxa aparente com 5% de inflação dão 1,10 / 1,05 - 1 = 4,76% de taxa real.'],
     ['Descontos',
      'Desconto comercial (bancário, por fora): D = N x d x t, sobre o valor nominal N. Desconto racional (por dentro): D = N x i x t / (1 + i x t), '
      'ou seja, sobre o valor atual. O desconto comercial simples é maior que o racional. Composto: valor atual A = N / (1 + i) elevado a t.'],
     ['Capitalização contínua',
      'M = C x e elevado a (r x t), com e igual a cerca de 2,718; é o limite da capitalização composta quando o período tende a zero.'],
     ['Anuidades e equivalência de capitais',
      'Valor presente de n prestações iguais PMT postecipadas: PV = PMT x [1 - (1 + i) elevado a -n] / i. Capitais equivalentes têm o '
      'mesmo valor na data focal, usando a mesma taxa.'],
     ['SAC (amortização constante)',
      'Amortização = PV / n, constante; juros calculados sobre o saldo devedor e decrescentes; prestações decrescentes. Exemplo: PV = 1.200, '
      'n = 3, i = 10%: amortização 400; prestações 520, 480 e 440.'],
     ['Sistema francês (Price)',
      'Prestação constante: PMT = PV x i / [1 - (1 + i) elevado a -n]; juros decrescentes e amortização crescente. Exemplo: mesmo caso, PMT = 120 / '
      '0,248685 = 482,54. O sistema misto (SAM) usa a média aritmética das prestações do SAC e do Price.'],
     ['VPL e TIR',
      'VPL = soma dos fluxos de caixa descontados à taxa mínima de atratividade, menos o investimento inicial; aceita-se o projeto se VPL > 0. '
      'TIR é a taxa de desconto que zera o VPL; aceita-se se TIR > taxa mínima de atratividade. Payback é o tempo para recuperar o investimento.']],
    ['Composto Supera o Simples Depois do Primeiro Período',
     'Em um período, juros simples e compostos coincidem. Depois disso, o composto rende mais. Taxa nominal com capitalização mensal '
     'não é taxa efetiva: converta antes de comparar.'])
sec('15. Distribuições de Frequência, Dados Agrupados e Gráficos',
    'Complementa a seção 5 com dados em tabelas de frequência e com as médias geométrica e harmônica.',
    [['Tabela de frequências',
      'Frequência absoluta (fi), relativa (fi / n), acumulada (Fi) e percentual. Em variáveis contínuas, agrupam-se os dados em classes '
      'de mesma amplitude; a regra de Sturges sugere cerca de 1 + 3,3 x log10(n) classes.'],
     ['Média em dados agrupados',
      'Média = soma de (fi x ponto médio da classe) / n, supondo os valores concentrados no ponto médio.'],
     ['Mediana em dados agrupados',
      'Md = limite inferior da classe mediana + [(n/2 - frequência acumulada anterior) / frequência da classe mediana] x amplitude da classe.'],
     ['Moda em dados agrupados',
      'Fórmula de Czuber: Mo = limite inferior da classe modal + [D1 / (D1 + D2)] x amplitude, em que D1 é a diferença entre a frequência da '
      'classe modal e a da anterior e D2, entre a da modal e a da seguinte.'],
     ['Assimetria e curtose',
      'Primeiro coeficiente de Pearson: (média - moda) / desvio-padrão; positivo indica assimetria à direita. Curtose mede o achatamento '
      'em relação à normal.'],
     ['Médias geométrica e harmônica',
      'Geométrica = raiz n-ésima do produto dos valores (para taxas de crescimento e números-índices). Harmônica = n / soma dos inversos (para '
      'médias de razões, como velocidades em trechos iguais). Para valores positivos e distintos: harmônica < geométrica < aritmética.'],
     ['Gráficos',
      'Histograma (barras contíguas para variáveis contínuas), polígono de frequências, ogiva (frequências acumuladas), gráfico de barras e de '
      'setores (categóricas), boxplot (mediana, quartis e outliers pela regra de 1,5 x IQR) e diagrama de dispersão (relação entre duas variáveis).']],
    ['Mediana Interpola, Moda Usa Diferenças',
     'Na mediana agrupada, use n/2 e a frequência acumulada anterior. Na moda de Czuber, use as diferenças com as classes vizinhas.'])
sec('16. Amostragem, Tamanho da Amostra e Dados Categorizados',
    'Técnicas de amostragem citadas no programa e análise de tabelas de contingência.',
    [['Amostragem probabilística',
      'Aleatória simples (todos têm a mesma chance); sistemática (escolhe um ponto inicial e depois um elemento a cada k, com k = N/n); '
      'estratificada (divide em estratos homogêneos e sorteia em cada um, proporcional ou uniforme); por conglomerados (sorteia grupos e '
      'observa todos ou parte dos seus elementos); multiestágio.'],
     ['Amostragem não probabilística',
      'Por conveniência, por julgamento (intencional), por cotas e bola de neve. Não permitem calcular o erro amostral com rigor '
      'probabilístico.'],
     ['Erros',
      'Erro amostral: diferença aleatória entre amostra e população, que diminui com o tamanho da amostra. Erros não amostrais (cobertura, '
      'resposta, medição, viés de seleção) não diminuem apenas aumentando n.'],
     ['Tamanho da amostra',
      'Para a média: n = (Z x sigma / E) ao quadrado, com E a margem de erro. Para proporção: n = Z ao quadrado x p x (1 - p) / E ao quadrado; sem '
      'informação prévia, use p = 0,5 (pior caso). Exemplo: 95% de confiança e E = 5%: n = 1,96 ao quadrado x 0,25 / 0,05 ao quadrado = 384,16, '
      'arredondado para 385.'],
     ['Tabelas de contingência',
      'Cruzam duas variáveis categóricas. Frequência esperada sob independência: E = (total da linha x total da coluna) / n.'],
     ['Teste qui-quadrado de independência',
      'Estatística: soma de (O - E) ao quadrado / E, com (linhas - 1) x (colunas - 1) graus de liberdade. Valor alto, comparado ao crítico, '
      'indica associação entre as variáveis. Também se aplica a testes de aderência.']],
    ['Estratificar Reduz Variância Quando os Estratos são Homogêneos',
     'Na estratificada, formar estratos internamente parecidos e diferentes entre si melhora a precisão. Em conglomerados, o ideal é '
     'que cada grupo seja heterogêneo por dentro.'])
sec('17. Inferência em Detalhe: Testes para Médias e Proporções e Intervalos de Confiança',
    'Complementa a seção 9 com as estatísticas de teste e os intervalos para média e proporção.',
    [['Teste para a média (variância conhecida ou n grande)',
      'z = (X barra - mu0) / (sigma / raiz(n)). Com sigma desconhecido, usa-se s e a distribuição t de Student com n - 1 graus de '
      'liberdade: t = (X barra - mu0) / (s / raiz(n)).'],
     ['Teste para a proporção',
      'z = (p chapéu - p0) / raiz(p0 x (1 - p0) / n), com p chapéu a proporção amostral. Vale para amostras grandes.'],
     ['Testes unilaterais e bilaterais',
      'Bilateral: H1 com "diferente de"; unilateral: H1 com "maior que" ou "menor que". Valores críticos de Z: bilateral a 5% = +/- 1,96; '
      'unilateral a 5% = 1,645.'],
     ['Intervalos de confiança',
      'Média com sigma desconhecido: X barra +/- t x s / raiz(n). Proporção: p chapéu +/- Z x raiz(p chapéu x (1 - p chapéu) / n). Maior '
      'confiança dá intervalo mais largo; maior n dá intervalo mais estreito.'],
     ['Relação entre IC e teste',
      'Um teste bilateral a nível alfa rejeita H0: mu = mu0 exatamente quando mu0 está fora do IC de (1 - alfa) de confiança.'],
     ['Poder do teste',
      'Aumenta com n maior, alfa maior, diferença real maior e menor variabilidade. Erro Tipo I e Erro Tipo II variam em sentidos opostos '
      'para o mesmo n.']],
    ['IC e Teste Contam a Mesma História',
     'Se o valor da hipótese nula está fora do intervalo de confiança de 95%, o teste bilateral a 5% rejeita H0. Se está dentro, não '
     'rejeita.'])
sec('18. Regressão e Correlação em Detalhe',
    'Complementa a seção 9 com os estimadores de mínimos quadrados e um exemplo numérico completo.',
    [['Estimadores de MQO',
      'b1 = soma de (Xi - X barra)(Yi - Y barra) / soma de (Xi - X barra) ao quadrado = r x (sY / sX); b0 = Y barra - b1 x X barra. A reta '
      'passa pelo ponto (X barra, Y barra), e a soma dos resíduos é zero.'],
     ['Decomposição da variação',
      'SQT (total) = SQR (explicada pela regressão) + SQE (dos erros). R2 = SQR / SQT.'],
     ['Exemplo numérico',
      'X = 1, 2, 3, 4, 5 e Y = 2, 4, 5, 4, 5. Médias: 3 e 4. Soma dos produtos dos desvios = 6; soma dos quadrados de X = 10; logo b1 = 0,6 e '
      'b0 = 4 - 0,6 x 3 = 2,2. A soma dos quadrados de Y = 6, então r = 6 / raiz(10 x 6) = 0,775 e R2 = 0,6.'],
     ['Interpretação',
      'b1: variação média de Y para cada unidade a mais de X. b0: valor previsto de Y quando X = 0 (pode não ter sentido prático). R2 = 0,6: '
      '60% da variação de Y é explicada pela relação linear com X.'],
     ['Pressupostos e cuidados',
      'Linearidade, independência e variância constante dos erros e normalidade dos resíduos (para inferência). Evite extrapolar fora do '
      'intervalo dos dados. Correlação não implica causalidade. Outliers podem influenciar muito a reta.'],
     ['Regressão múltipla e ANOVA',
      'Na regressão múltipla, cada coeficiente mede o efeito de uma variável mantendo as demais fixas; multicolinearidade entre preditores '
      'instabiliza as estimativas (verifica-se pelo fator de inflação da variância). A ANOVA compara médias de grupos pelo teste F.']],
    ['R2 Mede Ajuste, Não Causa',
     'Um R2 alto indica bom ajuste linear, mas não prova relação causal nem que o modelo é adequado (verifique resíduos e a forma da relação).'])
sec('19. Séries Temporais, Números-Índices e Análise Multivariada',
    'Tópicos do programa SEFAZ-CE 2026 e do edital SEFAZ-BA 2022: séries temporais, médias móveis e análise multivariada.',
    [['Componentes de uma série temporal',
      'Tendência (movimento de longo prazo), sazonalidade (padrão que se repete em períodos fixos, como o de fim de ano), ciclo (oscilações '
      'de prazo mais longo e irregular) e componente irregular ou aleatório. Modelos aditivo (soma) e multiplicativo (produto).'],
     ['Médias móveis',
      'Média móvel simples de ordem k: média dos k últimos valores, que suaviza a série e reduz o ruído. Exemplo: série 10, 12, 14, 13; média '
      'móvel de ordem 3: (10+12+14)/3 = 12 e (12+14+13)/3 = 13. Quanto maior k, mais suave e mais atrasada é a média.'],
     ['Suavização exponencial',
      'S_t = alfa x Y_t + (1 - alfa) x S_(t-1), com 0 < alfa < 1: dá mais peso às observações recentes.'],
     ['Números-índices',
      'Relacionam valores de um período a uma base. Índice de Laspeyres pondera pelas quantidades do período-base; o de Paasche, pelas do '
      'período atual; o de Fisher é a média geométrica dos dois.'],
     ['Análise multivariada: técnicas',
      'Estuda várias variáveis ao mesmo tempo: regressão múltipla, análise de componentes principais (PCA, reduz dimensões preservando '
      'variância), análise fatorial (fatores latentes), análise de agrupamentos (cluster), análise discriminante (classificação) e MANOVA.'],
     ['Ênfase para estimar e prever',
      'Em séries, evite embaralhar dados na validação; em previsões, informe a incerteza (intervalos de previsão).']],
    ['Média Móvel Suaviza, Sazonalidade Repete',
     'A média móvel filtra oscilações de curto prazo e evidencia a tendência. A sazonalidade é o padrão que se repete em períodos '
     'regulares e conhecidos.'])
sec('20. Referências e Conferência',
    'Conferência realizada em 21/09/2026. Todos os exemplos numéricos foram recalculados.',
    [['Referências',
      'Bussab e Morettin, Estatística Básica; Triola, Introdução à Estatística; Sheldon Ross, Probabilidade; Iezzi et al., Fundamentos de '
      'Matemática Elementar; Puccini, Matemática Financeira; Edital SEFAZ-CE 2026 (FCC), Anexo VI, e Edital SEFAZ-BA 2022 (FGV), Anexo I.'],
     ['Corrigido nesta revisão',
      'Regra empírica: 2 desvios-padrão contêm cerca de 95,45%, e 95% correspondem a 1,96 desvio-padrão; 68,26% para 68,27%; valor '
      'crítico de 99% para 2,576; exemplo de permutação com repetição (BANANA no lugar de SEFAZ e BANCO); média > mediana e "n >= 30" '
      'como regras práticas e não absolutas; "média 4 e variância 4 é inequivocamente Poisson" corrigido; TCL como aproximação; '
      'Erro Tipo II como "não rejeitar" H0; redundância na fórmula de combinação; seção de armadilhas atribuída às bancas sem evidência.'],
     ['A conferir',
      'Regras práticas variam entre autores (n >= 30, n >= 100 e p <= 0,01, número de classes de Sturges); arredondamentos de valores '
      'críticos. Notação e convenções de cada banca.']],
    ['Regra de Conteúdo', 'Este material não afirma nada sem fonte. Se houver divergência com o livro-texto adotado, ele prevalece.'])

ap['subtitle'] = ('Lógica e Argumentação, Conjuntos, Porcentagem, PA e PG, Geometria, Matemática Financeira (SAC, Price, VPL, TIR), Combinatória, '
                  'Probabilidade, Estatística Descritiva e Agrupada, Normal e TCL, Amostragem, Inferência, Regressão, Séries Temporais e Multivariada')
json.dump(dados, open(ARQ, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('Estatística atualizada: %d seções.' % len(S))
