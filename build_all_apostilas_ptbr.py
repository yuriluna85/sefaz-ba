import os
from fpdf import FPDF

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONCURSO_DIR = os.path.join(BASE_DIR, 'Concurso SEFAZ')

class UniversalStudyBookletPDF(FPDF):
    def __init__(self, subject_name):
        super().__init__()
        self.subject_name = subject_name
        self.alias_nb_pages()
        self.set_auto_page_break(auto=True, margin=15)

    def clean_text(self, text):
        replacements = {
            '\u201c': '"', '\u201d': '"',
            '\u2018': "'", '\u2019': "'",
            '\u2013': '-', '\u2014': '-',
            '\u2022': '*', '\u2026': '...',
            '\xa0': ' ',
        }
        for orig, rep in replacements.items():
            text = text.replace(orig, rep)
        return text.encode('latin-1', 'replace').decode('latin-1')

    def header(self):
        self.set_fill_color(101, 163, 13)  # Lime-600 #65a30d
        self.rect(0, 0, 210, 8, 'F')
        
        self.set_y(12)
        self.set_font('Helvetica', 'B', 8)
        self.set_text_color(110, 110, 110)
        self.cell(100, 5, self.clean_text('SEFAZ-BA 2026 - REVISÃO DIDÁTICA E GLOSSÁRIO COMPLETO'), 0, 0, 'L')
        self.set_font('Helvetica', 'BI', 8)
        self.set_text_color(101, 163, 13)
        self.cell(0, 5, self.clean_text(self.subject_name.upper()), 0, 1, 'R')
        
        self.set_draw_color(220, 220, 220)
        self.line(10, 18, 200, 18)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_draw_color(220, 220, 220)
        self.line(10, 282, 200, 282)
        
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(100, 10, self.clean_text('Material Atualizado em Português Brasileiro Fluido (TI & Geral)'), 0, 0, 'L')
        
        self.set_font('Helvetica', 'B', 8)
        self.cell(0, 10, self.clean_text(f'Página {self.page_no()}/{{nb}}'), 0, 0, 'R')

    def add_cover(self, title, subtitle):
        self.add_page()
        self.ln(25)
        
        self.set_font('Helvetica', 'B', 22)
        self.set_text_color(15, 23, 42)
        self.multi_cell(0, 10, self.clean_text(title), 0, 'C')
        self.ln(8)
        
        self.set_draw_color(101, 163, 13)
        self.set_line_width(1.5)
        self.line(40, self.get_y(), 170, self.get_y())
        self.set_line_width(0.2)
        self.ln(12)
        
        self.set_font('Helvetica', '', 12)
        self.set_text_color(71, 85, 105)
        self.multi_cell(0, 7, self.clean_text(subtitle), 0, 'C')
        self.ln(35)
        
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(15, 23, 42)
        self.cell(0, 6, self.clean_text('PREPARAÇÃO ESTRATÉGICA SEFAZ-BA 2026'), 0, 1, 'C')
        self.set_font('Helvetica', '', 10)
        self.set_text_color(100, 116, 139)
        self.cell(0, 6, self.clean_text('Cargos: Auditor Fiscal (TI) & Agente de Tributos Estaduais (Geral)'), 0, 1, 'C')
        self.cell(0, 6, self.clean_text('Linguagem Clara em Português Brasileiro e Glossário Didático de Siglas'), 0, 1, 'C')
        self.ln(40)
        
        self.set_font('Helvetica', 'I', 9)
        self.set_text_color(148, 163, 184)
        self.cell(0, 10, self.clean_text('Edição revisada: sem jargões obscuros, com explicação de todas as siglas técnicas.'), 0, 1, 'C')

    def add_section(self, section_title):
        self.ln(3)
        self.set_font('Helvetica', 'B', 11.5)
        self.set_text_color(15, 23, 42)
        self.set_fill_color(241, 245, 249)
        self.cell(0, 9, self.clean_text(f'  {section_title}'), 0, 1, 'L', fill=True)
        self.ln(2)

    def add_subsection(self, sub_title):
        self.ln(2)
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(101, 163, 13)
        self.cell(0, 6, self.clean_text(sub_title), 0, 1, 'L')
        self.ln(1)

    def add_paragraph(self, text):
        self.set_font('Helvetica', '', 9.5)
        self.set_text_color(51, 65, 85)
        self.multi_cell(0, 5.2, self.clean_text(text))
        self.ln(2)

    def add_bullet_point(self, title, description):
        self.set_font('Helvetica', 'B', 9.5)
        self.set_text_color(15, 23, 42)
        self.cell(8, 6, '-', 0, 0, 'C')
        self.cell(0, 6, self.clean_text(title), 0, 1, 'L')
        self.set_font('Helvetica', '', 9.5)
        self.set_text_color(51, 65, 85)
        self.set_x(18)
        self.multi_cell(0, 5, self.clean_text(description))
        self.ln(1.5)

    def add_tip_box(self, title, tip_text):
        self.ln(2)
        x = self.get_x()
        y = self.get_y()
        self.set_fill_color(247, 254, 231)
        self.set_draw_color(101, 163, 13)
        self.set_font('Helvetica', '', 9.5)
        lines = len(self.multi_cell(180, 5, self.clean_text(f'DICA DIDÁTICA: {tip_text}'), dry_run=True, output="LINES"))
        box_height = (lines * 5) + 12
        
        self.rect(x, y, 190, box_height, 'DF')
        self.set_fill_color(101, 163, 13)
        self.rect(x, y, 4, box_height, 'F')
        
        self.set_xy(x + 8, y + 3)
        self.set_font('Helvetica', 'B', 9.5)
        self.set_text_color(63, 98, 18)
        self.cell(0, 5, self.clean_text(title.upper()), 0, 1, 'L')
        
        self.set_x(x + 8)
        self.set_font('Helvetica', 'I', 9.5)
        self.set_text_color(57, 88, 12)
        self.multi_cell(178, 5, self.clean_text(tip_text))
        self.set_y(y + box_height + 4)

# DATA DICTIONARY FOR ALL 15 SUBJECTS
BOOKLETS_DATA = [
    {
        "filename": "Apostila_Auditoria_Fiscal.pdf",
        "subject": "Auditoria Fiscal",
        "title": "Manual de Estudos: Auditoria Fiscal",
        "subtitle": "Conceitos Didáticos, Análise de Risco e Materialidade, Planejamento Dinâmico e Amostragem",
        "glossary": [
            ("NBC TA", "Norma Brasileira de Contabilidade Técnica de Auditoria (regras para auditores externos)."),
            ("NBC TI", "Norma Brasileira de Contabilidade Técnica de Auditoria Interna (regras para auditores do próprio órgão)."),
            ("CFC", "Conselho Federal de Contabilidade (autarquia que edita as normas contábeis no Brasil)."),
            ("CIAP", "Controle de Crédito de ICMS do Ativo Permanente (aproveitamento do imposto em 1/48 por mês).")
        ],
        "sections": [
            {
                "title": "1. Conceito e Tipos de Auditoria sem Jargões",
                "content": "A auditoria é um processo sistemático de verificação objetiva de operações financeiras e tributárias. Ela avalia se os livros e obrigações fiscais refletem a realidade e cumprem a lei.",
                "bullets": [
                    ("Auditoria Interna:", "Realizada por servidores do próprio órgão com foco em melhoria contínua e assessoria operacional."),
                    ("Auditoria Externa / Independente:", "Realizada por profissionais autônomos para emitir parecer formal sobre a veracidade das contas.")
                ],
                "tip": ("Planejamento Dinâmico", "O planejamento da auditoria não é uma etapa estanque ou isolada. Ele é contínuo e evolui conforme novas evidências são encontradas em campo.")
            }
        ]
    },
    {
        "filename": "Apostila_Contabilidade_Geral.pdf",
        "subject": "Contabilidade Geral",
        "title": "Manual de Estudos: Contabilidade Geral",
        "subtitle": "Patrimônio, Lançamentos Contábeis, Demonstrações Financeiras e Pronunciamentos do CPC",
        "glossary": [
            ("CPC", "Comitê de Pronunciamentos Contábeis (órgão que converge a contabilidade brasileira ao padrão internacional IFRS)."),
            ("DRE", "Demonstração do Resultado do Exercício (relatório que mostra se a empresa teve lucro ou prejuízo no período)."),
            ("DFC", "Demonstração dos Fluxos de Caixa (relatório que detalha todas as entradas e saídas efetivas de dinheiro)."),
            ("DMPL", "Demonstração das Mutações do Patrimônio Líquido (detalha as variações no capital dos sócios e reservas).")
        ],
        "sections": [
            {
                "title": "1. Mecanismo de Débito e Crédito em Português Simples",
                "content": "Diferente do senso comum bancário, na contabilidade o 'Débito' representa a aplicação de recursos (bens e direitos) e o 'Crédito' representa a origem dos recursos (passivo e patrimônio líquido).",
                "bullets": [
                    ("Bens e Direitos (Ativo):", "Aumentam com lançamentos a Débito e diminuem com lançamentos a Crédito."),
                    ("Obrigacões (Passivo) e Patrimônio Líquido:", "Aumentam com lançamentos a Crédito e diminuem com lançamentos a Débito.")
                ],
                "tip": ("Regra das Partidas Dobradas", "Para todo e qualquer lançamento contábil, a soma dos débitos deve ser rigorosamente igual à soma dos créditos!")
            }
        ]
    },
    {
        "filename": "Apostila_Direito_Tributario.pdf",
        "subject": "Direito Tributário",
        "title": "Manual de Estudos: Direito Tributário",
        "subtitle": "Sistema Tributário Nacional, Código Tributário Nacional (CTN) e Limitações ao Poder de Tributar",
        "glossary": [
            ("CTN", "Código Tributário Nacional (Lei nº 5.172/1966, que disciplina as regras gerais sobre tributos no Brasil)."),
            ("STN", "Sistema Tributário Nacional (conjunto de princípios e regras constitucionais que regem a cobrança de impostos)."),
            ("ICMS", "Imposto sobre Circulação de Mercadorias e Serviços (principal imposto estadual arrecadado pela SEFAZ)."),
            ("IPVA", "Imposto sobre a Propriedade de Veículos Automotores.")
        ],
        "sections": [
            {
                "title": "1. Conceito Legal de Tributo (Art. 3º do CTN)",
                "content": "Tributo é toda prestação pecuniária compulsória (obrigatória em dinheiro), que não constitua sanção de ato ilícito (não é multa), instituída em lei e cobrada mediante atividade administrativa plenamente vinculada.",
                "bullets": [
                    ("Não é Multa:", "O tributo nasce de um fato lícito (ex: vender mercadoria ou ter propriedade). A multa nasce de uma infração à lei."),
                    ("Atividade Vinculada:", "O fiscal de tributos é obrigado por lei a cobrar o valor devido, sem margem para vontades pessoais.")
                ],
                "tip": ("Fato Gerador", "Fato gerador é o acontecimento da vida real previsto na lei que faz nascer a obrigação de pagar o tributo.")
            }
        ]
    },
    {
        "filename": "Apostila_Legislacao_Tributaria_BA.pdf",
        "subject": "Legislação Tributária da Bahia",
        "title": "Manual de Estudos: Legislação Tributária do Estado da Bahia",
        "subtitle": "ICMS-BA, IPVA-BA, ITD-BA e Processo Administrativo Fiscal (PAF-BA)",
        "glossary": [
            ("RICMS-BA", "Regulamento do ICMS do Estado da Bahia (Decreto estadual que consolida as regras do imposto no estado)."),
            ("PAF-BA", "Processo Administrativo Fiscal da Bahia (Lei nº 3.956/1981, que regula contestações e recursos de autuações)."),
            ("CONSEF", "Conselho de Fazenda Estadual (órgão colegiado encarregado de julgar os recursos fiscais na Bahia)."),
            ("ITD", "Imposto sobre Transmissão Causa Mortis e Doação (imposto estadual sobre heranças e doações).")
        ],
        "sections": [
            {
                "title": "1. Estrutura dos Tributos Estaduais Baianos",
                "content": "A Secretaria da Fazenda do Estado da Bahia (SEFAZ-BA) administra três impostos principais previstos na Constituição Estadual e Federal: ICMS, IPVA e ITD.",
                "bullets": [
                    ("ICMS-BA:", "Imposto incidente sobre operações de circulação de mercadorias e prestação de serviços de transporte intermunicipal e comunicação."),
                    ("PAF-BA:", "O processo administrativo garante a ampla defesa do contribuinte autuado antes de qualquer cobrança judicial.")
                ],
                "tip": ("Substituição Tributária", "No ICMS, a lei pode atribuir a um único fabricante a responsabilidade de recolher o imposto de toda a cadeia de vendas subsequente.")
            }
        ]
    },
    {
        "filename": "Apostila_Direito_Administrativo.pdf",
        "subject": "Direito Administrativo",
        "title": "Manual de Estudos: Direito Administrativo",
        "subtitle": "Organização Administrativa, Atos Administrativos e Nova Lei de Licitações (Lei 14.133/2021)",
        "glossary": [
            ("NLLC", "Nova Lei de Licitações e Contratos (Lei nº 14.133/2021, que unificou as regras de compras públicas no Brasil)."),
            ("LIA", "Lei de Improbidade Administrativa (Lei nº 8.429/1992 com alterações da Lei nº 14.230/2021)."),
            ("PAE", "Processo Administrativo Eletrônico no âmbito da administração pública.")
        ],
        "sections": [
            {
                "title": "1. Princípios Expressos da Administração Pública (LIMPE)",
                "content": "O artigo 37 da Constituição Federal estabelece os cinco princípios fundamentais que regem a conduta de todo servidor público: Legalidade, Impessoalidade, Moralidade, Publicidade e Eficiência.",
                "bullets": [
                    ("Legalidade:", "O administrador público só pode fazer o que a lei expressamente autoriza."),
                    ("Impessoalidade:", "O atendimento e as decisões públicas devem ser neutros, sem favoritismos ou perseguições.")
                ],
                "tip": ("Atos Administrativos", "Todo ato administrativo possui atributos de presunção de legitimidade, imperatividade e autoexecutariedade.")
            }
        ]
    },
    {
        "filename": "Apostila_Direito_Constitucional.pdf",
        "subject": "Direito Constitucional",
        "title": "Manual de Estudos: Direito Constitucional",
        "subtitle": "Direitos Fundamentais, Organização do Estado e Repartição de Competências Tributárias",
        "glossary": [
            ("CF/88", "Constituição da República Federativa do Brasil de 1988 (Lei Maior do país)."),
            ("STF", "Supremo Tribunal Federal (órgão máximo de guarda da Constituição no Brasil)."),
            ("ADI", "Ação Direta de Inconstitucionalidade (mecanismo para anular leis que violem a Constituição).")
        ],
        "sections": [
            {
                "title": "1. Direitos e Garantias Fundamentais",
                "content": "Os direitos fundamentais são cláusulas pétreas que garantem a liberdade, igualdade, segurança e propriedade dos cidadãos perante o Estado.",
                "bullets": [
                    ("Princípio da Isonomia:", "Todos são iguais perante a lei, sem distinção de qualquer natureza."),
                    ("Inviolabilidade do Domicílio:", "A casa é asilo inviolável do indivíduo, ninguém nela podendo penetrar sem consentimento, salvo em flagrante delito, desastre ou por determinação judicial durante o dia.")
                ],
                "tip": ("Cláusulas Pétreas", "São matérias que não podem ser abolidas nem mesmo por Proposta de Emenda à Constituição (PEC).")
            }
        ]
    },
    {
        "filename": "Apostila_Banco_Dados_BI.pdf",
        "subject": "Banco de Dados & BI",
        "title": "Manual de Estudos: Banco de Dados e Business Intelligence",
        "subtitle": "Modelagem Relacional, Linguagem SQL, Data Warehouse e Modelagem Dimensional",
        "glossary": [
            ("SQL", "Structured Query Language (Linguagem Padrão de Consulta a Bancos de Dados Relacionais)."),
            ("BI", "Business Intelligence (Conjunto de estratégias e ferramentas para transformação de dados em insights de negócios)."),
            ("OLAP", "Online Analytical Processing (Tecnologia de análise multidimensional de dados para tomada de decisão)."),
            ("ETL", "Extract, Transform, Load (Processo de extração, transformação e carga de dados em um Data Warehouse).")
        ],
        "sections": [
            {
                "title": "1. Bancos de Dados Relacionais e Linguagem SQL",
                "content": "Os bancos de dados relacionais organizam informações em tabelas compostas por linhas (registros) e colunas (atributos). A linguagem SQL é utilizada para manipular e consultar essas estruturas.",
                "bullets": [
                    ("DDL (Data Definition Language):", "Comandos de definição de estrutura como CREATE, ALTER, DROP."),
                    ("DML (Data Manipulation Language):", "Comandos de manipulação de dados como SELECT, INSERT, UPDATE, DELETE.")
                ],
                "tip": ("Modelagem Dimensional (Star Schema)", "Em Data Warehouses de fiscalização, utiliza-se a tabela Fato no centro rodeada por tabelas Dimensão para consultas analíticas rápidas.")
            }
        ]
    },
    {
        "filename": "Apostila_Ciencia_Dados_Big_Data.pdf",
        "subject": "Ciência de Dados & Big Data",
        "title": "Manual de Estudos: Ciência de Dados e Big Data",
        "subtitle": "Arquiteturas Distribuidas, Machine Learning, Mineração de Dados e Detecção de Fraudes",
        "glossary": [
            ("HDFS", "Hadoop Distributed File System (Sistema de arquivos distribuído para armazenamento de grandes volumes de dados)."),
            ("ML", "Machine Learning / Aprendizado de Máquina (Algoritmos que aprendem padrões a partir de dados históricos)."),
            ("NLP", "Natural Language Processing / Processamento de Linguagem Natural (Análise automatizada de textos e documentos).")
        ],
        "sections": [
            {
                "title": "1. Os V's do Big Data aplicados à Fiscalização",
                "content": "O ecossistema de Big Data na fiscalização tributária lida com os 5 V's tradicionais: Volume, Velocidade, Variedade, Veracidade e Valor.",
                "bullets": [
                    ("Detecção de Anomalias:", "Modelos de Machine Learning identificam desvios de padrões em notas fiscais eletrônicas para combater sonegação."),
                    ("Processamento em Tempo Real:", "Ferramentas como Apache Spark processam milhões de eventos fiscais por segundo.")
                ],
                "tip": ("Aprendizado Supervisionado vs Não Supervisionado", "No aprendizado supervisionado treinamos modelos com dados rotulados (fraude/não fraude). No não supervisionado o algoritmo agrupa dados por similaridade nativa.")
            }
        ]
    },
    {
        "filename": "Apostila_Engenharia_Software.pdf",
        "subject": "Engenharia de Software",
        "title": "Manual de Estudos: Engenharia de Software",
        "subtitle": "Metodologias Ágeis, Arquitetura de Microsserviços, Engenharia de Requisitos e Testes",
        "glossary": [
            ("UML", "Unified Modeling Language (Linguagem de modelagem visual para diagramação de sistemas)."),
            ("CI/CD", "Continuous Integration / Continuous Deployment (Integração e Implantação Contínuas de software)."),
            ("API", "Application Programming Interface (Interface de Programação de Aplicações para comunicação entre sistemas).")
        ],
        "sections": [
            {
                "title": "1. Metodologias Ágeis (Scrum e Kanban)",
                "content": "A engenharia de software moderna prioriza entregas incrementais e iterativas de valor, substituindo modelos rígidos tradicionais por ciclos curtos de desenvolvimento.",
                "bullets": [
                    ("Sprint no Scrum:", "Ciclo de trabalho com duração fixa (geralmente de 2 a 4 semanas) focado na entrega de um incremento funcional."),
                    ("Kanban:", "Gestão visual do fluxo de trabalho por meio de cartões em colunas (A Fazer, Em Andamento, Concluído).")
                ],
                "tip": ("Arquitetura de Microsserviços", "Aplicações modernas dividem sistemas monolíticos em serviços autônomos e independentes comunicando-se via APIs HTTP/REST.")
            }
        ]
    },
    {
        "filename": "Apostila_Gestao_Governanca_TI.pdf",
        "subject": "Gestão e Governança de TI",
        "title": "Manual de Estudos: Gestão e Governança de TI",
        "subtitle": "Frameworks COBIT 2019, ITIL v4, PMBOK 7ª Edição e Alinhamento Estratégico",
        "glossary": [
            ("COBIT", "Control Objectives for Information and Related Technology (Framework focado na governança de TI corporativa)."),
            ("ITIL", "Information Technology Infrastructure Library (Biblioteca de melhores práticas para gerenciamento de serviços de TI)."),
            ("PMBOK", "Project Management Body of Knowledge (Guia de melhores práticas para gestão de projetos do PMI).")
        ],
        "sections": [
            {
                "title": "1. Governança vs Gerenciamento de TI (COBIT)",
                "content": "O COBIT estabelece uma distinção clara entre Governança (avaliação, direcionamento e monitoramento por parte da alta administração) e Gerenciamento (planejamento, construção, execução e monitoramento operacional de atividades).",
                "bullets": [
                    ("Governança (EDM):", "Avaliar, Direcionar e Monitorar."),
                    ("Gerenciamento (APO, BAI, DSS, MEA):", "Alinhar, Planejar, Construir, Entregar, Suportar e Monitorar.")
                ],
                "tip": ("ITIL v4 e Sistema de Valor de Serviço (SVS)", "O ITIL v4 foca na co-criação de valor junto aos clientes internos e externos por meio de fluxos de valor de serviço.")
            }
        ]
    },
    {
        "filename": "Apostila_Seguranca_Informacao.pdf",
        "subject": "Segurança da Informação",
        "title": "Manual de Estudos: Segurança da Informação",
        "subtitle": "Princípios da Segurança (CIDA), Criptografia, ISO 27001 e Lei Geral de Proteção de Dados (LGPD)",
        "glossary": [
            ("LGPD", "Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709/2018, que regula o tratamento de dados pessoais no Brasil)."),
            ("ANPD", "Autoridade Nacional de Proteção de Dados (órgão federal responsável por fiscalizar a LGPD)."),
            ("CIDA", "Confidencialidade, Integridade, Disponibilidade e Autenticidade (pilares da segurança da informação).")
        ],
        "sections": [
            {
                "title": "1. Pilares Fundamentais da Segurança",
                "content": "A segurança da informação visa proteger os ativos de dados contra acessos não autorizados, alterações indevidas ou indisponibilidade de serviços.",
                "bullets": [
                    ("Confidencialidade:", "Garante que a informação só seja acessada por pessoas devidamente autorizadas."),
                    ("Integridade:", "Garante que a informação não seja alterada ou corrompida de forma não autorizada.")
                ],
                "tip": ("LGPD no Setor Público", "A administração pública deve tratar dados pessoais estritamente para o atendimento de sua finalidade pública e execução das competências legais.")
            }
        ]
    },
    {
        "filename": "Apostila_Estatistica_RLM.pdf",
        "subject": "Estatística & RLM",
        "title": "Manual de Estudos: Estatística e Raciocínio Lógico-Matemático",
        "subtitle": "Lógica Proposicional, Análise Combinatória, Probabilidade e Estatística Descritiva",
        "glossary": [
            ("RLM", "Raciocínio Lógico-Matemático."),
            ("DP", "Desvio Padrão (medida de dispersão dos dados em relação à média)."),
            ("VAR", "Variância (quadrado do desvio padrão).")
        ],
        "sections": [
            {
                "title": "1. Lógica Proposicional e Tabelas-Verdade",
                "content": "A lógica matemática analisa a validade de argumentos formados por proposições simples e compostas conectadas por operadores lógicos (E, OU, SE... ENTÃO, SE E SOMENTE SE).",
                "bullets": [
                    ("Condicional (Se P, então Q):", "Só é falsa quando a primeira proposição P for Verdadeira e a segunda Q for Falsa (V -> F é Falo)."),
                    ("Negação de 'Se P então Q':", "Conserva a primeira E nega a segunda (P e Não Q).")
                ],
                "tip": ("Medidas de Tendência Central", "Média é o valor médio aritmético; Mediana é o valor central com os dados ordenados; Moda é o valor que mais se repete.")
            }
        ]
    },
    {
        "filename": "Apostila_Financas_Publicas.pdf",
        "subject": "Finanças Públicas",
        "title": "Manual de Estudos: Finanças Públicas & AFO",
        "subtitle": "Orçamento Público, PPA, LDO, LOA, Lei de Responsabilidade Fiscal (LRF) e Receitas Públicas",
        "glossary": [
            ("AFO", "Administração Financeira e Orçamentária."),
            ("LRF", "Lei de Responsabilidade Fiscal (Lei Complementar nº 101/2000, que estabelece normas de finanças voltadas para a gestão fiscal responsável)."),
            ("PPA", "Plano Plurianual (planejamento estratégico de 4 anos)."),
            ("LDO", "Lei de Diretrizes Orçamentárias."),
            ("LOA", "Lei Orçamentária Anual.")
        ],
        "sections": [
            {
                "title": "1. O Triplo Orçamentário (PPA, LDO, LOA)",
                "content": "A gestão financeira pública no Brasil segue um planejamento integrado composto por três leis orçamentárias interligadas aprovadas pelo Poder Legislativo.",
                "bullets": [
                    ("PPA (Plano Plurianual):", "Define diretrizes, objetivos e metas de médio prazo para 4 anos."),
                    ("LDO (Diretrizes Orçamentárias):", "Orienta a elaboração da LOA e define as metas fiscais anuais."),
                    ("LOA (Orçamento Anual):", "Estima as receitas e fixa as despesas para o exercício financeiro de 1 ano.")
                ],
                "tip": ("Regra de Ouro Orçamentária", "Veda a realização de operações de créditos (empréstimos) que excedam o montante das despesas de capital (investimentos).")
            }
        ]
    },
    {
        "filename": "Apostila_Igualdade_Racial_Genero.pdf",
        "subject": "Igualdade Racial & Gênero",
        "title": "Manual de Estudos: Legislação sobre Igualdade Racial e de Gênero",
        "subtitle": "Estatuto da Igualdade Racial (Lei 12.288/2010), Legislação Estadual da Bahia e Políticas Afirmativas",
        "glossary": [
            ("PIR", "Políticas de Promoção da Igualdade Racial."),
            ("SINAPIR", "Sistema Nacional de Promoção da Igualdade Racial."),
            ("CSEPIR", "Conselho Estadual para a Reparação e Promoção da Igualdade Racial da Bahia.")
        ],
        "sections": [
            {
                "title": "1. Legislação de Proteção e Promoção da Igualdade na Bahia",
                "content": "O Estado da Bahia é pioneiro no fortalecimento de políticas públicas afirmativas e no combate ao racismo institucional, garantindo cotas e diretrizes de inclusão em concursos públicos.",
                "bullets": [
                    ("Ações Afirmativas:", "Medidas especiais e temporárias adotadas pelo Estado para reparar desigualdades históricas acumuladas."),
                    ("Discriminação Racial:", "Toda distinção, exclusão, restrição ou preferência baseada em raça ou cor que anule o exercício de direitos.")
                ],
                "tip": ("Estatuto da Igualdade Racial", "Garante o direito à saúde integral, educação, cultura, moradia e trabalho digno para a população negra.")
            }
        ]
    },
    {
        "filename": "Apostila_Lingua_Portuguesa.pdf",
        "subject": "Língua Portuguesa",
        "title": "Manual de Estudos: Língua Portuguesa para Bancas Fiscais",
        "subtitle": "Interpretação de Textos, Sintaxe, Coesão, Concordância e Regência Foco FCC/FGV",
        "glossary": [
            ("FCC", "Fundação Carlos Chagas (banca tradicional em concursos fiscais estaduais)."),
            ("FGV", "Fundação Getulio Vargas (banca com forte cobrança de semântica e interpretação).")
        ],
        "sections": [
            {
                "title": "1. Coesão Textual e Reescritação de Frases",
                "content": "As bancas examinadoras de área fiscal cobram com rigor a clareza, a correção gramatical e a equivalência de sentidos na reescrita de frases.",
                "bullets": [
                    ("Conjunctions Adversativas (mas, porém, contudo, todavia, no entanto):", "Introduzem ideias de oposição ou contraste."),
                    ("Uso da Crase:", "Acontece quando há a fusão da preposição 'a' com o artigo feminino 'a'. Não ocorre crase antes de verbos ou palavras masculinas.")
                ],
                "tip": ("Crase Facultativa", "A crase é facultativa antes de nomes próprios femininos, antes de pronomes possessivos femininos e depois da preposição 'até'.")
            }
        ]
    }
]

def generate_all_booklets():
    print("Iniciando a geração e revisão didática de TODAS as 15 apostilas em PT-BR...")
    os.makedirs(CONCURSO_DIR, exist_ok=True)
    
    count = 0
    for b in BOOKLETS_DATA:
        pdf = UniversalStudyBookletPDF(b["subject"])
        pdf.add_cover(b["title"], b["subtitle"])
        
        # PAGE 2: GLOSSARY
        pdf.add_page()
        pdf.add_section("0. Glossário Introdutório de Siglas e Termos da Matéria")
        pdf.add_paragraph("Apresentamos o significado didático e direto das principais siglas cobradas nesta disciplina:")
        for term, desc in b["glossary"]:
            pdf.add_bullet_point(f"{term}:", desc)
            
        # SECTIONS
        for sec in b["sections"]:
            pdf.add_page()
            pdf.add_section(sec["title"])
            pdf.add_paragraph(sec["content"])
            for title, desc in sec["bullets"]:
                pdf.add_bullet_point(title, desc)
            if "tip" in sec:
                t_title, t_text = sec["tip"]
                pdf.add_tip_box(t_title, t_text)
                
        out_path = os.path.join(CONCURSO_DIR, b["filename"])
        pdf.output(out_path)
        size_kb = os.path.getsize(out_path) / 1024
        count += 1
        print(f"[{count}/15] Gerada com sucesso: {b['filename']} ({size_kb:.1f} KB)")
        
    print("\nTODAS AS 15 APOSTILAS FORAM REVISADAS E REGERADAS EM PT-BR FLUIDO!")

if __name__ == "__main__":
    generate_all_booklets()
