"""Aplica a auditoria da Apostila de Banco de Dados e BI (Fase 1) e acrescenta as seções de Engenharia de Dados do
programa SEFAZ-CE 2026 (B02) e do edital SEFAZ-BA 2022. Idempotente.
Relatório: dados/auditoria_apostilas/05_dados.md
Uso (na pasta do app): python dados/auditoria_apostilas/aplicar_05_dados.py
"""
import json
import os
import sys

APP = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARQ = os.path.join(APP, 'apostilas_conteudo.json')
dados = json.load(open(ARQ, encoding='utf-8'))
ap = next(a for a in dados if 'Banco_Dados' in a['filename'])
S = ap['sections']

if any(s['title'].startswith('11.') for s in S):
    print('Apostila de Dados já atualizada; nada a fazer.')
    sys.exit(0)


def bul(sec, inicio):
    return next(b for b in sec['bullets'] if b[0].strip().startswith(inicio))


def trocar(txt, velho, novo):
    assert velho in txt, 'trecho não encontrado: ' + velho[:70]
    return txt.replace(velho, novo)


# ---- Seção 2 (ER) ----
S[1]['tip'][1] = trocar(S[1]['tip'][1], 'Muitos-para-Mutos', 'Muitos-para-Muitos')

# ---- Seção 3 (normalização) ----
S[2]['tip'] = ['Mnemônico das Três Primeiras Formas Normais',
               'A frase atribuída a William Kent resume: todo atributo não chave deve depender da chave (1FN), de toda a chave (2FN) e de '
               'nada além da chave (3FN). A variação "so help me Codd" é um trocadilho conhecido, não parte da definição.']

# ---- Seção 4 (SQL) ----
b = bul(S[3], 'Comandos DDL')
b[1] = ('CREATE (cria tabelas, esquemas, visões e índices), ALTER (altera estruturas), DROP (remove objetos) e TRUNCATE TABLE (remove '
        'todos os registros de uma tabela de forma rápida, liberando páginas de dados, sem WHERE, sem disparar triggers de linha e '
        'com registro mínimo no log). O TRUNCATE é tratado como DDL na maioria dos SGBDs, embora o padrão SQL o inclua entre os '
        'comandos de dados; confira a classificação adotada pelo enunciado.')
S[3]['tip'] = ['Diferença Crítica: TRUNCATE versus DELETE',
               'DELETE é DML: remove linhas, aceita WHERE, registra cada exclusão no log e dispara triggers. TRUNCATE remove todas as '
               'linhas de uma vez, não aceita WHERE, é muito mais rápido e não dispara triggers de linha. Quanto ao contador de '
               'auto-incremento, o efeito depende do SGBD (MySQL e SQL Server o reiniciam; o PostgreSQL só com RESTART IDENTITY). Quanto '
               'ao rollback, também varia: em Oracle e MySQL o TRUNCATE confirma implicitamente; em SQL Server e PostgreSQL pode ser '
               'desfeito dentro de uma transação.']

# ---- Seção 5 (SQL avançado) ----
b = bul(S[4], 'Agrupamento e Filtragem')
b[1] = ('A cláusula WHERE filtra as linhas individuais ANTES do agrupamento. A cláusula HAVING filtra os grupos gerados pelo GROUP BY, '
        'normalmente com condições sobre funções agregadas (COUNT, SUM, AVG, MIN, MAX) ou sobre as colunas de agrupamento.')
b = bul(S[4], 'Operadores de Conjunto')
b[1] = ('UNION combina o resultado de duas consultas compatíveis e ELIMINA linhas duplicadas (o que pode exigir ordenação ou hash). '
        'UNION ALL preserva todas as linhas, com desempenho em geral superior por não precisar eliminar duplicatas.')

# ---- Seção 7 (NoSQL e CAP) ----
b = bul(S[6], 'O Teorema CAP')
b[1] = ('O teorema de Brewer afirma que um sistema distribuído não consegue oferecer, ao mesmo tempo, as três propriedades: Consistência '
        '(C, todos os nós veem o mesmo dado; no sentido de linearizabilidade), Disponibilidade (A, toda requisição a um nó funcional '
        'recebe resposta) e Tolerância a Partições de rede (P, o sistema continua operando com falha de comunicação entre nós). '
        'Como partições de rede acontecem em sistemas distribuídos, na prática a escolha é, durante a partição, entre manter a '
        'consistência (CP) ou a disponibilidade (AP). O modelo PACELC estende a ideia: se há partição (P), escolhe-se entre A e C; senão '
        '(E, else), escolhe-se entre latência (L) e consistência (C).')
b = bul(S[6], 'Família NoSQL de Grafos')
b[1] = ('Estruturados em vértices (nós), arestas (relacionamentos) e propriedades. Otimizados para percorrer redes de relacionamentos. '
        'Exemplos: Neo4j e Amazon Neptune. São úteis em cenários como rastreamento de vínculos societários e detecção de fraudes em '
        'rede.')
S[6]['tip'] = ['CAP: a Escolha Acontece na Partição',
               'Sistemas distribuídos precisam tolerar partições. Durante a partição, escolhem entre consistência (CP) e disponibilidade '
               '(AP). Um sistema de nó único, sem partição de rede, não se enquadra na discussão de CAP.']

# ---- Seção 8 (BI e DAMA) ----
b = bul(S[7], 'Governança de Dados com DAMA-DMBOK')
b[0] = 'Governança de Dados e o DAMA-DMBOK (2ª edição)'
b[1] = ('O DAMA-DMBOK2 organiza a gestão de dados em 11 áreas de conhecimento, com a Governança de Dados no centro: Governança de Dados; '
        'Arquitetura de Dados; Modelagem e Projeto de Dados; Armazenamento e Operações de Dados; Segurança de Dados; Integração e '
        'Interoperabilidade de Dados; Gestão de Documentos e Conteúdo; Dados Mestres e de Referência; Data Warehousing e Business '
        'Intelligence; Metadados; e Qualidade de Dados. A ética no tratamento de dados é tema de um capítulo próprio, não uma das 11 '
        'áreas.')

# ---- Seção 9 (dimensional) ----
b = bul(S[8], 'Tipos Especiais de Dimensões')
b[1] = b[1] + (' Existem ainda variações usadas na literatura de Kimball: SCD Tipo 0 (mantém o valor original), Tipo 4 (mini-dimensão) e '
               'Tipo 6 (combina os tipos 1, 2 e 3).')
S[8]['tip'] = ['Alerta de Prova - Surrogate Key',
               'Na modelagem dimensional recomenda-se que as dimensões usem chave substituta (surrogate key), artificial e sequencial, em vez '
               'da chave natural do sistema de origem. Isso isola o DW de mudanças nos sistemas transacionais e viabiliza SCD Tipo 2, em que a '
               'mesma chave natural aparece em várias linhas de dimensão.']

# ---- Seção 10 (armadilhas) ----
S[9]['title'] = '10. Armadilhas Conceituais Recorrentes em Banco de Dados e BI'
S[9]['content'] = ('Pontos conceituais que costumam gerar erro em questões sobre banco de dados e BI. Servem de revisão rápida; a base de '
                   'cada ponto está nas seções anteriores.')
for i, bl in enumerate(S[9]['bullets']):
    if bl[0].startswith('Pegadinha 7'):
        S[9]['bullets'][i] = ['Pegadinha 7: Triggers e Transações',
                              'O trigger executa no contexto da instrução que o disparou. Se ele falhar, a instrução é desfeita; o '
                              'efeito sobre a transação como um todo depende do SGBD e da configuração.']
    if bl[0].startswith('Pegadinha 8'):
        S[9]['bullets'][i] = ['Pegadinha 8: Níveis de Isolamento e Leitura Fantasma',
                              'Pelo padrão ANSI, Repeatable Read impede leitura não repetível, mas pode permitir leitura fantasma; só '
                              'Serializable impede todas as anomalias. Na prática, alguns SGBDs (como PostgreSQL e o InnoDB do MySQL) '
                              'previnem fantasmas em Repeatable Read; siga o padrão a menos que o enunciado cite o produto.']

# ---- Seções novas ----
def sec(t, c, bl, tip):
    S.append({'title': t, 'content': c, 'bullets': bl, 'tip': tip})


sec('11. Índices, Otimização de Consultas e Administração de SGBDs',
    'O desempenho de um banco depende de como os dados são organizados e acessados. Esta seção reúne índices, planos de execução e '
    'pontos de administração dos SGBDs citados no programa (Oracle, SQL Server e PostgreSQL).',
    [['Índices',
      'B-tree (árvore balanceada, o padrão; bom para igualdade, faixa e ordenação), hash (só igualdade), bitmap (poucos valores '
      'distintos, comum em DW no Oracle). Índice composto respeita a ordem das colunas. Índice de cobertura (covering) contém todas as '
      'colunas da consulta, evitando ir à tabela. Índices aceleram leituras, mas custam espaço e desaceleram escritas.'],
     ['Clusterizado e não clusterizado',
      'No SQL Server, o índice clusterizado define a ordem física das linhas da tabela (só um por tabela); os não clusterizados são '
      'estruturas separadas que apontam para as linhas.'],
     ['Plano de execução e estatísticas',
      'O otimizador escolhe o plano com base em estatísticas (cardinalidade, seletividade). EXPLAIN (PostgreSQL e MySQL) e o plano de '
      'execução do Oracle e do SQL Server mostram acessos e junções. Estatísticas desatualizadas levam a planos ruins.'],
     ['Algoritmos de junção',
      'Nested loop (laço aninhado, bom com poucas linhas e índice), hash join (constrói tabela hash de uma entrada; bom para grandes '
      'volumes sem índice) e merge join (junção por ordenação e intercalação; usa entradas ordenadas).'],
     ['Particionamento',
      'Divide tabelas grandes por faixa (range), lista (list) ou hash. Melhora gestão e desempenho (poda de partições) e facilita '
      'arquivar dados antigos.'],
     ['Recuperação e alta disponibilidade',
      'Recuperação a um ponto no tempo (PITR): restauração de um backup completo mais reaplicação dos logs. Oracle: RMAN, Data Guard e RAC. '
      'SQL Server: modelos de recuperação Full, Bulk-logged e Simple; Always On e log shipping. PostgreSQL: arquivamento de WAL, '
      'replicação por streaming, MVCC e VACUUM.']],
    ['Índice Ajuda a Ler e Atrapalha a Escrever',
     'Cada índice adicional precisa ser atualizado a cada INSERT, UPDATE e DELETE. Crie índices para consultas frequentes e seletivas, '
     'não para todas as colunas.'])
sec('12. SQL Procedural: PL/SQL, T-SQL, PL/pgSQL e CTE',
    'Extensões procedurais permitem lógica no servidor de banco. Cada SGBD tem a sua: PL/SQL (Oracle), T-SQL (SQL Server) e PL/pgSQL '
    '(PostgreSQL).',
    [['PL/SQL (Oracle)',
      'Linguagem procedural em blocos: DECLARE (declarações), BEGIN (comandos), EXCEPTION (tratamento de erros) e END. Permite '
      'variáveis, condicionais, laços, cursores, procedimentos, funções, triggers e pacotes (packages, que agrupam código relacionado).'],
     ['Cursores',
      'Percorrem o resultado de uma consulta linha a linha. Costumam ser mais lentos que operações em conjunto (set-based); prefira '
      'uma instrução SQL única quando possível.'],
     ['Procedimento e função',
      'Função retorna um valor e pode ser usada em expressões SQL; procedimento executa ações e não é usado dentro de uma expressão. '
      'Ambos são compilados e armazenados no banco.'],
     ['Tratamento de exceções',
      'Erros são capturados em blocos de exceção (EXCEPTION no PL/SQL, TRY...CATCH no T-SQL, EXCEPTION no PL/pgSQL), com reversão '
      'parcial ou total da transação conforme o caso.'],
     ['CTE e consultas recursivas',
      'A cláusula WITH define uma expressão de tabela comum (CTE), que organiza consultas complexas. CTE recursiva percorre hierarquias '
      '(por exemplo, estrutura de cargos ou de categorias).']],
    ['Prefira Operações em Conjunto',
     'SQL é declarativo e otimizado para conjuntos. Laços e cursores linha a linha são a exceção, não a regra.'])
sec('13. Concorrência e Recuperação em Profundidade',
    'Complementa a seção 6 com variações do bloqueio em duas fases, deadlock, MVCC e recuperação.',
    [['2PL estrito e rigoroso',
      'O 2PL básico tem fase de crescimento e fase de encolhimento. No 2PL estrito (strict), a transação não libera seus bloqueios '
      'exclusivos (de gravação) até confirmar ou abortar, evitando leituras de dados não confirmados. No 2PL rigoroso (rigorous), ela '
      'não libera nenhum bloqueio, compartilhado ou exclusivo, até confirmar ou abortar. O bloqueio conservador obtém todos os '
      'bloqueios antes de iniciar.'],
     ['Deadlock',
      'Ocorre quando transações esperam umas pelas outras em ciclo. Detecção: grafo de espera (wait-for graph) com ciclo e escolha de '
      'vítima para abortar. Prevenção: esquemas como wait-die e wound-wait, baseados em timestamps.'],
     ['Ordenação por timestamp e MVCC',
      'A ordenação por timestamp atribui a cada transação um carimbo e rejeita operações fora de ordem. No MVCC (controle de '
      'concorrência multiversão), o SGBD mantém versões dos dados: leitores enxergam um instantâneo consistente sem bloquear escritores '
      'e vice-versa (usado, por exemplo, em PostgreSQL e Oracle).'],
     ['Recuperação (ARIES)',
      'Baseada em log com WAL e pontos de verificação (checkpoints). O algoritmo ARIES usa as políticas steal (páginas sujas podem ir ao '
      'disco antes do commit) e no-force (não é preciso forçar as páginas ao disco no commit) e três fases na recuperação: análise, '
      'refazer (redo) e desfazer (undo).'],
     ['Granularidade e bloqueios',
      'Bloqueios podem ser em linha, página, tabela ou banco; granularidade menor aumenta a concorrência, e a maior reduz a '
      'sobrecarga. Bloqueios de intenção (IS, IX, SIX) sinalizam bloqueios em níveis inferiores.']],
    ['Estrito Segura os Exclusivos, Rigoroso Segura Todos',
     'Strict 2PL: mantém os bloqueios exclusivos até o fim da transação. Rigorous 2PL: mantém todos os bloqueios até o fim. Não confundir '
     'com o protocolo de duas fases básico.'])
sec('14. Bancos Colunares, Formatos de Arquivo e Outros Modelos',
    'O modo de armazenar os dados (por linha ou por coluna) muda muito o desempenho conforme o uso.',
    [['Armazenamento por linha e por coluna',
      'Por linha: os valores de uma linha ficam juntos; bom para OLTP, com leitura e escrita de registros inteiros. Por coluna: os '
      'valores de cada coluna ficam juntos; bom para OLAP, pois lê só as colunas necessárias e comprime melhor, mas é menos indicado '
      'para muitas escritas de linhas isoladas. Exemplos de bancos colunares analíticos: ClickHouse, Amazon Redshift e Google BigQuery.'],
     ['Formatos de arquivo',
      'CSV e JSON são texto e legíveis. XML é hierárquico e verboso. Avro é binário orientado a linha, com esquema embutido, comum em '
      'streaming (Kafka). Parquet e ORC são binários colunares, com compressão e leitura seletiva de colunas, usados em data lakes.'],
     ['Particionamento e compressão em data lakes',
      'Dados em Parquet costumam ser particionados em diretórios por coluna (por exemplo, ano e mês), permitindo ler só as partições '
      'necessárias. Compressão (como Snappy e Zstandard) reduz espaço e I/O.'],
     ['Outros modelos',
      'Séries temporais (InfluxDB, TimescaleDB) para dados indexados no tempo; NewSQL (como CockroachDB e Google Spanner), que combina '
      'SQL e transações ACID com escala horizontal; mecanismos de busca (Elasticsearch) para texto.']],
    ['Coluna para Analisar, Linha para Transacionar',
     'Formato colunar favorece consultas analíticas sobre poucas colunas de muitas linhas. Formato por linha favorece operações '
     'transacionais sobre linhas inteiras.'])
sec('15. Arquiteturas de Dados: DW, Data Mart, Data Lake, Lakehouse e Data Mesh',
    'As arquiteturas de dados evoluíram do DW tradicional para modelos que unem flexibilidade e governança.',
    [['Data Mart',
      'Subconjunto do DW voltado a uma área ou assunto. Dependente: alimentado pelo DW corporativo. Independente: construído direto '
      'das fontes.'],
     ['Data Lake em camadas (medalhão)',
      'Organiza os dados em zonas de qualidade crescente: bruta (bronze), refinada (silver) e pronta para consumo (gold). Guarda dados '
      'brutos em diversos formatos, com esquema na leitura.'],
     ['Lakehouse',
      'Combina a flexibilidade e o baixo custo do data lake com recursos de DW: transações ACID, aplicação de esquema, viagem no tempo '
      '(time travel) e desempenho em SQL, por meio de formatos de tabela abertos como Delta Lake, Apache Iceberg e Apache Hudi.'],
     ['Data Mesh (Zhamak Dehghani)',
      'Abordagem sociotécnica descentralizada, com quatro princípios: propriedade dos dados orientada a domínios; dados como produto; '
      'plataforma de dados self-service; e governança federada e computacional.'],
     ['Data Fabric',
      'Arquitetura que usa metadados e automação para integrar e governar dados distribuídos em várias fontes, sem necessariamente '
      'mover tudo para um único repositório.'],
     ['Lambda e Kappa',
      'Lambda combina uma camada em lote e uma camada de velocidade (streaming) e mescla os resultados. Kappa usa apenas '
      'processamento de fluxo, reprocessando o log quando necessário.']],
    ['Mesh Descentraliza, Lakehouse Unifica',
     'Data Mesh trata de organização e propriedade (domínios, dados como produto). Lakehouse trata de tecnologia de armazenamento e '
     'consulta (lake com ACID). São conceitos de planos diferentes.'])
sec('16. Integração e Ingestão de Dados: Formatos, APIs e Segurança',
    'A captação de dados envolve escolher a forma de acesso, o formato e as proteções durante a coleta e o trânsito.',
    [['Fontes e estilos de integração',
      'Lote (batch, cargas periódicas de arquivos ou tabelas), API (REST com JSON, ou SOAP com XML e contrato WSDL), mensageria e '
      'eventos, e CDC (captura de alterações do log do banco, tratada na apostila de Middleware).'],
     ['REST e SOAP',
      'REST é um estilo arquitetural sobre HTTP, com recursos identificados por URI e métodos HTTP, geralmente com JSON. SOAP é um '
      'protocolo baseado em XML com contrato formal (WSDL) e extensões (como WS-Security).'],
     ['Segurança na captação',
      'Criptografia em trânsito com TLS; autenticação e autorização (chaves de API, OAuth 2.0, TLS mútuo); minimização, mascaramento e '
      'pseudonimização de dados pessoais conforme a LGPD; controle de acesso e trilha de auditoria.'],
     ['Buffer, ordenação e integridade',
      'Buffers e filas absorvem picos e aplicam contrapressão (backpressure). Ordenação: distinga tempo do evento e tempo de '
      'processamento. Integridade: validação de esquema, somas de verificação (checksums) e cargas idempotentes para tolerar reenvio.'],
     ['Cargas completas e incrementais',
      'Completa: recarrega tudo. Incremental: carrega só o que mudou, usando marca de data ("marca d\'água", high-water mark) ou CDC. '
      'Upsert (MERGE) atualiza registros existentes e insere os novos.']],
    ['Reenvio é Normal, Carga Idempotente é a Defesa',
     'Falhas e reenvios podem duplicar dados. Cargas idempotentes (upsert por chave, deduplicação) garantem o mesmo resultado ao repetir.'])
sec('17. Pipelines de Dados: ETL, ELT, Orquestração e Tolerância a Falhas',
    'Um pipeline move e transforma dados de forma automatizada, confiável e auditável.',
    [['ETL e ELT',
      'ETL transforma antes de carregar, em área intermediária (staging). ELT carrega primeiro e transforma no destino, aproveitando o '
      'poder do DW ou do lakehouse. Ferramentas como o dbt organizam transformações em SQL versionadas dentro do destino.'],
     ['Orquestração',
      'Coordena a ordem e as dependências das etapas. O Apache Airflow define pipelines como DAGs (grafos acíclicos dirigidos) de tarefas, '
      'com agendamento, reexecução e monitoramento.'],
     ['Tolerância a falhas',
      'Tentativas repetidas (retries), com espera crescente (exponential backoff); pontos de verificação (checkpoints) para retomar do '
      'ponto em que parou; tarefas idempotentes; quarentena ou fila de mensagens mortas para registros inválidos; reprocessamento '
      '(backfill) de períodos passados.'],
     ['Pipelines como código',
      'Definições versionadas em Git, revisão de código, testes automatizados (de dados e de transformações), integração e entrega '
      'contínuas (CI/CD) e ambientes separados de desenvolvimento, homologação e produção.'],
     ['Registro, auditoria e linhagem',
      'Logs estruturados de cada execução, contagem de registros lidos, gravados e rejeitados, e metadados de linhagem (de onde vem cada '
      'dado e por quais transformações passou), úteis para auditoria e depuração.']],
    ['Pipeline Bom é Repetível e Observável',
     'Deve poder rodar de novo sem duplicar dados (idempotência), avisar quando falha (monitoramento) e permitir rastrear a origem de '
     'cada valor (linhagem).'])
sec('18. Governança e Qualidade de Dados',
    'Governança define regras, papéis e processos para tratar os dados como ativo. Qualidade de dados mede se eles servem ao uso pretendido.',
    [['Dimensões da qualidade de dados',
      'Completude, unicidade, oportunidade (timeliness), validade, acurácia e consistência (as seis dimensões da DAMA UK). Cada uma '
      'pode ter regras e indicadores medidos por perfilamento (profiling) e validações.'],
     ['Metadados, catálogo e glossário',
      'Metadados descrevem os dados: técnicos (esquema, tipos), de negócio (significado, dono) e operacionais (carga, volume). O '
      'catálogo de dados torna os ativos pesquisáveis; o glossário de negócio padroniza termos.'],
     ['Linhagem',
      'Mostra a origem e o caminho dos dados, permitindo análise de impacto e auditoria.'],
     ['Papéis',
      'Dono dos dados (data owner: responsável pela decisão sobre o dado), curador ou steward (garante qualidade e definições) e '
      'custodiante (gerencia tecnicamente o armazenamento e a segurança).'],
     ['Dados mestres e deduplicação',
      'Gestão de dados mestres (MDM) mantém uma visão única e confiável de entidades como contribuinte e produto (o "registro de '
      'ouro"). Deduplicação identifica registros duplicados por regras e medidas de similaridade, com blocagem para reduzir '
      'comparações.'],
     ['Políticas de acesso e conformidade',
      'Controle por papéis (RBAC) ou atributos (ABAC), segurança em nível de linha e de coluna, mascaramento de dados sensíveis, '
      'classificação de dados e conformidade com a LGPD.']],
    ['Qualidade Depende do Uso',
     'Um dado pode ser adequado a uma análise e insuficiente para outra. Por isso as regras de qualidade são definidas com o negócio.'])
sec('19. Streaming e Processamento em Tempo Real',
    'O processamento de fluxo trata eventos continuamente, com baixa latência, em vez de esperar lotes.',
    [['Lote versus fluxo',
      'Lote processa grandes volumes em intervalos, priorizando vazão (throughput). Fluxo processa eventos ao chegarem, priorizando '
      'latência. Há sempre compromisso entre latência, vazão e custo.'],
     ['Tempo do evento e tempo de processamento',
      'Tempo do evento é quando o fato ocorreu; tempo de processamento é quando o sistema o vê. Eventos podem chegar fora de ordem ou '
      'atrasados; marcas d\'água (watermarks) estimam até quando esperar por dados atrasados.'],
     ['Janelas',
      'Tumbling (fixas e sem sobreposição), sliding ou hopping (sobrepostas, deslizam em passos) e de sessão (agrupam eventos por '
      'períodos de atividade, encerrados por inatividade).'],
     ['Spark Structured Streaming',
      'API sobre o Spark SQL que trata o fluxo como uma tabela que cresce continuamente. O modo padrão executa em micro-lotes. '
      'Usa checkpoints e permite semântica de exatamente uma vez com fontes e destinos apropriados.'],
     ['Kafka e outros motores',
      'O Kafka é a base comum de transporte e armazenamento dos eventos (veja a apostila de Middleware). Apache Flink é um motor '
      'de processamento de fluxo com estado, voltado a processamento evento a evento.'],
     ['Particionamento e escalabilidade',
      'O paralelismo vem de particionar os dados por chave; o número de partições limita o paralelismo dos consumidores. '
      'Chaves muito desbalanceadas geram partições quentes (hot partitions).']],
    ['Janela Fixa, Deslizante ou de Sessão',
     'Tumbling: blocos consecutivos sem sobreposição. Sliding: blocos que se sobrepõem. Session: blocos definidos pela atividade do '
     'usuário, encerrados por um intervalo de inatividade.'])
sec('20. Referências e Conferência',
    'Conferência realizada em 21/09/2026.',
    [['Referências',
      'Elmasri e Navathe, Sistemas de Banco de Dados; Silberschatz, Korth e Sudarshan; Kimball e Ross, The Data Warehouse Toolkit; Inmon; '
      'DAMA-DMBOK 2ª edição; Kleppmann, Designing Data-Intensive Applications; documentação oficial de PostgreSQL, Oracle, SQL Server, '
      'Apache Spark, Airflow, Delta Lake, Iceberg e Hudi; Dehghani, Data Mesh; Edital SEFAZ-CE 2026 (FCC), Anexo VI, e Edital '
      'SEFAZ-BA 2022 (FGV), Anexo I.'],
     ['Corrigido nesta revisão',
      'Lista das 11 áreas do DAMA-DMBOK (Ética não é uma das 11; Governança de Dados é); "TRUNCATE sempre reinicia auto-incremento e é DDL" '
      '(depende do SGBD); "nenhum sistema distribuído pode ser CA" (reformulado com o contexto da partição e o PACELC); HAVING '
      '"exclusivamente" sobre agregações; UNION "com ordenação implícita"; uso de grafos "no Fisco" sem fonte; trigger e rollback '
      'automático da transação (depende do SGBD); Repeatable Read e fantasmas (nuance por SGBD); afirmação absoluta sobre chave substituta; '
      'seção de armadilhas atribuída às bancas sem evidência.'],
     ['A conferir',
      'Comportamento específico por SGBD e versão (TRUNCATE, isolamento, PITR); formatos de tabela abertos (Delta, Iceberg, Hudi) e suas '
      'versões; ferramentas citadas como exemplo.']],
    ['Regra de Conteúdo', 'Este material não afirma nada sem fonte. Se houver divergência com a documentação do produto, a documentação prevalece.'])

ap['subtitle'] = ('Modelagem, Álgebra, SQL, Normalização, ACID e Concorrência, Índices e Otimização, PL/SQL, NoSQL e CAP, Colunar, DW e OLAP, '
                  'Lakehouse e Data Mesh, Ingestão, Pipelines, Qualidade de Dados, Streaming e DAMA-DMBOK')
json.dump(dados, open(ARQ, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('Dados atualizada: %d seções.' % len(S))
