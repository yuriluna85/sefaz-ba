import json
import os

QUESTIONS_FILE = r"G:\Meu Drive\ESPECIALIZAÇÕES\Concurso SEFAZ\..\Concurso SEFAZ Dashboard\questions.json"

new_fcc_questions = [
    {
        "id": "q_ti_7",
        "category": "ti",
        "subject": "Banco de Dados - SQL",
        "source": "FCC - Sefaz-SP (Adaptada)",
        "question": "Considere a existência de uma tabela chamada 'vendas' com as colunas 'id_vendedor', 'data_venda' e 'valor_venda'. Para selecionar o id do vendedor e a soma total de suas vendas, retornando apenas os vendedores cujo valor acumulado de vendas seja superior a R$ 50.000,00, deve-se utilizar qual sintaxe SQL?",
        "options": {
            "A": "SELECT id_vendedor, SUM(valor_venda) FROM vendas WHERE SUM(valor_venda) > 50000 GROUP BY id_vendedor;",
            "B": "SELECT id_vendedor, SUM(valor_venda) FROM vendas GROUP BY id_vendedor HAVING SUM(valor_venda) > 50000;",
            "C": "SELECT id_vendedor, SUM(valor_venda) FROM vendas GROUP BY id_vendedor WHERE valor_venda > 50000;",
            "D": "SELECT id_vendedor, SUM(valor_venda) FROM vendas HAVING SUM(valor_venda) > 50000;",
            "E": "SELECT id_vendedor, SUM(valor_venda) FROM vendas WHERE valor_venda > 50000 GROUP BY id_vendedor;"
        },
        "correct": "B",
        "explanation": "Em SQL, funções agregadas (como SUM) não podem ser utilizadas na cláusula WHERE. Para filtrar o resultado de agrupamentos (GROUP BY), deve-se utilizar a cláusula HAVING. Portanto, a resposta correta é a alternativa B."
    },
    {
        "id": "q_ti_8",
        "category": "ti",
        "subject": "Tecnologia da Informação - Python",
        "source": "FCC - Área Fiscal (Adaptada)",
        "question": "Na linguagem Python, utilizando a biblioteca Pandas, dispõe-se de um DataFrame chamado 'df_contribuintes'. Qual comando deve ser executado para retornar a contagem de linhas e colunas (estrutura dimensional) desse DataFrame na forma de uma tupla?",
        "options": {
            "A": "df_contribuintes.dimensions()",
            "B": "df_contribuintes.size",
            "C": "df_contribuintes.shape",
            "D": "df_contribuintes.columns.count()",
            "E": "df_contribuintes.info()"
        },
        "correct": "C",
        "explanation": "No Pandas, o atributo '.shape' retorna uma tupla representando a dimensionalidade do DataFrame (número de linhas, número de colunas). O atributo '.size' retorna o número total de elementos (linhas x colunas)."
    },
    {
        "id": "q_ti_9",
        "category": "ti",
        "subject": "Engenharia de Software",
        "source": "FCC - TRT (Adaptada)",
        "question": "Os padrões de projeto (Design Patterns) do GoF catalogam soluções para problemas comuns no desenvolvimento orientado a objetos. Qual padrão de projeto tem como objetivo garantir que uma classe tenha apenas uma única instância em toda a aplicação e fornecer um ponto global de acesso para ela?",
        "options": {
            "A": "Factory Method",
            "B": "Singleton",
            "C": "Builder",
            "D": "Facade",
            "E": "Observer"
        },
        "correct": "B",
        "explanation": "O padrão Singleton garante a existência de apenas uma instância de uma determinada classe durante o ciclo de vida da aplicação, mantendo um construtor privado e um método estático que gerencia e retorna a referência da instância única."
    },
    {
        "id": "q_ti_10",
        "category": "ti",
        "subject": "Governança de TI - ITIL v4",
        "source": "FCC - ALESP (Adaptada)",
        "question": "No framework ITIL v4, a cadeia de valor de serviço (Service Value Chain) é um modelo operacional que descreve as principais atividades necessárias para responder à demanda e facilitar a criação de valor. Qual atividade da cadeia de valor de serviço tem como propósito assegurar um entendimento compartilhado dos requisitos, da visão e dos objetivos de melhoria para todos os produtos e serviços?",
        "options": {
            "A": "Engajar (Engage)",
            "B": "Planejar (Plan)",
            "C": "Melhorar (Improve)",
            "D": "Obter/Construir (Obtain/Build)",
            "E": "Desenho e Transição (Design and Transition)"
        },
        "correct": "B",
        "explanation": "O propósito da atividade 'Planejar' (Plan) é assegurar o entendimento compartilhado da visão, situação atual, direção e melhoria para os quatro aspectos e todos os produtos e serviços da organização."
    },
    {
        "id": "q_ti_11",
        "category": "ti",
        "subject": "Tecnologia da Informação - Regulamentação",
        "source": "FCC - TRF (Adaptada)",
        "question": "Com base na Lei de Acesso à Informação (LAI — Lei nº 12.527/2011), as informações relativas à soberania nacional e à integridade do território nacional, caso reveladas, possam colocar em risco a segurança da sociedade ou do Estado. Essas informações podem ser classificadas como ultrassecretas, secretas ou reservadas, e seus prazos máximos de restrição de acesso são, respectivamente:",
        "options": {
            "A": "30 anos, 20 anos e 10 anos.",
            "B": "25 anos, 15 anos e 5 anos.",
            "C": "20 anos, 10 anos e 5 anos.",
            "D": "15 anos, 10 anos e 2 anos.",
            "E": "50 anos, 25 anos e 10 anos."
        },
        "correct": "B",
        "explanation": "De acordo com o art. 24, § 1º da Lei nº 12.527/2011 (LAI), os prazos máximos de classificação são: Ultrassecreta (25 anos), Secreta (15 anos) e Reservada (5 anos)."
    },
    {
        "id": "q_gen_9",
        "category": "general",
        "subject": "Direito Administrativo - Licitações",
        "source": "FCC - DPE-SP (Adaptada)",
        "question": "A Lei Federal nº 14.133/2021 (Nova Lei de Licitações e Contratos) introduziu uma nova modalidade de licitação destinada a contratações que envolvam inovação tecnológica ou técnica, onde a administração pública debate soluções com licitantes previamente selecionados. Trata-se da modalidade denominada:",
        "options": {
            "A": "Pregão Eletrônico",
            "B": "Diálogo Competitivo",
            "C": "Concurso de Ideias",
            "D": "Tomada de Preços",
            "E": "Credenciamento Tecnológico"
        },
        "correct": "B",
        "explanation": "O 'Diálogo Competitivo' é a nova modalidade trazida pela Lei nº 14.133/2021, que consiste em conversas da administração com licitantes selecionados em busca de soluções para necessidades complexas, seguido da apresentação das propostas finais."
    },
    {
        "id": "q_gen_10",
        "category": "general",
        "subject": "Direito Constitucional",
        "source": "FCC - SEFAZ-PE (Adaptada)",
        "question": "O princípio da anterioridade tributária protege o contribuinte contra surpresas fiscais. De acordo com a Constituição Federal de 1988, a instituição ou majoração de qual dos seguintes tributos constitui exceção ao princípio da anterioridade nonagesimal (noventena), podendo ser cobrado imediatamente após a publicação da lei (respeitada apenas a anterioridade do exercício)?",
        "options": {
            "A": "Contribuições da Seguridade Social",
            "B": "Imposto sobre a Propriedade Territorial Urbana (IPTU) - apenas em relação à base de cálculo.",
            "C": "Imposto sobre a Renda e Proventos de Qualquer Natureza (IR).",
            "D": "Imposto sobre Circulação de Mercadorias e Serviços (ICMS).",
            "E": "Taxas de Serviços de Segurança Pública."
        },
        "correct": "C",
        "explanation": "O Imposto sobre a Renda (IR) é exceção expressa à anterioridade nonagesimal (noventena), nos termos do art. 150, § 1º, da CF/88. Ele obedece apenas à anterioridade de exercício (anual), podendo ser cobrado no dia 1º de janeiro do exercício seguinte ao da publicação da lei, sem necessidade de esperar 90 dias. O IPTU (base de cálculo) e o IPVA (base de cálculo) também são exceções à noventena."
    },
    {
        "id": "q_gen_11",
        "category": "general",
        "subject": "Direito Comercial",
        "source": "FCC - TJ-MS (Adaptada)",
        "question": "No âmbito do Direito Societário e da Sociedade Limitada regida pelo Código Civil brasileiro, qual órgão ou ato é responsável por aprovar a exclusão extrajudicial de um sócio minoritário que esteja colocando em risco a continuidade da empresa por atos de inegável gravidade?",
        "options": {
            "A": "Decisão judicial unânime do Tribunal de Justiça.",
            "B": "Deliberação da maioria dos sócios, representando mais da metade do capital social, em assembleia ou reunião convocada para esse fim.",
            "C": "Decisão discricionária exclusiva do sócio administrador.",
            "D": "Recomendação do Ministério Público Estadual.",
            "E": "Votação unânime de todos os demais sócios, independentemente da quota de capital."
        },
        "correct": "B",
        "explanation": "Conforme o art. 1.085 do Código Civil, nas sociedades limitadas de dois ou mais sócios, a exclusão por justa causa de um sócio minoritário pode ser feita extrajudicialmente por deliberação da maioria dos sócios, representando mais da metade do capital social (desde que haja previsão no contrato social)."
    },
    {
        "id": "q_gen_12",
        "category": "general",
        "subject": "Direito Civil",
        "source": "FCC - TRT (Adaptada)",
        "question": "Prescrição e decadência são institutos que tratam da perda de direitos pelo decurso do tempo. De acordo com o Código Civil brasileiro, a principal diferença técnica entre eles reside em:",
        "options": {
            "A": "A prescrição extingue o direito subjetivo em si, ao passo que a decadência extingue apenas a pretensão da ação judicial correspondente.",
            "B": "A prescrição pode ser suspensa ou interrompida pelos motivos previstos em lei, enquanto os prazos decadenciais, em regra, não se suspendem nem se interrompem.",
            "C": "A decadência somente pode ser alegada pelo devedor, ao passo que a prescrição deve ser decretada de ofício pelo juiz em qualquer instância.",
            "D": "Os prazos de prescrição são fixados pelas partes em contrato, ao passo que os de decadência são determinados exclusivamente por lei federal.",
            "E": "A prescrição aplica-se somente a direitos não patrimoniais, ao passo que a decadência aplica-se a obrigações comerciais."
        },
        "correct": "B",
        "explanation": "O Código Civil (art. 207) estabelece que, salvo disposição em contrário, os prazos de decadência não correm contra incapazes nem sofrem suspensão ou interrupção. Por outro lado, a prescrição pode ser suspensa ou interrompida (arts. 197 a 204). Além disso, a prescrição extingue a pretensão, enquanto a decadência extingue o próprio direito."
    },
    {
        "id": "q_gen_13",
        "category": "general",
        "subject": "Contabilidade Avançada",
        "source": "FCC - Metrô-SP (Adaptada)",
        "question": "Na contabilidade de empresas coligadas e controladas, o Método de Equivalência Patrimonial (MEP) deve ser aplicado para avaliar investimentos relevantes. Quando a investida apura um lucro líquido no período e distribui dividendos para a investidora, o lançamento na investidora referente ao recebimento desses dividendos envolve:",
        "options": {
            "A": "Débito em Caixa/Bancos e Crédito em Receita de Dividendos (DRE).",
            "B": "Débito em Caixa/Bancos e Crédito na conta de Investimentos em Coligadas (Ativo).",
            "C": "Débito em Receita de Equivalência Patrimonial e Crédito em Caixa/Bancos.",
            "D": "Débito em Investimentos em Coligadas (Ativo) e Crédito em Lucros Acumulados.",
            "E": "Débito em Caixa/Bancos e Crédito em Receita de Equivalência Patrimonial."
        },
        "correct": "B",
        "explanation": "Pelo Método de Equivalência Patrimonial (MEP), o recebimento de dividendos de coligadas/controladas não é reconhecido como receita na DRE. O dividendo reduz o patrimônio líquido da coligada e, consequentemente, reduz o valor do investimento da investidora. Assim, o lançamento correto é Débito em Caixa/Bancos e Crédito na conta do Investimento (reduzindo o Ativo)."
    }
]

if __name__ == "__main__":
    if os.path.exists(QUESTIONS_FILE):
        try:
            with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
                questions = json.load(f)
            
            existing_ids = {q['id'] for q in questions}
            added = 0
            
            for q in new_fcc_questions:
                if q['id'] not in existing_ids:
                    questions.append(q)
                    added += 1
            
            with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
                json.dump(questions, f, indent=4, ensure_ascii=False)
                
            print(f"Sucesso! Adicionadas {added} novas questões FCC ao banco de dados.")
        except Exception as e:
            print(f"Erro: {e}")
    else:
        print("Arquivo questions.json não encontrado.")
