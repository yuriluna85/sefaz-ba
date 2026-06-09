import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_FILE = os.path.join(BASE_DIR, 'questions.json')
DISCURSIVAS_FILE = os.path.join(BASE_DIR, 'discursivas.json')

real_questions = [
    {
        "id": "q_gen_real_1",
        "category": "general",
        "subject": "Direito Tributário",
        "source": "FGV - SEFAZ-AM (2022)",
        "question": "Determinado Estado da Federação passou a cobrar IPVA dos proprietários de embarcações e aeronaves com base em lei estadual específica, sob o argumento de que são veículos automotores. À luz da jurisprudência consolidada do Supremo Tribunal Federal (STF), a cobrança do IPVA sobre tais bens é:",
        "options": {
            "A": "Constitucional, desde que a alíquota seja uniforme e idêntica àquela aplicada a veículos terrestres.",
            "B": "Inconstitucional, pois o conceito constitucional de veículos automotores para fins de IPVA restringe-se aos veículos terrestres.",
            "C": "Constitucional, porque o IPVA é de competência plena dos Estados e do Distrito Federal, abrangendo qualquer meio de transporte.",
            "D": "Inconstitucional, salvo se houver autorização prévia por meio de Lei Complementar Federal específica para cada Estado.",
            "E": "Constitucional, contanto que o valor arrecadado seja revertido integralmente para a melhoria da infraestrutura portuária e aeroportuária do Estado."
        },
        "correct": "B",
        "explanation": "O STF possui jurisprudência pacífica no sentido de que o IPVA (Art. 155, III, CF/88) incide apenas sobre veículos automotores terrestres, não alcançando embarcações e aeronaves (RE 379.572 e RE 255.111)."
    },
    {
        "id": "q_gen_real_2",
        "category": "general",
        "subject": "Direito Tributário",
        "source": "FGV - SEFAZ-AM (2022)",
        "question": "Determinado Estado da Federação instituiu, por meio de decisão administrativa fiscal, a cobrança de IPVA sobre bicicletas elétricas por analogia às motocicletas. À luz do Código Tributário Nacional (CTN) e dos princípios constitucionais tributários, essa cobrança é:",
        "options": {
            "A": "Válida, pois a analogia é método de integração expressamente permitido pelo CTN para cobrança de novos tributos.",
            "B": "Inválida, pois o emprego da analogia não poderá resultar na exigência de tributo não previsto em lei.",
            "C": "Válida, desde que a alíquota cobrada seja inferior à menor alíquota vigente no Estado para motocicletas de baixa cilindrada.",
            "D": "Inválida, salvo se houver convênio firmado no âmbito do CONFAZ autorizando a equiparação.",
            "E": "Válida, sob o princípio da igualdade tributária, visto que ambos os veículos possuem propulsão mecânica."
        },
        "correct": "B",
        "explanation": "De acordo com o art. 108, § 1º, do CTN, o emprego da analogia não poderá resultar na exigência de tributo não previsto em lei, preservando o princípio constitucional da legalidade tributária (art. 150, I, CF/88)."
    },
    {
        "id": "q_ti_real_1",
        "category": "ti",
        "subject": "Banco de Dados",
        "source": "FGV - SEFAZ-MG (2023)",
        "question": "No âmbito dos bancos de dados Oracle, a SGA (System Global Area) e a PGA (Program Global Area) são estruturas de memória fundamentais. A diferença primordial entre SGA e PGA reside no fato de que:",
        "options": {
            "A": "A SGA é uma área de memória compartilhada por todos os processos do servidor, enquanto a PGA é uma área privada dedicada a uma única sessão ou processo de servidor individual.",
            "B": "A SGA armazena apenas dados temporários de consultas, enquanto a PGA guarda os logs de redo e undo de transações ativas.",
            "C": "A SGA é alocada dinamicamente na máquina do cliente, ao passo que a PGA reside permanentemente no servidor de disco do banco de dados.",
            "D": "A PGA gerencia o cache de blocos de dados (Buffer Cache), enquanto a SGA gerencia apenas a ordenação SQL e variáveis locais.",
            "E": "Ambas são compartilhadas, mas a PGA serve apenas para conexões não autenticadas e a SGA para transações em produção."
        },
        "correct": "A",
        "explanation": "A SGA (System Global Area) é compartilhada e contém dados e informações de controle do banco de dados (como buffer cache, shared pool, redo log buffer). A PGA (Program Global Area) é uma região de memória privada de cada processo de servidor, contendo dados e informações de controle de uma sessão individual (como dados de ordenação e sessão)."
    },
    {
        "id": "q_ti_real_2",
        "category": "ti",
        "subject": "Banco de Dados - BI",
        "source": "FGV - SEFAZ-MG (2023)",
        "question": "Na modelagem dimensional para Data Warehouses proposta por Ralph Kimball, os esquemas de modelagem são fundamentais para otimização de consultas analíticas. Considere o esquema Estrela (Star Schema) e o esquema Floco de Neve (Snowflake Schema). A principal diferença entre eles é que o esquema Floco de Neve:",
        "options": {
            "A": "Não possui tabelas fatos, sendo composto unicamente por tabelas dimensão diretamente integradas.",
            "B": "Normaliza as tabelas dimensão, dividindo-as em subdimensões secundárias, enquanto o esquema estrela mantém as dimensões totalmente desnormalizadas.",
            "C": "Desnormaliza a tabela fato para eliminar completamente o uso de junções (joins) em tempo de execução.",
            "D": "Utiliza apenas chaves naturais ao invés de chaves substitutas (surrogate keys) na tabela fato principal.",
            "E": "Duplica a tabela fato para garantir o isolamento físico de dados históricos e atuais."
        },
        "correct": "B",
        "explanation": "No Star Schema (esquema estrela), as dimensões são desnormalizadas in tabelas únicas conectadas à tabela fato. No Snowflake Schema (esquema floco de neve), as tabelas de dimensão são normalizadas, gerando subdimensões (tabelas secundárias), o que economiza espaço de armazenamento mas exige mais joins em consultas."
    },
    {
        "id": "q_ti_real_3",
        "category": "ti",
        "subject": "Segurança da Informação",
        "source": "FGV - SEFAZ-MG (2023)",
        "question": "Sob a ótica da Lei Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018), em relação à transferência internacional de dados pessoais pela administração pública para organismos internacionais ou entidades governamentais estrangeiras, assinale a afirmativa correta:",
        "options": {
            "A": "É expressamente vedada por razões de soberania de dados nacionais, independentemente de convênios fiscais bilaterais.",
            "B": "É permitida desde que o país ou organismo destinatário ofereça grau de proteção de dados pessoais adequado ao previsto na LGPD.",
            "C": "Exige autorização prévia de todos os contribuintes do Estado por meio de plebiscito digital.",
            "D": "Fica sujeita à anonimização reversível compulsória executada por chave criptográfica exclusiva sob posse da Receita Federal.",
            "E": "É permitida sem qualquer restrição jurídica por envolver transações fiscais internacionais e de controle aduaneiro."
        },
        "correct": "B",
        "explanation": "De acordo com o Art. 33, I, da LGPD, a transferência internacional de dados pessoais é permitida para países ou organismos internacionais que proporcionem grau de proteção de dados pessoais adequado ao previsto na lei brasileira."
    },
    {
        "id": "q_gen_real_3",
        "category": "general",
        "subject": "Legislação Tributária Estadual",
        "source": "FGV - SEFAZ-BA (2022)",
        "question": "Com base no Processo Administrativo Fiscal da Bahia (PAF — Decreto Estadual nº 7.629/1999), a peça que inicia formalmente a fase de contencioso administrativo para julgamento de exigência de crédito tributário formulada em Auto de Infração é denominada:",
        "options": {
            "A": "Petição de Embargos Fiscais.",
            "B": "Impugnação ou Reclamação.",
            "C": "Recurso Ordinário de Ofício.",
            "D": "Representação Fiscal para Fins Penais.",
            "E": "Notificação de Lançamento Avulso."
        },
        "correct": "B",
        "explanation": "A defesa apresentada pelo sujeito passivo no PAF da Bahia contra o lançamento efetuado por Auto de Infração ou Notificação de Lançamento inicia a fase contenciosa e é denominada impugnação (ou reclamação)."
    }
]

real_discursivas = [
    {
        "id": "d_ti_real_1",
        "category": "ti",
        "subject": "Banco de Dados e Governança (DAMA-DMBOK)",
        "banca": "FGV",
        "title": "Qualidade de Dados e Metadados (SEFAZ-MG 2023)",
        "context": "A Secretaria da Fazenda constatou diversas inconsistências no cruzamento de dados cadastrais de notas fiscais eletrônicas de saída com as bases federais da Receita Federal. O Diretor de TI recomendou a implementação de um programa de Governança de Dados alinhado ao framework DAMA-DMBOK v2, focando nas áreas de Qualidade de Dados e Gerenciamento de Metadados.",
        "question": "Considerando o DAMA-DMBOK v2, responda:\n\n1) Defina o que são 'Metadados' e diferencie Metadados Técnicos de Metadados de Negócio, citando um exemplo aplicável ao ambiente fazendário para cada um.\n2) Explique três dimensões de Qualidade de Dados (Data Quality) que devem ser monitoradas no cadastro de contribuintes para evitar inconsistências fiscais.",
        "criteria": {
            "item1": "Metadados: Definir como dados sobre dados. Diferenciar Metadados de Negócio (ex: significado de 'Alíquota Efetiva' ou 'Contribuinte Ativo') de Metadados Técnicos (ex: tipo do campo, tamanho da coluna, nome físico da tabela `TB_NFE`). (Valor: 50%)",
            "item2": "Dimensões de Qualidade: Explicar três dimensões, tais como: Acurácia/Exatidão (se o valor corresponde à realidade), Completude (se todos os campos obrigatórios estão preenchidos), Consistência (se o valor bate em diferentes bases) ou Tempestividade (se o dado está atualizado no momento da consulta). (Valor: 50%)"
        },
        "sample_answer": "1) Metadados são dados que descrevem outros dados, facilitando a descoberta, entendimento e governança dos ativos de informação.\n- Metadados de Negócio: Focam no significado e regras de negócio. Exemplo: A definição conceitual do que é considerado 'Simples Nacional' ou a regra de quem tem direito à isenção de ICMS.\n- Metadados Técnicos: Descrevem os detalhes físicos e estruturais dos dados. Exemplo: O nome físico da tabela de notas fiscais (`cadastro_empresas`), a chave primária (`cnpj`), o tipo de dado da coluna `aliquota` (DECIMAL(5,2)) e as permissões de acesso ao banco.\n\n2) As dimensões de Qualidade de Dados (DAMA-DMBOK) a serem monitoradas são:\n- Completude: Garante que todos os dados necessários estejam presentes (ex: todas as notas fiscais eletrônicas contêm o CNPJ do destinatário preenchido).\n- Consistência: Garante que os dados em diferentes sistemas não se contradigam (ex: o CNPJ do contribuinte ativo no banco do estado deve ser idêntico ao cadastrado na base da Receita Federal).\n- Acurácia (ou Exatidão): Garante que a informação registrada reflita fielmente o estado real (ex: o valor total da nota fiscal deve corresponder à soma exata das mercadorias vendidas)."
    }
]

def append_to_json(file_path, new_items):
    if not os.path.exists(file_path):
        print(f"Erro: {file_path} não encontrado.")
        return 0
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            items = json.load(f)
    except Exception as e:
        print(f"Erro ao ler {file_path}: {e}")
        return 0

    existing_ids = {item['id'] for item in items}
    added_count = 0
    
    for item in new_items:
        if item['id'] not in existing_ids:
            items.append(item)
            added_count += 1
            
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(items, f, indent=4, ensure_ascii=False)
        return added_count
    except Exception as e:
        print(f"Erro ao salvar {file_path}: {e}")
        return 0

if __name__ == "__main__":
    added_q = append_to_json(QUESTIONS_FILE, real_questions)
    print(f"Sucesso! Adicionadas {added_q} novas questões reais a questions.json.")
    
    added_d = append_to_json(DISCURSIVAS_FILE, real_discursivas)
    print(f"Sucesso! Adicionadas {added_d} novas discursivas reais a discursivas.json.")
