"""Etapa final de organização do questions.json (idempotente).

1. Remove as 30 "variantes" em texto-molde da SEFAZ-CE e cria 30 questões novas, elaboradas
   pelo YLuna85 LABs, cada uma com fundamento em norma ou padrão citado (verificável).
2. Questões antigas: troca rótulos "(Adaptada)" / "(Simulada)" (que atribuíam a bancas questões
   que não vieram delas), define cargos e escopo pelo assunto e marca revisao = legado_nao_auditado.
3. Oculta itens com problema conhecido (ex.: q_gen_15).

Cargos: auditor_ti (Auditor Fiscal - TI) e agente (Agente de Tributos). Escopo: edital_ba_2022
(assunto do edital SEFAZ-BA/FGV 2022), correlato (comum em provas fiscais, não listado em 2022)
ou fora. O edital do Auditor Fiscal 2026 ainda não foi publicado.

Uso: python organizar_banco.py [--dry-run]
"""
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
ARQ = os.path.join(BASE, 'questions.json')

AT, AG = 'auditor_ti', 'agente'
AMBOS = [AT, AG]
ED, COR = 'edital_ba_2022', 'correlato'
CE = {'C': 'Certo', 'E': 'Errado'}

# (assunto, tópico, cargos, escopo, enunciado, gabarito, explicação, fundamento)
NOVAS = [
    ('Direito Tributário', 'Conceito de tributo', AMBOS, ED,
     'O tributo pode ter por objeto a punição de ato ilícito, desde que a sanção esteja prevista em lei.', 'E',
     'O conceito legal de tributo exclui expressamente a sanção de ato ilícito: é prestação pecuniária compulsória que não constitui sanção de ato ilícito. A punição é feita por multa, que não é tributo.',
     'CTN, art. 3º'),
    ('Direito Tributário', 'Obrigação tributária principal', AMBOS, ED,
     'A obrigação tributária principal tem por objeto o pagamento de tributo ou penalidade pecuniária e extingue-se juntamente com o crédito dela decorrente.', 'C',
     'É a redação do §1º do art. 113 do CTN. A obrigação acessória, por sua vez, tem por objeto prestações positivas ou negativas previstas na legislação no interesse da arrecadação ou da fiscalização.',
     'CTN, art. 113, §1º'),
    ('Direito Tributário', 'Suspensão e exclusão do crédito', AMBOS, ED,
     'A anistia é hipótese de suspensão da exigibilidade do crédito tributário.', 'E',
     'A anistia é modalidade de exclusão do crédito tributário (junto com a isenção). As hipóteses de suspensão da exigibilidade estão no art. 151, como a moratória, o depósito do montante integral e as reclamações e recursos administrativos.',
     'CTN, arts. 151 e 175'),
    ('Direito Tributário', 'Extinção do crédito', AMBOS, ED,
     'A remissão é uma das modalidades de extinção do crédito tributário.', 'C',
     'O art. 156 do CTN lista as modalidades de extinção do crédito tributário, e a remissão consta do inciso IV, ao lado do pagamento, da compensação, da transação, da prescrição e da decadência, entre outras.',
     'CTN, art. 156, IV'),
    ('Direito Tributário', 'Decadência', AMBOS, ED,
     'Em regra, o direito de a Fazenda Pública constituir o crédito tributário extingue-se após cinco anos, contados do primeiro dia do exercício seguinte àquele em que o lançamento poderia ter sido efetuado.', 'C',
     'É a regra geral de decadência do art. 173, I, do CTN: prazo de cinco anos, com termo inicial no primeiro dia do exercício seguinte àquele em que o lançamento poderia ter sido efetuado.',
     'CTN, art. 173, I'),
    ('Direito Tributário', 'Prescrição', AMBOS, ED,
     'A ação para a cobrança do crédito tributário prescreve em dez anos, contados da data de sua constituição definitiva.', 'E',
     'O prazo de prescrição da ação de cobrança do crédito tributário é de cinco anos, contados da constituição definitiva (art. 174 do CTN), e não de dez.',
     'CTN, art. 174'),
    ('Direito Tributário', 'Princípio da legalidade tributária', AMBOS, ED,
     'É vedado à União, aos Estados, ao Distrito Federal e aos Municípios exigir ou aumentar tributo sem lei que o estabeleça.', 'C',
     'É o princípio da legalidade tributária, previsto no art. 150, I, da Constituição Federal, entre as limitações ao poder de tributar.',
     'CF/88, art. 150, I'),
    ('Direito Constitucional', 'Concurso público', AMBOS, ED,
     'A investidura em cargo ou emprego público depende de aprovação prévia em concurso público, ressalvadas as nomeações para cargo em comissão declarado em lei de livre nomeação e exoneração.', 'C',
     'É a regra do art. 37, II, da Constituição Federal: o concurso é a regra de ingresso, e os cargos em comissão de livre nomeação e exoneração são a exceção.',
     'CF/88, art. 37, II'),
    ('Direito Constitucional', 'Responsabilidade civil do Estado', AMBOS, ED,
     'Pela Constituição Federal, os danos que agentes de pessoas jurídicas de direito público causem a terceiros geram responsabilidade civil subjetiva do Estado, que exige a comprovação de dolo ou culpa.', 'E',
     'O art. 37, §6º, da Constituição adota a responsabilidade objetiva das pessoas jurídicas de direito público pelos danos que seus agentes, nessa qualidade, causarem a terceiros. Dolo ou culpa só são discutidos na ação de regresso contra o agente.',
     'CF/88, art. 37, §6º'),
    ('Direito Administrativo', 'Decadência da anulação de atos', AMBOS, ED,
     'Segundo a Lei nº 9.784/1999, o direito da Administração de anular os atos administrativos de que decorram efeitos favoráveis aos destinatários decai em cinco anos, contados da data em que foram praticados, salvo comprovada má-fé.', 'C',
     'É a redação do art. 54 da Lei nº 9.784/1999 (processo administrativo federal).',
     'Lei nº 9.784/1999, art. 54'),
    ('Direito Administrativo', 'Princípios da Administração Pública', AMBOS, ED,
     'Os princípios expressos no caput do art. 37 da Constituição Federal são legalidade, moralidade, publicidade, eficiência e razoabilidade.', 'E',
     'O caput do art. 37 traz cinco princípios: legalidade, impessoalidade, moralidade, publicidade e eficiência. A razoabilidade não consta do caput (é princípio implícito), e falta a impessoalidade na lista do item.',
     'CF/88, art. 37, caput'),
    ('Direito Administrativo', 'Nepotismo', AMBOS, ED,
     'Segundo a Súmula Vinculante nº 13 do STF, a nomeação de cônjuge ou parente até o terceiro grau da autoridade nomeante, para cargo em comissão ou de confiança na mesma pessoa jurídica, viola a Constituição Federal.', 'C',
     'A Súmula Vinculante 13 veda o nepotismo, inclusive o cruzado, na Administração direta e indireta de qualquer dos Poderes, com base nos princípios do art. 37 da Constituição.',
     'STF, Súmula Vinculante nº 13'),
    ('Licitações e Contratos', 'Modalidades da Lei 14.133/2021', [AT], ED,
     'A Lei nº 14.133/2021 não prevê as modalidades de licitação convite e tomada de preços.', 'C',
     'O art. 28 da Lei nº 14.133/2021 prevê cinco modalidades: pregão, concorrência, concurso, leilão e diálogo competitivo. Convite e tomada de preços eram da Lei nº 8.666/1993.',
     'Lei nº 14.133/2021, art. 28'),
    ('Licitações e Contratos', 'Diálogo competitivo', [AT], ED,
     'Na Lei nº 14.133/2021, o diálogo competitivo é a modalidade destinada exclusivamente à alienação de bens imóveis da Administração.', 'E',
     'O diálogo competitivo (art. 32) é modalidade para contratar objetos que envolvam inovação, soluções técnicas complexas ou necessidade de adaptar soluções do mercado. A alienação de bens é objeto do leilão.',
     'Lei nº 14.133/2021, arts. 28 e 32'),
    ('Licitações e Contratos', 'Pregão', [AT], ED,
     'Segundo a Lei nº 14.133/2021, o pregão é a modalidade obrigatória para a aquisição de bens e serviços comuns.', 'C',
     'A lei define o pregão como a modalidade de licitação obrigatória para aquisição de bens e serviços comuns (art. 6º, XLI). Bens e serviços comuns são aqueles com padrões de desempenho e qualidade definidos objetivamente no edital.',
     'Lei nº 14.133/2021, art. 6º, XLI'),
    ('Proteção de Dados (LGPD)', 'Conceitos', [AT], COR,
     'Para a LGPD, dado pessoal é a informação relacionada a pessoa natural identificada ou identificável.', 'C',
     'É a definição do art. 5º, I, da Lei nº 13.709/2018. Dados de pessoas jurídicas não são dados pessoais para a LGPD.',
     'Lei nº 13.709/2018, art. 5º, I'),
    ('Proteção de Dados (LGPD)', 'Dado pessoal sensível', [AT], COR,
     'Para a LGPD, dado pessoal sensível é qualquer dado pessoal de pessoa natural, independentemente de seu conteúdo.', 'E',
     'Dado pessoal sensível é o dado sobre origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico, quando vinculado a uma pessoa natural. Não é todo dado pessoal.',
     'Lei nº 13.709/2018, art. 5º, II'),
    ('Proteção de Dados (LGPD)', 'Encarregado', [AT], COR,
     'O controlador deverá indicar encarregado pelo tratamento de dados pessoais, e a identidade e as informações de contato do encarregado devem ser divulgadas publicamente, de preferência no sítio eletrônico do controlador.', 'C',
     'O art. 41 da LGPD exige a indicação do encarregado e a divulgação pública de sua identidade e contato.',
     'Lei nº 13.709/2018, art. 41, caput e §1º'),
    ('Proteção de Dados (LGPD)', 'Sanções administrativas', [AT], COR,
     'Entre as sanções administrativas previstas na LGPD está a multa simples de até 2% do faturamento da pessoa jurídica de direito privado no último exercício, limitada, no total, a R$ 50.000.000,00 por infração.', 'C',
     'É a multa do art. 52, II, da LGPD, aplicada pela ANPD. O limite é de R$ 50 milhões por infração.',
     'Lei nº 13.709/2018, art. 52, II'),
    ('Proteção de Dados (LGPD)', 'Tratamento pelo poder público', [AT], COR,
     'A LGPD proíbe qualquer tratamento de dados pessoais pelo poder público sem o consentimento do titular.', 'E',
     'O tratamento de dados pessoais pela administração pública pode ocorrer, sem consentimento, para a execução de políticas públicas previstas em leis e regulamentos (art. 7º, III) e para o cumprimento de suas atribuições legais (art. 23), com observância de finalidade pública e transparência.',
     'Lei nº 13.709/2018, arts. 7º, III, e 23'),
    ('Igualdade Racial e de Gênero', 'Lei Maria da Penha', AMBOS, ED,
     'A Lei Maria da Penha considera formas de violência doméstica e familiar contra a mulher a violência física, psicológica, sexual, patrimonial e moral.', 'C',
     'O art. 7º da Lei nº 11.340/2006 lista essas cinco formas de violência doméstica e familiar contra a mulher.',
     'Lei nº 11.340/2006, art. 7º'),
    ('Igualdade Racial e de Gênero', 'Estatuto da Igualdade Racial', AMBOS, ED,
     'O Estatuto da Igualdade Racial destina-se a garantir a efetivação da igualdade de oportunidades exclusivamente à população indígena.', 'E',
     'O art. 1º da Lei nº 12.288/2010 diz que o Estatuto se destina a garantir à população negra a efetivação da igualdade de oportunidades, a defesa dos direitos étnicos individuais, coletivos e difusos e o combate à discriminação e às demais formas de intolerância étnica.',
     'Lei nº 12.288/2010, art. 1º'),
    ('Redes de Computadores', 'TCP', [AT], ED,
     'O estabelecimento de uma conexão TCP utiliza o handshake de três vias (three-way handshake), composto pelos segmentos SYN, SYN+ACK e ACK.', 'C',
     'O TCP é orientado à conexão e a estabelece com a troca de três segmentos: o cliente envia SYN, o servidor responde SYN+ACK e o cliente confirma com ACK.',
     'RFC 9293 (TCP), seção 3.5'),
    ('Redes de Computadores', 'UDP', [AT], ED,
     'O protocolo UDP é orientado à conexão e garante a entrega ordenada e sem perdas dos datagramas.', 'E',
     'O UDP não é orientado à conexão e não oferece garantia de entrega, ordenação nem retransmissão. Essas garantias são do TCP.',
     'RFC 768 (UDP)'),
    ('Segurança da Informação', 'Funções hash', [AT], ED,
     'Uma função hash criptográfica produz um resumo (digest) de tamanho fixo, independentemente do tamanho da mensagem de entrada.', 'C',
     'Uma das propriedades das funções hash é gerar saída de tamanho fixo (por exemplo, 256 bits no SHA-256) a partir de entradas de qualquer tamanho. O resumo é usado para verificar integridade.',
     'FIPS PUB 180-4 (SHS)'),
    ('Segurança da Informação', 'Assinatura digital', [AT], ED,
     'Na assinatura digital baseada em criptografia assimétrica, a mensagem (ou seu resumo) é assinada com a chave pública do signatário, e a verificação é feita com a chave privada.', 'E',
     'É o inverso: o signatário assina com sua chave privada, que só ele possui, e qualquer pessoa verifica a assinatura com a chave pública correspondente. Isso garante autoria e não repúdio.',
     'Padrão de criptografia de chave pública (ex.: RFC 8017, PKCS #1)'),
    ('Banco de Dados', 'SQL: WHERE e HAVING', AMBOS, ED,
     'Em SQL, a cláusula WHERE filtra as linhas antes do agrupamento, enquanto a cláusula HAVING filtra os grupos formados por GROUP BY.', 'C',
     'WHERE atua sobre as linhas da tabela antes do agrupamento e não aceita funções agregadas. HAVING atua depois do GROUP BY e permite condições sobre agregações, como SUM ou COUNT.',
     'ISO/IEC 9075 (SQL)'),
    ('Redes de Computadores', 'IPv6', [AT], ED,
     'O IPv6 utiliza endereços de 32 bits, o que o torna equivalente ao IPv4 em capacidade de endereçamento.', 'E',
     'Os endereços IPv6 têm 128 bits, contra 32 bits do IPv4, o que amplia enormemente o espaço de endereçamento.',
     'RFC 8200 (IPv6)'),
    ('Gerenciamento de Projetos', 'Scrum: Sprint', [AT], ED,
     'De acordo com o Scrum Guide de 2020, a Sprint tem duração de no máximo um mês.', 'C',
     'O Scrum Guide 2020 define as Sprints como eventos de duração fixa de um mês ou menos, para manter a consistência e permitir inspeção e adaptação frequentes.',
     'Scrum Guide 2020'),
    ('Governança de TI', 'ITIL 4: dimensões', [AT], ED,
     'A ITIL 4 organiza a abordagem holística do gerenciamento de serviços em quatro dimensões: organizações e pessoas; informação e tecnologia; parceiros e fornecedores; e fluxos de valor e processos.', 'C',
     'São as quatro dimensões do gerenciamento de serviços da ITIL 4, que devem ser consideradas para cada serviço e cada prática.',
     'ITIL 4 Foundation'),
]

# Rótulos de assunto (antigas) que estão no edital 2022 e valem para os dois cargos.
GERAIS_ED = ('Direito Tributário', 'Legislação Tributária', 'Direito Constitucional', 'Direito Administrativo',
             'Contabilidade Geral', 'Estatística', 'Língua Portuguesa', 'Raciocínio', 'Igualdade')
LEGADO_OCULTO = {
    'q_gen_15': 'DIFAL não incide em aquisição para revenda; a premissa do enunciado (varejista adquirente) torna o item inadequado.',
}
BANCAS = ('FCC', 'FGV', 'Cebraspe', 'CESPE')


def rotulo_fonte(src):
    if '(Adaptada)' in src or '(Simulada)' in src or 'Adaptada' in src or 'Simulada' in src:
        estilo = next((b for b in BANCAS if b in src), 'banca')
        return 'Inédita - elaborada por YLuna85 LABs (estilo %s)' % estilo
    return src


def classificar_legado(q):
    subj = q.get('subject', '')
    if q.get('category') == 'ti':
        return [AT], ED
    if any(k in subj for k in GERAIS_ED):
        return list(AMBOS), ED
    return [AT], COR


def main():
    dry = '--dry-run' in sys.argv
    qs = json.load(open(ARQ, encoding='utf-8'))

    # 1. troca variantes-molde pelas novas
    qs = [q for q in qs if not q['id'].startswith('sefaz_ce_2021_var_item_') and not q['id'].startswith('ylabs_')]
    for i, (subj, top, cargos, esc, enun, gab, exp, fund) in enumerate(NOVAS, 1):
        qs.append({
            'id': 'ylabs_%03d' % i,
            'category': 'general' if AG in cargos else 'ti',
            'subject': subj, 'topic': top,
            'source': 'Elaborada por YLuna85 LABs (fundamento: %s)' % fund,
            'format': 'certo_errado',
            'question': enun,
            'options': dict(CE), 'correct': gab,
            'explanation': 'Gabarito: %s. %s Fundamento: %s.' % ('CERTO' if gab == 'C' else 'ERRADO', exp, fund),
            'fundamento': fund, 'origem': 'elaborada',
            'escopo': esc, 'cargos': list(cargos),
        })

    # 2. antigas
    n_leg = 0
    for q in qs:
        if 'cargos' in q:
            continue
        cargos, esc = classificar_legado(q)
        q['cargos'], q['escopo'] = cargos, esc
        q['source'] = rotulo_fonte(q.get('source', ''))
        q['revisao'] = 'legado_nao_auditado'
        if q['id'] in LEGADO_OCULTO:
            q['disponivel'] = False
            q['motivo_indisponivel'] = LEGADO_OCULTO[q['id']]
        n_leg += 1
    print('novas:', len(NOVAS), '| antigas classificadas:', n_leg, '| total:', len(qs))
    if not dry:
        json.dump(qs, open(ARQ, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print('questions.json gravado.')


if __name__ == '__main__':
    sys.exit(main())
