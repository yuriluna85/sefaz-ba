import os
import sys
import json
from fpdf import FPDF

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONCURSO_DIR = os.path.join(BASE_DIR, 'Concurso SEFAZ')
JSON_FILE = os.path.join(BASE_DIR, 'apostilas_conteudo.json')

# Dicionário global de siglas para o glossário
GLOSSARIO_SIGLAS = {
    "ACID": "Atomicidade, Consistência, Isolamento e Durabilidade. Propriedades fundamentais para transações em SGBDs.",
    "BI": "Business Intelligence. Inteligência de Negócios para mineração e análise estratégica de dados.",
    "CAP": "Consistência, Disponibilidade e Tolerância a Partições. Teorema limitador para sistemas distribuídos.",
    "CEBRASPE": "Centro de Seleção e de Promoção de Eventos. Banca examinadora oficial de concursos públicos.",
    "CFC": "Conselho Federal de Contabilidade. Órgão responsável pela edição das NBCs no território nacional.",
    "CIAP": "Controle de Crédito de ICMS do Ativo Permanente. Controle fiscal de apropriação de créditos de bens imobilizados.",
    "CID": "Confidencialidade, Integridade e Disponibilidade. Pilares de sustentação da Segurança da Informação.",
    "COBIT": "Control Objectives for Information and Related Technologies. Framework global de Governança de TI.",
    "CPC": "Comitê de Pronunciamentos Contábeis. Emissor de normas convergentes com padrões internacionais.",
    "FGV": "Fundação Getulio Vargas. Banca examinadora de certames e instituição de pesquisa econômica.",
    "ICMS": "Imposto sobre Operações Relativas à Circulação de Mercadorias e Prestações de Serviços de Transporte.",
    "IPVA": "Imposto sobre a Propriedade de Veículos Automotores. Tributo de competência estadual.",
    "ITD": "Imposto sobre Transmissão Causa Mortis e Doação. Tributo sobre heranças e doações na Bahia.",
    "ITIL": "Information Technology Infrastructure Library. Boas práticas de Gerenciamento de Serviços de TI.",
    "KDD": "Knowledge Discovery in Databases. Processo sistemático de descoberta de conhecimento em bases de dados.",
    "LDO": "Lei de Diretrizes Orçamentárias. Define as metas e prioridades para o orçamento do exercício seguinte.",
    "LOA": "Lei Orçamentária Anual. Estima as receitas e fixa as despesas públicas para o exercício financeiro.",
    "NBC TA": "Normas Brasileiras de Contabilidade Técnicas de Auditoria Independente. Alinhadas ao padrão internacional.",
    "NBC TI": "Normas Brasileiras de Contabilidade Técnicas de Auditoria Interna. Foco nos processos organizacionais.",
    "NoSQL": "Not Only SQL. Família de SGBDs não relacionais estruturados para alto desempenho e escalabilidade.",
    "OLAP": "Online Analytical Processing. Ferramentas analíticas baseadas em cubos de dados multidimensionais.",
    "PAF-BA": "Processo Administrativo Fiscal do Estado da Bahia. Lei nº 3.956/1981 que regula o contencioso.",
    "PPA": "Plano Plurianual. Planejamento estratégico governamental de médio prazo (4 anos).",
    "RICMS-BA": "Regulamento do ICMS do Estado da Bahia. Decreto regulamentador do principal imposto estadual.",
    "RUP": "Rational Unified Process. Processo de desenvolvimento de software disciplinado e preditivo.",
    "SGBD": "Sistema de Gerenciamento de Banco de Dados. Software de controle e armazenamento seguro de dados.",
    "SEFAZ-BA": "Secretaria da Fazenda do Estado da Bahia. Órgão de arrecadação e controle fiscal baiano.",
    "SQL": "Structured Query Language. Linguagem declarativa padrão para consulta em SGBDs relacionais.",
    "TI": "Tecnologia da Informação. Recursos de hardware, software e infraestrutura de rede corporativa.",
    "XP": "Extreme Programming. Metodologia ágil de engenharia de software focada em excelência técnica."
}

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
        # Encode em latin-1 nativo para preservar acentos em PT-BR
        return text.encode('latin-1', 'replace').decode('latin-1')

    def header(self):
        # Chancela YLuna85 Labs: Azul Royal (#0D6EFD)
        self.set_fill_color(13, 110, 253)
        self.rect(0, 0, 210, 8, 'F')
        
        self.set_y(12)
        self.set_font('Helvetica', 'B', 8)
        self.set_text_color(110, 110, 110)
        self.cell(100, 5, self.clean_text('YLUNA85 LABS - HUB DE ESTUDOS SEFAZ-BA'), 0, 0, 'L')
        self.set_font('Helvetica', 'BI', 8)
        self.set_text_color(13, 110, 253)
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
        self.cell(100, 10, self.clean_text('Chancela YLuna85 LABs - Preparação Conjunta'), 0, 0, 'L')
        
        self.set_font('Helvetica', 'B', 8)
        self.cell(0, 10, self.clean_text(f'Página {self.page_no()}/{{nb}}'), 0, 0, 'R')

    def add_cover(self, title, subtitle):
        self.add_page()
        self.ln(25)
        
        self.set_font('Helvetica', 'B', 22)
        self.set_text_color(15, 23, 42)
        self.multi_cell(0, 10, self.clean_text(title), 0, 'C')
        self.ln(8)
        
        # Linha sob o título na cor Azul Royal da chancela
        self.set_draw_color(13, 110, 253)
        self.set_line_width(1.5)
        self.line(40, self.get_y(), 170, self.get_y())
        self.set_line_width(0.2)
        self.ln(12)
        
        self.set_font('Helvetica', '', 12)
        self.set_text_color(71, 85, 105)
        self.multi_cell(0, 7, self.clean_text(subtitle), 0, 'C')
        self.ln(35)
        
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(13, 110, 253)
        self.cell(0, 6, self.clean_text('CHANCELA EDITORIAL YLUNA85 LABS'), 0, 1, 'C')
        self.set_font('Helvetica', '', 10)
        self.set_text_color(100, 116, 139)
        self.cell(0, 6, self.clean_text('Preparação Conjunta: Auditor Fiscal (TI) & Agente de Tributos Estaduais'), 0, 1, 'C')
        self.cell(0, 6, self.clean_text('Revisão Ortográfica e Glossário Geral de Siglas'), 0, 1, 'C')
        self.ln(40)
        
        self.set_font('Helvetica', 'I', 9)
        self.set_text_color(148, 163, 184)
        self.cell(0, 10, self.clean_text('Material de livre circulação interna. Revisado em Português Brasileiro (pt-BR).'), 0, 1, 'C')

    def add_section(self, section_title):
        self.ln(3)
        self.set_font('Helvetica', 'B', 11.5)
        self.set_text_color(15, 23, 42)
        # Background suave YLuna85 (#F0F4FC)
        self.set_fill_color(240, 244, 252)
        self.cell(0, 9, self.clean_text(f'  {section_title}'), 0, 1, 'L', fill=True)
        self.ln(2)

    def add_subsection(self, sub_title):
        self.ln(2)
        self.set_font('Helvetica', 'B', 10)
        # Roxo Violeta (#7952B3) da chancela
        self.set_text_color(121, 82, 179)
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
        # Caixa estilizada com Azul Royal e Fundo Suave
        self.set_fill_color(240, 244, 252)
        self.set_draw_color(13, 110, 253)
        self.set_font('Helvetica', '', 9.5)
        
        # Calcular altura da caixa dinamicamente
        lines = len(self.multi_cell(180, 5, self.clean_text(f'EXPLICANDO A SIGLA / DICA DIDÁTICA: {tip_text}'), dry_run=True, output="LINES"))
        box_height = (lines * 5) + 12
        
        self.rect(x, y, 190, box_height, 'DF')
        self.set_fill_color(13, 110, 253)
        self.rect(x, y, 4, box_height, 'F')
        
        self.set_xy(x + 8, y + 3)
        self.set_font('Helvetica', 'B', 9.5)
        self.set_text_color(13, 110, 253)
        self.cell(0, 5, self.clean_text(title.upper()), 0, 1, 'L')
        
        self.set_x(x + 8)
        self.set_font('Helvetica', 'I', 9.5)
        self.set_text_color(51, 65, 85)
        self.multi_cell(178, 5, self.clean_text(tip_text))
        self.set_y(y + box_height + 4)

    def add_glossary(self):
        # Adiciona uma página específica de glossário ao final do caderno
        self.add_page()
        self.ln(3)
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(13, 110, 253) # Azul Royal
        self.cell(0, 9, self.clean_text('  GLOSSÁRIO DE SIGLAS E ABREVIATURAS'), 0, 1, 'L', fill=False)
        self.set_draw_color(13, 110, 253)
        self.set_line_width(1.2)
        self.line(10, self.get_y(), 200, self.get_y())
        self.set_line_width(0.2)
        self.ln(6)
        
        self.set_font('Helvetica', '', 9.5)
        self.set_text_color(51, 65, 85)
        self.multi_cell(0, 5.2, self.clean_text('Consulte abaixo o significado e a expansão explicativa de todas as siglas contábeis, tributárias e de TI presentes nas apostilas de preparação:'))
        self.ln(4)
        
        # Grid ordenado de siglas
        for sigla, desc in sorted(GLOSSARIO_SIGLAS.items()):
            # Verifica quebra de página preventiva
            if self.get_y() > 260:
                self.add_page()
                self.ln(5)
            self.set_font('Helvetica', 'B', 9.5)
            self.set_text_color(121, 82, 179) # Roxo Violeta
            self.cell(28, 6, self.clean_text(sigla), 0, 0, 'L')
            self.set_font('Helvetica', '', 9.5)
            self.set_text_color(51, 65, 85)
            self.multi_cell(0, 6, self.clean_text(desc))
            self.ln(1)

def generate_all_booklets():
    if not os.path.exists(JSON_FILE):
        print(f"[ERRO] Arquivo de conteúdo não localizado: {JSON_FILE}")
        return
        
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        booklets_data = json.load(f)
        
    print(f"Iniciando a geração de {len(booklets_data)} apostilas completas a partir do JSON...")
    os.makedirs(CONCURSO_DIR, exist_ok=True)
    
    count = 0
    for b in booklets_data:
        pdf = UniversalStudyBookletPDF(b["subject"])
        pdf.add_cover(b["title"], b["subtitle"])
        
        for sec in b["sections"]:
            pdf.add_page()
            pdf.add_section(sec["title"])
            pdf.add_paragraph(sec["content"])
            
            for title, desc in sec.get("bullets", []):
                pdf.add_bullet_point(title, desc)
                
            if sec.get("tip"):
                t_title, t_text = sec["tip"]
                pdf.add_tip_box(t_title, t_text)
                
        # Adiciona o Glossário de Siglas ao final
        pdf.add_glossary()
        
        out_path = os.path.join(CONCURSO_DIR, b["filename"])
        pdf.output(out_path)
        size_kb = os.path.getsize(out_path) / 1024
        count += 1
        print(f"[{count}/{len(booklets_data)}] Gerada com sucesso: {b['filename']} ({size_kb:.1f} KB)")
        
    print("\nTODAS AS APOSTILAS FORAM REVISADAS E REGERADAS EM PT-BR FLUIDO A PARTIR DO JSON!")

if __name__ == "__main__":
    generate_all_booklets()
