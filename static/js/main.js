// ==========================================================================
// SEFAZ-BA 2026 PORTAL DE ESTUDOS — JAVASCRIPT FRONTEND
// ==========================================================================

// Complete syllabus structure for both tracks
const SYLLABUS_TI = [
  {
    id: "portugues",
    name: "Língua Portuguesa",
    icon: "fa-language",
    topics: [
      "Compreensão e Interpretação de Texto",
      "Ortografia Oficial e Acentuação",
      "Morfologia (Classes de Palavras e Flexões)",
      "Sintaxe da Oração e do Período",
      "Concordância Verbal e Nominal",
      "Regência Verbal e Nominal",
      "Uso do Sinal Indicativo de Crase",
      "Pontuação e Articulação de Ideias"
    ]
  },
  {
    id: "dir_adm",
    name: "Direito Administrativo",
    icon: "fa-gavel",
    topics: [
      "Organização Administrativa e Terceiro Setor",
      "Agentes Públicos e Regime Jurídico",
      "Poderes da Administração Pública",
      "Ato Administrativo (Requisitos, Atributos, Extinção)",
      "Licitações e Contratos Administrativos (Lei 14.133/2021)",
      "Controle da Administração Pública",
      "Responsabilidade Civil do Estado"
    ]
  },
  {
    id: "dir_const",
    name: "Direito Constitucional",
    icon: "fa-shield-halved",
    topics: [
      "Direitos e Garantias Fundamentais",
      "Organização Político-Administrativa do Estado",
      "Poder Executivo (Atribuições e Responsabilidades)",
      "Poder Legislativo (Processo Legislativo e Fiscalização)",
      "Poder Judiciário e Funções Essenciais à Justiça",
      "Ordem Econômica e Financeira"
    ]
  },
  {
    id: "dir_trib",
    name: "Direito Tributário",
    icon: "fa-coins",
    topics: [
      "Sistema Tributário Nacional na CF/88",
      "Código Tributário Nacional (CTN)",
      "Tributos: Conceitos, Espécies e Classificações",
      "Competência e Capacidade Tributária",
      "Limitações Constitucionais ao Poder de Tributar",
      "Crédito Tributário: Constituição, Suspensão, Extinção, Exclusão",
      "Garantias e Privilégios do Crédito Tributário",
      "Administração Tributária (Fiscalização, Sigilo, Dívida Ativa)"
    ]
  },
  {
    id: "contabilidade",
    name: "Contabilidade Geral",
    icon: "fa-calculator",
    topics: [
      "Conceitos, Objetivos e Campo de Atuação",
      "Patrimônio: Componentes, Ativo, Passivo e PL",
      "Contas e Plano de Contas, Método das Partidas Dobradas",
      "Fatos Contábeis e Lançamentos de Escrituração",
      "Balanço Patrimonial (Critérios de Avaliação e Estrutura)",
      "Demonstração do Resultado do Exercício (DRE)",
      "Demonstração dos Fluxos de Caixa (DFC) e DVA"
    ]
  },
  {
    id: "rlm_estatistica",
    name: "Estatística e RLM",
    icon: "fa-chart-pie",
    topics: [
      "Lógica Proposicional e Argumentação Lógica",
      "Diagramas Lógicos e Resolução de Problemas",
      "Estatística Descritiva: Média, Mediana, Moda",
      "Medidas de Dispersão: Variância e Desvio Padrão",
      "Probabilidade e Distribuições Teóricas (Binomial, Normal)"
    ]
  },
  {
    id: "igualdade_racial",
    name: "Igualdade Racial e Gênero",
    icon: "fa-people-group",
    topics: [
      "Estatuto da Igualdade Racial da Bahia (Lei Estadual 13.182/2014)",
      "Políticas de Ações Afirmativas e Combate ao Racismo Institucional"
    ]
  },
  {
    id: "gestao_ti",
    name: "Gestão e Governança de TI",
    icon: "fa-diagram-project",
    topics: [
      "COBIT 2019: Princípios, Objetivos de Governança e Processos",
      "ITIL v4: Conceitos-Chave e Sistema de Valor de Serviço",
      "DAMA-DMBOK v2: Governança, Qualidade e Arquitetura de Dados",
      "Gestão de Projetos (PMBOK v7) e Metodologias Ágeis (Scrum, Kanban)"
    ]
  },
  {
    id: "eng_software",
    name: "Engenharia de Software e APIs",
    icon: "fa-cubes",
    topics: [
      "Ciclos de Vida de Desenvolvimento de Software",
      "Engenharia de Requisitos e Casos de Uso",
      "Padrões de Projeto (Design Patterns) Comuns",
      "Modelagem de Processos Organizacionais (BPMN v2)",
      "Arquitetura de APIs RESTful e Padrão de Microserviços"
    ]
  },
  {
    id: "banco_dados",
    name: "Banco de Dados & BI",
    icon: "fa-database",
    topics: [
      "Modelagem Conceitual (Entidade-Relacionamento), Lógica e Física",
      "Bancos de Dados Relacionais vs NoSQL (Key-Value, Documentos)",
      "Linguagem SQL Avançada: DDL, DML, Subqueries, JOINS, Indexes",
      "Data Warehouse: Modelagem Dimensional (Star e Snowflake Schema)",
      "Processos de Extração, Transformação e Carga (ETL)"
    ]
  },
  {
    id: "ciencia_dados",
    name: "Ciência de Dados & Big Data",
    icon: "fa-brain",
    topics: [
      "Arquiteturas de Big Data (Hadoop, MapReduce, Spark)",
      "Mineração de Dados: Regras de Associação, Clusterização",
      "Algoritmos de Machine Learning (Árvores de Decisão, Regressões)",
      "Bibliotecas de Análise em Python (Pandas, NumPy, Scikit-learn)"
    ]
  },
  {
    id: "seguranca_ti",
    name: "Segurança da Informação",
    icon: "fa-key",
    topics: [
      "Normas ABNT NBR ISO/IEC 27001 e ISO/IEC 27002",
      "Princípios de Criptografia Simétrica, Assíncrona e Hash",
      "Assinatura Digital e Infraestrutura de Chaves Públicas (ICP-Brasil)",
      "Lei Geral de Proteção de Dados (LGPD — Lei 13.709/2018)",
      "Segurança em Nuvem e Gerenciamento de Vulnerabilidades"
    ]
  },
  {
    id: "auditoria_ti",
    name: "Auditoria de TI",
    icon: "fa-magnifying-glass-chart",
    topics: [
      "Técnicas de Auditoria Assistida por Computador (TAACs)",
      "Auditoria de Controles Gerais de TI e Segurança de Sistemas"
    ]
  }
];

const SYLLABUS_BROTHER = [
  {
    id: "portugues",
    name: "Língua Portuguesa",
    icon: "fa-language",
    topics: [
      "Compreensão e Interpretação de Texto",
      "Ortografia Oficial e Acentuação",
      "Morfologia (Classes de Palavras e Flexões)",
      "Sintaxe da Oração e do Período",
      "Concordância Verbal e Nominal",
      "Regência Verbal e Nominal",
      "Uso do Sinal Indicativo de Crase",
      "Pontuação e Articulação de Ideias"
    ]
  },
  {
    id: "dir_adm",
    name: "Direito Administrativo",
    icon: "fa-gavel",
    topics: [
      "Organização Administrativa e Terceiro Setor",
      "Agentes Públicos e Regime Jurídico",
      "Poderes da Administração Pública",
      "Ato Administrativo (Requisitos, Atributos, Extinção)",
      "Licitações e Contratos Administrativos (Lei 14.133/2021)",
      "Controle da Administração Pública",
      "Responsabilidade Civil do Estado"
    ]
  },
  {
    id: "dir_const",
    name: "Direito Constitucional",
    icon: "fa-shield-halved",
    topics: [
      "Direitos e Garantias Fundamentais",
      "Organização Político-Administrativa do Estado",
      "Poder Executivo (Atribuições e Responsabilidades)",
      "Poder Legislativo (Processo Legislativo e Fiscalização)",
      "Poder Judiciário e Funções Essenciais à Justiça",
      "Ordem Econômica e Financeira"
    ]
  },
  {
    id: "dir_trib",
    name: "Direito Tributário",
    icon: "fa-coins",
    topics: [
      "Sistema Tributário Nacional na CF/88",
      "Código Tributário Nacional (CTN)",
      "Tributos: Conceitos, Espécies e Classificações",
      "Competência e Capacidade Tributária",
      "Limitações Constitucionais ao Poder de Tributar",
      "Crédito Tributário: Constituição, Suspensão, Extinção, Exclusão",
      "Garantias e Privilégios do Crédito Tributário",
      "Administração Tributária (Fiscalização, Sigilo, Dívida Ativa)"
    ]
  },
  {
    id: "contabilidade",
    name: "Contabilidade Geral",
    icon: "fa-calculator",
    topics: [
      "Conceitos, Objetivos e Campo de Atuação",
      "Patrimônio: Componentes, Ativo, Passivo e PL",
      "Contas e Plano de Contas, Método das Partidas Dobradas",
      "Fatos Contábeis e Lançamentos de Escrituração",
      "Balanço Patrimonial (Critérios de Avaliação e Estrutura)",
      "Demonstração do Resultado do Exercício (DRE)",
      "Demonstração dos Fluxos de Caixa (DFC) e DVA"
    ]
  },
  {
    id: "rlm_estatistica",
    name: "Estatística e RLM",
    icon: "fa-chart-pie",
    topics: [
      "Lógica Proposicional e Argumentação Lógica",
      "Diagramas Lógicos e Resolução de Problemas",
      "Estatística Descritiva: Média, Mediana, Moda",
      "Medidas de Dispersão: Variância e Desvio Padrão",
      "Probabilidade e Distribuições Teóricas (Binomial, Normal)"
    ]
  },
  {
    id: "igualdade_racial",
    name: "Igualdade Racial e Gênero",
    icon: "fa-people-group",
    topics: [
      "Estatuto da Igualdade Racial da Bahia (Lei Estadual 13.182/2014)",
      "Políticas de Ações Afirmativas e Combate ao Racismo Institucional"
    ]
  },
  {
    id: "lte_ba",
    name: "Legislação Tributária Estadual (Bahia)",
    icon: "fa-landmark",
    topics: [
      "Regulamento do ICMS da Bahia (RICMS-BA): Fato Gerador e Base de Cálculo",
      "ICMS: Substituição Tributária e Alíquotas Internas/Interestaduais",
      "Imposto sobre a Propriedade de Veículos Automotores (IPVA)",
      "Imposto sobre Transmissão Causa Mortis e Doação (ITD)",
      "Taxas de Serviços Estaduais na Bahia",
      "Processo Administrativo Fiscal da Bahia (PAF — Decreto 7.629/99)",
      "Cadastro Geral e Livros Fiscais da Bahia"
    ]
  },
  {
    id: "auditoria_fiscal",
    name: "Auditoria Fiscal",
    icon: "fa-magnifying-glass-arrow-right",
    topics: [
      "Normas Brasileiras de Auditoria (NBC TA)",
      "Técnicas e Procedimentos de Auditoria de Estoques e Caixa",
      "Auditoria de Livros Fiscais e Cruzamento de Dados (SPED)",
      "Amostragem em Auditoria e Relatórios de Parecer Fiscal"
    ]
  },
  {
    id: "financas_publicas",
    name: "Finanças Públicas e Orçamento",
    icon: "fa-scale-balanced",
    topics: [
      "Lei de Responsabilidade Fiscal (LRF — LC 101/2000)",
      "Instrumentos Orçamentários: PPA, LDO e LOA",
      "Classificação da Receita e Despesa Pública",
      "Créditos Adicionais e Estágios da Despesa",
      "Controle Interno e Tribunais de Contas"
    ]
  }
];

// New Syllabus Databases
const SYLLABUS_RFB_AUDITOR = [
  {
    id: "portugues",
    name: "Língua Portuguesa",
    icon: "fa-language",
    topics: [
      "Compreensão e Interpretação de Texto",
      "Ortografia Oficial e Acentuação",
      "Morfologia (Classes de Palavras e Flexões)",
      "Sintaxe da Oração e do Período",
      "Concordância Verbal e Nominal",
      "Regência Verbal e Nominal",
      "Uso do Sinal Indicativo de Crase",
      "Pontuação e Articulação de Ideias"
    ]
  },
  {
    id: "dir_adm",
    name: "Direito Administrativo",
    icon: "fa-gavel",
    topics: [
      "Organização Administrativa e Terceiro Setor",
      "Agentes Públicos e Regime Jurídico",
      "Poderes da Administração Pública",
      "Ato Administrativo (Requisitos, Atributos, Extinção)",
      "Licitações e Contratos Administrativos (Lei 14.133/2021)",
      "Controle da Administração Pública",
      "Responsabilidade Civil do Estado"
    ]
  },
  {
    id: "dir_const",
    name: "Direito Constitucional",
    icon: "fa-shield-halved",
    topics: [
      "Direitos e Garantias Fundamentais",
      "Organização Político-Administrativa do Estado",
      "Poder Executivo (Atribuições e Responsabilidades)",
      "Poder Legislativo (Processo Legislativo e Fiscalização)",
      "Poder Judiciário e Funções Essenciais à Justiça",
      "Ordem Econômica e Financeira"
    ]
  },
  {
    id: "dir_trib",
    name: "Direito Tributário",
    icon: "fa-coins",
    topics: [
      "Sistema Tributário Nacional na CF/88",
      "Código Tributário Nacional (CTN)",
      "Tributos: Conceitos, Espécies e Classificações",
      "Competência e Capacidade Tributária",
      "Limitações Constitucionais ao Poder de Tributar",
      "Crédito Tributário: Constituição, Suspensão, Extinção, Exclusão",
      "Garantias e Privilégios do Crédito Tributário",
      "Administração Tributária (Fiscalização, Sigilo, Dívida Ativa)"
    ]
  },
  {
    id: "contabilidade",
    name: "Contabilidade Geral",
    icon: "fa-calculator",
    topics: [
      "Conceitos, Objetivos e Campo de Atuação",
      "Patrimônio: Componentes, Ativo, Passivo e PL",
      "Contas e Plano de Contas, Método das Partidas Dobradas",
      "Fatos Contábeis e Lançamentos de Escrituração",
      "Balanço Patrimonial (Critérios de Avaliação e Estrutura)",
      "Demonstração do Resultado do Exercício (DRE)",
      "Demonstração dos Fluxos de Caixa (DFC) e DVA"
    ]
  },
  {
    id: "rlm_estatistica",
    name: "Estatística e RLM",
    icon: "fa-chart-pie",
    topics: [
      "Lógica Proposicional e Argumentação Lógica",
      "Diagramas Lógicos e Resolução de Problemas",
      "Estatística Descritiva: Média, Mediana, Moda",
      "Medidas de Dispersão: Variância e Desvio Padrão",
      "Probabilidade e Distribuições Teóricas (Binomial, Normal)"
    ]
  },
  {
    id: "auditoria",
    name: "Auditoria",
    icon: "fa-magnifying-glass-arrow-right",
    topics: [
      "Normas Brasileiras de Auditoria (NBC TA)",
      "Técnicas e Procedimentos de Auditoria de Estoques e Caixa",
      "Auditoria de Livros Fiscais e Cruzamento de Dados (SPED)",
      "Amostragem em Auditoria e Relatórios de Parecer Fiscal"
    ]
  },
  {
    id: "ingles",
    name: "Língua Inglesa",
    icon: "fa-flag-usa",
    topics: [
      "Compreensão de Textos Técnicos em Inglês",
      "Vocabulário de Termos Econômicos e Tributários",
      "Estruturas Gramaticais e Coesão Textual"
    ]
  },
  {
    id: "economia_financas",
    name: "Economia e Finanças Públicas",
    icon: "fa-chart-line",
    topics: [
      "Microeconomia: Oferta, Demanda e Estruturas de Mercado",
      "Macroeconomia: Política Fiscal, Monetária e Cambial",
      "Finanças Públicas: Orçamento, Receita, Despesa e LRF",
      "Déficit Público, Dívida Pública e Financiamento do Estado"
    ]
  },
  {
    id: "adm_geral_publica",
    name: "Administração Geral e Pública",
    icon: "fa-users-gear",
    topics: [
      "Planejamento, Organização, Direção e Controle",
      "Modelos de Administração Pública: Burocrático e Gerencial",
      "Gestão de Pessoas, Gestão da Qualidade e Projetos",
      "Ética e Transparência na Gestão Pública Federal"
    ]
  },
  {
    id: "fluencia_dados",
    name: "Fluência em Dados (TI)",
    icon: "fa-database",
    topics: [
      "Conceitos de Big Data e Engenharia de Dados",
      "Bancos de Dados Relacionais e Linguagem SQL",
      "Segurança da Informação e LGPD",
      "Análise de Dados com Python e R"
    ]
  },
  {
    id: "dir_previdenciario",
    name: "Direito Previdenciário",
    icon: "fa-handshake-angle",
    topics: [
      "Seguridade Social: Origem, Princípios e Organização",
      "Regime Geral de Previdência Social (RGPS): Beneficiários",
      "Financiamento da Seguridade Social: Contribuições",
      "Decisões e Jurisprudência Previdenciária dos Tribunais Superiores"
    ]
  },
  {
    id: "leg_tributaria_fed",
    name: "Legislação Tributária Federal",
    icon: "fa-gavel",
    topics: [
      "Imposto de Renda da Pessoa Física (IRPF) e Jurídica (IRPJ)",
      "Contribuição Social sobre o Lucro Líquido (CSLL)",
      "PIS/Pasep e COFINS: Incidência Cumulativa e Não-Cumulativa",
      "Imposto sobre Produtos Industrializados (IPI)",
      "Processo Administrativo Fiscal Federal (Decreto 70.235/72)"
    ]
  },
  {
    id: "comercio_aduaneira",
    name: "Comércio e Legislação Aduaneira",
    icon: "fa-ship",
    topics: [
      "Teoria do Comércio Internacional e Barreiras Tarifárias",
      "Acordo Geral sobre Tarifas e Comércio (GATT) e OMC",
      "Regulamento Aduaneiro: Jurisdição e Controle",
      "Regimes Aduaneiros Especiais (Drawback, Entreposto)",
      "Valoração Aduaneira e Classificação Fiscal de Mercadorias (NCM)"
    ]
  }
];

const SYLLABUS_RFB_ANALISTA = [
  {
    id: "portugues",
    name: "Língua Portuguesa",
    icon: "fa-language",
    topics: [
      "Compreensão e Interpretação de Texto",
      "Ortografia Oficial e Acentuação",
      "Morfologia (Classes de Palavras e Flexões)",
      "Sintaxe da Oração e do Período",
      "Concordância Verbal e Nominal",
      "Regência Verbal e Nominal",
      "Uso do Sinal Indicativo de Crase",
      "Pontuação e Articulação de Ideias"
    ]
  },
  {
    id: "rlm_estatistica",
    name: "Estatística e RLM",
    icon: "fa-chart-pie",
    topics: [
      "Lógica Proposicional e Argumentação Lógica",
      "Diagramas Lógicos e Resolução de Problemas",
      "Estatística Descritiva: Média, Mediana, Moda",
      "Medidas de Dispersão: Variância e Desvio Padrão",
      "Probabilidade e Distribuições Teóricas (Binomial, Normal)"
    ]
  },
  {
    id: "contabilidade",
    name: "Contabilidade Geral",
    icon: "fa-calculator",
    topics: [
      "Conceitos, Objetivos e Campo de Atuação",
      "Patrimônio: Componentes, Ativo, Passivo e PL",
      "Contas e Plano de Contas, Método das Partidas Dobradas",
      "Fatos Contábeis e Lançamentos de Escrituração",
      "Balanço Patrimonial (Critérios de Avaliação e Estrutura)",
      "Demonstração do Resultado do Exercício (DRE)",
      "Demonstração dos Fluxos de Caixa (DFC) e DVA"
    ]
  },
  {
    id: "adm_geral_publica",
    name: "Administração Geral e Pública",
    icon: "fa-users-gear",
    topics: [
      "Planejamento, Organização, Direção e Controle",
      "Modelos de Administração Pública: Burocrático e Gerencial",
      "Gestão de Pessoas, Gestão da Qualidade e Projetos",
      "Ética e Transparência na Gestão Pública Federal"
    ]
  },
  {
    id: "fluencia_dados",
    name: "Fluência em Dados (TI)",
    icon: "fa-database",
    topics: [
      "Conceitos de Big Data e Engenharia de Dados",
      "Bancos de Dados Relacionais e Linguagem SQL",
      "Segurança da Informação e LGPD",
      "Análise de Dados com Python e R"
    ]
  },
  {
    id: "dir_adm",
    name: "Direito Administrativo",
    icon: "fa-gavel",
    topics: [
      "Organização Administrativa e Terceiro Setor",
      "Agentes Públicos e Regime Jurídico",
      "Poderes da Administração Pública",
      "Ato Administrativo (Requisitos, Atributos, Extinção)",
      "Licitações e Contratos Administrativos (Lei 14.133/2021)",
      "Controle da Administração Pública",
      "Responsabilidade Civil do Estado"
    ]
  },
  {
    id: "dir_const",
    name: "Direito Constitucional",
    icon: "fa-shield-halved",
    topics: [
      "Direitos e Garantias Fundamentais",
      "Organização Político-Administrativa do Estado",
      "Poder Executivo (Atribuições e Responsabilidades)",
      "Poder Legislativo (Processo Legislativo e Fiscalização)",
      "Poder Judiciário e Funções Essenciais à Justiça",
      "Ordem Econômica e Financeira"
    ]
  },
  {
    id: "dir_trib_fed",
    name: "Direito Tributário e Legislação Federal",
    icon: "fa-coins",
    topics: [
      "Sistema Tributário Nacional na CF/88",
      "Crédito Tributário no CTN: Constituição, Extinção, Exclusão",
      "Imposto de Renda (IR) e Imposto sobre Produtos Industrializados (IPI)",
      "Contribuições Federais (PIS, COFINS, CSLL)",
      "Processo Administrativo Fiscal Federal (Decreto 70.235/72)"
    ]
  },
  {
    id: "leg_aduaneira",
    name: "Legislação Aduaneira",
    icon: "fa-ship",
    topics: [
      "Controle Aduaneiro de Veículos e Mercadorias",
      "Imposto de Importação (II) e Imposto de Exportação (IE)",
      "Infrações e Penalidades na Legislação Aduaneira"
    ]
  }
];

const SYLLABUS_BACEN_AUDITOR = [
  {
    id: "portugues",
    name: "Língua Portuguesa",
    icon: "fa-language",
    topics: [
      "Compreensão e Interpretação de Texto",
      "Ortografia Oficial e Acentuação",
      "Morfologia (Classes de Palavras e Flexões)",
      "Sintaxe da Oração e do Período",
      "Concordância Verbal e Nominal",
      "Regência Verbal e Nominal",
      "Uso do Sinal Indicativo de Crase",
      "Pontuação e Articulação de Ideias"
    ]
  },
  {
    id: "dir_adm",
    name: "Direito Administrativo",
    icon: "fa-gavel",
    topics: [
      "Organização Administrativa e Terceiro Setor",
      "Agentes Públicos e Regime Jurídico",
      "Poderes da Administração Pública",
      "Ato Administrativo (Requisitos, Atributos, Extinção)",
      "Licitações e Contratos Administrativos (Lei 14.133/2021)",
      "Controle da Administração Pública",
      "Responsabilidade Civil do Estado"
    ]
  },
  {
    id: "economia",
    name: "Macro e Microeconomia",
    icon: "fa-chart-line",
    topics: [
      "Teoria do Consumidor e Teoria da Firma",
      "Estruturas de Mercado: Monopólio e Oligopólio",
      "Contabilidade Nacional e Determinação da Renda",
      "Políticas Macroeconômicas (Fiscal, Monetária, Cambial)",
      "Modelos Macroeconômicos (IS-LM, OA-DA)"
    ]
  },
  {
    id: "estatistica_logica",
    name: "Lógica e Estatística",
    icon: "fa-chart-pie",
    topics: [
      "Lógica Proposicional e Argumentação Lógica",
      "Estatística Descritiva: Média, Mediana, Moda",
      "Medidas de Dispersão: Variância e Desvio Padrão",
      "Amostragem, Probabilidade e Distribuição Normal"
    ]
  },
  {
    id: "ciencia_dados",
    name: "Ciência de Dados",
    icon: "fa-brain",
    topics: [
      "Arquiteturas de Big Data (Hadoop, MapReduce, Spark)",
      "Mineração de Dados: Regras de Associação, Clusterização",
      "Algoritmos de Machine Learning (Árvores de Decisão, Regressões)",
      "Bibliotecas de Análise em Python (Pandas, NumPy, Scikit-learn)"
    ]
  },
  {
    id: "seguranca_ti",
    name: "Segurança da Informação",
    icon: "fa-key",
    topics: [
      "Normas ABNT NBR ISO/IEC 27001 e ISO/IEC 27002",
      "Princípios de Criptografia Simétrica, Assíncrona e Hash",
      "Assinatura Digital e Infraestrutura de Chaves Públicas (ICP-Brasil)",
      "Lei Geral de Proteção de Dados (LGPD — Lei 13.709/2018)"
    ]
  },
  {
    id: "eng_software",
    name: "Engenharia de Software",
    icon: "fa-cubes",
    topics: [
      "Ciclos de Vida de Desenvolvimento de Software",
      "Engenharia de Requisitos e Casos de Uso",
      "Padrões de Projeto (Design Patterns) Comuns",
      "Arquitetura de APIs RESTful e Padrão de Microserviços"
    ]
  },
  {
    id: "infraestrutura_ti",
    name: "Infraestrutura em TI",
    icon: "fa-server",
    topics: [
      "Arquitetura de Computadores e Sistemas Operacionais (Linux, Windows Server)",
      "Protocolos de Redes de Computadores (TCP/IP, DNS, HTTP)",
      "Virtualização, Computação em Nuvem e Contêineres (Docker, Kubernetes)"
    ]
  },
  {
    id: "banco_dados",
    name: "Banco de Dados & BI",
    icon: "fa-database",
    topics: [
      "Modelagem Conceitual (Entidade-Relacionamento), Lógica e Física",
      "Bancos de Dados Relacionais vs NoSQL",
      "Linguagem SQL: DDL, DML, Subqueries, JOINS, Indexes",
      "Processos de Extração, Transformação e Carga (ETL)"
    ]
  },
  {
    id: "gestao_ti",
    name: "Gestão de TI",
    icon: "fa-diagram-project",
    topics: [
      "COBIT 2019: Princípios, Objetivos de Governança e Processos",
      "ITIL v4: Conceitos-Chave e Sistema de Valor de Serviço"
    ]
  }
];

const SYLLABUS_BACEN_TECNICO = [
  {
    id: "portugues",
    name: "Língua Portuguesa",
    icon: "fa-language",
    topics: [
      "Compreensão e Interpretação de Texto",
      "Ortografia Oficial e Acentuação",
      "Morfologia (Classes de Palavras e Flexões)",
      "Sintaxe da Oração e do Período",
      "Concordância Verbal e Nominal",
      "Regência Verbal e Nominal",
      "Uso do Sinal Indicativo de Crase",
      "Pontuação e Articulação de Ideias"
    ]
  },
  {
    id: "rlm",
    name: "Raciocínio Lógico-Matemático",
    icon: "fa-calculator",
    topics: [
      "Lógica Proposicional e Argumentação Lógica",
      "Equações e Sistemas de Primeiro e Segundo Grau",
      "Porcentagem, Juros Simples e Compostos",
      "Análise Combinatória e Probabilidade Básica"
    ]
  },
  {
    id: "dir_adm",
    name: "Direito Administrativo",
    icon: "fa-gavel",
    topics: [
      "Organização Administrativa e Terceiro Setor",
      "Agentes Públicos e Regime Jurídico",
      "Poderes da Administração Pública",
      "Ato Administrativo (Requisitos, Atributos, Extinção)"
    ]
  },
  {
    id: "dir_const",
    name: "Direito Constitucional",
    icon: "fa-shield-halved",
    topics: [
      "Direitos e Garantias Fundamentais",
      "Organização Político-Administrativa do Estado",
      "Poder Executivo (Atribuições e Responsabilidades)"
    ]
  },
  {
    id: "nocoes_economia",
    name: "Noções de Economia",
    icon: "fa-chart-line",
    topics: [
      "Microeconomia: Oferta, Demanda e Equilíbrio de Mercado",
      "Macroeconomia: Inflação, PIB e Desemprego",
      "Sistema Financeiro Nacional e Banco Central"
    ]
  },
  {
    id: "atendimento_vendas",
    name: "Atendimento e Vendas",
    icon: "fa-comments",
    topics: [
      "Técnicas de Vendas e Negociação no Setor Financeiro",
      "Ética e Ouvidoria no Atendimento ao Cidadão"
    ]
  }
];

// App State
let activeCertame = 'sefaz'; // 'sefaz', 'rfb', 'bacen'

let appState = {
  user_ti: {
    checked: []
  },
  user_brother: {
    checked: []
  }
};

// Total Topics count for statistics (dynamic variables)
let activeTotalTiTopics = SYLLABUS_TI.reduce((acc, curr) => acc + curr.topics.length, 0);
let activeTotalBrotherTopics = SYLLABUS_BROTHER.reduce((acc, curr) => acc + curr.topics.length, 0);

// Initialize Dashboard
document.addEventListener("DOMContentLoaded", () => {
  setupTabs();
  calculateCountdown();
  renderSyllabus();
  loadProgress();
  loadLocalFiles();
  loadQuestions();
  loadNews();
});

// Fetch and render Google News RSS items
function loadNews() {
  const container = document.getElementById("news-timeline-container");
  if (!container) return;
  
  fetch('static/news_data.json')
    .then(res => {
      if (!res.ok) throw new Error("News JSON not found");
      return res.json();
    })
    .then(data => {
      if (data.length === 0) return;
      
      const tagColors = {
        "SEFAZ-BA": "#3E9A2D",       // Verde oficial do IF Baiano / Sefaz
        "Receita Federal": "#06b6d4", // Cyan
        "Banco Central": "#8b5cf6"    // Purple
      };
      
      container.innerHTML = data.slice(0, 4).map(item => {
        let displayDate = "";
        try {
          const date = new Date(item.pubDate);
          displayDate = date.toLocaleDateString('pt-BR', { day: '2-digit', month: 'short' });
        } catch (e) {
          displayDate = item.pubDate;
        }
        
        const color = tagColors[item.tag] || "#06b6d4";
        
        return `
          <div class="timeline-item">
            <div class="tl-badge active" style="background-color: ${color}; border-color: ${color};"><i class="fa-solid fa-newspaper" style="font-size: 12px; color: #fff;"></i></div>
            <div class="tl-content">
              <span class="tl-date" style="display: flex; align-items: center; gap: 8px;">
                ${displayDate} 
                <span class="quiz-badge" style="font-size: 9px; padding: 2px 6px; border-color: ${color}; color: ${color}; border-style: solid; border-width: 1px; border-radius: 4px;">${item.tag}</span>
              </span>
              <h4 style="margin: 6px 0 4px 0;"><a href="${item.link}" target="_blank" style="color:#fff; text-decoration:none; font-weight: 600;">${item.title}</a></h4>
              <p style="font-size:12px; color:var(--text-muted); margin:0;">Fonte: ${item.source} | Capturado em: ${item.fetchedAt.split(' ')[0]}</p>
            </div>
          </div>
        `;
      }).join('');
    })
    .catch(err => {
      console.log("Using default static timeline for news (local news data not populated yet).");
    });
}

// Setup Page Tabs
function setupTabs() {
  const navItems = document.querySelectorAll(".nav-item");
  const tabContents = document.querySelectorAll(".tab-content");

  navItems.forEach(item => {
    item.addEventListener("click", () => {
      // Remove active from all items
      navItems.forEach(nav => nav.classList.remove("active"));
      tabContents.forEach(tab => tab.classList.remove("active"));

      // Set current active
      item.classList.add("active");
      const tabId = item.getAttribute("data-tab");
      document.getElementById(tabId).classList.add("active");

      // Update header title
      const titleMapping = {
        "dashboard": "Painel Geral",
        "trilhas": "Trilhas de Estudo",
        "videoaulas": "Videoaulas & Dicas",
        "materiais": "Materiais de Apoio Local",
        "cronograma": "Cronograma Semanal",
        "simulados": "Simulados Interativos",
        "glossario": "Glossário de Siglas (Contabilidade & Auditoria)",
        "remuneracoes": "Comparativo de Remunerações"
      };
      document.getElementById("page-title").textContent = titleMapping[tabId];

      if (tabId === "simulados") {
        startSimulado(quizCategory);
      }
    });
  });
}

// Global countdown target date
let targetCountdownDate = "2026-11-15T09:00:00";

// Calculate Days remaining to tentative exam date
function calculateCountdown() {
  const targetDate = new Date(targetCountdownDate);
  const currentDate = new Date();
  const diffTime = targetDate - currentDate;
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
  
  document.getElementById("days-val").textContent = diffDays > 0 ? diffDays : 0;
}

// Switch Trilha subtabs inside Trilhas section
function switchTrilha(type) {
  const btnTi = document.getElementById("btn-trilha-ti");
  const btnBrother = document.getElementById("btn-trilha-brother");
  const contentTi = document.getElementById("trilha-ti-content");
  const contentBrother = document.getElementById("trilha-brother-content");

  if (type === 'ti') {
    btnTi.classList.add("active");
    btnBrother.classList.remove("active");
    contentTi.classList.add("active");
    contentBrother.classList.remove("active");
  } else {
    btnTi.classList.remove("active");
    btnBrother.classList.add("active");
    contentTi.classList.remove("active");
    contentBrother.classList.add("active");
  }
}

// Render Syllabus HTML dynamically
function renderSyllabus() {
  const containerTi = document.getElementById("accordion-ti");
  const containerBrother = document.getElementById("accordion-brother");

  // Determine active syllabus arrays
  let syllabusTi = [];
  let syllabusBrother = [];

  if (activeCertame === 'sefaz') {
    syllabusTi = SYLLABUS_TI;
    syllabusBrother = SYLLABUS_BROTHER;
  } else if (activeCertame === 'rfb') {
    syllabusTi = SYLLABUS_RFB_AUDITOR;
    syllabusBrother = SYLLABUS_RFB_ANALISTA;
  } else if (activeCertame === 'bacen') {
    syllabusTi = SYLLABUS_BACEN_AUDITOR;
    syllabusBrother = SYLLABUS_BACEN_TECNICO;
  }

  // Update dynamic totals
  activeTotalTiTopics = syllabusTi.reduce((acc, curr) => acc + curr.topics.length, 0);
  activeTotalBrotherTopics = syllabusBrother.reduce((acc, curr) => acc + curr.topics.length, 0);

  // Render TI/Auditor Track
  containerTi.innerHTML = syllabusTi.map((subject, sIdx) => {
    const topicsHtml = subject.topics.map((topic, tIdx) => {
      const topicId = `${activeCertame}-ti-${subject.id}-${tIdx}`;
      return `
        <div class="topic-item" onclick="toggleTopicCheckbox('${topicId}')">
          <div class="custom-checkbox-wrapper">
            <input type="checkbox" id="${topicId}" class="checkbox-input ti-checkbox" data-subject="${subject.id}" onchange="onCheckboxChange(event)">
            <span class="checkmark"></span>
          </div>
          <span class="topic-label">${topic}</span>
        </div>
      `;
    }).join('');

    return `
      <div class="accordion-item" id="item-${activeCertame}-ti-${subject.id}">
        <div class="accordion-header" onclick="toggleAccordion('item-${activeCertame}-ti-${subject.id}')">
          <div class="subject-info-title">
            <div class="subject-icon"><i class="fa-solid ${subject.icon}"></i></div>
            <span>${subject.name}</span>
          </div>
          <div class="subject-progress">
            <span class="subject-progress-count" id="count-${activeCertame}-ti-${subject.id}">0/${subject.topics.length}</span>
            <i class="fa-solid fa-chevron-down chevron-icon"></i>
          </div>
        </div>
        <div class="accordion-content">
          <div class="topics-list">
            ${topicsHtml}
          </div>
        </div>
      </div>
    `;
  }).join('');

  // Render Brother/Analista/Técnico Track
  containerBrother.innerHTML = syllabusBrother.map((subject, sIdx) => {
    const topicsHtml = subject.topics.map((topic, tIdx) => {
      const topicId = `${activeCertame}-br-${subject.id}-${tIdx}`;
      return `
        <div class="topic-item" onclick="toggleTopicCheckbox('${topicId}')">
          <div class="custom-checkbox-wrapper">
            <input type="checkbox" id="${topicId}" class="checkbox-input brother-checkbox" data-subject="${subject.id}" onchange="onCheckboxChange(event)">
            <span class="checkmark"></span>
          </div>
          <span class="topic-label">${topic}</span>
        </div>
      `;
    }).join('');

    return `
      <div class="accordion-item" id="item-${activeCertame}-br-${subject.id}">
        <div class="accordion-header" onclick="toggleAccordion('item-${activeCertame}-br-${subject.id}')">
          <div class="subject-info-title">
            <div class="subject-icon"><i class="fa-solid ${subject.icon}"></i></div>
            <span>${subject.name}</span>
          </div>
          <div class="subject-progress">
            <span class="subject-progress-count" id="count-${activeCertame}-br-${subject.id}">0/${subject.topics.length}</span>
            <i class="fa-solid fa-chevron-down chevron-icon"></i>
          </div>
        </div>
        <div class="accordion-content">
          <div class="topics-list">
            ${topicsHtml}
          </div>
        </div>
      </div>
    `;
  }).join('');
}

// Toggle accordion open/close state
function toggleAccordion(id) {
  const item = document.getElementById(id);
  const isActive = item.classList.contains("active");
  
  // Optional: close other accordions in the same track
  const parent = item.parentElement;
  parent.querySelectorAll(".accordion-item").forEach(acc => acc.classList.remove("active"));
  
  if (!isActive) {
    item.classList.add("active");
  }
}

// Help click on row check checkbox
function toggleTopicCheckbox(id) {
  // Prevent double trigger if clicking directly on checkbox input
  if (event.target.tagName === 'INPUT' || event.target.classList.contains('checkmark')) return;
  const checkbox = document.getElementById(id);
  if (checkbox) {
    checkbox.checked = !checkbox.checked;
    // Dispatch change event manually
    const changeEvent = new Event('change', { bubbles: true });
    checkbox.dispatchEvent(changeEvent);
  }
}

// Save checked states when checkbox is toggled
function onCheckboxChange(e) {
  updatePercentages();
  saveProgress();
}

// Update study percentages on dashboard, sidebar, and subject counters
function updatePercentages() {
  // Get all checked boxes from active and inactive certames
  const checkedTi = [];
  document.querySelectorAll(".ti-checkbox").forEach(chk => {
    if (chk.checked) {
      if (!checkedTi.includes(chk.id)) checkedTi.push(chk.id);
    }
  });
  
  if (appState.user_ti && appState.user_ti.checked) {
    appState.user_ti.checked.forEach(id => {
      if (!id.startsWith(`${activeCertame}-ti-`)) {
        if (!checkedTi.includes(id)) checkedTi.push(id);
      }
    });
  }

  // Count active checked
  const activeCheckedTi = checkedTi.filter(id => id.startsWith(`${activeCertame}-ti-`));
  const tiPct = Math.round((activeCheckedTi.length / activeTotalTiTopics) * 100) || 0;
  
  document.getElementById("ti-progress-bar").style.width = `${tiPct}%`;
  document.getElementById("ti-progress-pct-txt").textContent = `${tiPct}%`;
  document.getElementById("ti-sidebar-pct").textContent = `${tiPct}%`;
  document.getElementById("ti-trilha-pct").textContent = `${tiPct}%`;

  // Determine active syllabus arrays
  let syllabusTi = [];
  let syllabusBrother = [];

  if (activeCertame === 'sefaz') {
    syllabusTi = SYLLABUS_TI;
    syllabusBrother = SYLLABUS_BROTHER;
  } else if (activeCertame === 'rfb') {
    syllabusTi = SYLLABUS_RFB_AUDITOR;
    syllabusBrother = SYLLABUS_RFB_ANALISTA;
  } else if (activeCertame === 'bacen') {
    syllabusTi = SYLLABUS_BACEN_AUDITOR;
    syllabusBrother = SYLLABUS_BACEN_TECNICO;
  }

  // Update TI Subject counts
  syllabusTi.forEach(subject => {
    const total = subject.topics.length;
    const checked = activeCheckedTi.filter(id => id.startsWith(`${activeCertame}-ti-${subject.id}-`)).length;
    const countEl = document.getElementById(`count-${activeCertame}-ti-${subject.id}`);
    if (countEl) countEl.textContent = `${checked}/${total}`;
  });

  // 2. Brother Progress
  const checkedBrother = [];
  document.querySelectorAll(".brother-checkbox").forEach(chk => {
    if (chk.checked) {
      if (!checkedBrother.includes(chk.id)) checkedBrother.push(chk.id);
    }
  });
  
  if (appState.user_brother && appState.user_brother.checked) {
    appState.user_brother.checked.forEach(id => {
      if (!id.startsWith(`${activeCertame}-br-`)) {
        if (!checkedBrother.includes(id)) checkedBrother.push(id);
      }
    });
  }

  const activeCheckedBrother = checkedBrother.filter(id => id.startsWith(`${activeCertame}-br-`));
  const broPct = Math.round((activeCheckedBrother.length / activeTotalBrotherTopics) * 100) || 0;

  document.getElementById("brother-progress-bar").style.width = `${broPct}%`;
  document.getElementById("brother-progress-pct-txt").textContent = `${broPct}%`;
  document.getElementById("brother-sidebar-pct").textContent = `${broPct}%`;
  document.getElementById("brother-trilha-pct").textContent = `${broPct}%`;

  // Update Brother Subject counts
  syllabusBrother.forEach(subject => {
    const total = subject.topics.length;
    const checked = activeCheckedBrother.filter(id => id.startsWith(`${activeCertame}-br-${subject.id}-`)).length;
    const countEl = document.getElementById(`count-${activeCertame}-br-${subject.id}`);
    if (countEl) countEl.textContent = `${checked}/${total}`;
  });

  appState.user_ti.checked = checkedTi;
  appState.user_brother.checked = checkedBrother;
}

// Fetch user progress from server
function loadProgress() {
  const isStaticHost = window.location.hostname.includes('github.io') || window.location.protocol === 'file:';

  if (isStaticHost) {
    console.log("Static Host detected. Using localStorage for progress.");
    const localData = localStorage.getItem("sefaz_progress_data");
    if (localData) {
      try {
        const parsed = JSON.parse(localData);
        applyProgressData(parsed);
      } catch (e) {
        console.error("Error parsing localStorage progress:", e);
      }
    }
    return;
  }

  fetch('api/progress')
    .then(res => {
      if (!res.ok) throw new Error("Flask API not available");
      const contentType = res.headers.get("content-type");
      if (!contentType || !contentType.includes("application/json")) {
        throw new Error("Response is not JSON");
      }
      return res.json();
    })
    .then(data => {
      applyProgressData(data);
    })
    .catch(err => {
      console.log("Using localStorage fallback for progress (Static Host)");
      const localData = localStorage.getItem("sefaz_progress_data");
      if (localData) {
        try {
          const parsed = JSON.parse(localData);
          applyProgressData(parsed);
        } catch (e) {
          console.error("Error parsing localStorage progress:", e);
        }
      }
    });
}

// Helper to apply loaded progress to checkboxes
function applyProgressData(data) {
  appState = data;
  
  // Reset all first
  document.querySelectorAll(".checkbox-input").forEach(chk => chk.checked = false);

  if (data.user_ti && data.user_ti.checked) {
    data.user_ti.checked.forEach(id => {
      const chk = document.getElementById(id);
      if (chk) chk.checked = true;
    });
  }

  if (data.user_brother && data.user_brother.checked) {
    data.user_brother.checked.forEach(id => {
      const chk = document.getElementById(id);
      if (chk) chk.checked = true;
    });
  }

  updatePercentages();
}

// Switch Certame
function switchCertame(certame) {
  activeCertame = certame;

  // Update certame selector buttons UI
  document.querySelectorAll(".certame-btn").forEach(btn => btn.classList.remove("active"));
  const activeBtn = document.getElementById(`btn-certame-${certame}`);
  if (activeBtn) activeBtn.classList.add("active");

  // Update Hero Card details dynamically
  const heroTitle = document.getElementById("hero-title");
  const heroDesc = document.getElementById("hero-desc");
  const heroStatTi = document.getElementById("hero-stat-ti");
  const heroLabelTi = document.getElementById("hero-label-ti");
  const heroStatBrother = document.getElementById("hero-stat-brother");
  const heroLabelBrother = document.getElementById("hero-label-brother");
  const heroStatSalary = document.getElementById("hero-stat-salary");
  const statusPillText = document.getElementById("status-pill-text");
  const countdownTitleEl = document.getElementById("countdown-title-el");
  const countdownDescEl = document.getElementById("countdown-desc-el");

  // Update track selector labels and descriptions based on active certame
  const labelTi = document.getElementById("label-trilha-ti");
  const labelBrother = document.getElementById("label-trilha-brother");
  const headingTi = document.getElementById("heading-trilha-ti");
  const descTi = document.getElementById("desc-trilha-ti");
  const headingBrother = document.getElementById("heading-trilha-brother");
  const descBrother = document.getElementById("desc-trilha-brother");

  if (certame === 'sefaz') {
    if (heroTitle) heroTitle.textContent = "Rumo à SEFAZ-BA 2026";
    if (heroDesc) heroDesc.innerHTML = "Uma oportunidade histórica com <strong>200 vagas</strong> autorizadas no orçamento! Prepare-se estrategicamente para Auditor Fiscal (Especialidade TI) e Agente de Tributos Estaduais (Qualquer Formação).";
    if (heroStatTi) heroStatTi.textContent = "100";
    if (heroLabelTi) heroLabelTi.textContent = "Vagas Auditor (TI/Outros)";
    if (heroStatBrother) heroStatBrother.textContent = "100";
    if (heroLabelBrother) heroLabelBrother.textContent = "Vagas Agente (Qualquer Nível)";
    if (heroStatSalary) heroStatSalary.textContent = "R$ 33,8k";
    if (statusPillText) statusPillText.textContent = "Comissão Formada (Provas em datas distintas)";
    if (countdownTitleEl) countdownTitleEl.textContent = "Estimativa do Edital";
    if (countdownDescEl) countdownDescEl.textContent = "Baseado na previsão de provas no final de 2026.";
    targetCountdownDate = "2026-11-15T09:00:00";

    if (labelTi) labelTi.textContent = "Trilha Auditor Fiscal (Tecnologia da Informação)";
    if (labelBrother) labelBrother.textContent = "Trilha Agente de Tributos (Qualquer Formação)";
    if (headingTi) headingTi.textContent = "Trilha de Estudos: Auditor Fiscal - TI";
    if (descTi) descTi.textContent = "Contempla as disciplinas de conhecimentos gerais (peso fiscal) e as específicas de TI.";
    if (headingBrother) headingBrother.textContent = "Trilha de Estudos: Agente de Tributos Estaduais";
    if (descBrother) descBrother.textContent = "Focada em qualquer formação acadêmica, com forte peso em Legislação Tributária da Bahia (LTE) e Auditoria.";
  } else if (certame === 'rfb') {
    if (heroTitle) heroTitle.textContent = "Rumo à Receita Federal 2026";
    if (heroDesc) heroDesc.innerHTML = "Concurso nacional autorizado com remunerações excelentes. Estude as disciplinas federais para Auditor-Fiscal e Analista-Tributário de forma integrada.";
    if (heroStatTi) heroStatTi.textContent = "30";
    if (heroLabelTi) heroLabelTi.textContent = "Vagas Auditor-Fiscal";
    if (heroStatBrother) heroStatBrother.textContent = "116";
    if (heroLabelBrother) heroLabelBrother.textContent = "Vagas Analista-Tributário";
    if (heroStatSalary) heroStatSalary.textContent = "R$ 35,6k";
    if (statusPillText) statusPillText.textContent = "Autorizado (146 vagas)";
    if (countdownTitleEl) countdownTitleEl.textContent = "Publicação do Edital";
    if (countdownDescEl) countdownDescEl.textContent = "Edital previsto para até janeiro de 2027.";
    targetCountdownDate = "2026-12-20T09:00:00";

    if (labelTi) labelTi.textContent = "Trilha Auditor-Fiscal da Receita";
    if (labelBrother) labelBrother.textContent = "Trilha Analista-Tributário da Receita";
    if (headingTi) headingTi.textContent = "Trilha de Estudos: Auditor-Fiscal (RFB)";
    if (descTi) descTi.textContent = "Direcionada ao edital federal de Auditor, abrangendo Legislação Aduaneira e Tributária Federal.";
    if (headingBrother) headingBrother.textContent = "Trilha de Estudos: Analista-Tributário (RFB)";
    if (descBrother) descBrother.textContent = "Focada nas matérias gerais e específicas de nível federal para o cargo de Analista.";
  } else if (certame === 'bacen') {
    if (heroTitle) heroTitle.textContent = "Rumo ao Banco Central 2026";
    if (heroDesc) heroDesc.innerHTML = "Certame federal de alta relevância com regime de subsídio e alta valorização. Prepare-se para Auditor (TI/Economia) e Técnico do Banco Central.";
    if (heroStatTi) heroStatTi.textContent = "100";
    if (heroLabelTi) heroLabelTi.textContent = "Vagas Auditor (TI/Eco)";
    if (heroStatBrother) heroStatBrother.textContent = "50";
    if (heroLabelBrother) heroLabelBrother.textContent = "Vagas Técnico (Nível Médio)";
    if (heroStatSalary) heroStatSalary.textContent = "R$ 21,1k";
    if (statusPillText) statusPillText.textContent = "Autorizado (170 vagas)";
    if (countdownTitleEl) countdownTitleEl.textContent = "Publicação do Edital";
    if (countdownDescEl) countdownDescEl.textContent = "Edital previsto para o segundo semestre de 2026.";
    targetCountdownDate = "2026-12-15T09:00:00";

    if (labelTi) labelTi.textContent = "Trilha Auditor (Tecnologia da Informação)";
    if (labelBrother) labelBrother.textContent = "Trilha Técnico do Banco Central";
    if (headingTi) headingTi.textContent = "Trilha de Estudos: Auditor do Banco Central (TI)";
    if (descTi) descTi.textContent = "Conteúdo direcionado à área de TI e inovação tecnológica do BACEN.";
    if (headingBrother) headingBrother.textContent = "Trilha de Estudos: Técnico do Banco Central (Nível Médio)";
    if (descBrother) descBrother.textContent = "Preparação para o cargo de Técnico, focando em Macro/Microeconomia básica e RLM.";
  }

  // Recalculate countdown immediately
  calculateCountdown();

  // Rerender Syllabus and restore checked states from appState
  renderSyllabus();
  
  // Re-apply checked states to newly rendered checkboxes
  if (appState.user_ti && appState.user_ti.checked) {
    appState.user_ti.checked.forEach(id => {
      const chk = document.getElementById(id);
      if (chk) chk.checked = true;
    });
  }

  if (appState.user_brother && appState.user_brother.checked) {
    appState.user_brother.checked.forEach(id => {
      const chk = document.getElementById(id);
      if (chk) chk.checked = true;
    });
  }

  updatePercentages();
}

// POST current checklist progress to backend
function saveProgress() {
  // Always save to localStorage as backup
  localStorage.setItem("sefaz_progress_data", JSON.stringify(appState));

  const isStaticHost = window.location.hostname.includes('github.io') || window.location.protocol === 'file:';
  if (isStaticHost) return;

  fetch('api/progress', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(appState)
  })
  .then(res => {
    if (!res.ok) throw new Error("Flask API write failed");
    const contentType = res.headers.get("content-type");
    if (!contentType || !contentType.includes("application/json")) {
      throw new Error("Response is not JSON");
    }
    return res.json();
  })
  .then(data => {
    console.log("Progress saved to server successfully");
  })
  .catch(err => console.log("Progress saved locally (localStorage only)"));
}

// Fetch local PDFs list from Flask API
function loadLocalFiles() {
  const container = document.getElementById("file-list");
  container.innerHTML = `
    <div class="loading-state">
      <i class="fa-solid fa-circle-notch fa-spin"></i> Carregando arquivos...
    </div>
  `;

  const STATIC_FILES = [
    { name: "Apostila_Auditoria_Fiscal.pdf", size: "22.8 KB", url: "Concurso SEFAZ/Apostila_Auditoria_Fiscal.pdf" },
    { name: "Apostila_Banco_Dados_BI.pdf", size: "22.5 KB", url: "Concurso SEFAZ/Apostila_Banco_Dados_BI.pdf" },
    { name: "Apostila_Ciencia_Dados_Big_Data.pdf", size: "22.3 KB", url: "Concurso SEFAZ/Apostila_Ciencia_Dados_Big_Data.pdf" },
    { name: "Apostila_Contabilidade_Geral.pdf", size: "23.2 KB", url: "Concurso SEFAZ/Apostila_Contabilidade_Geral.pdf" },
    { name: "Apostila_Direito_Administrativo.pdf", size: "23.2 KB", url: "Concurso SEFAZ/Apostila_Direito_Administrativo.pdf" },
    { name: "Apostila_Direito_Constitucional.pdf", size: "25.3 KB", url: "Concurso SEFAZ/Apostila_Direito_Constitucional.pdf" },
    { name: "Apostila_Direito_Tributário.pdf", size: "23.4 KB", url: "Concurso SEFAZ/Apostila_Direito_Tributário.pdf" },
    { name: "Apostila_Engenharia_Software.pdf", size: "22.1 KB", url: "Concurso SEFAZ/Apostila_Engenharia_Software.pdf" },
    { name: "Apostila_Estatistica_RLM.pdf", size: "22.8 KB", url: "Concurso SEFAZ/Apostila_Estatistica_RLM.pdf" },
    { name: "Apostila_Finanças_Publicas.pdf", size: "23.1 KB", url: "Concurso SEFAZ/Apostila_Finanças_Publicas.pdf" },
    { name: "Apostila_Gestão_Governança_TI.pdf", size: "21.9 KB", url: "Concurso SEFAZ/Apostila_Gestão_Governança_TI.pdf" },
    { name: "Apostila_Igualdade_Racial_Gênero.pdf", size: "22.3 KB", url: "Concurso SEFAZ/Apostila_Igualdade_Racial_Gênero.pdf" },
    { name: "Apostila_Legislação_Tributária_BA.pdf", size: "22.4 KB", url: "Concurso SEFAZ/Apostila_Legislação_Tributária_BA.pdf" },
    { name: "Apostila_Língua_Portuguesa.pdf", size: "26.7 KB", url: "Concurso SEFAZ/Apostila_Língua_Portuguesa.pdf" },
    { name: "Apostila_Segurança_Informação.pdf", size: "22.3 KB", url: "Concurso SEFAZ/Apostila_Segurança_Informação.pdf" }
  ];

  const isStaticHost = window.location.hostname.includes('github.io') || window.location.protocol === 'file:';

  if (isStaticHost) {
    container.innerHTML = `
      <div class="static-files-note" style="background-color: rgba(6, 182, 212, 0.05); border: 1px solid rgba(6, 182, 212, 0.15); padding: 12px; border-radius: 6px; margin-bottom: 16px; font-size: 13px; color: var(--accent-cyan); display: flex; align-items: center; gap: 8px;">
        <i class="fa-solid fa-globe"></i>
        <span>Exibindo arquivos no Modo Estático (GitHub Pages). Links de download diretos do repositório.</span>
      </div>
    ` + STATIC_FILES.map(file => `
      <div class="file-item">
        <div class="file-info">
          <i class="fa-solid fa-file-pdf file-icon"></i>
          <div class="file-details">
            <span class="file-name">${file.name}</span>
            <span class="file-meta">Tamanho: ${file.size}</span>
          </div>
        </div>
        <div class="file-actions">
          <a href="${file.url}" target="_blank" class="btn btn-secondary" style="font-size: 12.5px; padding: 6px 12px; margin-right: 8px; border-color: rgba(255,255,255,0.1);"><i class="fa-solid fa-eye"></i> Visualizar</a>
          <a href="${file.url}" download class="btn" style="font-size: 12.5px; padding: 6px 12px; background: rgba(6, 182, 212, 0.1); border-color: rgba(6, 182, 212, 0.2); color: var(--accent-cyan);"><i class="fa-solid fa-download"></i> Baixar</a>
        </div>
      </div>
    `).join('');
    return;
  }

  fetch('api/files')
    .then(res => {
      if (!res.ok) throw new Error("Flask API not available");
      const contentType = res.headers.get("content-type");
      if (!contentType || !contentType.includes("application/json")) {
        throw new Error("Response is not JSON");
      }
      return res.json();
    })
    .then(files => {
      if (files.error) {
        throw new Error(files.error);
      }
      
      if (files.length === 0) {
        container.innerHTML = `
          <div class="empty-state">
            <i class="fa-solid fa-box-open"></i> Nossos materiais não foram encontrados na pasta "Concurso SEFAZ".
          </div>
        `;
        return;
      }

      container.innerHTML = files.map(file => `
        <div class="file-item">
        <div class="file-info">
          <i class="fa-solid fa-file-pdf file-icon"></i>
          <div class="file-details">
            <span class="file-name">${file.name}</span>
            <span class="file-meta">Tamanho: ${file.size}</span>
          </div>
        </div>
        <div class="file-actions">
          <a href="${file.url}" target="_blank" class="btn btn-secondary" style="font-size: 12.5px; padding: 6px 12px; margin-right: 8px; border-color: rgba(255,255,255,0.1);"><i class="fa-solid fa-eye"></i> Visualizar</a>
          <a href="${file.url}" download class="btn" style="font-size: 12.5px; padding: 6px 12px; background: rgba(6, 182, 212, 0.1); border-color: rgba(6, 182, 212, 0.2); color: var(--accent-cyan);"><i class="fa-solid fa-download"></i> Baixar</a>
        </div>
      </div>
      `).join('');
    })
    .catch(err => {
      console.warn("Local files API not available. Using GitHub Pages static fallback.", err);
      
      container.innerHTML = `
        <div class="static-files-note" style="background-color: rgba(6, 182, 212, 0.05); border: 1px solid rgba(6, 182, 212, 0.15); padding: 12px; border-radius: 6px; margin-bottom: 16px; font-size: 13px; color: var(--accent-cyan); display: flex; align-items: center; gap: 8px;">
          <i class="fa-solid fa-globe"></i>
          <span>Exibindo arquivos no Modo Estático (GitHub Pages). Links de download diretos do repositório.</span>
        </div>
      ` + STATIC_FILES.map(file => `
        <div class="file-item">
          <div class="file-info">
            <i class="fa-solid fa-file-pdf file-icon"></i>
            <div class="file-details">
              <span class="file-name">${file.name}</span>
              <span class="file-meta">Tamanho: ${file.size}</span>
            </div>
          </div>
          <div class="file-actions">
            <a href="${file.url}" target="_blank" class="btn btn-secondary" style="font-size: 12.5px; padding: 6px 12px; margin-right: 8px; border-color: rgba(255,255,255,0.1);"><i class="fa-solid fa-eye"></i> Visualizar</a>
            <a href="${file.url}" download class="btn" style="font-size: 12.5px; padding: 6px 12px; background: rgba(6, 182, 212, 0.1); border-color: rgba(6, 182, 212, 0.2); color: var(--accent-cyan);"><i class="fa-solid fa-download"></i> Baixar</a>
          </div>
        </div>
      `).join('');
    });
}

// ==========================================================================
// SIMULADO / QUIZ LOGIC
// ==========================================================================

let allQuestions = [];
let activeQuizQuestions = [];
let currentQuestionIdx = 0;
let selectedOption = null;
let quizCategory = 'ti';
let score = { correct: 0, total: 0 };
let answerChecked = false;

// Fetch questions from the Flask backend API
function loadQuestions() {
  const isStaticHost = window.location.hostname.includes('github.io') || window.location.protocol === 'file:';

  if (isStaticHost) {
    console.log("Static Host detected. Fetching static JSON files directly.");
    fetch('questions.json')
      .then(res => {
        if (!res.ok) throw new Error("Static file questions.json not found");
        return res.json();
      })
      .then(data => {
        allQuestions = data;
      })
      .catch(err2 => console.error("Error loading static questions.json:", err2));

    fetch('discursivas.json')
      .then(res => {
        if (!res.ok) throw new Error("Static file discursivas.json not found");
        return res.json();
      })
      .then(data => {
        allDiscursivas = data;
        if (currentQuizType === 'disc') {
          startDiscursiva(discursivaCategory);
        }
      })
      .catch(err2 => console.error("Error loading static discursivas.json:", err2));
    return;
  }

  fetch('api/questions')
    .then(res => {
      if (!res.ok) throw new Error("Flask API not available");
      const contentType = res.headers.get("content-type");
      if (!contentType || !contentType.includes("application/json")) {
        throw new Error("Response is not JSON");
      }
      return res.json();
    })
    .then(data => {
      allQuestions = data;
    })
    .catch(err => {
      console.log("Using static fallback for questions.json");
      fetch('questions.json')
        .then(res => {
          if (!res.ok) throw new Error("Static file questions.json not found");
          const contentType = res.headers.get("content-type");
          if (!contentType || !contentType.includes("application/json")) {
            throw new Error("Static response is not JSON");
          }
          return res.json();
        })
        .then(data => {
          allQuestions = data;
        })
        .catch(err2 => console.error("Error loading static questions.json:", err2));
    });

  fetch('api/discursivas')
    .then(res => {
      if (!res.ok) throw new Error("Flask API not available");
      const contentType = res.headers.get("content-type");
      if (!contentType || !contentType.includes("application/json")) {
        throw new Error("Response is not JSON");
      }
      return res.json();
    })
    .then(data => {
      allDiscursivas = data;
    })
    .catch(err => {
      console.log("Using static fallback for discursivas.json");
      fetch('discursivas.json')
        .then(res => {
          if (!res.ok) throw new Error("Static file discursivas.json not found");
          const contentType = res.headers.get("content-type");
          if (!contentType || !contentType.includes("application/json")) {
            throw new Error("Static response is not JSON");
          }
          return res.json();
        })
        .then(data => {
          allDiscursivas = data;
          if (currentQuizType === 'disc') {
            startDiscursiva(discursivaCategory);
          }
        })
        .catch(err2 => console.error("Error loading static discursivas.json:", err2));
    });
}

// Start simulated exam for a specific category ('ti' or 'general')
// Global configuration options for quiz
let quizSize = '10'; // Default size
let quizOrder = 'random'; // Default order

// Start simulated exam for a specific category ('ti' or 'general')
function startSimulado(category) {
  quizCategory = category;
  
  // Update sub-tab buttons style
  const btnTi = document.getElementById("btn-simulado-ti");
  const btnBrother = document.getElementById("btn-simulado-brother");
  if (category === 'ti') {
    btnTi.classList.add("active");
    btnBrother.classList.remove("active");
  } else {
    btnTi.classList.remove("active");
    btnBrother.classList.add("active");
  }

  // Filter base questions:
  // - If category is 'ti', include both 'ti' (P2) and 'general' (P1) questions!
  // - If category is 'general', include only 'general' questions.
  if (category === 'ti') {
    activeQuizQuestions = allQuestions.filter(q => q.category === 'ti' || q.category === 'general');
  } else {
    activeQuizQuestions = allQuestions.filter(q => q.category === 'general');
  }

  // Render setup configuration screen
  renderQuizSetup();
}

// Render the quiz configuration setup screen
function renderQuizSetup() {
  const container = document.getElementById("quiz-card");
  const isBrother = quizCategory === 'brother' || quizCategory === 'general';
  const cargoName = quizCategory === 'ti' ? "Auditor Fiscal (TI)" : "Agente de Tributos";
  const numAvailable = activeQuizQuestions.length;

  container.innerHTML = `
    <div class="quiz-setup-card ${isBrother ? 'setup-brother' : ''}">
      <div class="setup-header">
        <i class="fa-solid fa-sliders setup-icon"></i>
        <h3>Configurar Simulado: ${cargoName}</h3>
      </div>
      <p class="setup-desc">
        ${quizCategory === 'ti' 
          ? "Este simulado mescla <strong>Conhecimentos Gerais (P1)</strong> e <strong>Específicos de TI (P2)</strong> para simular o edital completo." 
          : "Este simulado foca nas disciplinas de <strong>Conhecimentos Gerais e Específicos</strong> comuns ao cargo."}
        <br>Total de questões disponíveis no banco: <strong>${numAvailable}</strong>.
      </p>

      <div class="setup-section">
        <label><i class="fa-solid fa-list-ol"></i> Quantidade de Questões:</label>
        <div class="setup-options">
          <button class="setup-opt-btn ${quizSize === '10' ? 'active' : ''}" onclick="selectQuizSize('10')">10 Questões</button>
          <button class="setup-opt-btn ${quizSize === '20' ? 'active' : ''}" onclick="selectQuizSize('20')">20 Questões</button>
          <button class="setup-opt-btn ${quizSize === '40' ? 'active' : ''}" onclick="selectQuizSize('40')">40 Questões</button>
          <button class="setup-opt-btn ${quizSize === 'all' ? 'active' : ''}" onclick="selectQuizSize('all')">Todas (${numAvailable})</button>
        </div>
      </div>

      <div class="setup-section">
        <label><i class="fa-solid fa-shuffle"></i> Ordem das Questões:</label>
        <div class="setup-options">
          <button class="setup-opt-btn ${quizOrder === 'random' ? 'active' : ''}" onclick="selectQuizOrder('random')">Aleatória (Embaralhar)</button>
          <button class="setup-opt-btn ${quizOrder === 'sequence' ? 'active' : ''}" onclick="selectQuizOrder('sequence')">Padrão do Banco</button>
        </div>
      </div>

      <button class="start-quiz-btn" onclick="launchSimuladoWithConfig()">
        <i class="fa-solid fa-play"></i> Iniciar Simulado
      </button>
    </div>
  `;
}

// Select size configuration
function selectQuizSize(size) {
  quizSize = size;
  renderQuizSetup();
}

// Select order configuration
function selectQuizOrder(order) {
  quizOrder = order;
  renderQuizSetup();
}

// Launch the quiz with current configurations
function launchSimuladoWithConfig() {
  // Apply filtering again (just to be safe)
  let baseQuestions = [];
  if (quizCategory === 'ti') {
    baseQuestions = allQuestions.filter(q => q.category === 'ti' || q.category === 'general');
  } else {
    baseQuestions = allQuestions.filter(q => q.category === 'general');
  }

  // Handle Order
  if (quizOrder === 'random') {
    // Fisher-Yates Shuffle
    for (let i = baseQuestions.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [baseQuestions[i], baseQuestions[j]] = [baseQuestions[j], baseQuestions[i]];
    }
  }

  // Handle Size
  if (quizSize !== 'all') {
    const sizeNum = parseInt(quizSize, 10);
    activeQuizQuestions = baseQuestions.slice(0, sizeNum);
  } else {
    activeQuizQuestions = baseQuestions;
  }

  // Reset quiz state
  currentQuestionIdx = 0;
  selectedOption = null;
  answerChecked = false;
  score.correct = 0;
  score.total = activeQuizQuestions.length;

  renderQuestion();
}


// Render the current question card
function renderQuestion() {
  const container = document.getElementById("quiz-card");
  
  if (activeQuizQuestions.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <i class="fa-solid fa-triangle-exclamation text-cyan"></i> Nenhuma questão cadastrada para este simulado ainda.
      </div>
    `;
    return;
  }

  if (currentQuestionIdx >= activeQuizQuestions.length) {
    showQuizSummary();
    return;
  }

  const q = activeQuizQuestions[currentQuestionIdx];
  
  // Generate options list
  let optionsHtml = '';
  for (const [key, val] of Object.entries(q.options)) {
    const isSelected = selectedOption === key;
    optionsHtml += `
      <div class="quiz-option ${isSelected ? 'selected' : ''} ${quizCategory === 'brother' || quizCategory === 'general' ? 'option-brother' : ''}" 
           id="opt-${key}" 
           onclick="selectQuizOption('${key}')">
        <div class="option-letter">${key}</div>
        <div class="option-text">${val}</div>
      </div>
    `;
  }

  container.innerHTML = `
    <div class="quiz-meta-info">
      <span class="quiz-badge badge-subject">${q.subject}</span>
      <span class="quiz-badge badge-source">${q.source}</span>
      <span class="quiz-badge badge-source">Questão ${currentQuestionIdx + 1} de ${activeQuizQuestions.length}</span>
    </div>
    
    <div class="quiz-question-text">
      ${q.question}
    </div>
    
    <div class="quiz-options-list">
      ${optionsHtml}
    </div>

    <!-- Explanation slide-down box -->
    <div class="quiz-explanation-box" id="explanation-box">
      <div class="explanation-title" id="explanation-title"></div>
      <div class="explanation-text" id="explanation-text"></div>
    </div>
    
    <div class="quiz-actions">
      <span class="text-muted" style="font-size: 13px;">Acertos: ${score.correct}/${currentQuestionIdx}</span>
      <button class="btn" id="quiz-action-btn" onclick="checkQuizAnswer()" disabled>
        Verificar Resposta
      </button>
    </div>
  `;
}

// Select option handler
function selectQuizOption(optionKey) {
  if (answerChecked) return; // Cannot change answer after submission

  selectedOption = optionKey;
  
  // Remove selected class from all options
  document.querySelectorAll(".quiz-option").forEach(opt => opt.classList.remove("selected"));
  
  // Add selected class to current option
  const optCard = document.getElementById(`opt-${optionKey}`);
  if (optCard) optCard.classList.add("selected");

  // Enable button
  const actionBtn = document.getElementById("quiz-action-btn");
  if (actionBtn) actionBtn.removeAttribute("disabled");
}

// Check if answer is correct and reveal explanation
function checkQuizAnswer() {
  const actionBtn = document.getElementById("quiz-action-btn");
  if (actionBtn && (actionBtn.textContent.trim() === "Próxima Questão" || actionBtn.textContent.trim() === "Finalizar Simulado")) {
    nextQuizQuestion();
    return;
  }

  if (!selectedOption || answerChecked) return;

  answerChecked = true;
  const q = activeQuizQuestions[currentQuestionIdx];
  const isCorrect = selectedOption === q.correct;
  
  // Highlights
  const correctCard = document.getElementById(`opt-${q.correct}`);
  if (correctCard) {
    correctCard.classList.remove("selected");
    correctCard.classList.add("correct-answer");
  }

  if (!isCorrect) {
    const wrongCard = document.getElementById(`opt-${selectedOption}`);
    if (wrongCard) {
      wrongCard.classList.remove("selected");
      wrongCard.classList.add("wrong-answer");
    }
  } else {
    score.correct++;
  }

  // Render explanation box
  const expBox = document.getElementById("explanation-box");
  const expTitle = document.getElementById("explanation-title");
  const expText = document.getElementById("explanation-text");

  if (isCorrect) {
    expBox.className = "quiz-explanation-box correct";
    expTitle.innerHTML = `<i class="fa-solid fa-circle-check text-correct"></i> Resposta Correta!`;
    expTitle.className = "explanation-title text-correct";
  } else {
    expBox.className = "quiz-explanation-box wrong";
    expTitle.innerHTML = `<i class="fa-solid fa-circle-xmark text-wrong"></i> Resposta Incorreta (Gabarito: ${q.correct})`;
    expTitle.className = "explanation-title text-wrong";
  }

  if (q.option_explanations) {
    let breakdownHtml = `
      <div class="option-breakdown-title" style="margin-top: 14px; margin-bottom: 10px; font-weight: 600; font-size: 13.5px; color: #fff;">
        Justificativa de cada alternativa:
      </div>
      <div class="option-breakdown-list" style="display: flex; flex-direction: column; gap: 8px;">
    `;
    
    for (const [key, val] of Object.entries(q.option_explanations)) {
      const isOptionCorrect = key === q.correct;
      const isSelectedOption = key === selectedOption;
      
      let icon = isOptionCorrect 
        ? 'fa-circle-check text-correct' 
        : 'fa-circle-xmark text-wrong';
        
      let itemBg = isOptionCorrect 
        ? 'rgba(16, 185, 129, 0.04)' 
        : (isSelectedOption ? 'rgba(239, 68, 68, 0.04)' : 'rgba(255, 255, 255, 0.01)');
        
      let itemBorder = isOptionCorrect 
        ? 'rgba(16, 185, 129, 0.15)' 
        : (isSelectedOption ? 'rgba(239, 68, 68, 0.15)' : 'var(--border-color)');
        
      breakdownHtml += `
        <div class="option-breakdown-item" style="background-color: ${itemBg}; border: 1px solid ${itemBorder}; padding: 10px 14px; border-radius: 6px; display: flex; align-items: flex-start; gap: 10px; font-size: 13px; line-height: 1.5;">
          <i class="fa-solid ${icon}" style="margin-top: 3px; font-size: 14px;"></i>
          <div>
            <strong style="color: #fff; margin-right: 4px;">Alternativa ${key}:</strong>
            <span style="color: var(--text-muted);">${val}</span>
          </div>
        </div>
      `;
    }
    
    breakdownHtml += `
      </div>
      <div style="margin-top: 16px; padding-top: 12px; border-top: 1px solid rgba(255,255,255,0.06); font-size: 13px; color: var(--text-muted); line-height: 1.5;">
        <strong>Resumo da Questão:</strong> ${q.explanation}
      </div>
    `;
    
    expText.innerHTML = breakdownHtml;
  } else {
    expText.textContent = q.explanation;
  }
  
  expBox.style.display = "block";

  // Toggle button text
  if (currentQuestionIdx + 1 >= activeQuizQuestions.length) {
    actionBtn.textContent = "Finalizar Simulado";
  } else {
    actionBtn.textContent = "Próxima Questão";
  }
}

// Proceed to next question
function nextQuizQuestion() {
  currentQuestionIdx++;
  selectedOption = null;
  answerChecked = false;
  renderQuestion();
}

// Render final score summary card
function showQuizSummary() {
  const container = document.getElementById("quiz-card");
  const pct = Math.round((score.correct / score.total) * 100) || 0;
  
  let resultIcon = "fa-trophy text-cyan";
  let resultTitle = "Excelente resultado!";
  let resultDesc = `Vocês acertaram ${score.correct} de ${score.total} questões (${pct}%). Continuem nesse ritmo!`;

  if (pct < 50) {
    resultIcon = "fa-circle-exclamation text-purple";
    resultTitle = "Precisamos revisar!";
    resultDesc = `Vocês acertaram ${score.correct} de ${score.total} questões (${pct}%). Revisem a teoria nas abas de trilha e tentem novamente!`;
  }

  container.innerHTML = `
    <div class="quiz-score-summary">
      <i class="fa-solid ${resultIcon}"></i>
      <h4>${resultTitle}</h4>
      <p>${resultDesc}</p>
      <button class="btn btn-secondary" onclick="startSimulado('${quizCategory}')">
        <i class="fa-solid fa-rotate-left"></i> Refazer Simulado
      </button>
    </div>
  `;
}

// ==========================================================================
// DISCURSIVA LOGIC
// ==========================================================================

let allDiscursivas = [];
let activeDiscursiva = null;
let activeDiscursivaList = [];
let currentDiscursivaIdx = 0;
let discursivaCategory = 'ti';
let discursivaAnswerChecked = false;
let currentQuizType = 'mc'; // 'mc' = Multiple Choice, 'disc' = Discursiva

// Switch between Multiple Choice and Discursiva
function switchQuizType(type) {
  currentQuizType = type;
  const btnMc = document.getElementById("btn-quiz-mc");
  const btnDisc = document.getElementById("btn-quiz-disc");
  const mcContainer = document.getElementById("mc-container");
  const discContainer = document.getElementById("discursiva-container");

  if (type === 'mc') {
    btnMc.classList.add("active");
    btnDisc.classList.remove("active");
    mcContainer.style.display = "block";
    discContainer.style.display = "none";
    
    // Reset buttons styles to normal ciano/borderless
    btnMc.style.backgroundColor = "rgba(6, 182, 212, 0.08)";
    btnMc.style.borderColor = "rgba(6, 182, 212, 0.15)";
    btnDisc.style.backgroundColor = "transparent";
    btnDisc.style.borderColor = "transparent";
    
    startSimulado(quizCategory);
  } else {
    btnMc.classList.remove("active");
    btnDisc.classList.add("active");
    
    // Change style on active class for discursivas (purple)
    btnDisc.style.backgroundColor = "rgba(139, 92, 246, 0.08)";
    btnDisc.style.borderColor = "rgba(139, 92, 246, 0.15)";
    btnMc.style.backgroundColor = "transparent";
    btnMc.style.borderColor = "transparent";
    
    mcContainer.style.display = "none";
    discContainer.style.display = "block";
    startDiscursiva(discursivaCategory);
  }
}

// Start discursiva study
function startDiscursiva(category) {
  discursivaCategory = category;
  
  const btnTi = document.getElementById("btn-discursiva-ti");
  const btnBrother = document.getElementById("btn-discursiva-brother");
  
  if (category === 'ti') {
    btnTi.classList.add("active");
    btnBrother.classList.remove("active");
  } else {
    btnTi.classList.remove("active");
    btnBrother.classList.add("active");
  }

  activeDiscursivaList = allDiscursivas.filter(d => d.category === category);
  currentDiscursivaIdx = 0;
  
  if (activeDiscursivaList.length > 0) {
    activeDiscursiva = activeDiscursivaList[currentDiscursivaIdx];
  } else {
    activeDiscursiva = null;
  }
  
  discursivaAnswerChecked = false;
  renderDiscursiva();
}

// Render discursiva card
function renderDiscursiva() {
  const container = document.getElementById("discursiva-card");
  
  if (!activeDiscursiva) {
    container.innerHTML = `
      <div class="empty-state">
        <i class="fa-solid fa-triangle-exclamation text-cyan"></i> Nenhuma questão discursiva cadastrada para esta trilha ainda.
      </div>
    `;
    return;
  }

  const d = activeDiscursiva;
  
  container.innerHTML = `
    <div class="quiz-meta-info">
      <span class="quiz-badge badge-subject">${d.subject}</span>
      <span class="quiz-badge badge-source">Banca: ${d.banca}</span>
      <span class="quiz-badge badge-source">Discursiva ${currentDiscursivaIdx + 1} de ${activeDiscursivaList.length}</span>
    </div>

    <h4 style="color:#fff; font-family:var(--font-display); font-size:16px; margin-bottom:12px;">${d.title}</h4>
    
    <div class="discursiva-context-box">
      <strong>Contexto / Caso:</strong><br>
      ${d.context}
    </div>

    <div class="quiz-question-text" style="font-size:14.5px; border-left:3px solid var(--accent-cyan); padding-left:14px;">
      <strong>Enunciado da Questão:</strong><br>
      ${d.question.replace(/\n/g, '<br>')}
    </div>

    <div class="discursiva-input-area">
      <label for="user-discursiva-ans" style="display:block; font-size:12px; color:var(--text-muted); margin-bottom:8px; font-weight:600;">Rascunho de Resposta (opcional):</label>
      <textarea id="user-discursiva-ans" class="discursiva-textarea ${discursivaCategory === 'general' ? 'focus-brother' : ''}" placeholder="Escrevam aqui um rascunho da resposta de vocês antes de abrir a correção oficial do professor..."></textarea>
    </div>

    <!-- Feedback correction criteria & sample answer -->
    <div class="quiz-explanation-box correct" id="discursiva-feedback-box" style="display:none; background-color:rgba(255, 255, 255, 0.02); border-color:var(--border-color);">
      <div class="explanation-title text-cyan" style="color:var(--accent-cyan);"><i class="fa-solid fa-clipboard-check"></i> Critérios de Correção (Banca ${d.banca})</div>
      <div class="criteria-list">
        <div class="criteria-item"><strong>Item 1:</strong> ${d.criteria.item1}</div>
        <div class="criteria-item"><strong>Item 2:</strong> ${d.criteria.item2}</div>
      </div>
      
      <div class="explanation-title text-correct" style="margin-top:20px; color:var(--accent-green);"><i class="fa-solid fa-circle-check"></i> Resposta Padrão Sugerida pelo Professor</div>
      <div class="explanation-text" style="background-color:rgba(16, 185, 129, 0.02); border:1px solid rgba(16, 185, 129, 0.1); padding:16px; border-radius:6px; white-space: pre-line; color:var(--text-main); font-size:13.5px;">${d.sample_answer}</div>
    </div>

    <div class="quiz-actions" style="margin-top:20px;">
      <button class="btn btn-secondary" id="discursiva-restart-btn" onclick="restartDiscursivaCurrent()" style="display:none;">
        <i class="fa-solid fa-rotate-left"></i> Limpar Rascunho
      </button>
      <button class="btn" id="discursiva-action-btn" onclick="checkDiscursivaAnswer()">
        Verificar Padrão de Resposta (Espelho)
      </button>
    </div>
  `;
}

// Reveal discursiva correction criteria and sample answer
function checkDiscursivaAnswer() {
  const btn = document.getElementById("discursiva-action-btn");
  const restartBtn = document.getElementById("discursiva-restart-btn");
  const feedbackBox = document.getElementById("discursiva-feedback-box");
  
  if (discursivaAnswerChecked) {
    if (currentDiscursivaIdx + 1 < activeDiscursivaList.length) {
      currentDiscursivaIdx++;
      activeDiscursiva = activeDiscursivaList[currentDiscursivaIdx];
      discursivaAnswerChecked = false;
      renderDiscursiva();
    } else {
      startDiscursiva(discursivaCategory);
    }
    return;
  }

  discursivaAnswerChecked = true;
  feedbackBox.style.display = "block";
  if (restartBtn) restartBtn.style.display = "inline-flex";

  if (currentDiscursivaIdx + 1 < activeDiscursivaList.length) {
    btn.textContent = "Próxima Questão Discursiva";
  } else {
    btn.textContent = "Reiniciar do Início";
    btn.className = "btn btn-secondary";
  }
}

// Restart current discursiva question (clear text)
function restartDiscursivaCurrent() {
  const ta = document.getElementById("user-discursiva-ans");
  if (ta) ta.value = "";
  
  discursivaAnswerChecked = false;
  renderDiscursiva();
}

// Interactive YouTube Video Player Handler
function changeVideo(iframeId, videoId, btn) {
  const iframe = document.getElementById(iframeId);
  if (iframe) {
    iframe.src = `https://www.youtube.com/embed/${videoId}`;
  }
  
  // Update active status inside the playlist
  const playlist = btn.parentElement;
  playlist.querySelectorAll(".playlist-btn").forEach(b => b.classList.remove("active"));
  btn.classList.add("active");
}

// Filter Glossario Cards
function filterGlossario() {
  const input = document.getElementById('glossario-search');
  if (!input) return;
  const filter = input.value.toLowerCase();
  const cards = document.querySelectorAll('.glossario-card');
  
  cards.forEach(card => {
    const text = card.textContent.toLowerCase();
    if (text.includes(filter)) {
      card.style.display = "block";
    } else {
      card.style.display = "none";
    }
  });
}

function clearGlossarioSearch() {
  const input = document.getElementById('glossario-search');
  if (input) {
    input.value = "";
    filterGlossario();
  }
}

