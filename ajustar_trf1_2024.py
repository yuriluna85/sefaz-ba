"""Ajusta as 80 questões do TRF1 2024 (FGV) no questions.json.

- Analista Judiciário, Suporte em TI (ids q_trf1_fgv_ana_41..80): gabarito conferido 40/40 com o
  gabarito oficial preliminar da FGV (PDF em Concurso SEFAZ/). Recebe classificação, escopo/cargos
  e explicações verificáveis.
- Técnico Judiciário, TI (ids q_trf1_fgv_tec_41..80): o banco divergia do gabarito oficial em 28 de 40
  itens (ex.: item 41, cache de 64 KB com blocos de 64 B e 2 vias = 512 conjuntos, 9 bits) e a FGV
  retificou o gabarito definitivo desse cargo. Ficam fora dos simulados até haver gabarito
  verificado. O campo correct recebe o gabarito preliminar, apenas como referência.
- Limpa cortes de palavra do OCR usando vocabulário dos textos limpos.

Uso: python ajustar_trf1_2024.py [--dry-run]
"""
import collections
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
ARQ = os.path.join(BASE, 'questions.json')

# gabarito oficial PRELIMINAR da FGV, Técnico Judiciário TI, itens 41-80 (Tipo 1)
GAB_TEC_PRELIM = dict(zip(range(41, 81), 'ABDBAEBEDCBBCBDEACDA' + 'BCAAAEEDCDABCBECCCCB'))

AT, AG = 'auditor_ti', 'agente'
ED, COR, FORA = 'edital_ba_2022', 'correlato', 'fora'

# n -> (assunto, tópico, escopo, cargos, explicação)
ANA = {
    41: ('Redes de Computadores', 'Enquadramento e código de linha', ED, [AT],
         'O enquadramento pode usar violações de código da camada física: sinais que não ocorrem nos dados regulares (como símbolos especiais de início e fim de quadro do 4B/5B) delimitam o quadro sem adicionar bits extras aos dados.'),
    42: ('Redes de Computadores', 'Ethernet 10 Gbps', ED, [AT],
         'Para 30 km a 10 Gbps é necessário fibra monomodo de longo alcance: 10GBase-ER alcança até 40 km. 10GBase-LR chega a 10 km, 10GBase-SR a poucas centenas de metros em fibra multimodo, e 10GBase-T e 10GBase-CX4 são de cobre e curto alcance.'),
    43: ('Redes de Computadores', 'Endereçamento IPv6', ED, [AT],
         'Um endereço IPv6 tem 128 bits, em até 8 grupos hexadecimais. A notação ::192.31.20.46 é sintaticamente válida (formato com IPv4 embutido). Os endereços com W ou G contêm caracteres não hexadecimais, o com 5 grupos e sem "::" está incompleto, e os dois primeiros são IPv4.'),
    44: ('Redes de Computadores', 'Roteamento OSPF', ED, [AT],
         'ECMP (Equal-Cost Multi-Path) é a técnica que distribui o tráfego entre caminhos de mesmo custo, promovendo balanceamento de carga, como faz o OSPF quando encontra dois caminhos de custo igual.'),
    45: ('Redes de Computadores', 'Voz sobre IP e SIP', COR, [AT],
         'No SIP, o método REGISTER informa ao servidor de localização a posição atual do usuário, o que permite localizá-lo e estabelecer a conexão. INVITE inicia sessões e ACK confirma o estabelecimento.'),
    46: ('Redes de Computadores', 'Arquiteturas de firewall', ED, [AT],
         'Na classificação de configurações de firewall, um único firewall entre o roteador interno e o externo caracteriza o bastião único em linha. As demais variações usam dois bastiões ou posição em T (DMZ).'),
    47: ('Banco de Dados', 'NoSQL e modelo BASE', ED, [AT],
         'Bancos NoSQL distribuídos costumam adotar o modelo BASE, com consistência eventual, em vez das propriedades ACID rígidas, para ganhar escalabilidade e disponibilidade na ingestão de grandes volumes.'),
    48: ('Banco de Dados', 'Integridade referencial em SQL', ED, [AT],
         'A cláusula FOREIGN KEY implementa a integridade referencial: impede que uma transação crie ou destrua relacionamentos inconsistentes entre tabelas.'),
    49: ('Banco de Dados', 'Controle de concorrência: 2PL', ED, [AT],
         'No bloqueio em duas fases rigoroso (rigorous 2PL), a transação não libera nenhum bloqueio, exclusivo ou compartilhado, até confirmar (commit) ou abortar. No 2PL estrito (strict), só os bloqueios exclusivos são retidos até o fim.'),
    50: ('Banco de Dados', 'Junção por ordenação e intercalação', ED, [AT],
         'Na junção por ordenação-intercalação (sort-merge join), as relações são ordenadas pelos atributos de junção e cada arquivo é percorrido uma única vez, combinando os registros. Quando as relações não estão ordenadas fisicamente, é necessária ordenação externa.'),
    51: ('Informática', 'Microsoft Word: comparar documentos', ED, [AT, AG],
         'A opção de linha preta legal (Legal Blackline) do recurso Comparar do Word compara dois documentos e mostra apenas o que foi alterado entre eles.'),
    52: ('Sistemas Operacionais e Servidores', 'Servidor Apache Tomcat', COR, [AT],
         'No Apache Tomcat, a porta do conector HTTP é definida no arquivo server.xml (elemento Connector). O padrão é a porta 8080.'),
    53: ('Sistemas Operacionais e Servidores', 'Agendamento com cron (Linux)', ED, [AT],
         'O formato do crontab é: minuto, hora, dia do mês, mês e dia da semana. Todos os dias às 19h10 é "10 19 * * *".'),
    54: ('Virtualização', 'VMware vSphere HA', ED, [AT],
         'No cluster vSphere HA, o monitoramento de VMs e aplicações é configurado no painel Falhas e Respostas (Failures and Responses).'),
    55: ('Computação em Nuvem', 'Características essenciais (NIST SP 800-145)', COR, [AT],
         'Recursos compartilhados entre vários consumidores e atribuídos dinamicamente conforme a demanda caracterizam o pool de recursos (resource pooling), uma das cinco características essenciais da nuvem do NIST.'),
    56: ('Armazenamento de Dados', 'Storage CAS', COR, [AT],
         'No CAS (Content Addressable Storage) o endereço do dado é derivado de seu conteúdo (hash). Conteúdos idênticos geram o mesmo endereço, o que elimina duplicações e garante a integridade.'),
    57: ('Informática', 'Microsoft PowerPoint: modo de exibição do apresentador', ED, [AT, AG],
         'O modo de exibição do apresentador mostra ao orador o slide atual, o próximo, as anotações, o cronômetro e ferramentas como caneta, apontador laser e lupa, sem que a plateia veja essa tela.'),
    58: ('Segurança da Informação', 'Criptografia e pilares da segurança', ED, [AT, AG],
         'Criptografia protege as informações contra acesso indevido (confidencialidade), comprova a autoria (não repúdio), verifica se a informação foi alterada (integridade) e valida usuários (autenticação).'),
    59: ('Segurança da Informação', 'Segurança em redes sem fio', ED, [AT],
         'WEP usa RC4 com chave estática, o que é inseguro. WPA2 usa AES (CCMP), e o WPA original antecedeu o WPA2. A associação descrita no enunciado segue essa evolução dos protocolos.'),
    60: ('Redes de Computadores', 'Proxy reverso e balanceamento', ED, [AT],
         'O equipamento posicionado à frente de servidores web replicados, recebendo as requisições da Internet e repassando-as às réplicas, é um proxy reverso. Ele distribui a carga e melhora a disponibilidade.'),
    61: ('Segurança da Informação', 'Tipos de malware', ED, [AT, AG],
         'Worm é o malware que se propaga enviando cópias de si mesmo automaticamente, sem precisar infectar arquivos hospedeiros. Vírus dependem de hospedeiro, trojans se disfarçam de programas legítimos e backdoors abrem acesso remoto.'),
    62: ('Segurança da Informação', 'ISO/IEC 27002:2013: controle de acesso', ED, [AT],
         'Entre os controles de restrição de acesso à informação da ISO/IEC 27002:2013 (9.4.1) está limitar as informações contidas nas saídas. Registro de tentativas de acesso, troca de senha e avisos gerais pertencem a outros controles.'),
    63: ('Governança de TI', 'PDTIC e PETIC', COR, [AT],
         'O Plano Diretor de TIC (PDTIC) é o instrumento de diagnóstico, planejamento e gestão dos recursos e processos de TIC para um período, situado no nível tático, entre o planejamento estratégico e o operacional.'),
    64: ('Governança de TI', 'Princípios de governança do COBIT 2019', ED, [AT],
         'Entre os princípios do sistema de governança do COBIT 2019, o sistema de governança dinâmico é aquele capaz de considerar os impactos da alteração de um ou mais fatores de desenho. As demais opções descrevem outros princípios.'),
    65: ('Governança de TI', 'Análise SWOT no planejamento de TIC', COR, [AT],
         'No SWOT, forças e fraquezas são internas e controláveis, enquanto oportunidades e ameaças são do ambiente externo e não controláveis. As ameaças são as que podem impedir o alcance das metas e comprometer o crescimento.'),
    66: ('Gerenciamento de Projetos', 'Scrum e incerteza', ED, [AT],
         'No Scrum, a incerteza é tratada com ciclos curtos e iterativos (sprints), que geram incrementos e permitem inspecionar e adaptar o produto com frequência.'),
    67: ('Gerenciamento de Projetos', 'Gerenciamento de riscos', ED, [AT],
         'O planejamento de respostas é revisado até que o risco residual seja compatível com o apetite a risco da organização. Não é necessário zerar todos os riscos nem reduzi-los todos a baixo impacto ou probabilidade.'),
    68: ('Segurança da Informação', 'Vulnerabilidades e ameaças', ED, [AT],
         'Usar rede pública sem proteção é uma vulnerabilidade (fragilidade explorável) que permitiu a ameaça de captura do tráfego. Por isso a exploração é da vulnerabilidade de conexões de rede pública desprotegida.'),
    69: ('Governança de TI', 'ITIL 4: oferta de serviços', ED, [AT],
         'No glossário da ITIL 4, oferta de serviço (service offering) é a descrição formal de um ou mais serviços, projetada para atender às necessidades de um grupo de consumidores-alvo, e pode incluir bens, acesso a recursos e ações de serviço.'),
    70: ('Governança de TI', 'ITIL 4: gerenciamento de relacionamento', ED, [AT],
         'Na ITIL 4, o gerenciamento de relacionamento de serviços consiste nas atividades conjuntas de prestador e consumidor para garantir a cocriação contínua de valor com base na provisão e no consumo de serviços.'),
    71: ('Legislação do Poder Judiciário (TRF1)', 'Contratação de soluções de TIC no Judiciário', FORA, [], None),
    72: ('Legislação do Poder Judiciário (TRF1)', 'ENTIC-JUD', FORA, [], None),
    73: ('Legislação do Poder Judiciário (TRF1)', 'PDPJ-Br', FORA, [], None),
    74: ('Proteção de Dados (LGPD)', 'Consentimento para dados de crianças', COR, [AT],
         'A LGPD (Lei nº 13.709/2018, art. 14, §1º) exige, para tratar dados de crianças, consentimento específico e em destaque dado por pelo menos um dos pais ou pelo responsável legal.'),
    75: ('Legislação do Poder Judiciário (TRF1)', 'PSEC-PJ e PGCC-PJ', FORA, [], None),
    76: ('Legislação do Poder Judiciário (TRF1)', 'PDPJ-Br e computação em nuvem', FORA, [], None),
    77: ('Direito Penal', 'Corrupção passiva (art. 317 do CP)', FORA, [],
         'Solicitar, em razão da função, vantagem indevida configura corrupção passiva (CP, art. 317). A concussão (art. 316) exige que o agente exija a vantagem, e não apenas a solicite.'),
    78: ('Direito Penal', 'Fuga de pessoa presa', FORA, [],
         'A fuga do preso, sem violência ou grave ameaça contra pessoa, não é crime no Código Penal: a autoevasão é fato atípico. O crime de arrebatamento de preso é praticado por terceiros.'),
    79: ('Direito Penal', 'Tráfico de influência (art. 332 do CP)', FORA, [],
         'Solicitar vantagem a pretexto de influir em ato praticado por funcionário público no exercício da função é tráfico de influência (CP, art. 332). A exploração de prestígio (art. 357) refere-se à influência sobre juiz, jurado, membro do MP e outros sujeitos processuais.'),
    80: ('Direito Penal', 'Falso testemunho (art. 342 do CP)', FORA, [],
         'O art. 342 do CP pune quem faz afirmação falsa, nega ou cala a verdade como testemunha, inclusive em inquérito policial. Calar a verdade sobre fatos relevantes configura falso testemunho.'),
}


def vocabulario(qs):
    """Palavras frequentes de textos sem cortes (questões que não são do TRF1, aditadas das provas)."""
    cont = collections.Counter()
    for q in qs:
        if q['id'].startswith('q_trf1'):
            continue
        partes = [q['question'], q.get('explanation', '')] + list(q['options'].values())
        for p in partes:
            cont.update(w.lower() for w in re.findall(r'[A-Za-zÀ-ÿ]+', p))
    return {w for w, c in cont.items() if c >= 2}


PROPRIAS = set('a e o é à ao as os da de do em um na no se ou já há ir ser ter por mas com que foi são seu sua nas nos dos das uns pra lá cá só vê vá dá pé pá dó sê ele ela eu tu nós vós me te lhe'.split())


def colar(txt, vocab):
    toks = txt.split(' ')
    out = []
    i = 0
    while i < len(toks):
        a = toks[i]
        if i + 1 < len(toks):
            b = toks[i + 1]
            ma, mb = re.fullmatch(r'([A-Za-zÀ-ÿ]{1,3})', a), re.fullmatch(r'([A-Za-zÀ-ÿ]+[,.;:]?)', b)
            if ma and mb and a.lower() not in PROPRIAS:
                junto = (a + b).lower().rstrip(',.;:')
                if junto in vocab and b.lower().rstrip(',.;:') not in ('',):
                    out.append(a + b)
                    i += 2
                    continue
        out.append(a)
        i += 1
    return ' '.join(out)


def limpar(txt, vocab):
    if not isinstance(txt, str):
        return txt
    txt = re.sub(r'\b(Lei|Decreto|Resolução) n[oº]?\s?(\d)', lambda m: '%s nº %s' % (m.group(1), m.group(2)), txt)
    txt = re.sub(r'(\w) -(se|lo|la|los|las|lhe|lhes|me|te|nos)\b', r'\1-\2', txt)
    return colar(txt, vocab)


def main():
    dry = '--dry-run' in sys.argv
    qs = json.load(open(ARQ, encoding='utf-8'))
    vocab = vocabulario(qs)
    alterados = 0
    for q in qs:
        m = re.match(r'q_trf1_fgv_(ana|tec)_(\d+)$', q['id'])
        if not m:
            continue
        tipo, n = m.group(1), int(m.group(2))
        q['question'] = limpar(q['question'], vocab)
        q['options'] = {k: limpar(v, vocab) for k, v in q['options'].items()}
        q.pop('option_explanations', None)
        if tipo == 'tec':
            q['correct'] = GAB_TEC_PRELIM[n]
            q['source'] = 'FGV - TRF 1ª Região (2024) - Técnico Judiciário (TI), questão %d' % n
            q['cargos'], q['escopo'] = [], FORA
            q['disponivel'] = False
            q['motivo_indisponivel'] = ('Gabarito não verificado: o banco divergia do gabarito oficial preliminar e a FGV '
                                        'retificou o gabarito definitivo deste cargo.')
            q['explanation'] = 'Item fora dos simulados até que o gabarito definitivo da FGV seja verificado.'
            q['revisao'] = 'gabarito_nao_verificado'
            continue
        subj, top, esc, cargos, exp = ANA[n]
        q['subject'], q['topic'], q['escopo'], q['cargos'] = subj, top, esc, list(cargos)
        q['source'] = 'FGV - TRF 1ª Região (2024) - Analista Judiciário (Suporte em TI), questão %d' % n
        q['category'] = 'general' if AG in cargos else 'ti'
        q['gabarito_oficial_conferido'] = True
        q['gabarito_status'] = 'preliminar'
        if exp:
            q['explanation'] = 'Gabarito oficial da FGV (divulgado como preliminar; conferido com o gabarito do TRF1). %s' % exp
            q.pop('revisao', None)
        else:
            q['explanation'] = 'Gabarito oficial da FGV (divulgado como preliminar; conferido com o gabarito do TRF1). Item de norma específica do Poder Judiciário, fora do escopo da SEFAZ-BA; fundamentação detalhada não incluída.'
            q['revisao'] = 'explicacao_minima'
        alterados += 1
    print('analista ajustadas:', alterados)
    if not dry:
        json.dump(qs, open(ARQ, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print('questions.json gravado.')


if __name__ == '__main__':
    sys.exit(main())
