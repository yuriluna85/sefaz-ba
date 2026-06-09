import json
import os

QUESTIONS_FILE = r"G:\Meu Drive\ESPECIALIZAÇÕES\Concurso SEFAZ Dashboard\questions.json"

new_questions = [
    {
        "id": "q_gen_4",
        "category": "general",
        "subject": "Direito Tributário - Reforma Tributária",
        "source": "FGV - SEFAZ-RN (Simulada)",
        "question": "A Emenda Constitucional nº 132/2023 alterou profundamente o Sistema Tributário Nacional ao introduzir o modelo de Imposto sobre o Valor Agregado (IVA) Dual. Com base nessa reforma, assinale a afirmativa correta sobre a CBS (Contribuição sobre Bens e Serviços) e o IBS (Imposto sobre Bens e Serviços):",
        "options": {
            "A": "A CBS é de competência dos Estados e Municípios, enquanto o IBS é de competência exclusiva da União.",
            "B": "Ambos possuem caráter puramente cumulativo e incidem apenas sobre bens materiais tangíveis.",
            "C": "O IBS será gerido de forma integrada por um Comitê Gestor que conta com representantes dos Estados, do Distrito Federal e dos Municípios.",
            "D": "A CBS e o IBS incidirão obrigatoriamente nas operações de exportação de mercadorias para o exterior, eliminando a imunidade tributária antiga.",
            "E": "A alíquota do IBS será única para todos os bens e serviços em todo o território nacional, sendo expressamente vedados regimes diferenciados ou descontos."
        },
        "correct": "C",
        "explanation": "De acordo com a EC 132/2023, o IBS será administrado por um Comitê Gestor com representação paritária de Estados, DF e Municípios, enquanto a CBS será administrada pela União. Ambos seguem o regime de não cumulatividade ampla (IVA Dual), desoneram as exportações e preveem regimes favorecidos para setores como saúde, transporte público e educação."
    },
    {
        "id": "q_ti_4",
        "category": "ti",
        "subject": "Tecnologia da Informação - Fluência em Dados",
        "source": "Cebraspe - SEFAZ-RN (Simulada)",
        "question": "No âmbito das disciplinas de Ciência de Dados e Big Data, o conceito ou dimensão de 'Veracidade' refere-se prioritariamente a qual dos seguintes aspectos?",
        "options": {
            "A": "À velocidade operacional com que os dados fiscais estruturados são processados na nuvem.",
            "B": "À confiabilidade, qualidade e acurácia dos dados, garantindo que análises e decisões não se baseiem em informações inconsistentes ou incorretas.",
            "C": "Ao volume maciço de terabytes gerados em redes sociais e transações de comércio eletrônico.",
            "D": "À variedade de formatos e estruturas de arquivos, incluindo dados estruturados e semiestruturados.",
            "E": "Ao valor monetário obtido após a aplicação de algoritmos de inteligência artificial sobre os dados."
        },
        "correct": "B",
        "explanation": "A Veracidade (um dos 5 V's tradicionais do Big Data) está ligada diretamente à integridade, qualidade e confiabilidade dos dados coletados, assegurando que as conclusões analíticas de fato correspondam à realidade."
    },
    {
        "id": "q_gen_5",
        "category": "general",
        "subject": "Direito Tributário - Geral",
        "source": "Cebraspe - SEFAZ-RN (Simulada)",
        "question": "Em relação à solidariedade tributária devedora regulamentada pelas normas gerais do Código Tributário Nacional (CTN), assinale a afirmativa correta:",
        "options": {
            "A": "A solidariedade tributária comporta benefício de ordem, devendo o fisco acionar primeiro o sujeito passivo principal indicado no contrato social.",
            "B": "A solidariedade devedora decorre unicamente da convenção de vontades entre as partes (autonomia contratual), não dependendo de expressa previsão em lei.",
            "C": "A interrupção da prescrição em desfavor de um dos coobrigados solidários não prejudica nem aproveita aos demais devedores.",
            "D": "São solidariamente obrigadas as pessoas que tenham interesse comum na situação que constitua o fato gerador da obrigação principal.",
            "E": "A isenção pessoal concedida a um dos devedores solidários extingue integralmente o débito para todos os demais coobrigados."
        },
        "correct": "D",
        "explanation": "Conforme o art. 124, I, do CTN, as pessoas que tenham interesse comum na situação que constitua o fato gerador da obrigação principal são solidariamente obrigadas. O parágrafo único deixa claro que a solidariedade não comporta benefício de ordem."
    },
    {
        "id": "q_gen_6",
        "category": "general",
        "subject": "Auditoria Fiscal - Procedimentos",
        "source": "FGV - Área Fiscal (Simulada)",
        "question": "No transcorrer de uma auditoria em uma distribuidora, o auditor fiscal depara-se com suspeitas de omissão de saídas tributadas (subavaliação de receita). Para detectar com precisão essa subavaliação, qual o procedimento de auditoria mais adequado?",
        "options": {
            "A": "Partir do livro razão contábil e confrontar os lançamentos de vendas com as notas fiscais correspondentes de modo a atestar sua ocorrência real.",
            "B": "Selecionar uma amostra física de notas fiscais de saídas emitidas e rastreá-las até os respectivos lançamentos nos livros diário e razão contábil.",
            "C": "Efetuar a contagem física do estoque remanescente e confrontá-la diretamente com o balanço patrimonial publicado da controladora.",
            "D": "Confirmar saldos de contas a pagar por meio de cartas de circularização enviadas aos clientes inadimplentes.",
            "E": "Verificar a regularidade formal da conciliação bancária de encerramento do exercício."
        },
        "correct": "B",
        "explanation": "Para auditar a subavaliação (omissão de registro), o auditor deve testar do documento de origem (nota fiscal/fato físico) para o registro contábil. Se ele partir do registro para o documento (opção A), estará testando a superavaliação (venda fictícia)."
    },
    {
        "id": "q_ti_5",
        "category": "ti",
        "subject": "Tecnologia da Informação - Regulamentação",
        "source": "Cebraspe - SEFAZ-RN (Simulada)",
        "question": "À luz da Lei Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018), o tratamento de dados pessoais realizado por órgãos e entidades da administração pública para a execução de políticas públicas previstas em leis ou regulamentos:",
        "options": {
            "A": "Depende de consentimento expresso e por escrito do titular em todos os atos de tratamento.",
            "B": "É dispensado de consentimento, desde que o tratamento seja realizado para o atendimento de sua finalidade pública, na persecução do interesse público.",
            "C": "É vedado por envolver segredo de estado e segredo de justiça na área fiscal tributária.",
            "D": "Exige autorização judicial ou parecer prévio obrigatório da Autoridade Nacional de Proteção de Dados (ANPD).",
            "E": "Somente é lícito caso os dados sejam previamente anonimizados por processo irreversível."
        },
        "correct": "B",
        "explanation": "Conforme o art. 7º, III, da LGPD, o tratamento de dados pessoais pode ser efetuado pela administração pública para a execução de políticas públicas previstas em leis e regulamentos, sendo dispensado o consentimento, embora devendo observar a finalidade e a transparência pública."
    },
    {
        "id": "q_gen_7",
        "category": "general",
        "subject": "Contabilidade de Custos - Métodos",
        "source": "FGV - Área Fiscal (Simulada)",
        "question": "Determinada indústria produz 1.000 unidades de um produto e vende 800 unidades no mesmo mês, restando 200 no estoque final. Sob a perspectiva da apuração de lucro líquido do período, a comparação entre o Custeio por Absorção e o Custeio Variável revela que:",
        "options": {
            "A": "O lucro líquido do período será menor no custeio por absorção.",
            "B": "O valor atribuído ao estoque final de produtos acabados será menor no custeio por absorção.",
            "C": "O lucro líquido do período será maior no custeio por absorção.",
            "D": "O Custo dos Produtos Vendidos (CPV) será matematicamente idêntico em ambos os métodos.",
            "E": "Os custos fixos de fabricação são lançados integralmente como despesa do período no custeio por absorção."
        },
        "correct": "C",
        "explanation": "No custeio por absorção, a parcela dos custos fixos correspondente às 200 unidades em estoque é ativada no balanço patrimonial. No custeio variável, todos os custos fixos são despesados na DRE. Isso faz com que o CPV seja menor no absorção, elevando o lucro líquido."
    },
    {
        "id": "q_ti_6",
        "category": "ti",
        "subject": "Tecnologia da Informação - Banco de Dados",
        "source": "Cebraspe - Área Fiscal (Simulada)",
        "question": "O Teorema CAP é uma diretriz amplamente consolidada no projeto de arquiteturas distribuídas e de bancos de dados NoSQL. Esse teorema postula que um sistema distribuído de dados não consegue assegurar simultaneamente quais propriedades?",
        "options": {
            "A": "Concorrência (Concurrency), Acesso (Access) e Performance (Performance).",
            "B": "Consistência (Consistency), Disponibilidade (Availability) e Tolerância a Partição (Partition Tolerance).",
            "C": "Criptografia (Cryptography), Autenticação (Authentication) e Privacidade (Privacy).",
            "D": "Custódia (Custody), Auditoria (Audit) e Processabilidade (Processability).",
            "E": "Conexão (Connection), Adaptabilidade (Adaptability) e Portabilidade (Portability)."
        },
        "correct": "B",
        "explanation": "O Teorema CAP (ou Teorema de Brewer) estabelece que um banco de dados distribuído pode garantir no máximo duas das três propriedades ao mesmo tempo: Consistência (C), Disponibilidade (A) e Tolerância a Partição de Rede (P)."
    },
    {
        "id": "q_gen_8",
        "category": "general",
        "subject": "Economia do Setor Público",
        "source": "FGV - Área Fiscal (Simulada)",
        "question": "Na teoria das falhas de mercado de Economia do Setor Público, um bem público puro caracteriza-se essencialmente pela conjunção de quais propriedades?",
        "options": {
            "A": "Rivalidade no consumo e Excludibilidade pelo sistema de preços.",
            "B": "Alta rentabilidade comercial e livre concorrência perfeita.",
            "C": "Não rivalidade no consumo e Não excludibilidade de consumidores.",
            "D": "Monopólio natural de produção e tabelamento estatal de tarifas.",
            "E": "Externalidades negativas e assimetria de informações."
        },
        "correct": "C",
        "explanation": "Bens públicos puros são caracterizados por duas propriedades econômicas fundamentais: (1) Não rivalidade (o consumo por um indivíduo não reduz o consumo de outros) e (2) Não excludibilidade (é impossível impedir as pessoas de consumirem o bem após fornecido)."
    }
]

if __name__ == "__main__":
    if os.path.exists(QUESTIONS_FILE):
        try:
            with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
                questions = json.load(f)
            
            # Avoid duplicate ids
            existing_ids = {q['id'] for q in questions}
            added_count = 0
            
            for q in new_questions:
                if q['id'] not in existing_ids:
                    questions.append(q)
                    added_count += 1
                    
            with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
                json.dump(questions, f, indent=4, ensure_ascii=False)
                
            print(f"Sucesso! Foram adicionadas {added_count} novas questões no arquivo questions.json.")
        except Exception as e:
            print(f"Erro ao atualizar o arquivo: {e}")
    else:
        print("Arquivo questions.json não encontrado.")
