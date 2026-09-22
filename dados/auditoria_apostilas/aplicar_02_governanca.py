"""Aplica a auditoria da Apostila de Gestão e Governança de TI (Fase 1) e acrescenta as seções do
programa SEFAZ-CE 2026 (B02) que faltavam. Idempotente. Relatório: dados/auditoria_apostilas/02_governanca.md
Uso (na pasta do app): python dados/auditoria_apostilas/aplicar_02_governanca.py
"""
import json
import os
import sys

APP = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARQ = os.path.join(APP, 'apostilas_conteudo.json')
dados = json.load(open(ARQ, encoding='utf-8'))
ap = next(a for a in dados if 'Gest' in a['filename'] and 'Govern' in a['filename'])
S = ap['sections']

if any(s['title'].startswith('11.') for s in S):
    print('Apostila de Governança já atualizada; nada a fazer.')
    sys.exit(0)


def bul(sec, inicio):
    return next(b for b in sec['bullets'] if b[0].strip().startswith(inicio))


def trocar(txt, velho, novo):
    assert velho in txt, 'trecho não encontrado: ' + velho[:70]
    return txt.replace(velho, novo)


# ---- Seção 1 ----
b = bul(S[0], 'Planejamento Estratégico de TIC')
b[0] = 'PETIC e PDTIC'
b[1] = ('O PETIC (Plano Estratégico de TIC) está no nível estratégico e define a direção da TIC alinhada ao planejamento '
        'institucional. O PDTIC (Plano Diretor de TIC) está no nível tático: é o instrumento de diagnóstico, planejamento e gestão '
        'dos recursos e processos de TIC para um período determinado, atendendo às necessidades finalísticas e de informação do '
        'órgão. No SISP (Poder Executivo federal), o Guia de Elaboração de PDTIC organiza o trabalho em preparação, diagnóstico e '
        'planejamento. Veja a seção 11.')
S[0]['tip'] = ['Regra Prática: Governança Direciona, Gestão Executa',
               'A Governança define o que deve ser alcançado (avalia, direciona e monitora). A Gestão define como alcançar e executa no '
               'dia a dia. Governança não se confunde com execução gerencial.']
S[0]['content'] = S[0]['content'].replace('O postulado fundamental consolidado pelo TCU e frameworks internacionais estabelece a '
                                          'separação clara e estrita entre Governança e Gestão de TI.',
                                          'Os referenciais de governança do setor público e os frameworks internacionais, como o COBIT, '
                                          'distinguem com clareza Governança de Gestão de TI.')

# ---- Seção 2: COBIT ----
b = bul(S[1], 'Os 7 Componentes')
b[1] = trocar(b[1], '3. Princípios, Políticas e Frameworks', '3. Princípios, Políticas e Procedimentos')
b = bul(S[1], 'Fatores de Design')
b[0] = 'Os 11 Fatores de Design do COBIT 2019'
b[1] = ('Elementos de contexto que orientam a adaptação do sistema de governança: 1. Estratégia da Empresa; 2. Metas Corporativas; 3. '
        'Perfil de Risco; 4. Questões Relacionadas a I&T; 5. Cenário de Ameaças; 6. Requisitos de Conformidade; 7. Papel da TI; 8. '
        'Modelo de Terceirização da TI; 9. Métodos de Implementação de TI (Ágil, DevOps, Tradicional); 10. Estratégia de Adoção de '
        'Tecnologia; 11. Tamanho da Empresa.')
b = bul(S[1], 'Níveis de Capacidade')
b[1] = ('Mede a capacidade dos processos em uma escala de 0 a 5, baseada no CMMI: do nível 0 (sem capacidade básica, abordagem '
        'incompleta) ao nível 5 (processo otimizado, com melhoria contínua), passando por níveis intermediários (1 a 4) de disciplina e '
        'previsibilidade crescentes. Confira no texto oficial do COBIT os rótulos exatos de cada nível.')

# ---- Seção 4: ITIL ----
S[3]['content'] = trocar(S[3]['content'], 'mantida pela AXELOS',
                         'publicada pela AXELOS e hoje pertencente ao grupo PeopleCert')
b = bul(S[4], 'Habilitação de Mudança')
b[1] = ('Prática que assegura a avaliação e a autorização segura de alterações. Tipos: 1. Mudança padrão (baixo risco, '
        'pré-autorizada e rotineira, como criar uma conta de usuário); 2. Mudança normal (exige avaliação de risco e impacto e '
        'autorização da autoridade de mudança, que pode ser uma pessoa ou um grupo, como um comitê de mudanças/CAB); 3. Mudança '
        'emergencial (precisa ser implementada rapidamente, por exemplo para restaurar serviço crítico, com processo de autorização '
        'acelerado).')

# ---- Seção 6: PMBOK / EVA ----
b = bul(S[5], 'A Evolução do PMBOK')
b[1] = b[1] + ' O edital do CE 2026 cita a 7ª edição; confira a edição citada no edital da SEFAZ-BA quando sair.'
S[5]['bullets'][3] = [
    'Gerenciamento do Valor Agregado (EVA / Earned Value Management)',
    'Integra escopo, cronograma e custo. Valor Planejado (VP ou PV): orçamento do trabalho que deveria estar feito. Valor Agregado (VA '
    'ou EV): orçamento do trabalho efetivamente realizado. Custo Real (CR ou AC): o que foi gasto com o trabalho realizado. Variação '
    'de Custos = VA menos CR. Variação de Prazos = VA menos VP. Índice de Desempenho de Custos (IDC) = VA dividido por CR. Índice de '
    'Desempenho de Prazos (IDP) = VA dividido por VP. IDC maior que 1: custo abaixo do previsto. IDP maior que 1: adiantado. '
    'Estimativa no Término (EAC) = Orçamento no Término dividido pelo IDC (quando a variação atual é típica).']
S[5]['tip'] = ['Alerta de Prova - Leitura do EVA',
               'Para IDC e IDP a fronteira é 1. Maior que 1 é favorável (custou menos, está adiantado). Menor que 1 é desfavorável '
               '(estourando custo, atrasado). Variações positivas são favoráveis; negativas, desfavoráveis.']

# ---- Seção 7: Scrum (ajuste de dica) ----
b = bul(S[6], 'Os 5 Eventos')
b[1] = trocar(b[1], 'duração fixa de 1 a 4 semanas', 'duração fixa de um mês ou menos')

# ---- Seção 8: Kanban ----
b = bul(S[7], 'O Método Kanban')
b[1] = trocar(b[1], '5. Implementar ciclos de feedback.',
              '5. Implementar ciclos de feedback; 6. Melhorar colaborativamente e evoluir de forma experimental.')

# ---- Seção 9: CMMI e MPS.BR ----
b = bul(S[8], 'CMMI-DEV v2.0')
b[0] = 'CMMI V2.0 (Capability Maturity Model Integration)'
b[1] = ('Mantido pelo CMMI Institute, da ISACA. Na versão 2.0 há níveis de maturidade da organização (1 a 5) e níveis de capacidade '
        '(0 a 5) por área de prática. Níveis de maturidade: 1 Inicial (processos imprevisíveis e reativos); 2 Gerenciado (planejados e '
        'executados no nível de projeto); 3 Definido (padronizados na organização); 4 Quantitativamente Gerenciado (controlados por '
        'métricas estatísticas); 5 Em Otimização (melhoria contínua e inovação).')
b = bul(S[8], 'O Modelo MPS.BR')
b[1] = ('Modelo brasileiro coordenado pela SOFTEX, baseado nas normas ISO/IEC 12207 e ISO/IEC 15504 (esta substituída pela série '
        'ISO/IEC 33000). Tem 7 níveis de maturidade, do mais simples ao mais maduro: G (Parcialmente Gerenciado), F (Gerenciado), E '
        '(Parcialmente Definido), D (Largamente Definido), C (Definido), B (Gerenciado Quantitativamente) e A (Em Otimização). As '
        'metas do programa são a meta técnica (criar e aprimorar os modelos) e a meta de mercado (disseminá-los). O MPS.BR atende a '
        'diferentes perfis de empresas, com atenção especial às pequenas e médias.')
S[8]['tip'] = ['Cuidado com Equivalências entre Modelos',
               'CMMI e MPS.BR têm escalas diferentes (números de 1 a 5 e letras de G a A). As correspondências entre níveis são '
               'aproximadas; use apenas a equivalência que a questão ou a fonte oficial informar. G é o nível de entrada do MPS.BR.']

# ---- Seção 10: pegadinhas ----
S[9]['title'] = '10. Armadilhas Conceituais Recorrentes em Governança e Gestão de TI'
S[9]['content'] = ('Pontos conceituais que costumam gerar erro em questões de Governança e Gestão de TI. Servem de revisão rápida; a '
                   'base de cada ponto está nas seções anteriores.')
for i, bl in enumerate(S[9]['bullets']):
    if bl[0].startswith('Pegadinha 5'):
        S[9]['bullets'][i] = ['Pegadinha 5: IDC e IDP Maiores que 1 são Favoráveis',
                              'No EVA, IDC maior que 1 significa custo abaixo do previsto e IDP maior que 1 significa cronograma '
                              'adiantado.']
    if bl[0].startswith('Pegadinha 8'):
        S[9]['bullets'][i] = ['Pegadinha 8: Daily Scrum Dura no Máximo 15 Minutos',
                              'A Daily tem timebox de 15 minutos e é um evento para os Developers inspecionarem o progresso rumo à '
                              'Meta da Sprint.']
    if bl[0].startswith('Pegadinha 9'):
        S[9]['bullets'][i] = ['Pegadinha 9: G é o Nível Inicial do MPS.BR',
                              'A escala do MPS.BR vai de G (mais simples) até A (mais madura).']
S[9]['tip'] = ['Síntese Final de Governança de TI',
               'Governança é avaliar, dirigir e monitorar (EDM); incidente restaura rápido e problema investiga a causa; no Scrum '
               'atuam PO, SM e Developers; a EAP é de entregas; IDC e IDP maiores que 1 são favoráveis.']

# ---- Seções novas ----
S.append({
    'title': '11. PETIC, PDTIC, Portfólio e Gestão de Demandas de TIC',
    'content': ('O planejamento de TIC liga a estratégia da organização à execução: o plano estratégico define a direção, o plano '
                'diretor traduz essa direção em necessidades, metas, ações e recursos para um período, e a gestão de portfólio e de '
                'demandas prioriza o que será feito.'),
    'bullets': [
        ['PETIC (estratégico) e PDTIC (tático)',
         'PETIC: estratégia de TIC alinhada ao planejamento institucional, de médio e longo prazo. PDTIC: plano diretor com '
         'diagnóstico da situação atual, inventário de necessidades, metas e ações, gestão de riscos e plano orçamentário e de '
         'investimentos para o período. Um segundo nível, o plano operacional, detalha a execução.'],
        ['Guia de PDTIC do SISP',
         'No Poder Executivo federal, o Guia de Elaboração de PDTIC do SISP organiza o trabalho em três fases: preparação, '
         'diagnóstico e planejamento. Esse guia é referência federal; a Bahia tem regramento próprio (ver seção 12).'],
        ['Portfólio, programa e projeto (PMBOK)',
         'Portfólio: conjunto de projetos, programas e operações gerenciados em grupo para atingir objetivos estratégicos. Programa: '
         'projetos relacionados, gerenciados de forma coordenada para obter benefícios que não teriam isoladamente. Projeto: esforço '
         'temporário para criar produto, serviço ou resultado exclusivo.'],
        ['Gestão de demandas e priorização',
         'Demandas são registradas, analisadas e priorizadas por critérios como alinhamento estratégico, valor esperado, risco, '
         'custo e capacidade. Na ITIL 4 existem as práticas de gerenciamento de portfólio e de gerenciamento de relacionamento; o '
         'COBIT 2019 trata do tema em APO05 (Portfólio) e APO08 (Relacionamentos).'],
        ['Business Relationship Management (BRM)',
         'Prática de ligar a área de TI às áreas de negócio: entender necessidades, alinhar expectativas e apoiar a realização de '
         'benefícios e valor. Na ITIL 4, corresponde à prática de gerenciamento de relacionamento.'],
    ],
    'tip': ['PETIC Direciona, PDTIC Detalha',
            'PETIC responde "para onde vamos" (estratégico). PDTIC responde "o que faremos, com quais recursos e em que período" '
            '(tático). Instrumentos diferentes: não confundir.']})
S.append({
    'title': '12. Contratações de TIC e a Lei nº 14.133/2021',
    'content': ('A contratação de soluções de TIC segue a Lei nº 14.133/2021 (Lei de Licitações e Contratos Administrativos). O '
                'planejamento da contratação produz documentos como o Estudo Técnico Preliminar e o Termo de Referência, e a execução '
                'exige gestão e fiscalização do contrato. O edital SEFAZ-BA 2022 cobrava o Decreto estadual nº 15.404/2014 (contratação '
                'de TIC no Estado da Bahia); consulte o texto vigente do decreto.'),
    'bullets': [
        ['Estudo Técnico Preliminar (ETP), art. 18',
         'Documento constitutivo da primeira etapa do planejamento. Entre seus elementos: descrição da necessidade, previsão no plano '
         'de contratações anual, requisitos da contratação, estimativas de quantidades, levantamento de mercado, estimativa de valor, '
         'descrição da solução como um todo, justificativas para parcelar ou não, resultados pretendidos, providências prévias, '
         'contratações correlatas, impactos ambientais e posicionamento conclusivo sobre a adequação da contratação. Obrigatórios, no '
         'mínimo: descrição da necessidade, estimativa das quantidades, estimativa do valor, justificativa do parcelamento ou não e '
         'posicionamento conclusivo.'],
        ['Termo de Referência (TR), art. 6º, XXIII',
         'Documento necessário à contratação de bens e serviços, com os parâmetros e elementos descritivos: definição do objeto '
         '(natureza, quantitativos, prazo e possibilidade de prorrogação); fundamentação da contratação; descrição da solução; '
         'requisitos; modelo de execução do objeto; modelo de gestão do contrato; critérios de medição e de pagamento; forma e '
         'critérios de seleção do fornecedor; estimativas de valor; adequação orçamentária.'],
        ['Gestão e fiscalização do contrato',
         'A Administração designa representantes para acompanhar e fiscalizar a execução (art. 117). Em contratos de TIC, o '
         'acompanhamento usa indicadores e níveis de serviço definidos no TR e no contrato, ligados aos critérios de medição e de '
         'pagamento.'],
        ['SLA e níveis de serviço em contratos',
         'O Acordo de Nível de Serviço (SLA) fixa métricas objetivas (disponibilidade, tempo de resposta e de solução, qualidade) e '
         'as consequências do descumprimento, como ajuste no pagamento (glosa) ou sanção. Contratos de terceirizados que sustentam '
         'serviços internos são chamados de contratos de apoio (underpinning contracts) na ITIL.'],
        ['Prazo dos contratos de serviços contínuos',
         'Contratos de serviços e fornecimentos contínuos podem ter prazo de até 5 anos, prorrogáveis sucessivamente até 10 anos '
         '(arts. 106 e 107), observadas as condições legais. Confira o texto vigente ao estudar.'],
        ['Referência federal para TIC',
         'Para os órgãos do SISP, a IN SGD/ME nº 94/2022 dispõe sobre a contratação de soluções de TIC, com fases de planejamento, '
         'seleção do fornecedor e gestão do contrato. É norma federal; na Bahia, aplicar o regramento estadual.'],
    ],
    'tip': ['ETP Antes do TR',
            'O ETP investiga a necessidade e as alternativas (levantamento de mercado e viabilidade). O TR descreve o que será '
            'contratado e como será executado e pago. Um não substitui o outro.']})
S.append({
    'title': '13. Gestão Financeira de TI: TCO, ROI, CAPEX, OPEX e FinOps',
    'content': ('A gestão financeira de TI mostra o custo e o valor da tecnologia para decidir, priorizar e prestar contas. No COBIT '
                '2019, o objetivo APO06 (Gerenciamento de Orçamento e Custos) trata do tema.'),
    'bullets': [
        ['TCO (Custo Total de Propriedade)',
         'Soma de todos os custos ao longo do ciclo de vida da solução: aquisição, implantação, operação, manutenção, treinamento, '
         'suporte e descarte. Compara alternativas melhor do que olhar só o preço de compra.'],
        ['ROI (Retorno sobre o Investimento)',
         'ROI = (ganho do investimento menos custo do investimento) dividido pelo custo do investimento, em geral em percentual. '
         'Complementam a análise o payback (tempo de retorno), o valor presente líquido (VPL) e a taxa interna de retorno (TIR).'],
        ['CAPEX e OPEX',
         'CAPEX (despesa de capital): investimento na aquisição de ativos duráveis, como servidores e licenças perpétuas. OPEX '
         '(despesa operacional): custos recorrentes de operação, como assinatura de nuvem, suporte e manutenção. No orçamento '
         'público, a Lei nº 4.320/1964 (art. 12) classifica as despesas em correntes e de capital.'],
        ['FinOps: conceito',
         'Prática operacional e cultural que maximiza o valor de negócio da nuvem, viabiliza decisões baseadas em dados e cria '
         'responsabilidade financeira pela colaboração entre engenharia, finanças e negócio (FinOps Foundation).'],
        ['FinOps: fases e princípios',
         'Fases clássicas do ciclo: Informar (visibilidade e alocação de custos), Otimizar (reduzir desperdício e melhorar o uso) e '
         'Operar (governança e melhoria contínua). Princípios: equipes colaboram; o valor de negócio orienta as decisões; todos são '
         'responsáveis pelo seu uso; dados de custo são acessíveis, oportunos e precisos; a prática é habilitada centralmente; aproveita-se o modelo de custo variável da nuvem.'],
        ['Práticas de custo na nuvem',
         'Tagueamento de recursos para alocar custos por área ou projeto, cotas e limites (budgets e alertas), dimensionamento '
         'adequado (rightsizing), compromissos de uso e desligamento de recursos ociosos.'],
    ],
    'tip': ['TCO Olha o Ciclo Todo, ROI Olha o Retorno',
            'TCO agrega todos os custos do ciclo de vida. ROI compara ganho e custo. CAPEX é investimento em ativo; OPEX é custo '
            'recorrente de operação (a nuvem tende a deslocar gasto de CAPEX para OPEX).']})
S.append({
    'title': '14. Gestão de Processos: BPM, BPMN, DMN e BPMS',
    'content': ('BPM (Business Process Management) é a disciplina de gerenciar processos de negócio de ponta a ponta para melhorar '
                'resultados. O ciclo envolve planejar, analisar, desenhar, implementar, monitorar e refinar processos.'),
    'bullets': [
        ['AS-IS e TO-BE',
         'AS-IS é o modelo do processo como ele funciona hoje, base para diagnóstico. TO-BE é o modelo do processo futuro, com as '
         'melhorias propostas. TO-RUN é termo usado por alguns autores para o modelo detalhado para execução ou automação; confirme '
         'a definição adotada pela fonte da questão.'],
        ['BPMN 2.0 (OMG; ISO/IEC 19510)',
         'Notação padrão para modelar processos. Grupos de elementos: objetos de fluxo (eventos de início, intermediários e de fim; '
         'atividades, como tarefas e subprocessos; gateways), objetos de conexão (fluxo de sequência, fluxo de mensagem e '
         'associação), raias e piscinas (swimlanes: pools e lanes) e artefatos (objetos de dados, anotações e grupos).'],
        ['Gateways do BPMN',
         'Exclusivo (XOR): apenas um caminho. Paralelo (AND): todos os caminhos, simultâneos. Inclusivo (OR): um ou mais caminhos '
         'conforme condições. Baseado em eventos: o caminho segue o primeiro evento que ocorrer.'],
        ['DMN (Decision Model and Notation, OMG)',
         'Padrão para modelar decisões de negócio, separado do fluxo do processo. Usa o diagrama de requisitos de decisão (DRD) e '
         'tabelas de decisão, com regras avaliadas por uma linguagem de expressões (FEEL). Complementa o BPMN: o processo chama a '
         'decisão.'],
        ['BPMS',
         'Suíte de software para modelar, executar (motor de processos), monitorar e otimizar processos automatizados, geralmente '
         'aderente ao BPMN.'],
    ],
    'tip': ['BPMN Modela o Fluxo, DMN Modela a Decisão',
            'Fluxo de atividades e eventos é BPMN. Regras de decisão em tabelas são DMN. AS-IS mostra o presente; TO-BE, o futuro '
            'desejado.']})
S.append({
    'title': '15. Melhoria de Processos: Lean, Six Sigma e Mapeamento do Fluxo de Valor',
    'content': ('Lean, Six Sigma e o mapeamento do fluxo de valor são abordagens de melhoria de processos: o Lean busca eliminar '
                'desperdícios e acelerar o fluxo de valor; o Six Sigma busca reduzir a variação e os defeitos com base em dados.'),
    'bullets': [
        ['Princípios Lean',
         'Especificar valor, mapear o fluxo de valor, criar fluxo contínuo, produção puxada e busca da perfeição (Womack e Jones).'],
        ['Os oito desperdícios (Lean)',
         'Defeitos, superprodução, espera, talento não utilizado, transporte, estoque, movimentação e excesso de processamento.'],
        ['Value Stream Mapping (VSM)',
         'Mapeia o fluxo de material e de informação, do pedido à entrega, diferenciando atividades que agregam valor das que não '
         'agregam, e compara tempo de processamento com tempo total de espera e passagem (lead time).'],
        ['Six Sigma e DMAIC',
         'Metodologia orientada a dados para reduzir variação e defeitos. Ciclo DMAIC: Definir, Medir, Analisar, Melhorar (Improve) e '
         'Controlar. Nível seis sigma corresponde a cerca de 3,4 defeitos por milhão de oportunidades (DPMO). Papéis: faixas amarela, '
         'verde, preta e mestre.'],
        ['Kaizen e Lean IT',
         'Kaizen é a melhoria contínua feita por todos, em pequenos passos. Lean IT aplica os princípios Lean à gestão de serviços e '
         'ao desenvolvimento de TI.'],
    ],
    'tip': ['Lean Corta Desperdício, Six Sigma Corta Variação',
            'Lean foca fluxo e desperdício; Six Sigma foca variabilidade e defeitos (DMAIC). Na prática, as duas são combinadas '
            '(Lean Six Sigma).']})
S.append({
    'title': '16. Referências e Conferência',
    'content': ('Conferência realizada em 21/09/2026. Os itens indicados como conferir dependem de texto pago ou de versão vigente.'),
    'bullets': [
        ['Referências',
         'COBIT 2019 Framework (ISACA); ITIL 4 Foundation; PMBOK Guide 6ª e 7ª edições (PMI); Scrum Guide 2020; Lei nº 14.133/2021 '
         '(arts. 6º, 18, 106, 107 e 117); Lei nº 4.320/1964; Decreto estadual nº 15.404/2014 (BA); IN SGD/ME nº 94/2022; Guia de '
         'PDTIC do SISP; OMG BPMN 2.0 e DMN; FinOps Foundation Framework; Edital SEFAZ-CE 2026 (FCC), Anexo VI.'],
        ['Corrigido nesta revisão',
         'Fórmulas do EVA com notação ambígua e símbolos de LaTeX; fatores de design do COBIT 2019 (eram 9, são 11); componentes do '
         'COBIT (procedimentos, não frameworks); níveis de capacidade do COBIT sem rótulos não confirmados; ITIL 4 (mantenedora); '
         'mudança na ITIL 4 (autoridade de mudança); Kanban (seis práticas); CMMI V2.0 (não "CMMI-DEV v2.0"); MPS.BR (metas e ISO '
         '33000); equivalência CMMI e MPS.BR removida por não ser exata; PDTIC (sem prazo inventado); Sprint de "1 a 4 semanas" '
         'para "um mês ou menos"; atribuições a bancas removidas.'],
        ['A conferir',
         'Rótulos dos níveis de capacidade do COBIT 2019; texto do Decreto estadual nº 15.404/2014; incisos do art. 18 da Lei 14.133 '
         'e detalhes da IN SGD/ME 94/2022 no texto vigente; fases exatas do Guia de PDTIC do SISP; edição do PMBOK citada no edital '
         'da BA; definição adotada para TO-RUN.'],
    ],
    'tip': ['Regra de Conteúdo', 'Este material não afirma nada sem fonte. Se houver divergência com a norma vigente, a norma prevalece.']})

ap['subtitle'] = ('COBIT 2019, ITIL 4, PMBOK 7ª/6ª Ed., Scrum, Kanban, XP, CMMI V2.0, MPS.BR, PETIC/PDTIC, Contratações de TIC '
                  '(Lei 14.133), TCO/ROI/FinOps, BPMN/DMN e Lean/Six Sigma')
json.dump(dados, open(ARQ, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('Governança atualizada: %d seções.' % len(S))
