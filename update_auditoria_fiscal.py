import os
from fpdf import FPDF

# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONCURSO_DIR = os.path.join(BASE_DIR, 'Concurso SEFAZ')

class ExtendedStudyBookletPDF(FPDF):
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
        # Top bar
        self.set_fill_color(101, 163, 13)  # Lime-600 #65a30d
        self.rect(0, 0, 210, 8, 'F')
        
        # Header text
        self.set_y(12)
        self.set_font('Helvetica', 'B', 8)
        self.set_text_color(110, 110, 110)
        self.cell(100, 5, self.clean_text('SEFAZ - HUB DE ESTUDOS'), 0, 0, 'L')
        self.set_font('Helvetica', 'BI', 8)
        self.set_text_color(101, 163, 13)
        self.cell(0, 5, self.clean_text(self.subject_name.upper()), 0, 1, 'R')
        
        # Divider line
        self.set_draw_color(220, 220, 220)
        self.line(10, 18, 200, 18)
        self.ln(5)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        
        # Divider line
        self.set_draw_color(220, 220, 220)
        self.line(10, 282, 200, 282)
        
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(100, 10, self.clean_text('Manual Completo - Preparação Conjunta (TI & Geral)'), 0, 0, 'L')
        
        # Page number
        self.set_font('Helvetica', 'B', 8)
        self.cell(0, 10, self.clean_text(f'Página {self.page_no()}/{{nb}}'), 0, 0, 'R')

    def add_cover(self, title, subtitle):
        self.add_page()
        self.ln(30)
        
        # Subject Title
        self.set_font('Helvetica', 'B', 24)
        self.set_text_color(15, 23, 42)  # Slate-900
        self.multi_cell(0, 10, self.clean_text(title), 0, 'C')
        self.ln(10)
        
        # Decorative divider line
        self.set_draw_color(101, 163, 13)
        self.set_line_width(1.5)
        self.line(40, self.get_y(), 170, self.get_y())
        self.set_line_width(0.2)
        self.ln(12)
        
        # Subtitle
        self.set_font('Helvetica', '', 13)
        self.set_text_color(71, 85, 105)  # Slate-600
        self.multi_cell(0, 8, self.clean_text(subtitle), 0, 'C')
        self.ln(40)
        
        # Meta info
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(15, 23, 42)
        self.cell(0, 6, self.clean_text('CONCURSO: SEFAZ'), 0, 1, 'C')
        self.set_font('Helvetica', '', 10)
        self.set_text_color(100, 116, 139)
        self.cell(0, 6, self.clean_text('Cargos: Auditor Fiscal (TI) & Agente de Tributos Estaduais (Geral)'), 0, 1, 'C')
        self.cell(0, 6, self.clean_text('Foco de Bancas: FGV e FCC'), 0, 1, 'C')
        self.ln(50)
        
        # Footer of cover
        self.set_font('Helvetica', 'I', 9)
        self.set_text_color(148, 163, 184)
        self.cell(0, 10, self.clean_text('Este material foi consolidado com base na bibliografia recomendada e provas recentes.'), 0, 1, 'C')

    def add_section(self, section_title):
        self.ln(3)
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(15, 23, 42)
        # Background bar
        self.set_fill_color(241, 245, 249) # Slate-100
        self.cell(0, 10, self.clean_text(f'  {section_title}'), 0, 1, 'L', fill=True)
        self.ln(3)

    def add_subsection(self, sub_title):
        self.ln(2)
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(101, 163, 13) # Lime-600
        self.cell(0, 7, self.clean_text(sub_title), 0, 1, 'L')
        self.ln(1)

    def add_paragraph(self, text):
        self.set_font('Helvetica', '', 9.5)
        self.set_text_color(51, 65, 85)  # Slate-700
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
        
        self.set_fill_color(247, 254, 231) # Lime-50
        self.set_draw_color(101, 163, 13)
        
        self.set_font('Helvetica', '', 9.5)
        lines = len(self.multi_cell(180, 5, self.clean_text(f'DICA DE REVISÃO: {tip_text}'), dry_run=True, output="LINES"))
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

def build_auditoria_fiscal_pdf():
    pdf = ExtendedStudyBookletPDF("Auditoria Fiscal")
    
    # ----------------------------------------------------
    # PAGE 1: COVER PAGE
    # ----------------------------------------------------
    pdf.add_cover(
        "Manual de Estudos: Auditoria Fiscal",
        "Conceitos e Normas de Auditoria, Risco e Materialidade, Planejamento, Procedimentos e Evidências, Amostragem, Auditoria Fiscal de Estoques, Caixa, Passivos e Parecer do Auditor"
    )
    
    # ----------------------------------------------------
    # PAGE 2: CONCEITOS E TIPOS DE AUDITORIA
    # ----------------------------------------------------
    pdf.add_page()
    pdf.add_section("1. Conceito e Tipos de Auditoria: Interna, Externa e Perícia")
    
    pdf.add_paragraph(
        "A auditoria é um processo sistemático de obter e avaliar objetivamente evidências sobre afirmações a respeito de eventos e ações econômicas, para estabelecer o grau de conformidade e comunicar os resultados aos usuários interessados."
    )
    
    pdf.add_subsection("Auditoria Interna (NBC TI 01), Externa (NBC TA 200) e Perícia Contábil (NBC TP 01)")
    pdf.add_bullet_point(
        "Auditoria Interna:",
        "Realizada por funcionários da própria organização. Seu objetivo é assessorar a alta administração no cumprimento de metas, avaliando a eficácia dos controles internos, gestão de riscos e governança. Tem foco operacional e preventivo."
    )
    pdf.add_bullet_point(
        "Auditoria Independente (Externa):",
        "Realizada por profissional autônomo sem vínculo empregatício. Seu objetivo principal é expressar uma opinião sobre se as demonstrações contábeis foram preparadas, em todos os aspectos relevantes, em conformidade com as normas vigentes."
    )
    pdf.add_bullet_point(
        "Perícia Contábil:",
        "Destinada a produzir prova técnica para instruir processos judiciais ou extrajudiciais. A diferença técnica crucial é que o perito contábil deve responder a quesitos técnicos formulados pelo juiz ou pelas partes, enquanto o auditor não se submete a esses questionamentos formais de lide."
    )
    
    pdf.add_tip_box(
        "Diferença no Foco e Subordinação",
        "A auditoria interna está subordinada à administração da entidade e busca avaliar a eficiência operacional e o cumprimento de normas internas. A perícia busca esclarecer controvérsias fáticas para terceiros (juízes/árbitros)."
    )

    # ----------------------------------------------------
    # PAGE 3: RISCO DE AUDITORIA E COMPLEXIDADE
    # ----------------------------------------------------
    pdf.add_page()
    pdf.add_section("2. Risco de Auditoria e Complexidade Ambiental (NBC TA 315)")
    
    pdf.add_paragraph(
        "O Risco de Auditoria é a possibilidade de o auditor expressar uma opinião inadequada quando as demonstrações contiverem distorções relevantes. Ele é composto pelo Risco de Distorção Relevante (RDR = Inerente * Controle) e pelo Risco de Detecção (RD)."
    )
    
    pdf.add_subsection("Componentes do Risco sob a Ótica da Complexidade")
    pdf.add_bullet_point(
        "Risco Inerente (RI):",
        "A susceptibilidade de uma conta ou transação a distorções relevantes antes de considerar os controles internos. Ele aumenta drasticamente em ambientes de alta complexidade tecnológica, instabilidade de mercado ou operações incomuns."
    )
    pdf.add_bullet_point(
        "Risco de Controle (RC):",
        "O risco de que uma distorção relevante não seja prevenida, detectada ou corrigida tempestivamente pelo controle interno da entidade."
    )
    pdf.add_bullet_point(
        "Risco de Detecção (RD):",
        "O risco de que os testes aplicados pelo auditor não detectem uma distorção existente. É o único componente diretamente controlado pelo auditor."
    )
    
    pdf.add_tip_box(
        "Limitações dos Controles e Ceticismo",
        "Mesmo quando os controles internos são formalmente bem estruturados, o risco inerente e o risco de auditoria aumentam em ambientes de alta complexidade. A confiança pessoal nos gestores nunca deve reduzir o ceticismo profissional do auditor."
    )

    # ----------------------------------------------------
    # PAGE 4: PLANEJAMENTO E REVISÃO DE MATERIALIDADE
    # ----------------------------------------------------
    pdf.add_page()
    pdf.add_section("3. Planejamento de Auditoria e Materialidade (NBC TA 300 / 320)")
    
    pdf.add_paragraph(
        "O planejamento não é uma fase isolada ou estanque da auditoria, mas um processo contínuo, iterativo e dinâmico que se inicia logo após a conclusão da auditoria anterior e se estende até a emissão do relatório final."
    )
    
    pdf.add_subsection("Estratégia Global, Plano de Trabalho e Revisões de Materialidade")
    pdf.add_bullet_point(
        "Estratégia Global:",
        "Estabelece o alcance, a época e a direção do trabalho, orientando o desenvolvimento do plano de auditoria."
    )
    pdf.add_bullet_point(
        "Plano de Auditoria (Programa):",
        "Detalha a natureza, época e extensão dos procedimentos a serem executados pela equipe."
    )
    pdf.add_bullet_point(
        "Revisão da Materialidade (NBC TA 320):",
        "A materialidade definida no planejamento não é imutável. Caso o auditor identifique novas distorções durante a execução, ele deve avaliar o efeito acumulado das pequenas distorções individuais (que separadamente parecem irrelevantes) e rever a materialidade."
    )
    
    pdf.add_tip_box(
        "Agregação de Distorções",
        "A soma de pequenos erros individualmente insignificantes pode tornar relevante o seu efeito conjunto nas demonstrações contábeis, exigindo a reavaliação imediata da materialidade e dos riscos associados."
    )

    # ----------------------------------------------------
    # PAGE 5: DOCUMENTAÇÃO DE AUDITORIA
    # ----------------------------------------------------
    pdf.add_page()
    pdf.add_section("4. Documentação de Auditoria e Papéis de Trabalho (NBC TA 230)")
    
    pdf.add_paragraph(
        "A documentação de auditoria (papéis de trabalho) é o registro escrito dos procedimentos de auditoria executados, das evidências obtidas e das conclusões alcançadas. Ela serve para comprovar que o trabalho foi realizado em conformidade com as normas."
    )
    
    pdf.add_subsection("Requisitos de Clareza e Insuficiência de Resumos Internos")
    pdf.add_bullet_point(
        "Padrão do Auditor Experiente:",
        "A documentação deve ser suficientemente clara para permitir que um auditor experiente, sem nenhuma conexão anterior com o trabalho, compreenda a natureza, a época, a extensão dos testes e os achados obtidos."
    )
    pdf.add_bullet_point(
        "Insuficiência de Explicações Verbais e Planilhas:",
        "Explicações verbais ou planilhas internas informais elaboradas pelo próprio contribuinte não substituem documentos fiscais originais (como notas fiscais e livros oficiais). Documentos fiscais originais e registros auditáveis são indispensáveis."
    )
    pdf.add_bullet_point(
        "Custódia e Arquivamento:",
        "O prazo mínimo de guarda dos papéis de trabalho é de 5 anos a contar da data de emissão do relatório. O arquivo final deve ser fechado administrativamente em até 60 dias."
    )
    
    pdf.add_tip_box(
        "Formalidade da Evidência",
        "A ausência de documentação original de entrada impede o creditamento fiscal legítimo do ICMS. O auditor fiscal não pode validar créditos com base em planilhas internas ou resumos sem lastro documental."
    )

    # ----------------------------------------------------
    # PAGE 6: EVIDÊNCIA DE AUDITORIA E BACKUPS
    # ----------------------------------------------------
    pdf.add_page()
    pdf.add_section("5. Evidência de Auditoria e Backups Digitais (NBC TA 500)")
    
    pdf.add_paragraph(
        "O auditor deve obter evidências de auditoria apropriadas (qualidade, relevância e confiabilidade) e suficientes (quantidade) para fundamentar sua opinião técnica."
    )
    
    pdf.add_subsection("Técnicas de Obtenção e Confiabilidade de Arquivos Digitais")
    pdf.add_bullet_point(
        "Métodos Tradicionais:",
        "Inspeção física e documental, observação direta, recálculo matemático, reexecução de controles e procedimentos analíticos globais."
    )
    pdf.add_bullet_point(
        "Confiabilidade de Backups Digitais:",
        "A destruição de documentos originais sob a justificativa de existência de backup digital não garante confiabilidade automática. A confiabilidade do documento digitalizado depende estritamente da segurança e dos controles existentes sobre a sua geração e armazenamento."
    )
    pdf.add_bullet_point(
        "Ceticismo com Arquivos Digitais:",
        "Arquivos eletrônicos sem assinaturas válidas, trilhas de auditoria ou gerados em sistemas com fraco controle interno são considerados de baixa confiabilidade."
    )
    
    pdf.add_tip_box(
        "Auditoria de Sistemas de TI",
        "Ao lidar com evidências digitais, o auditor fiscal deve certificar-se da integridade do banco de dados do contribuinte, avaliando logs e políticas de backup do sistema ERP."
    )

    # ----------------------------------------------------
    # PAGE 7: CONFIRMAÇÕES EXTERNAS E ESPECIALISTAS
    # ----------------------------------------------------
    pdf.add_page()
    pdf.add_section("6. Confirmações Externas e Uso de Especialistas (NBC TA 505 / 620)")
    
    pdf.add_paragraph(
        "O auditor utiliza procedimentos de confirmação externa (circularização) e pode, quando necessário, contratar o trabalho de um especialista para obter evidência em áreas fora da contabilidade."
    )
    
    pdf.add_subsection("Interferência na Circularização e Trabalho de Terceiros")
    pdf.add_bullet_point(
        "Interferência da Entidade (NBC TA 505):",
        "As confirmações externas tornam-se ineficazes e perdem a confiabilidade se houver indícios ou suspeitas de que a gerência da entidade auditada interferiu direta ou indiretamente na comunicação entre o auditor e o terceiro."
    )
    pdf.add_bullet_point(
        "Uso do Especialista do Auditor (NBC TA 620):",
        "Quando o auditor precisa avaliar reservas minerais (geólogo), estruturas de TI complexas ou processos judiciais específicos (advogado), ele pode contratar um especialista."
    )
    pdf.add_bullet_point(
        "Responsabilidade Técnica:",
        "O auditor deve avaliar a competência, a independência e a adequação do laudo emitido pelo especialista contratado. Contudo, o uso do trabalho do especialista não exime o auditor de sua responsabilidade integral pela opinião emitida."
    )
    
    pdf.add_tip_box(
        "Independência do Especialista",
        "Se o especialista contratado pelo auditor possuir conflito de interesses com a auditada, seu laudo será considerado inválido para fins de suporte da opinião."
    )

    # ----------------------------------------------------
    # PAGE 8: AMOSTRAGEM EM AUDITORIA
    # ----------------------------------------------------
    pdf.add_page()
    pdf.add_section("7. Amostragem em Auditoria (NBC TA 530)")
    
    pdf.add_paragraph(
        "A amostragem de auditoria consiste na aplicação de procedimentos em menos de 100% dos itens de uma população relevante para que todos tenham chance de seleção, permitindo tirar conclusões sobre a população total."
    )
    
    pdf.add_subsection("Riscos de Amostragem (Alfa e Beta) e Métodos")
    pdf.add_bullet_point(
        "Risco de Superconfiança / Aceitação Incorreta (Risco Beta):",
        "Concluir que os controles são eficazes quando não são, ou que não há distorção relevante quando há. Afeta a EFICÁCIA da auditoria, podendo levar a uma opinião incorreta."
    )
    pdf.add_bullet_point(
        "Risco de Subconfiança / Rejeição Incorreta (Risco Alfa):",
        "Concluir que os controles são ineficazes quando são eficazes, ou que há distorção quando não há. Afeta a EFICIÊNCIA da auditoria, gerando retrabalho desnecessário."
    )
    pdf.add_bullet_point(
        "Amostragem Estatística vs. Não-Estatística:",
        "A amostragem é estatística se houver seleção aleatória dos itens e uso de teoria de probabilidades para avaliar resultados e medir riscos. Caso contrário, é baseada em julgamento (não-estatística)."
    )
    
    pdf.add_tip_box(
        "Exclusão da Amostragem",
        "A amostragem não se aplica quando o auditor decide examinar 100% da população (ex: circularizar as únicas duas contas bancárias existentes) ou em procedimentos analíticos globais."
    )

    # ----------------------------------------------------
    # PAGE 9: AUDITORIA FISCAL DE ESTOQUES
    # ----------------------------------------------------
    pdf.add_page()
    pdf.add_section("8. Auditoria Fiscal de Estoques e Omissão de Receita (ICMS)")
    
    pdf.add_paragraph(
        "No âmbito do ICMS fiscalizado pela SEFAZ, a auditoria de estoques visa apurar fraudes relativas à sonegação fiscal, compras sem nota fiscal ou omissão de receita."
    )
    
    pdf.add_subsection("Direção dos Testes e Equação Física de Inventário")
    pdf.add_bullet_point(
        "Subavaliação / Omissão (Foco Fiscal):",
        "Para testar se há vendas sem nota fiscal (omissão), o teste parte da origem física (estoque físico ou documentos de entrada) em direção aos registros contábeis. Se o item físico existe ou foi comprado mas não está escriturado, há omissão."
    )
    pdf.add_bullet_point(
        "Superavaliação (Foco Comercial):",
        "Para testar se ativos estão inflados (fantasmas), o teste parte dos registros contábeis/livros fiscais em direção à origem física."
    )
    pdf.add_bullet_point(
        "Equação Geral do Inventário Físico:",
        "Estoque Final calculado = Estoque Inicial + Compras (entradas) - Vendas (saídas). Se o Estoque Final físico aferido for menor que o calculado, presume-se omissão de receita pelas saídas não registradas."
    )
    
    pdf.add_tip_box(
        "Presunções Legais do Fisco",
        "A constatação de entrada de mercadorias sem registro na escrita fiscal gera a presunção legal de que a mesma foi vendida sem nota fiscal, autorizando a cobrança do ICMS devido com multa."
    )

    # ----------------------------------------------------
    # PAGE 10: PASSIVO FICTÍCIO E AUDITORIA DE CAIXA
    # ----------------------------------------------------
    pdf.add_page()
    pdf.add_section("9. Passivo Fictício e Auditoria de Caixa (Estouro de Caixa)")
    
    pdf.add_paragraph(
        "Empresas que realizam vendas sem nota fiscal acumulam caixa informal (caixa dois). Para inserir esses recursos na empresa de forma aparentemente legal, simulam-se passivos fictícios ou empréstimos de sócios."
    )
    
    pdf.add_subsection("Saldo Credor de Caixa e Passivos Inexistentes")
    pdf.add_bullet_point(
        "Saldo Credor de Caixa (Estouro de Caixa):",
        "A conta Caixa (Ativo) registra numerário em espécie. Fisicamente, é impossível haver saldo negativo na gaveta. Contabilmente, se houver saldo credor no Caixa, significa que houve pagamentos maiores do que o saldo disponível. Presume-se a omissão de receita."
    )
    pdf.add_bullet_point(
        "Passivo Fictício:",
        "Obrigação escriturada no passivo que já foi paga 'por fora' (com caixa dois) ou que nunca existiu (simulação de empréstimo). O auditor descobre por meio da circularização dos credores."
    )
    pdf.add_bullet_point(
        "Suprimento Indevido de Caixa:",
        "Depósitos em dinheiro na conta bancária da empresa sem comprovação científica ou documental de sua origem lícita, fingindo empréstimos dos sócios."
    )
    
    pdf.add_tip_box(
        "Auditoria Diária de Caixa",
        "Muitas fraudes tentam maquiar o saldo do Caixa no dia 31/12 com depósitos temporários que são retirados em 02/01. O auditor deve analisar as movimentações diárias (razão auxiliar) e não apenas o fechamento do Balanço."
    )

    # ----------------------------------------------------
    # PAGE 11: RELATÓRIO DO AUDITOR INDEPENDENTE
    # ----------------------------------------------------
    pdf.add_page()
    pdf.add_section("10. Relatório e Opinião do Auditor (NBC TA 700 / 705)")
    
    pdf.add_paragraph(
        "O relatório é a peça formal onde o auditor expressa sua conclusão sobre a conformidade das demonstrações contábeis auditadas."
    )
    
    pdf.add_subsection("Tipos de Opinião e Efeitos da Materialidade e Relevância")
    pdf.add_bullet_point(
        "Opinião Não Modificada (Limpa - NBC TA 700):",
        "Expressa quando o auditor obtém segurança razoável de que as demonstrações estão livres de distorções relevantes e foram preparadas de acordo com as normas."
    )
    pdf.add_bullet_point(
        "Opinião Modificada com Ressalva:",
        "O auditor encontra distorções relevantes, mas não generalizadas; ou não consegue obter evidência, mas os efeitos possíveis seriam relevantes, mas não generalizados."
    )
    pdf.add_bullet_point(
        "Opinião Adversa:",
        "O auditor obtém evidência de que as distorções são relevantes E generalizadas (comprometem a estrutura global das demonstrações)."
    )
    pdf.add_bullet_point(
        "Abstenção de Opinião:",
        "O auditor não consegue obter evidência apropriada e suficiente (limitação extrema de escopo) e conclui que os efeitos de distorções não detectadas seriam relevantes E generalizados."
    )
    
    pdf.add_tip_box(
        "Parágrafo de Ênfase",
        "O parágrafo de ênfase chama a atenção do leitor para uma questão já divulgada corretamente nas notas explicativas, considerada essencial para a compreensão. Não modifica a opinião do auditor."
    )

    # ----------------------------------------------------
    # PAGE 12: AS 12 GRANDES PEGADINHAS DE AUDITORIA
    # ----------------------------------------------------
    pdf.add_page()
    pdf.add_section("11. As 12 Grandes Pegadinhas de Prova (FGV / FCC / Cebraspe)")
    
    pdf.add_paragraph(
        "Fique alerta para os seguintes pontos críticos recorrentes nas provas de auditor de fiscos estaduais:"
    )
    
    pdf.add_bullet_point(
        "1. Direção do Teste de Omissão:",
        "Para pegar vendas sem nota fiscal (subavaliação), parte-se do estoque físico ou nota de entrada para o livro fiscal, e não o contrário."
    )
    pdf.add_bullet_point(
        "2. Circularização Negativa sem Resposta:",
        "A ausência de resposta na circularização negativa denota conformidade do terceiro. É menos confiável e exige RDR baixo para ser adotada."
    )
    pdf.add_bullet_point(
        "3. Risco de Auditoria não é do Negócio:",
        "Insolvência, processos judiciais de mercado ou crise econômica são riscos do negócio, e não riscos de auditoria (emissão de parecer inadequado)."
    )
    pdf.add_bullet_point(
        "4. Prevenção de Fraudes e Erros:",
        "A responsabilidade primária pela prevenção de fraudes e erros é dos gestores e da governança da entidade, não do auditor externo."
    )
    pdf.add_bullet_point(
        "5. Amostragem em Testes de 100%:",
        "Não se aplica amostragem se a população for testada integralmente (100% de cobertura)."
    )
    pdf.add_bullet_point(
        "6. Risco de Amostragem vs. Não-Amostragem:",
        "O risco de amostragem advém do tamanho da amostra. O risco de não-amostragem decorre de erros metodológicos ou negligência do auditor."
    )
    pdf.add_bullet_point(
        "7. Abstenção de Opinião vs. Adversa:",
        "Abstenção ocorre por falta de evidência (limitação). Adversa ocorre porque a evidência foi obtida e comprova erros generalizados."
    )
    pdf.add_bullet_point(
        "8. CIAP não é Crédito Imediato:",
        "O crédito do ICMS sobre ativo imobilizado é apropriado em 1/48 avos por mês (CIAP), sendo ilegal o crédito integral no mês da aquisição."
    )
    pdf.add_bullet_point(
        "9. Caixa Credor Diário:",
        "O caixa não pode ter saldo credor em nenhum dia do ano. Lançamentos artificiais no Balanço de 31/12 não cobrem estouros ocorridos ao longo do ano."
    )
    pdf.add_bullet_point(
        "10. Propriedade dos Papéis de Trabalho:",
        "Pertencem exclusivamente ao auditor. A entidade não pode retê-los física ou digitalmente."
    )
    pdf.add_bullet_point(
        "11. Confiabilidade de Backups Digitais (Novo - SEFAZ-PI 2025):",
        "A confiabilidade de imagens digitalizadas e backups não deve ser presumida e depende da solidez dos controles de TI existentes."
    )
    pdf.add_bullet_point(
        "12. Responsabilidade sob Trabalho de Especialista (Novo - SEFAZ-PI 2025):",
        "O auditor utiliza laudos de especialistas (geólogo, engenheiro), mas a responsabilidade técnica pela opinião continua integralmente sua."
    )

    # Save output
    out_filename = "Apostila_Auditoria_Fiscal.pdf"
    out_path = os.path.join(CONCURSO_DIR, out_filename)
    try:
        pdf.output(out_path)
        size_mb = os.path.getsize(out_path) / (1024 * 1024)
        print(f"Generated and updated: {out_filename} ({size_mb:.2f} MB)")
    except Exception as e:
        print(f"Error generating {out_filename}: {e}")

if __name__ == "__main__":
    build_auditoria_fiscal_pdf()
