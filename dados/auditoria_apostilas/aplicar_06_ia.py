"""Aplica a auditoria da Apostila de Ciência de Dados e Big Data (Fase 1) e acrescenta as seções de IA do programa
SEFAZ-CE 2026 (B02): deep learning, IA generativa, agentes, MLOps, ética e governança de IA, Python. Idempotente.
Relatório: dados/auditoria_apostilas/06_ia.md
Uso (na pasta do app): python dados/auditoria_apostilas/aplicar_06_ia.py
"""
import json
import os
import sys

APP = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARQ = os.path.join(APP, 'apostilas_conteudo.json')
dados = json.load(open(ARQ, encoding='utf-8'))
ap = next(a for a in dados if 'Ciencia_Dados' in a['filename'])
S = ap['sections']

if any(s['title'].startswith('11.') for s in S):
    print('Apostila de Ciência de Dados já atualizada; nada a fazer.')
    sys.exit(0)


def bul(sec, inicio):
    return next(b for b in sec['bullets'] if b[0].strip().startswith(inicio))


def setb(sec, inicio, titulo, texto):
    b = bul(sec, inicio)
    b[0], b[1] = titulo, texto


# ---- Seção 1 ----
S[0]['content'] = S[0]['content'].replace(
    'a Ciência de Dados viabiliza a malha fina preditiva, a detecção de notas fiscais fraudulentas em tempo real e a seleção '
    'automatizada de contribuintes para fiscalização com base em matrizes de risco.',
    'a Ciência de Dados apoia a malha fina preditiva, a detecção de notas fiscais suspeitas e a seleção de contribuintes para '
    'fiscalização com base em matrizes de risco.')
b = bul(S[0], 'As 6 Fases do CRISP-DM')
b[1] = b[1].replace('; consome de 70% a 80% do esforço do projeto)',
                    '; costuma ser a etapa que mais consome esforço do projeto, com estimativas na literatura de cerca de 70% a 80%, sem valor exato)')

# ---- Seção 2 ----
setb(S[1], 'Detecção e Tratamento de Outliers', 'Detecção e Tratamento de Outliers',
     'Identificação por Z-Score (observações com módulo de Z maior que 3) ou pelo Intervalo Interquartil (IQR): valores abaixo de Q1 '
     'menos 1,5 vezes o IQR ou acima de Q3 mais 1,5 vezes o IQR. Tratamento por winsorização (limitação aos percentis extremos), '
     'transformação logarítmica ou remoção fundamentada.')
setb(S[1], 'Escalonamento', 'Escalonamento de Variáveis Numéricas',
     'Normalização Min-Max: leva os dados ao intervalo de 0 a 1 por X_norm = (X - X_min) / (X_max - X_min); sensível a outliers. '
     'Padronização Z-Score: Z = (X - média) / desvio padrão, com média zero e desvio padrão um; é adequada a algoritmos baseados em '
     'distância e em gradiente, como SVM, KNN e PCA.')
S[1]['tip'] = ['Regra Prática do Escalonamento',
               'Algoritmos baseados em distância (KNN, K-Means, SVM) e o PCA são sensíveis à escala, e redes neurais treinam melhor com '
               'variáveis padronizadas. Árvores de decisão e os ensembles baseados em árvores (Random Forest, XGBoost) são invariantes '
               'à escala, pois dependem apenas da ordenação dos valores. Ajuste o escalonador só nos dados de treino, para evitar '
               'vazamento de dados (data leakage).']

# ---- Seção 3 ----
S[2]['content'] = ('No aprendizado supervisionado, o modelo treina sobre variáveis preditoras (atributos, ou features, X) e uma variável '
                   'alvo conhecida (rótulo Y). O objetivo é aprender uma função f que mapeia X em Y e generaliza para dados novos.')
setb(S[2], 'Modelos de Regressão Linear Regularizada', 'Modelos de Regressão Linear Regularizada',
     'Regressão linear com penalização dos coeficientes para reduzir overfitting: 1. Ridge (regularização L2: penaliza a soma dos '
     'quadrados dos coeficientes, multiplicada por lambda; encolhe os coeficientes sem zerá-los); 2. Lasso (regularização L1: penaliza '
     'a soma dos módulos dos coeficientes, multiplicada por lambda; pode zerar coeficientes, funcionando como seleção de variáveis); '
     '3. ElasticNet (combinação de L1 e L2).')
setb(S[2], 'Regressão Logística', 'Regressão Logística',
     'Modelo de classificação (binária, com extensão a várias classes) que passa uma combinação linear dos atributos pela função '
     'sigmoide: P(Y=1 | X) = 1 / (1 + e elevado a -(b0 + b1x1 + ... + bnxn)). Estima a probabilidade de o evento ocorrer (por exemplo, '
     'a probabilidade de uma nota fiscal ser irregular) e o resultado é comparado a um limiar de decisão.')
setb(S[2], 'Árvores de Decisão', 'Árvores de Decisão (Decision Trees)',
     'Estrutura hierárquica com nó raiz, nós internos de decisão e folhas. A divisão dos nós usa critérios de pureza: índice de Gini '
     '(algoritmo CART) ou entropia com ganho de informação (ID3); o C4.5 usa a razão de ganho. São modelos bem interpretáveis, mas '
     'árvores muito profundas tendem ao overfitting.')

# ---- Seção 4 ----
setb(S[3], 'Bagging', 'Bagging (Bootstrap Aggregating) e Random Forest',
     'Treina vários modelos independentes, em paralelo, sobre amostras aleatórias com reposição (bootstrap). A previsão final é a média '
     '(regressão) ou a votação majoritária (classificação). O Random Forest aplica o bagging a árvores de decisão e sorteia também um '
     'subconjunto de atributos em cada divisão, o que descorrelaciona as árvores e reduz a VARIÂNCIA, sem aumentar substancialmente o '
     'viés.')

# ---- Seção 5 ----
setb(S[4], 'Agrupamento Baseado em Densidade', 'Agrupamento Baseado em Densidade: DBSCAN',
     'Agrupa pontos pela densidade da vizinhança, com dois parâmetros: epsilon (raio da vizinhança) e MinPts (mínimo de pontos para '
     'formar região densa). Classifica os pontos em núcleo, borda e ruído (outliers). Vantagens: não exige definir o número de clusters, '
     'encontra clusters de formato arbitrário e marca outliers como ruído. Limitações: sensível à escolha de epsilon e de MinPts e tem '
     'dificuldade com clusters de densidades muito diferentes e com dados de alta dimensão.')
setb(S[4], 'Agrupamento Hierárquico', 'Agrupamento Hierárquico',
     'Gera uma árvore de agrupamentos, representada em um dendrograma. Aglomerativo (de baixo para cima: cada ponto começa como um cluster '
     'e os clusters são fundidos) ou divisivo (de cima para baixo). Métodos de ligação: simples (distância mínima), completa (distância '
     'máxima), média e de Ward (minimiza o aumento da variância intra-cluster).')
setb(S[4], 'Mineração de Regras de Associação', 'Regras de Associação: Algoritmo Apriori',
     'Descobre regras do tipo "se A, então B" em transações. Suporte = proporção de transações que contêm A e B. Confiança = suporte de '
     '(A e B) dividido pelo suporte de A, ou seja, P(B dado A). Lift = P(A e B) dividido por P(A) x P(B): maior que 1 indica associação '
     'positiva; igual a 1, independência; menor que 1, associação negativa.')
S[4]['tip'] = ['K-Means versus DBSCAN',
               'K-Means exige definir k, assume clusters aproximadamente esféricos e é sensível a outliers. O DBSCAN não exige k, encontra '
               'formatos arbitrários e trata outliers como ruído, mas depende de epsilon e MinPts e sofre com densidades muito variadas.']

# ---- Seção 6 ----
setb(S[5], 'Técnicas de Validação Cruzada', 'Validação Cruzada (Cross-Validation)',
     'K-Fold: divide os dados em k partes, treina em k-1 e testa na restante, repetindo k vezes e tirando a média. K-Fold estratificado: '
     'preserva a proporção das classes em cada parte, recomendado para bases desbalanceadas. Em séries temporais, não se embaralha: a '
     'validação respeita a ordem do tempo (treino no passado, teste no futuro).')
setb(S[5], 'Métricas de Desempenho', 'Métricas de Classificação',
     'Acurácia = (VP + VN) / total (enganosa em bases desbalanceadas). Precisão = VP / (VP + FP): dos alertas, quantos eram reais. '
     'Revocação (recall, sensibilidade) = VP / (VP + FN): das ocorrências reais, quantas foram capturadas. Especificidade = VN / (VN + '
     'FP). F1-Score = 2 x Precisão x Revocação / (Precisão + Revocação), a média harmônica das duas. Em bases muito desbalanceadas, a '
     'curva Precisão-Revocação e sua área costumam ser mais informativas que a curva ROC.')
setb(S[5], 'Curva ROC', 'Curva ROC e AUC',
     'A curva ROC plota a taxa de verdadeiros positivos (sensibilidade), no eixo Y, contra a taxa de falsos positivos (1 menos a '
     'especificidade), no eixo X, para vários limiares de decisão. A AUC (área sob a curva) vai de 0,5, equivalente a um classificador '
     'aleatório, a 1,0, classificador perfeito (valores abaixo de 0,5 indicam desempenho pior que o acaso).')

# ---- Seção 7: Hadoop ----
setb(S[6], 'HDFS', 'HDFS (Hadoop Distributed File System)',
     'Arquitetura mestre e trabalhadores: 1. NameNode: gerencia o namespace e os metadados (mantidos em memória) e sabe em quais '
     'DataNodes estão os blocos; 2. DataNodes: armazenam os blocos no disco local; 3. Replicação: cada bloco (tamanho padrão de 128 MB) é '
     'replicado, por padrão, em 3 nós, com recuperação automática de falhas.')

# ---- Seção 8: Spark ----
S[7]['content'] = ('O Apache Spark é um motor unificado de processamento de dados em larga escala. Ele reduz o gargalo de leitura e '
                   'escrita em disco do MapReduce ao manter dados intermediários em memória. O projeto Spark informa, em seus '
                   'benchmarks, ganhos de até cerca de 100 vezes em memória e 10 vezes em disco sobre o MapReduce; o ganho real '
                   'depende da carga de trabalho.')
setb(S[7], 'Arquitetura do Apache Spark', 'Arquitetura do Apache Spark',
     'Driver (coordena a execução, cria a SparkSession e o plano de execução como DAG), gerenciador de cluster (YARN, Kubernetes ou o '
     'modo Standalone; o suporte ao Mesos foi depreciado) e executors (processos nos nós de trabalho que executam as tarefas e mantêm '
     'dados em cache).')

# ---- Seção 9: PLN e grafos ----
setb(S[8], 'Pipeline de Processamento', 'Pipeline de Processamento de Linguagem Natural (PLN)',
     '1. Tokenização (dividir o texto em tokens); 2. Remoção de stopwords (palavras muito frequentes e pouco informativas, como artigos '
     'e preposições); 3. Normalização léxica: stemming (corta sufixos por regras, gerando radicais que podem não existir no dicionário; '
     'o algoritmo de Porter é para o inglês, e para o português há stemmers como o RSLP) versus lematização (retorna o lema, a forma de '
     'dicionário, com apoio de análise morfológica).')
setb(S[8], 'Vetorização Textual', 'Vetorização Textual: TF-IDF versus Embeddings',
     'TF-IDF pondera a frequência do termo no documento pelo inverso de sua frequência no corpus, destacando termos característicos. '
     'Embeddings são vetores densos de números reais em que significados semelhantes ficam próximos. Word2Vec e FastText geram '
     'embeddings estáticos (um vetor por palavra); modelos como o BERT geram embeddings contextuais (o vetor depende da frase).')
S[8]['tip'] = ['Stemming versus Lematização',
               'Stemming corta o final da palavra e pode gerar radicais inexistentes (por exemplo, "estudante" para "estud"). Lematização '
               'usa o vocabulário e a morfologia para devolver o lema real (por exemplo, "estudando" para "estudar" e "melhores" para '
               '"melhor").']

# ---- Seção 10 ----
S[9]['title'] = '10. Armadilhas Conceituais Recorrentes em Ciência de Dados e Big Data'
S[9]['content'] = ('Pontos conceituais que costumam gerar erro em questões de ciência de dados, aprendizado de máquina e Big Data. '
                   'Servem de revisão rápida; a base de cada ponto está nas seções anteriores.')
for i, bl in enumerate(S[9]['bullets']):
    if bl[0].startswith('Pegadinha 8'):
        S[9]['bullets'][i] = ['Pegadinha 8: AUC de um Classificador Aleatório',
                              'Um modelo que decide por acaso tem AUC de cerca de 0,50 (a diagonal da curva ROC). O classificador '
                              'perfeito tem AUC igual a 1,00.']
    if bl[0].startswith('Pegadinha 6'):
        S[9]['bullets'][i] = ['Pegadinha 6: Árvores e Ensembles de Árvores são Invariantes à Escala',
                              'Random Forest e Gradient Boosting não exigem normalização ou padronização de variáveis numéricas, pois '
                              'usam a ordenação dos valores. Já KNN, K-Means, SVM e PCA são sensíveis à escala.']


def sec(t, c, bl, tip):
    S.append({'title': t, 'content': c, 'bullets': bl, 'tip': tip})


sec('11. Outros Paradigmas: Semissupervisionado, Autossupervisionado, por Reforço e Transferência',
    'Além do aprendizado supervisionado e do não supervisionado, o programa cita outros paradigmas.',
    [['Aprendizado semissupervisionado',
      'Usa poucos dados rotulados e muitos não rotulados. Exemplos de técnicas: autotreinamento (self-training, o modelo rotula com '
      'alta confiança e reaprende) e propagação de rótulos em grafos. Útil quando rotular é caro.'],
     ['Aprendizado autossupervisionado',
      'Os rótulos vêm dos próprios dados, sem anotação humana: por exemplo, prever uma palavra mascarada em uma frase ou o '
      'próximo token. É a base do pré-treinamento de grandes modelos de linguagem.'],
     ['Aprendizado por reforço',
      'Um agente interage com um ambiente: observa o estado, escolhe uma ação, recebe uma recompensa e busca uma política que '
      'maximize a recompensa acumulada. Conceitos: processo de decisão de Markov, função de valor, Q-learning e o dilema '
      'exploração versus explotação (explorar ações novas ou usar a melhor conhecida).'],
     ['Aprendizado por transferência',
      'Reaproveita um modelo já treinado em uma tarefa ou base grande e o ajusta (fine-tuning) para outra tarefa, com menos dados e menos '
      'custo.'],
     ['Aprendizado ativo',
      'O modelo escolhe quais exemplos não rotulados devem ser rotulados por um especialista, priorizando os mais informativos.']],
    ['Quem Fornece o Rótulo?',
     'Supervisionado: rótulos humanos para todos. Semissupervisionado: só para parte. Autossupervisionado: gerados dos próprios dados. '
     'Não supervisionado: sem rótulos. Por reforço: recompensas do ambiente.'])
sec('12. Redes Neurais e Deep Learning',
    'Redes neurais artificiais são modelos formados por camadas de unidades (neurônios) que combinam entradas com pesos e aplicam uma '
    'função não linear. Deep learning usa redes com muitas camadas.',
    [['Neurônio artificial e funções de ativação',
      'Cada neurônio calcula a soma ponderada das entradas mais um viés (bias) e aplica uma função de ativação: sigmoide (saída de 0 a 1), '
      'tanh (-1 a 1), ReLU (zero para valores negativos, identidade para positivos; muito usada em camadas ocultas) e softmax (transforma '
      'um vetor em probabilidades que somam 1; usada na saída de classificação multiclasse).'],
     ['Treinamento',
      'Função de perda mede o erro (erro quadrático médio em regressão; entropia cruzada em classificação). A retropropagação '
      '(backpropagation) calcula os gradientes e o gradiente descendente (em variantes como SGD, mini-lotes e Adam) atualiza os pesos. '
      'Uma época é uma passagem completa pelos dados de treino.'],
     ['Combate ao overfitting',
      'Regularização L1 e L2, dropout (desliga neurônios aleatoriamente no treino), parada antecipada (early stopping), aumento de dados '
      '(data augmentation) e normalização em lote (batch normalization). O problema do gradiente que desaparece (vanishing gradient) '
      'afeta redes profundas com certas ativações.'],
     ['Arquiteturas',
      'MLP (camadas totalmente conectadas); CNN (convoluções e pooling; imagens); RNN, LSTM e GRU (sequências; o LSTM usa portas de '
      'esquecimento, entrada e saída para reter informação de longo prazo); Transformers (autoatenção, base de LLMs); autoencoders '
      '(compressão e reconstrução); GANs (gerador e discriminador em disputa); modelos de difusão (geram dados removendo ruído '
      'gradualmente).'],
     ['Transformers',
      'Apresentados no artigo "Attention Is All You Need" (2017). Usam autoatenção para relacionar todas as posições de uma sequência '
      'em paralelo, sem recorrência, o que escala bem em GPUs e substituiu as RNNs na maior parte das tarefas de linguagem.'],
     ['Hardware',
      'GPUs e TPUs aceleram as multiplicações de matrizes do treinamento. Modelos maiores costumam melhorar o desempenho, mas isso '
      'depende dos dados e da arquitetura e tem custo alto.']],
    ['Desempenho Não é Independente do Tamanho do Modelo',
     'Aumentar ou reduzir o modelo muda a capacidade e o risco de overfitting. Não há garantia de que a precisão seja a mesma '
     'independentemente do tamanho da rede, inclusive em LSTM.'])
sec('13. IA Generativa e Grandes Modelos de Linguagem (LLMs)',
    'IA generativa cria conteúdo novo (texto, imagem, código, áudio). Os grandes modelos de linguagem (LLMs) são redes Transformer '
    'treinadas em enormes volumes de texto.',
    [['Como funcionam',
      'O texto é dividido em tokens, convertidos em embeddings e processados por camadas de autoatenção. No pré-treinamento, o modelo '
      'aprende a prever o próximo token. A geração produz um token por vez, amostrando da distribuição de probabilidades.'],
     ['Ajuste do modelo',
      'Ajuste fino supervisionado (fine-tuning) e ajuste por instruções treinam o modelo para seguir comandos. O aprendizado por reforço '
      'a partir de feedback humano (RLHF) alinha as respostas às preferências humanas. LoRA é uma técnica de ajuste eficiente em '
      'parâmetros que treina matrizes pequenas em vez de todos os pesos.'],
     ['Prompt e parâmetros de geração',
      'Engenharia de prompt orienta o modelo por instruções, exemplos (few-shot) e contexto. Aprendizado em contexto (in-context learning) '
      'é a capacidade de seguir um padrão dado no próprio prompt. Temperatura maior aumenta a aleatoriedade; top-p e top-k limitam os '
      'tokens candidatos. A janela de contexto limita o tamanho da entrada.'],
     ['RAG (geração aumentada por recuperação)',
      'Busca trechos relevantes em uma base de conhecimento (por similaridade de embeddings em um banco vetorial) e os inclui no prompt, '
      'para que o modelo responda com base neles. Reduz alucinações e permite dados atualizados, mas não as elimina.'],
     ['Limitações e riscos',
      'Alucinações (respostas plausíveis e falsas), vieses dos dados, vazamento de dados sensíveis, injeção de prompt e resultados não '
      'determinísticos. Exigem validação humana em decisões relevantes, controles de acesso e conformidade com a LGPD.'],
     ['Avaliação',
      'Perplexidade (para modelos de linguagem), métricas de sobreposição como BLEU e ROUGE (tradução e resumo), benchmarks de '
      'tarefas e avaliação humana. Nenhuma métrica isolada captura a qualidade geral.']],
    ['RAG Não é Retreinar o Modelo',
     'No RAG, o modelo não é retreinado: a informação externa é recuperada e incluída no contexto a cada consulta. Ajuste fino, '
     'ao contrário, altera os pesos do modelo.'])
sec('14. Agentes Inteligentes e Sistemas Multiagentes',
    'Um agente é uma entidade que percebe o ambiente por sensores e age sobre ele por atuadores, buscando atingir objetivos. Um '
    'agente racional escolhe a ação que maximiza o desempenho esperado (Russell e Norvig).',
    [['Tipos de agentes (Russell e Norvig)',
      'Reativo simples (age só pela percepção atual, por regras), reativo baseado em modelo (mantém um estado interno do ambiente), '
      'baseado em objetivos (escolhe ações que levam ao objetivo), baseado em utilidade (maximiza uma função de utilidade) e agente com '
      'aprendizado (melhora com a experiência).'],
     ['Propriedades do ambiente',
      'Totalmente ou parcialmente observável; determinístico ou estocástico; episódico ou sequencial; estático ou dinâmico; discreto ou '
      'contínuo; agente único ou multiagente.'],
     ['Sistemas multiagentes',
      'Vários agentes autônomos que interagem em um ambiente comum. Aspectos: comunicação (por exemplo, linguagens de comunicação de '
      'agentes, como a FIPA ACL), coordenação, cooperação, competição e negociação. Aplicam-se a simulação, logística e '
      'automação distribuída.'],
     ['Agentes baseados em LLM',
      'Combinam um modelo de linguagem com planejamento, memória e uso de ferramentas (chamada de funções e APIs) em um laço de '
      'raciocínio e ação; o padrão ReAct alterna raciocínio e ações. Protocolos como o MCP (Model Context Protocol) padronizam a '
      'conexão de modelos a ferramentas e dados.'],
     ['Riscos de agentes',
      'Agência excessiva (permissões maiores que o necessário), injeção de prompt por conteúdo externo e ações irreversíveis. '
      'Mitigações: privilégio mínimo, aprovação humana para ações críticas, registro e limites de execução (veja a apostila de '
      'Segurança).']],
    ['Reativo Simples Não Tem Memória',
     'O agente reativo simples decide só pela percepção atual. Para ambientes parcialmente observáveis, é preciso um agente com modelo '
     'interno (estado).'])
sec('15. MLOps: do Notebook à Produção',
    'MLOps aplica práticas de DevOps ao ciclo de vida de modelos de aprendizado de máquina, para implantá-los e mantê-los de forma '
    'confiável e reprodutível.',
    [['O que MLOps acrescenta ao DevOps',
      'Além do código, versiona dados e modelos; automatiza o treinamento; monitora a qualidade do modelo após a implantação. '
      'Além de CI e CD, inclui o treinamento contínuo (CT), que retreina o modelo quando necessário.'],
     ['Componentes',
      'Versionamento de código, dados e modelos; rastreamento de experimentos (por exemplo, MLflow); repositório de atributos (feature '
      'store); pipelines de treinamento, validação e implantação; registro de modelos (model registry); contêineres e orquestração '
      '(Docker, Kubernetes e Kubeflow).'],
     ['Níveis de maturidade (Google)',
      'Nível 0: processo manual. Nível 1: automação do pipeline de ML (treinamento contínuo). Nível 2: automação de CI/CD do pipeline.'],
     ['Formas de implantação',
      'Lote (batch): previsões periódicas. Online: modelo exposto por API (REST ou gRPC), com baixa latência. Fluxo (streaming): '
      'previsões sobre eventos contínuos. Na borda (edge): no dispositivo.'],
     ['Estratégias de liberação',
      'Canário (uma fração do tráfego), azul-verde (duas versões, com troca rápida), sombra (a nova versão recebe cópia do tráfego sem '
      'afetar respostas) e teste A/B.'],
     ['Monitoramento e deriva',
      'Deriva de dados (data drift: a distribuição das entradas muda), deriva de conceito (concept drift: a relação entre entradas e '
      'alvo muda) e queda de desempenho. Também monitorar latência, erros e uso de recursos. Limiares definem quando retreinar.'],
     ['Serviços de nuvem e documentação',
      'Plataformas gerenciadas como Amazon SageMaker, Azure Machine Learning e Google Vertex AI. Cartões de modelo (model cards) e '
      'documentação de conjuntos de dados registram uso pretendido, limitações e métricas.']],
    ['Modelo em Produção Envelhece',
     'Os dados do mundo mudam. Sem monitoramento de deriva e retreino, um modelo bom no dia da implantação perde qualidade com o tempo.'])
sec('16. Ética, Explicabilidade e Governança de IA',
    'A IA aplicada ao setor público exige transparência, justiça e responsabilidade, especialmente quando afeta direitos de '
    'contribuintes.',
    [['Interpretabilidade e explicabilidade',
      'Interpretabilidade: o quanto um humano entende o funcionamento do modelo (árvores e regressões são interpretáveis). Explicabilidade: '
      'métodos que explicam decisões de modelos complexos, como LIME e SHAP (explicações locais, por previsão), importância de atributos e '
      'gráficos de dependência parcial.'],
     ['Viés algorítmico',
      'Pode vir dos dados (amostras não representativas, rótulos enviesados), da modelagem e do uso. Métricas de justiça incluem '
      'paridade demográfica, igualdade de oportunidades e probabilidades equalizadas; em geral não é possível satisfazer todas ao '
      'mesmo tempo.'],
     ['LGPD e decisões automatizadas',
      'O art. 20 da LGPD assegura ao titular o direito de solicitar a revisão de decisões tomadas unicamente com base em tratamento '
      'automatizado de dados pessoais que afetem seus interesses, e o direito a informações claras sobre os critérios e '
      'procedimentos, observados os segredos comercial e industrial.'],
     ['Referências regulatórias e normativas',
      'NIST AI Risk Management Framework 1.0 (funções Governar, Mapear, Medir e Gerenciar); ISO/IEC 42001:2023 (sistema de gestão '
      'de IA); Regulamento (UE) 2024/1689, o AI Act europeu, com abordagem baseada em risco (risco inaceitável, alto, limitado e '
      'mínimo). No Brasil, o Projeto de Lei nº 2.338/2023, sobre IA, está em tramitação: conferir a situação atual.'],
     ['Boas práticas',
      'Transparência sobre o uso de IA, supervisão humana em decisões relevantes, testes de viés, documentação de dados e modelos, '
      'registro de decisões (auditabilidade) e minimização de dados pessoais.']],
    ['Explicar e Poder Contestar',
     'Em decisões automatizadas que afetam o contribuinte, a explicabilidade e a possibilidade de revisão (LGPD, art. 20) são '
     'requisitos, não opcionais.'])
sec('17. Avaliação de Regressão e Boas Práticas de Modelagem',
    'Complementa a seção 6 com métricas de regressão e cuidados para modelos confiáveis.',
    [['Métricas de regressão',
      'MAE (erro absoluto médio), MSE (erro quadrático médio), RMSE (raiz do MSE, na mesma unidade do alvo, penaliza mais os erros '
      'grandes) e R² (proporção da variância explicada pelo modelo, de 0 a 1 em casos usuais; R² ajustado penaliza atributos '
      'inúteis).'],
     ['Pressupostos da regressão linear',
      'Linearidade, independência dos erros, homocedasticidade (variância constante dos resíduos) e normalidade dos resíduos (importante '
      'para inferência). Multicolinearidade entre preditores prejudica a interpretação dos coeficientes.'],
     ['Divisão dos dados e vazamento',
      'Treino, validação (ajuste de hiperparâmetros) e teste (avaliação final, usado uma vez). Vazamento de dados (data leakage) ocorre '
      'quando informação do teste ou do futuro vaza para o treino, inflando o desempenho; por exemplo, escalonar antes de dividir.'],
     ['Desbalanceamento de classes',
      'Reamostragem (subamostragem da classe majoritária, sobreamostragem da minoritária, SMOTE, que sintetiza exemplos), pesos de '
      'classe, ajuste do limiar de decisão e métricas apropriadas (Precisão, Revocação, F1, PR-AUC).'],
     ['Ajuste de hiperparâmetros',
      'Busca em grade (grid search), busca aleatória (random search) e otimização bayesiana, sempre com validação cruzada. Hiperparâmetros '
      'são definidos antes do treino; parâmetros (como pesos) são aprendidos.'],
     ['Seleção de atributos',
      'Métodos de filtro (estatísticas univariadas), de envelope (wrapper, como eliminação recursiva) e embutidos (como Lasso e '
      'importância em árvores).']],
    ['Teste Só no Final',
     'O conjunto de teste não deve orientar decisões de modelagem. Se for reutilizado para escolher modelos, deixa de estimar '
     'bem o desempenho real.'])
sec('18. Hadoop e Spark: Complementos',
    'Complementa as seções 7 e 8 com pontos frequentes sobre o ecossistema Hadoop e o Spark.',
    [['Alta disponibilidade do HDFS',
      'O NameNode é um ponto único de falha em configuração simples. Com alta disponibilidade, há um NameNode ativo e um em espera '
      '(standby), com JournalNodes para compartilhar o log de edições. O Secondary NameNode não é um backup em espera: ele apenas faz '
      'pontos de verificação (checkpoints) dos metadados.'],
     ['Codificação de eliminação (Hadoop 3)',
      'A replicação tripla consome 200% de espaço extra. A codificação de eliminação (erasure coding) protege os dados com paridade e '
      'tem menor custo de armazenamento, ao custo de mais processamento.'],
     ['YARN em detalhe',
      'ResourceManager (escalonador e gestor de aplicações), NodeManager (por nó), ApplicationMaster (por aplicação, negocia recursos) e '
      'containers (unidades de recursos onde as tarefas executam).'],
     ['MapReduce: Combiner e Partitioner',
      'O combiner faz uma agregação local antes do shuffle, reduzindo tráfego de rede. O partitioner define a qual reducer cada chave '
      'vai (por padrão, por hash da chave).'],
     ['Ferramentas do ecossistema Hadoop',
      'Hive (consultas em SQL sobre dados no HDFS, com HiveQL), HBase (banco NoSQL colunar sobre HDFS), Pig (scripts de fluxo de '
      'dados), Sqoop (transferência entre Hadoop e bancos relacionais), Flume (ingestão de logs), Oozie (orquestração de fluxos) e '
      'ZooKeeper (coordenação distribuída).'],
     ['Spark: transformações estreitas e largas',
      'Estreitas (map, filter): cada partição de saída depende de uma partição de entrada, sem shuffle. Largas (reduceByKey, groupByKey, '
      'join): exigem shuffle entre partições, definindo fronteiras de estágios do DAG. reduceByKey agrega localmente antes do '
      'shuffle e tende a ser preferível ao groupByKey.'],
     ['Spark: DataFrames, cache e desempenho',
      'DataFrames e Datasets têm esquema e passam pelo otimizador Catalyst; RDDs não. cache() e persist() mantêm dados em memória para '
      'reutilização. Junção por broadcast envia uma tabela pequena a todos os executors. A execução adaptativa de consultas (AQE) '
      'ajusta o plano em tempo de execução. Assimetria de dados (data skew) causa tarefas lentas.']],
    ['Secondary NameNode Não é Reserva',
     'Pegadinha clássica: o Secondary NameNode não assume o lugar do NameNode em caso de falha. A alta disponibilidade usa um '
     'NameNode standby.'])
sec('19. Python para Ciência de Dados: NumPy, pandas e scikit-learn',
    'Python é a linguagem mais usada em ciência de dados, com um ecossistema de bibliotecas.',
    [['NumPy',
      'Arrays multidimensionais homogêneos (ndarray) com operações vetorizadas, mais rápidas que laços em Python. Atributos: shape (dimensões), '
      'dtype (tipo) e ndim. Broadcasting permite operar arrays de formas compatíveis.'],
     ['pandas',
      'Series (uma dimensão) e DataFrame (tabela com linhas e colunas rotuladas). Operações comuns: head(), info(), describe(), '
      'groupby(), merge() (junções), fillna() e dropna() (ausentes), apply() e leitura de arquivos (read_csv, read_parquet). O atributo '
      'shape de um DataFrame retorna a tupla (linhas, colunas).'],
     ['Seleção em pandas',
      'loc seleciona por rótulos e iloc por posições inteiras. Máscaras booleanas filtram linhas (df[df["valor"] > 100]).'],
     ['scikit-learn',
      'API consistente: fit() treina, predict() prediz e transform() transforma; fit_transform() combina os dois. Pipeline encadeia '
      'pré-processamento e modelo, evitando vazamento. Módulos para divisão de dados, validação cruzada, métricas e busca de '
      'hiperparâmetros.'],
     ['Visualização e ambiente',
      'Matplotlib, seaborn e plotly para gráficos. Jupyter Notebook para exploração interativa. PySpark leva a API do Spark para '
      'Python e usa DataFrames distribuídos.'],
     ['Boas práticas',
      'Ambientes virtuais e arquivos de dependências para reprodutibilidade; fixar sementes aleatórias; código de pipelines fora de '
      'notebooks quando for para produção.']],
    ['shape Devolve Tupla, size Devolve Total',
     'Em NumPy e pandas, shape devolve as dimensões (linhas, colunas), e size, o número total de elementos (linhas vezes colunas).'])
sec('20. Referências e Conferência',
    'Conferência realizada em 21/09/2026.',
    [['Referências',
      'Russell e Norvig, Artificial Intelligence: A Modern Approach; Goodfellow, Bengio e Courville, Deep Learning; Hastie, Tibshirani e '
      'Friedman, The Elements of Statistical Learning e ISLR; Géron, Hands-On Machine Learning; Vaswani et al., Attention Is All You Need '
      '(2017); Lewis et al. (RAG, 2020); Hu et al. (LoRA, 2021); Yao et al. (ReAct, 2022); documentação do Apache Hadoop, Apache Spark, '
      'scikit-learn, pandas e MLflow; NIST AI RMF 1.0; ISO/IEC 42001:2023; Lei nº 13.709/2018 (art. 20); Edital SEFAZ-CE 2026 (FCC), '
      'Anexo VI.'],
     ['Corrigido nesta revisão',
      'Fórmulas em LaTeX (apareciam literais no PDF) reescritas em texto; "70% a 80% do esforço" atribuído com ressalva; "obrigatoriamente '
      'padronizadas" para redes neurais reformulado; DBSCAN "imune" reformulado com limitações; Spark "até 100 vezes" atribuído aos '
      'benchmarks do projeto e Mesos marcado como depreciado; embeddings do BERT diferenciados dos estáticos; lematização de '
      '"melhores"; C4.5 usa razão de ganho; Random Forest "sem aumentar o viés" suavizado; Porter é para inglês; seção de armadilhas '
      'atribuída às bancas sem evidência.'],
     ['A conferir',
      'Situação do Projeto de Lei nº 2.338/2023 e do MCP; versões e recursos das bibliotecas; valores de referência de benchmarks; '
      'exemplos de plataformas de nuvem citados.']],
    ['Regra de Conteúdo', 'Este material não afirma nada sem fonte. Se houver divergência com a documentação oficial, ela prevalece.'])

ap['subtitle'] = ('CRISP-DM, Machine Learning, Ensembles, Agrupamento, Avaliação, Deep Learning, IA Generativa e LLMs, Agentes, MLOps, '
                  'Ética e Governança de IA, Hadoop, Spark, PLN e Python')
json.dump(dados, open(ARQ, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('Ciência de Dados atualizada: %d seções.' % len(S))
