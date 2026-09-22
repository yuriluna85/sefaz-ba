"""Reconstrói as questões reais da SEFAZ-CE 2021 (CEBRASPE, Auditor Fiscal de TI) no questions.json.

Fonte: caderno oficial (dados/sefaz_ce_2021_itens.json, extraído do PDF da prova) e gabarito
oficial definitivo (conferido: 59/60 dos básicos e 99/100 dos específicos; itens 29 e 81 anulados
e por isso ausentes do banco).

- Reconstrói o enunciado com o comando do bloco e o texto-base de cada item.
- Reclassifica assunto/tópico pelo conteúdo real do item (a classificação antiga era por posição).
- Define escopo (edital SEFAZ-BA 2022 / correlato / fora) e os cargos em que o item entra.
- Substitui as justificativas genéricas por explicações verificáveis; onde não há fundamento
  seguro, mantém explicação mínima e marca revisao = "explicacao_minima".

Uso: python reconstruir_sefaz_ce_2021.py [--dry-run]
"""
import json
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
ARQ = os.path.join(BASE, 'questions.json')
DADOS = os.path.join(BASE, 'dados', 'sefaz_ce_2021_itens.json')

AT = 'auditor_ti'
AG = 'agente'
AMBOS = [AT, AG]
SO_AT = [AT]
NENHUM = []
ED = 'edital_ba_2022'      # assunto listado no edital SEFAZ-BA 2022 (FGV)
COR = 'correlato'          # cobrado em provas fiscais de TI, não listado no edital 2022
FORA = 'fora'              # legislação de outro estado, economia, sociologia etc.

# (item inicial, item final, assunto, tópico, escopo, cargos)
GRUPOS = [
    (1, 4, 'Administração Pública', 'Governo digital, planejamento e gestão de pessoas', COR, SO_AT),
    (5, 11, 'Administração Pública', 'Lei de Acesso à Informação, Lei da Transparência e ética', COR, SO_AT),
    (12, 16, 'Teoria do Direito e Sociologia', 'Positivismo, marxismo e eficácia da norma', FORA, NENHUM),
    (17, 17, 'Educação Fiscal', 'Programa de Educação Fiscal do Ceará', FORA, NENHUM),
    (18, 19, 'Direito Tributário', 'ICMS: contribuinte e seletividade', ED, AMBOS),
    (20, 20, 'Finanças Públicas', 'Objetivos da tributação', COR, SO_AT),
    (21, 21, 'Direito Tributário', 'Competência tributária (ITBI)', ED, AMBOS),
    (22, 23, 'Educação Fiscal', 'Fundamentos da educação fiscal', FORA, NENHUM),
    (24, 26, 'Economia do Setor Público', 'Eficiência, equidade e falhas de mercado', FORA, NENHUM),
    (27, 28, 'Finanças Públicas', 'Despesa pública e LRF', COR, SO_AT),
    (30, 31, 'Informática', 'Sistemas operacionais e computação em nuvem', ED, SO_AT),
    (32, 32, 'Segurança da Informação', 'Firewall', ED, AMBOS),
    (33, 33, 'Segurança da Informação', 'Backup', ED, SO_AT),
    (34, 34, 'Segurança da Informação', 'VPN', ED, AMBOS),
    (35, 42, 'Raciocínio Lógico-Matemático', 'Progressões, lógica e análise combinatória', ED, AMBOS),
    (43, 44, 'Direito Tributário', 'ICMS na importação e interpretação do fato gerador', ED, AMBOS),
    (45, 48, 'Legislação Estadual do Ceará', 'IPVA-CE, ITCD-CE e FECOP (não vale para a Bahia)', FORA, NENHUM),
    (49, 60, 'Economia', 'História econômica, comércio internacional e macroeconomia', FORA, NENHUM),
    (61, 65, 'Gestão de Processos (BPM)', 'BPM, SWOT, KPI e BPMN', ED, SO_AT),
    (66, 71, 'Engenharia de Software', 'Web, requisitos, UML, testes, GRASP e frameworks', ED, SO_AT),
    (72, 80, 'Business Intelligence e Big Data', 'Big data, ETL/ELT, modelagem dimensional, DW e Hadoop', ED, SO_AT),
    (82, 82, 'Business Intelligence e Big Data', 'Ferramentas de BI', ED, SO_AT),
    (83, 83, 'Banco de Dados', 'SQL: GROUP BY e HAVING', ED, AMBOS),
    (84, 87, 'Contêineres e DevOps', 'DevOps, Docker e Kubernetes', COR, SO_AT),
    (88, 92, 'Gerenciamento de Projetos e Governança de TI', 'Abordagem ágil, Scrum, EAP e COBIT 2019', ED, SO_AT),
    (93, 98, 'Estatística', 'Poisson, TCL e estimação', ED, AMBOS),
    (99, 103, 'Licitações e Contratos', 'Lei nº 14.133/2021', ED, SO_AT),
    (104, 107, 'Governança de TI', 'CMMI e MPS.BR', ED, SO_AT),
    (108, 113, 'Inteligência Artificial e Machine Learning', 'Classificação, redes neurais e PLN', COR, SO_AT),
    (114, 116, 'Internet das Coisas', 'Arquitetura e protocolos IoT', COR, SO_AT),
    (117, 120, 'Computação em Nuvem', 'Modelos de implantação e características essenciais', COR, SO_AT),
    (121, 122, 'Contêineres e DevOps', 'Apache Kafka e Kubernetes', COR, SO_AT),
    (123, 123, 'Arquitetura de Software', 'SOA e REST', ED, SO_AT),
    (124, 124, 'Governança de TI', 'ITIL 4', ED, SO_AT),
    (125, 127, 'Virtualização', 'Virtualização de servidores', ED, SO_AT),
    (128, 133, 'Segurança da Informação', 'ISO/IEC 27002, autenticação de dois fatores e OWASP', ED, SO_AT),
    (134, 139, 'Arquitetura de Software', 'Sistemas distribuídos, MVC e ePING', COR, SO_AT),
    (140, 145, 'Redes de Computadores', 'Comunicação de dados, topologias, Ethernet e Wi-Fi', ED, SO_AT),
    (146, 150, 'Língua Inglesa', 'Interpretação de texto técnico', COR, SO_AT),
    (151, 155, 'Direito Constitucional', 'Sigilo, publicidade, livre iniciativa e seguridade', ED, AMBOS),
    (156, 160, 'Direito Administrativo', 'Atos administrativos e poderes da administração', ED, AMBOS),
]

# Itens que não podem ser respondidos com o que temos, ou cujo conteúdo mudou.
INDISPONIVEL = {
    38: 'Depende de figura (planta do imóvel) que não consta do caderno em texto.',
    93: 'Fórmulas com símbolos corrompidos na extração do caderno.',
    94: 'Fórmulas com símbolos corrompidos na extração do caderno.',
    95: 'Fórmulas com símbolos corrompidos na extração do caderno.',
    96: 'Depende de densidade e quadro com símbolos corrompidos na extração do caderno.',
    97: 'Depende de densidade e quadro com símbolos corrompidos na extração do caderno.',
    98: 'Depende de densidade e quadro com símbolos corrompidos na extração do caderno.',
    100: 'Regime de transição da Lei 14.133/2021 (art. 191) encerrado; item histórico.',
}

# Explicações verificáveis. Sem letras de alternativa. O prefixo com o gabarito é adicionado no código.
EXP = {
    1: 'A Estratégia de Governo Digital 2020-2022 (Decreto nº 10.332/2020) é o marco do período citado, e a Rede Nacional de Governo Digital, colaborativa e de adesão voluntária, consta entre suas iniciativas.',
    2: 'A gestão por competências alinha o desenvolvimento e o desempenho das pessoas aos objetivos da instituição, com critérios conhecidos de todos, o que favorece a eficiência e a transparência nas relações de trabalho.',
    3: 'O dever de cumprir o edital decorre do princípio da vinculação ao edital (instrumento convocatório), previsto entre os princípios da Lei nº 14.133/2021 (art. 5º), e não da probidade administrativa.',
    4: 'O planejamento estratégico olha para o futuro: além de analisar as condições presentes, permite construir cenários e definir metas e ações. Dizer que inviabiliza prospecções futuras contraria sua própria finalidade.',
    5: 'A Lei de Acesso à Informação (Lei nº 12.527/2011, art. 7º, II) garante acesso à informação contida em registros e documentos produzidos ou acumulados pelos órgãos, recolhidos ou não a arquivos públicos. Estar arquivado não impede o acesso.',
    6: 'A Lei da Transparência (LC nº 131/2009) alterou a LRF para exigir a liberação, em tempo real, de informações pormenorizadas sobre a execução orçamentária e financeira, em meios eletrônicos de acesso público (LRF, art. 48).',
    7: 'Pela LAI (art. 11, §6º), se a informação já está disponível ao público em formato impresso, eletrônico ou outro meio de acesso universal, o órgão informa por escrito o lugar e a forma de consulta, o que o desonera de fornecê-la diretamente, salvo se o requerente declarar não ter meios de fazê-lo por si.',
    8: 'A ética é dimensão que atravessa todas as esferas da vida (trabalho, família, sociedade e exercício da cidadania), e não se restringe ao ambiente profissional.',
    9: 'O Código de Ética do Servidor Público Civil Federal (Decreto nº 1.171/1994) afirma que o servidor decide não somente entre o legal e o ilegal, mas principalmente entre o honesto e o desonesto. A conduta ética vai além do que é apenas permitido.',
    10: 'É coerente com o Código de Conduta da Alta Administração Federal, que exige das autoridades públicas padrões éticos de integridade, moralidade e decoro, tanto em suas atividades públicas quanto nas privadas.',
    11: 'Pela LAI (art. 24, §4º), transcorrido o prazo de classificação ou consumado o evento que defina seu termo final, a informação torna-se automaticamente de acesso público. Não é necessária decisão fundamentada da autoridade.',
    18: 'A LC nº 87/1996 (art. 4º, parágrafo único, III) considera contribuinte do ICMS quem, ainda sem habitualidade, adquire em licitação mercadorias ou bens apreendidos ou abandonados.',
    19: 'Alíquotas diferentes conforme a essencialidade do bem ou serviço configuram seletividade (CF, art. 155, §2º), e não progressividade. Progressividade é o aumento da alíquota à medida que cresce a base de cálculo, como no imposto de renda.',
    20: 'Na classificação de Musgrave, os objetivos da tributação são alocativo, distributivo e estabilizador. A redução de desigualdades sociais é o objetivo distributivo; o estabilizador busca estabilidade de preços e nível de emprego.',
    21: 'O imposto sobre transmissão inter vivos, por ato oneroso, de bens imóveis (ITBI) é de competência dos Municípios e do Distrito Federal (CF, art. 156, II), e não dos Estados.',
    28: 'A LRF (art. 34) veda ao Banco Central emitir títulos da dívida pública. Os títulos são emitidos pelo Tesouro Nacional.',
    30: 'O sistema operacional multitarefa, como Windows e Linux, gerencia processos alternando o uso da CPU entre eles em pequenas fatias de tempo (time-sharing), o que dá a impressão de execução simultânea.',
    31: 'Google Docs e Office 365 são exemplos de SaaS (Software as a Service), não de PaaS. Segundo o NIST (SP 800-145), o PaaS oferece plataforma para o consumidor implantar suas próprias aplicações.',
    32: 'Para que o firewall cumpra seu papel, todo o tráfego entre a rede interna e a externa deve obrigatoriamente passar por ele. Se houver caminho alternativo, a política de filtragem pode ser contornada.',
    33: 'Atenção às definições: muitos autores definem o backup incremental como a cópia do que mudou desde o último backup de qualquer tipo (o diferencial seria desde o último completo). A banca considerou o enunciado correto, e o gabarito oficial é o que vale para a prova.',
    34: 'A VPN cria um túnel criptografado sobre uma rede pública, como a Internet, permitindo a troca segura de dados entre dois pontos.',
    35: 'Com 30% de desconto, a dívida inicial D cumpre 0,7 x D = 2.100, logo D = 3.000, que não é inferior a 2.800.',
    36: 'A primeira parcela é 2.100 dividido por n, e cada parcela seguinte vale 110% da anterior. Como a razão entre parcelas consecutivas é sempre 1,1, a sequência é uma progressão geométrica para qualquer n.',
    37: 'Com n = 3: primeira parcela 700, segunda 770 (700 x 1,1) e terceira 847 (770 x 1,1). A soma é 2.317, menor que 2.350.',
    39: 'Se III é falsa, Marisa não tem 45 anos e não trabalha no IPVA. Por II, quem trabalha no IPVA tem 34 anos; como Jair está no IPTU (I) e Marisa não está no IPVA, o do IPVA é Daniel, com 34 anos. Marisa não tem 45 nem 34, então tem 42, e Jair fica com 45 anos.',
    40: 'Somas de três tempos com diferenças de 5 ou 10 anos entre quaisquer dois só fecham 45 com 10, 15 e 20. Marisa começou depois de Jair (menos tempo) e Daniel antes (mais tempo): Daniel 20, Jair 15, Marisa 10. Daniel não tem 15 anos.',
    41: 'A disjunção "Carlos pagará o imposto ou Ana não comprará a casa" só é falsa se as duas partes forem falsas. Logo, Carlos não pagará o imposto e Ana comprará a casa.',
    42: 'Com cadeiras a 1 m uma da outra, três pessoas afastadas de pelo menos 3 m entre si precisam de 3 arcos de 3 cadeiras, ou seja, 9 cadeiras no mínimo. Isso também comporta as 6 pessoas, então 18 não é o mínimo.',
    43: 'A CF (art. 155, §2º, IX, a) prevê a incidência do ICMS sobre a entrada de bem ou mercadoria importados do exterior por pessoa física ou jurídica, ainda que não seja contribuinte habitual do imposto.',
    44: 'O CTN (art. 118) manda interpretar a definição legal do fato gerador abstraindo-se da validade jurídica dos atos praticados e dos efeitos dos fatos efetivamente ocorridos, o contrário do que diz o item.',
    66: 'O elemento main representa o conteúdo principal e exclusivo do documento. Conteúdo repetido em várias páginas, como menus e links de navegação compartilhados, fica fora dele (em nav, header ou aside).',
    67: 'A etnografia observa o trabalho real no ambiente das pessoas e revela requisitos ligados às práticas cotidianas. Não é a técnica adequada para levantar as características globais de um processo novo a ser implantado em toda uma organização.',
    68: 'No diagrama de sequência da UML, o fragmento combinado com o operador alt representa alternativas condicionais (como um se-senão), servindo para modelar fluxos alternativos de um caso de uso.',
    69: 'Em software orientado a objetos, um método herdado pode se comportar de forma diferente no contexto de cada subclasse. Por isso o método da superclasse deve ser testado em cada especialização.',
    70: 'No GRASP, o padrão Especialista na Informação atribui a responsabilidade à classe que possui a informação necessária. A responsabilidade de criar instâncias é do padrão Criador (Creator).',
    71: 'O Django adota o padrão MTV (Model-Template-View). O template é a camada de apresentação, responsável pela exibição das informações ao usuário.',
    73: 'O Hive fornece consultas em estilo SQL e data warehousing sobre o Hadoop, e o Sqoop transfere dados entre o Hadoop e bancos relacionais. Os papéis apontados no item estão invertidos.',
    76: 'Na modelagem dimensional, as tabelas fato guardam as medidas e os eventos de negócio (por exemplo, vendas), e as tabelas dimensão descrevem as entidades de contexto (cliente, produto, tempo).',
    77: 'Os três Vs do big data são volume, velocidade e variedade. Variedade se refere à diversidade de formatos e fontes dos dados (estruturados, semiestruturados e não estruturados), e não a métodos para identificar se um conjunto é big data.',
    78: 'Entre os objetivos do BI está dar acesso interativo aos dados e permitir que analistas os manipulem para realizar a análise adequada ao negócio.',
    79: 'Um data warehouse é orientado a assunto, integrado, não volátil (os dados, depois de inseridos, não são alterados pelos usuários) e variável no tempo, pois mantém histórico que apoia decisões.',
    80: 'O Hadoop roda em clusters para projetos de big data, e o Apache ZooKeeper é o serviço centralizado que mantém configuração, sincronização distribuída e serviços de grupo para aplicações distribuídas.',
    82: 'O Pentaho Data Integration (Kettle) é uma ferramenta de integração e ETL, e não de criação de dashboards. Dashboards interativos são função de ferramentas de visualização, como o Qlik.',
    83: 'Somando por categoria: a categoria 1 tem 10 + 30 + 25 = 65 e a categoria 2 tem 20 + 25 = 45. O HAVING mantém apenas totais maiores que 45, então só a categoria 1 aparece e o resultado tem uma única linha.',
    85: 'No Docker, as camadas da imagem base são somente leitura. As alterações feitas em um contêiner ficam em sua própria camada gravável (copy-on-write) e não são vistas por outros contêineres.',
    86: 'Um cluster Kubernetes tem pelo menos um nó de trabalho (worker node), que hospeda os pods, componentes da carga de trabalho da aplicação.',
    87: 'Contêineres compartilham o kernel do sistema operacional do host, e o isolamento entre eles é mais fraco que o de máquinas virtuais, que têm hipervisor e kernel próprios. Não se pode dizer que sejam menos vulneráveis a DoS por isso.',
    88: 'Quando os requisitos evoluem continuamente e o escopo é difícil de fixar no início, a abordagem ágil (protótipos, versões incrementais e refinamento contínuo dos requisitos) é a indicada.',
    89: 'No Scrum Guide (2020), os Developers são responsáveis por criar o Sprint Backlog, plano da Sprint construído a partir dos itens selecionados do Product Backlog.',
    90: 'A EAP decompõe as entregas em pacotes de trabalho. Critérios de aceitação e exclusões fazem parte da declaração do escopo (PMBOK), e as mudanças de escopo são tratadas pelo controle integrado de mudanças, que atualiza a linha de base do escopo.',
    91: 'No COBIT 2019, o domínio Construir, Adquirir e Implementar (BAI) traz dois processos distintos: BAI01 (Gerenciamento de Programas) e BAI11 (Gerenciamento de Projetos).',
    92: 'O COBIT 2019 distingue governança de gestão, mas inclui os métodos de implementação de TI (ágil, DevOps, tradicional) entre os fatores de projeto do sistema de governança. Portanto, o método ágil pode influenciá-lo.',
    99: 'A Lei nº 14.133/2021 traz a segregação de funções entre os princípios (art. 5º) e a detalha no art. 7º: evita concentrar funções suscetíveis a risco em um só agente, reduzindo a possibilidade de ocultação de erros e fraudes.',
    101: 'A Lei nº 14.133/2021 (art. 1º, §1º) não se aplica às empresas públicas, sociedades de economia mista e suas subsidiárias, que têm regime próprio na Lei nº 13.303/2016.',
    102: 'Pela Lei nº 14.133/2021 (art. 90, §2º), se o vencedor não assinar o contrato no prazo, a Administração pode convocar os licitantes remanescentes, na ordem de classificação, nas condições propostas pelo vencedor.',
    103: 'Pela Lei nº 14.133/2021 (art. 156, §5º), a declaração de inidoneidade tem prazo mínimo de 3 anos e máximo de 6 anos. Existe limite mínimo.',
    104: 'Descreve o nível 2 de capacidade do CMMI (gerenciado): o processo é planejado, executado por pessoas capacitadas, com recursos adequados, envolve as partes interessadas e é monitorado, controlado e revisado.',
    106: 'As metas do MPS.BR são a meta técnica (criar e aprimorar os modelos de melhoria de processos) e a meta de mercado (disseminá-los), e não as citadas no item.',
    107: 'O MPS.BR foi concebido para atender a diferentes perfis de empresas, com atenção especial a pequenas e médias empresas, e não com um modelo único e fixo para todos.',
    108: 'O Naive Bayes assume que os atributos são independentes entre si, condicionalmente à classe. É essa simplificação que o torna "ingênuo" e computacionalmente simples.',
    109: 'Árvores de decisão constroem as divisões de forma gulosa, de cima para baixo. Uma divisão indevida no início se propaga para os nós seguintes, então o item inverte o ponto: propagação de erro é uma desvantagem.',
    110: 'No nível mais básico, cada unidade de uma rede neural artificial tem um valor (entrada ou ativação) e pesos que indicam a importância relativa de cada conexão.',
    111: 'O desempenho de uma rede LSTM depende da arquitetura, dos dados e da capacidade do modelo. Não há garantia de manter a precisão independentemente de seu tamanho.',
    112: 'A polissemia (uma palavra ou frase com mais de um significado) é um dos desafios clássicos do processamento de linguagem natural, junto com ambiguidade e contexto.',
    116: 'O 6LoWPAN permite o uso de IPv6 em redes de sensores sem fio de baixa potência, e o MQTT é um protocolo leve de publicação e assinatura de mensagens, adequado a baixa largura de banda. Podem ser usados em conjunto.',
    119: 'Serviço medido (measured service) é uma das características essenciais da nuvem (NIST SP 800-145): o uso de recursos é monitorado, controlado e reportado, com transparência para provedor e consumidor.',
    120: 'O agrupamento de recursos para atender vários consumidores é a característica de pool de recursos (resource pooling). Elasticidade é a capacidade de aumentar ou reduzir recursos rapidamente conforme a demanda.',
    121: 'O Apache Kafka é uma plataforma de mensageria e integração de dados baseada em publicação e assinatura, em que produtores e consumidores atuam de forma assíncrona e desacoplada.',
    122: 'No Kubernetes, o kubelet é o agente executado em cada nó, que se comunica com o plano de controle e garante que os contêineres de um pod estejam em execução. O pod é o menor objeto implantável.',
    123: 'REST é um estilo arquitetural, e não um protocolo derivado do SOAP. Pode ser usado com diversos formatos, inclusive XML, sobre HTTP e no modelo cliente-servidor.',
    124: 'Na ITIL 4, o sistema de valor de serviço (SVS) é o conjunto maior, e a cadeia de valor de serviço é um de seus componentes, formada por atividades (planejar, melhorar, engajar, projetar e fazer a transição, obter ou construir, entregar e suportar). O item inverte a relação.',
    128: 'A ISO/IEC 27002:2013 orienta que, no relacionamento com fornecedores, sejam estabelecidos acordos de contingência e recuperação para assegurar a disponibilidade da informação.',
    129: 'A ISO/IEC 27002:2013 (controles criptográficos) cita assinaturas digitais e códigos de autenticação de mensagem para verificar a autenticidade e a integridade de informações sensíveis ou críticas.',
    130: 'A política de trabalho remoto deve respeitar a legislação vigente, inclusive de privacidade. Acessos a equipamentos particulares não podem ocorrer independentemente da lei.',
    131: 'A ISO/IEC 27002:2013 recomenda segregar as funções de controle de acesso (pedido, autorização e administração de acesso). Concentrá-las em um grupo restrito contraria esse controle.',
    132: 'Na autenticação de dois fatores, o segundo fator pode ser um código gerado por aplicativo autenticador ou enviado por e-mail (ou SMS).',
    133: 'A configuração de segurança inadequada é um risco da OWASP Top 10 e pode ser detectada por scanners e testes automatizados, que são recomendados para essa finalidade.',
    134: 'No padrão MVC, o modelo (model) encapsula as funcionalidades e os objetos de conteúdo da aplicação.',
    135: 'Disponibilidade e confiabilidade são atributos distintos: disponibilidade mede a prontidão do sistema em determinado momento, enquanto confiabilidade se refere à continuidade da operação correta.',
    136: 'Middleware é a camada de software que conecta aplicações e recursos, abstraindo protocolos de comunicação e a infraestrutura subjacente.',
    140: 'Verificações de paridade (VRC e LRC) detectam apenas parte dos erros e não são adequadas a ambientes muito ruidosos. Nesses casos, usam-se códigos mais robustos, como CRC e correção de erros.',
    141: 'Em redes ATM, o caminho fim a fim é a conexão de canal virtual (VCC), formada pela concatenação de enlaces de canal virtual (VCL). O VCL é cada enlace individual, e não a concatenação.',
    142: 'Na topologia de barramento o meio é compartilhado, e todos os nós ouvem todas as transmissões, o que facilita mensagens do tipo difusão (broadcast).',
    143: 'O que uma camada oferece à camada superior é o serviço. Protocolo é o conjunto de regras que rege a comunicação entre entidades de mesma camada em máquinas diferentes.',
    144: 'A rajada de quadros (frame bursting) do Gigabit Ethernet permite ao transmissor enviar vários quadros concatenados em uma única transmissão, aumentando a eficiência.',
    145: 'O EDCA (IEEE 802.11e) classifica o tráfego em categorias de acesso e dá prioridade a tráfego sensível a atraso, como voz e vídeo, na subcamada MAC.',
    146: 'O texto diz que só falta o som e a sensação de água no rosto ("All that is missing is the roar of the water"). Portanto, o método não adiciona o som da cachoeira.',
    147: 'O texto afirma que, quando as pessoas ficam fixadas em algo interessante, provavelmente aquilo não estava totalmente estático, ou seja, pode haver movimento.',
    148: 'O texto destaca como ponto especial que o método não exige nenhuma entrada do usuário nem informação extra, bastando a foto. Portanto, isso não é uma desvantagem.',
    149: 'O texto diz que desenvolver um método capaz de transformar uma única foto em um vídeo crível tem sido um desafio para a área.',
    150: 'O texto diz que os pesquisadores pretendem estender o trabalho a objetos mais variados, como o cabelo de uma pessoa esvoaçando ao vento. Inferir que poderiam animar uma mulher de moto sem capacete é compatível.',
    151: 'O sigilo fiscal (CTN, art. 198) alcança também quem legalmente recebe as informações da Fazenda, como os órgãos de persecução penal, que passam a ter o dever de resguardá-las.',
    152: 'O sigilo bancário não é absoluto. A LC nº 105/2001 admite sua quebra para apuração de ilícitos, em qualquer fase de inquérito ou processo, e o sigilo não pode servir de abrigo para a prática de crimes.',
    153: 'O STF (Tema 483 da repercussão geral, ARE 652.777) entendeu que é legítima a divulgação, em sítio eletrônico oficial, do nome e da remuneração de servidores públicos, em atendimento ao princípio da publicidade.',
    154: 'O STF (ADPF 324 e RE 958.252, Tema 725) reconheceu como lícita a terceirização de qualquer atividade, inclusive a atividade-fim, como expressão da livre iniciativa.',
    155: 'A decadência atinge o direito de revisar o ato de concessão do benefício (Lei nº 8.213/1991, art. 103). O direito ao benefício em si (fundo de direito) não decai, segundo o STF (RE 626.489).',
    156: 'A omissão administrativa, mesmo em atos discricionários, sujeita-se a controle judicial quanto à legalidade e aos limites da discricionariedade. O Judiciário não substitui o mérito, mas pode controlar a omissão ilegal.',
    157: 'O direito das minorias à criação de CPI (um terço, CF, art. 58, §3º) aplica-se, por simetria, às Assembleias Legislativas estaduais, segundo o STF.',
    158: 'A autotutela (Lei nº 9.784/1999, art. 53; Súmula 473 do STF) fundamenta a anulação de atos ilegais e a revogação por conveniência e oportunidade. A convalidação (art. 55) é a correção de vícios sanáveis, uma faculdade ligada à segurança jurídica, e não uma consequência natural da autotutela.',
    160: 'A CF (art. 49, V) atribui ao Congresso Nacional a competência para sustar os atos normativos do Poder Executivo que exorbitem do poder regulamentar. O abuso também é passível de controle jurisdicional.',
}

EXP_MINIMA = 'A fundamentação detalhada deste item ainda não foi incluída; vale o gabarito oficial definitivo da banca.'


def grupo(n):
    for ini, fim, subj, top, esc, cargos in GRUPOS:
        if ini <= n <= fim:
            return subj, top, esc, cargos
    raise KeyError(n)


def main():
    dry = '--dry-run' in sys.argv
    dados = json.load(open(DADOS, encoding='utf-8'))
    qs = json.load(open(ARQ, encoding='utf-8'))
    por_id = {q['id']: q for q in qs}
    n_min = 0
    n_ind = 0
    for it in dados['itens']:
        n = it['n']
        q = por_id.get('sefaz_ce_2021_real_item_%03d' % n)
        if q is None:          # itens 29 e 81 (anulados)
            continue
        subj, top, esc, cargos = grupo(n)
        partes = [p for p in (it['base'], it['comando'], it['enunciado']) if p]
        q['question'] = '\n\n'.join(partes)
        q['source'] = 'CEBRASPE - SEFAZ-CE 2021 (Auditor Fiscal de TI), item %d' % n
        q['subject'], q['topic'] = subj, top
        q['escopo'], q['cargos'] = esc, list(cargos)
        q['category'] = 'general' if AG in cargos else 'ti'
        rotulo = 'CERTO' if q['correct'] == 'C' else 'ERRADO'
        corpo = EXP.get(n)
        if corpo is None:
            corpo = EXP_MINIMA
            q['revisao'] = 'explicacao_minima'
            n_min += 1
        else:
            q.pop('revisao', None)
        q['explanation'] = 'Gabarito oficial definitivo (CEBRASPE): %s. %s' % (rotulo, corpo)
        q.pop('option_explanations', None)
        q['gabarito_oficial_conferido'] = True
        if n in INDISPONIVEL:
            q['disponivel'] = False
            q['motivo_indisponivel'] = INDISPONIVEL[n]
            n_ind += 1
        else:
            q.pop('disponivel', None)
            q.pop('motivo_indisponivel', None)
    print('itens reconstruídos; explicação mínima em %d; indisponíveis %d' % (n_min, n_ind))
    if not dry:
        json.dump(qs, open(ARQ, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print('questions.json gravado.')


if __name__ == '__main__':
    sys.exit(main())
