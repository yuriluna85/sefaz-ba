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
        self.cell(100, 5, self.clean_text('SEFAZ-BA - HUB DE ESTUDOS (REVISÃO FLUIDA E GLOSSÁRIO)'), 0, 0, 'L')
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
        self.cell(100, 10, self.clean_text('Manual Completo em Português Brasileiro - Preparação Conjunta (TI & Geral)'), 0, 0, 'L')
        
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
        self.cell(0, 6, self.clean_text('CONCURSO: SEFAZ-BA 2026'), 0, 1, 'C')
        self.set_font('Helvetica', '', 10)
        self.set_text_color(100, 116, 139)
        self.cell(0, 6, self.clean_text('Cargos: Auditor Fiscal (TI) & Agente de Tributos Estaduais (Geral)'), 0, 1, 'C')
        self.cell(0, 6, self.clean_text('Edição Especial: Linguagem Fluida em PT-BR & Explicação de Siglas Nativas'), 0, 1, 'C')
        self.ln(50)
        
        # Footer of cover
        self.set_font('Helvetica', 'I', 9)
        self.set_text_color(148, 163, 184)
        self.cell(0, 10, self.clean_text('Material revisado sem jargões obscuros, com glossário de siglas contábeis/fiscais.'), 0, 1, 'C')

    def add_section(self, section_title):
        self.ln(3)
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(15, 23, 42)
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
        lines = len(self.multi_cell(180, 5, self.clean_text(f'EXPLICANDO A SIGLA / DICA DIDÁTICA: {tip_text}'), dry_run=True, output="LINES"))
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
    
    # PAGE 1: COVER PAGE
    pdf.add_cover(
        "Manual de Estudos: Auditoria Fiscal",
        "Conceitos e Normas Didáticas, Análise de Risco e Materialidade, Planejamento Dinâmico, Amostragem e Papéis de Trabalho — Linguagem Clara em PT-BR com Glossário de Siglas"
    )
    
    # PAGE 2: GUIA DE SIGLAS ESPECIAIS DE AUDITORIA E CONTABILIDADE
    pdf.add_page()
    pdf.add_section("0. Glossário Introdutório de Siglas para Não-Contadores (Foco TI & Geral)")
    pdf.add_paragraph(
        "Para facilitar o estudo de quem não possui formação prévia em Contabilidade ou Direito, apresentamos abaixo o significado prático das principais siglas normativas citadas ao longo deste manual:"
    )
    pdf.add_bullet_point("NBC (Norma Brasileira de Contabilidade):", "Conjunto de regras técnicas e profissionais emitidas pelo Conselho Federal de Contabilidade (CFC) que regulam a profissão contábil e os exames no Brasil.")
    pdf.add_bullet_point("NBC TA (Norma Brasileira de Contabilidade Técnica de Auditoria):", "Normas específicas aplicadas aos auditores independentes/externos. O sufixo 'TA' indica 'Técnica de Auditoria' (ex: NBC TA 300, NBC TA 320). São convergentes com os padrões internacionais da IFAC.")
    pdf.add_bullet_point("NBC TI (Norma Brasileira de Contabilidade Técnica de Auditoria Interna):", "Regras aplicadas aos auditores internos, que pertencem aos quadros da própria empresa ou órgão público.")
    pdf.add_bullet_point("NBC TP (Norma Brasileira de Contabilidade Técnica de Perícia):", "Regras aplicadas aos peritos contábeis envolvidos em processos judiciais.")
    pdf.add_bullet_point("CFC (Conselho Federal de Contabilidade):", "Órgão federal autárquico que fiscaliza a profissão contábil e edita as normas NBC no Brasil.")
    pdf.add_bullet_point("CPC (Comitê de Pronunciamentos Contábeis):", "Entidade criada para emitir pronunciamentos técnicos contábeis em alinhamento com os padrões internacionais IFRS.")
    pdf.add_bullet_point("CIAP (Controle de Crédito de ICMS do Ativo Permanente):", "Documento e sistemática fiscal para apuração do crédito do imposto ICMS referente à compra de máquinas e equipamentos (ativo imobilizado), apropriado à razão de 1/48 por mês.")
    pdf.add_bullet_point("PAF-BA (Processo Administrativo Fiscal da Bahia):", "Rito legal e procedimental utilizado pela SEFAZ-BA para julgamento de contenciosos fiscais e autuações.")

    # PAGE 3: CONCEITOS E TIPOS DE AUDITORIA
    pdf.add_page()
    pdf.add_section("1. Conceito e Tipos de Auditoria: Interna, Externa e Perícia")
    pdf.add_paragraph(
        "A auditoria é um processo sistemático de obtenção e avaliação objetiva de evidências sobre operações econômicas e fiscais. O objetivo é verificar se as demonstrações contábeis e obrigações tributárias estão em conformidade com a lei e comunicar os resultados de forma clara."
    )
    pdf.add_subsection("Diferenciação Prática entre Auditoria Interna, Externa e Perícia")
    pdf.add_bullet_point(
        "Auditoria Interna (Regida pela NBC TI 01):",
        "Executada por servidores ou funcionários do próprio órgão/empresa. Possui foco operacional, preventivo e de assessoria à gestão para aprimorar os controles internos."
    )
    pdf.add_bullet_point(
        "Auditoria Independente / Externa (Regida pela NBC TA 200):",
        "Executada por profissionais ou órgãos externos autônomos sem vínculo empregatício. Seu foco principal é emitir um parecer (relatório final) formal sobre a veracidade e conformidade das demonstrações financeiras."
    )
    pdf.add_bullet_point(
        "Perícia Contábil (Regida pela NBC TP 01):",
        "Destinada a produzir prova técnica para instruir processos judiciais ou disputas. O perito responde a quesitos formulados por juízes ou pelas partes litigantes."
    )

    # PAGE 4: PLANEJAMENTO E MATERIALIDADE (CORREÇÃO DE VOCABULÁRIO FLUIDO)
    pdf.add_page()
    pdf.add_section("2. Planejamento de Auditoria e Materialidade (NBC TA 300 e NBC TA 320)")
    pdf.add_paragraph(
        "O planejamento não é uma etapa isolada ou estática da auditoria. Trata-se de um processo contínuo, iterativo e dinâmico que se inicia logo após a conclusão da auditoria anterior e se desenvolve ao longo de todo o trabalho."
    )
    pdf.add_tip_box(
        "Linguagem Clara: Entendendo a Dinâmica do Planejamento",
        "Em muitos textos antigos ou de tradução literal robótica, usa-se o termo 'estanque'. No português brasileiro atual, preferimos dizer que o planejamento 'não é uma etapa isolada ou compartimentada', ou seja, ele não fica engessado e pode ser revisado a qualquer momento durante os trabalhos em campo!"
    )
    pdf.add_subsection("Materialidade e Agregação de Erros (NBC TA 320)")
    pdf.add_paragraph(
        "A NBC TA 320 trata da Materialidade no Planejamento e na Execução da Auditoria. A materialidade representa o valor limite a partir do qual uma omissão ou erro nas demonstrações pode influenciar as decisões econômicas dos usuários."
    )
    pdf.add_bullet_point(
        "Revisão Contínua da Materialidade:",
        "Se durante a auditoria forem encontrados pequenos erros individuais, o auditor deve somá-los. O acúmulo de várias incorreções pequenas (que isoladamente pareciam irrelevantes) pode ultrapassar o limite global de materialidade, exigindo a revisão imediata do plano de auditoria."
    )

    # PAGE 5: REGRAS ESPECÍFICAS DE AUDITORIA FISCAL (SEFAZ-BA)
    pdf.add_page()
    pdf.add_section("3. Procedimentos Fiscais Específicos e Normas Recentes")
    pdf.add_bullet_point(
        "Caixa Credor Diário:",
        "Em auditoria fiscal, o saldo da conta Caixa nunca pode ser negativo (credor) em nenhum dia do ano. Lançamentos contábeis artificiais feitos no encerramento do exercício (31/12) não cobrem estouros de caixa ocorridos ao longo do ano."
    )
    pdf.add_bullet_point(
        "Apropriação do Crédito do ICMS no Ativo Imobilizado (CIAP):",
        "O crédito fiscal relativo à aquisição de bens do ativo permanente (máquinas, equipamentos) deve ser lançado mensalmente na proporção de 1/48 (um quarenta e oito avos) por mês, conforme a ficha CIAP. É ilegal efetuar a apropriação integral do crédito no mês da compra."
    )
    pdf.add_bullet_point(
        "Propriedade dos Papéis de Trabalho (NBC TA 230):",
        "Os papéis de trabalho (documentação da auditoria) pertencem exclusivamente ao auditor. A empresa fiscalizada ou auditada não pode reter física nem digitalmente esses arquivos."
    )

    # Save output
    out_filename = "Apostila_Auditoria_Fiscal.pdf"
    out_path = os.path.join(CONCURSO_DIR, out_filename)
    try:
        pdf.output(out_path)
        size_mb = os.path.getsize(out_path) / (1024 * 1024)
        print(f"Generated and updated cleanly: {out_filename} ({size_mb:.2f} MB)")
    except Exception as e:
        print(f"Error generating {out_filename}: {e}")

if __name__ == "__main__":
    build_auditoria_fiscal_pdf()
