"""Aplica a auditoria da Apostila de Segurança da Informação (Fase 1) e acrescenta as seções que faltavam
do programa SEFAZ-CE 2026 (B02). Idempotente: se a seção 11 já existir, não repete.
Relatório: dados/auditoria_apostilas/01_seguranca.md
Uso (na pasta do app): python dados/auditoria_apostilas/aplicar_01_seguranca.py
"""
import json
import os
import sys

APP = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARQ = os.path.join(APP, 'apostilas_conteudo.json')
dados = json.load(open(ARQ, encoding='utf-8'))
ap = next(a for a in dados if 'Seguran' in a['filename'])
S = ap['sections']


def trocar(txt, velho, novo):
    assert velho in txt, 'trecho não encontrado: ' + velho[:60]
    return txt.replace(velho, novo)


def bullet(sec, titulo_inicio):
    return next(b for b in sec['bullets'] if b[0].strip().startswith(titulo_inicio))


if any(s['title'].startswith('11.') for s in S):
    print('Apostila de Segurança já atualizada; nada a fazer.')
    sys.exit(0)

# ---- Correções nas seções existentes ----
b = bullet(S[0], 'Gestão de Incidentes')
b[0] = 'Gestão de Incidentes de Segurança (modelos de referência)'
b[1] = ('Dois ciclos muito cobrados: (1) NIST SP 800-61 Rev. 2: Preparação; Detecção e Análise; Contenção, Erradicação e '
        'Recuperação; Atividade Pós-Incidente. (2) Modelo de seis etapas do SANS: Preparação, Identificação, Contenção, '
        'Erradicação, Recuperação e Lições Aprendidas. Veja a seção 13.')

b = bullet(S[1], 'Algoritmos Simétricos')
b[1] = trocar(b[1], '3DES (Triple DES - aplica DES três vezes com chaves independentes, seguro porém lento)',
              '3DES (Triple DES/TDEA - aplica DES três vezes; é lento e obsoleto: o NIST, na SP 800-131A, o depreciou e o proíbe para cifração a partir de 2024)')

b = bullet(S[2], 'Funções Hash')
b[1] = trocar(b[1], '2. Efeito Avalanche (pequena alteração de 1 bit na entrada altera drasticamente mais de 50% do hash resultante)',
              '2. Efeito Avalanche (a alteração de um único bit na entrada muda, em média, cerca de metade dos bits do hash)')
b = bullet(S[2], 'Famílias de Algoritmos Hash')
b[1] = trocar(b[1], 'SHA-2 (SHA-256 e SHA-512 - padrão robusto e seguro adotado na NF-e e certificados digitais)',
              'SHA-2 (SHA-256 e SHA-512 - padrão robusto, amplamente usado em certificados digitais e assinaturas)')

S[3]['content'] = ('A Assinatura Digital é um mecanismo criptográfico que assegura a Autenticidade, a Integridade e o Não Repúdio de '
                   'documentos eletrônicos. No Brasil, a MP nº 2.200-2/2001 instituiu a ICP-Brasil e prevê (art. 10, §1º) que as '
                   'declarações constantes de documentos eletrônicos produzidos com certificado ICP-Brasil presumem-se verdadeiras em '
                   'relação aos signatários. A Lei nº 14.063/2020 classifica as assinaturas eletrônicas em simples, avançada e '
                   'qualificada; a qualificada é a que usa certificado digital ICP-Brasil.')
b = bullet(S[3], 'Tipos de Certificados')
b[1] = ('Tipo A (assinatura digital) e Tipo S (sigilo). Padrão A1: chave gerada por software e armazenada no computador, validade '
        'máxima de 1 ano. Padrão A3: chave gerada e armazenada em hardware criptográfico (cartão inteligente ou token), validade de até '
        '5 anos, conforme o DOC-ICP-04.')
b = bullet(S[3], 'Aplicação em Documentos Fiscais')
b[1] = ('A Nota Fiscal Eletrônica (modelo 55) é assinada pelo emitente no padrão XML Digital Signature (XML-DSig), com certificado '
        'digital ICP-Brasil (e-CNPJ), antes da autorização de uso pela SEFAZ. Segundo o Manual de Orientação do Contribuinte da NF-e, o '
        'padrão de assinatura usa RSA com resumo SHA-1 (conferir a versão vigente do manual).')

b = bullet(S[5], 'Protocolo TLS 1.3')
b[1] = trocar(b[1], 'sigilo progressivo perfeito (Perfect Forward Secrecy - PFS com ECDHE)',
              'sigilo progressivo perfeito (Perfect Forward Secrecy - PFS), com troca de chaves efêmera (ECDHE ou DHE)')

# Seção 8: OWASP
S[7]['content'] = ('A Open Web Application Security Project (OWASP) é a referência mundial de segurança de software e publica '
                   'periodicamente o Top 10 dos riscos mais críticos em aplicações web. A versão vigente é o OWASP Top 10:2025; a '
                   'versão de 2021 ainda aparece em provas e materiais e está listada para comparação.')
S[7]['bullets'][0] = [
    'OWASP Top 10:2025 (versão vigente)',
    'A01 Broken Access Control (controle de acesso quebrado; o SSRF foi incorporado a esta categoria); A02 Security Misconfiguration; '
    'A03 Software Supply Chain Failures (nova; amplia o antigo A06:2021, componentes vulneráveis e desatualizados); A04 Cryptographic '
    'Failures; A05 Injection; A06 Insecure Design; A07 Authentication Failures; A08 Software or Data Integrity Failures; A09 Security '
    'Logging and Alerting Failures; A10 Mishandling of Exceptional Conditions (nova).']
S[7]['bullets'].insert(1, [
    'OWASP Top 10:2021 (versão anterior, ainda cobrada)',
    'A01 Broken Access Control; A02 Cryptographic Failures; A03 Injection; A04 Insecure Design; A05 Security Misconfiguration; A06 '
    'Vulnerable and Outdated Components; A07 Identification and Authentication Failures; A08 Software and Data Integrity Failures; A09 '
    'Security Logging and Monitoring Failures; A10 Server-Side Request Forgery (SSRF).'])
b = bullet(S[7], 'Ataques de Injeção SQL')
b[1] = ('Ocorre quando dados fornecidos pelo usuário são concatenados diretamente na consulta SQL sem tratamento. Segundo o OWASP SQL '
        'Injection Prevention Cheat Sheet, a defesa primária são as consultas parametrizadas (prepared statements). Alternativas: '
        'procedimentos armazenados construídos com segurança, validação por lista de permissão (allow-list) e, como último recurso, '
        'escape de caracteres. Usar ORMs ajuda, mas não dispensa cuidado com consultas dinâmicas.')
S[7]['tip'] = ['A Defesa Primária contra SQL Injection',
               'A defesa primária recomendada pela OWASP é a consulta parametrizada (prepared statements): os dados nunca são '
               'interpretados como código SQL. Filtros de caracteres e substituição de aspas, isoladamente, são considerados '
               'insuficientes.']

# Seção 10: pegadinhas
S[9]['title'] = '10. Armadilhas Conceituais Recorrentes em Segurança da Informação'
S[9]['content'] = ('Pontos conceituais que costumam gerar erro em questões sobre Segurança da Informação, Criptografia e LGPD. '
                   'Servem de revisão rápida; a base de cada ponto está nas seções anteriores.')
for i, bl in enumerate(S[9]['bullets']):
    if bl[0].startswith('Pegadinha 6'):
        S[9]['bullets'][i] = ['Pegadinha 6: Consulta Parametrizada é a Defesa Primária contra SQL Injection',
                              'A OWASP recomenda como defesa primária as consultas parametrizadas. Filtrar caracteres ou trocar aspas '
                              'não é defesa suficiente.']
    if bl[0].startswith('Pegadinha 9'):
        S[9]['bullets'][i] = ['Pegadinha 9: Dado Anonimizado NÃO é Dado Pessoal (Salvo Reversão)',
                              'Se a anonimização é irreversível por meios técnicos razoáveis, a LGPD deixa de se aplicar ao dado. '
                              'Segundo o art. 12, o dado volta a ser tratado como pessoal se o processo puder ser revertido com '
                              'esforços próprios ou com esforços razoáveis.']

# ---- Seções novas (programa SEFAZ-CE 2026, B02) ----
S.append({
    'title': '11. Gestão de Riscos: ISO 31000:2018 e ISO/IEC 27005',
    'content': ('A gestão de riscos organiza como a instituição identifica, avalia e trata incertezas que afetam seus objetivos. A '
                'ISO 31000:2018 é a norma genérica de gestão de riscos, e a ISO/IEC 27005 aplica essa lógica aos riscos de segurança '
                'da informação, dando suporte à implementação de um SGSI conforme a ISO/IEC 27001.'),
    'bullets': [
        ['ISO 31000:2018: três componentes',
         'Princípios (oito: integrada, estruturada e abrangente, personalizada, inclusiva, dinâmica, melhor informação disponível, '
         'fatores humanos e culturais, melhoria contínua), Estrutura (framework) e Processo.'],
        ['Processo de gestão de riscos (ISO 31000:2018)',
         'Escopo, contexto e critérios; avaliação de riscos (identificação, análise e avaliação); tratamento de riscos. '
         'Comunicação e consulta, e monitoramento e análise crítica, ocorrem ao longo de todo o processo, além do registro e relato.'],
        ['Opções de tratamento de riscos (visão da ISO/IEC 27005)',
         'Modificação (mitigar, reduzindo probabilidade ou impacto com controles), retenção (aceitar), evitação (eliminar a atividade '
         'que gera o risco) e compartilhamento (transferir, por exemplo com seguro ou terceirização). Risco residual é o que resta '
         'após o tratamento.'],
        ['Cálculo e critérios',
         'Nível de risco é a combinação de probabilidade e impacto (consequência), avaliado de forma qualitativa ou quantitativa e '
         'comparado com os critérios de aceitação da organização.'],
    ],
    'tip': ['Alerta de Prova - Norma Certo, Guia Certo',
            'A ISO/IEC 27001 exige que a organização defina e aplique um processo de avaliação e tratamento de riscos de segurança '
            'da informação; a ISO/IEC 27005 é o guia de como fazer essa gestão de riscos. A ISO 31000 não é certificável.']})
S.append({
    'title': '12. Continuidade de Negócios: BIA, ISO 22301, RPO e RTO',
    'content': ('Continuidade de negócios é a capacidade de manter ou retomar atividades críticas em nível aceitável após uma '
                'interrupção. A ISO 22301 (ABNT NBR ISO 22301:2020) especifica os requisitos de um Sistema de Gestão de Continuidade '
                'de Negócios (SGCN) e admite certificação.'),
    'bullets': [
        ['BIA (Análise de Impacto nos Negócios)',
         'Identifica as atividades críticas, os impactos da interrupção ao longo do tempo, as dependências (pessoas, sistemas, '
         'fornecedores) e as prioridades de recuperação. É a base para definir RTO, RPO e o tempo máximo tolerável de interrupção.'],
        ['RTO, RPO e MTPD',
         'RTO (Recovery Time Objective): tempo alvo para restabelecer o serviço. RPO (Recovery Point Objective): ponto no tempo até '
         'o qual os dados devem ser recuperáveis, ou seja, a perda máxima de dados aceitável (medida em tempo). MTPD (Maximum '
         'Tolerable Period of Disruption): tempo máximo de interrupção tolerável; o RTO deve ser menor que o MTPD.'],
        ['PCN e DRP',
         'O Plano de Continuidade de Negócios cobre a manutenção das atividades críticas; o Plano de Recuperação de Desastres (DRP) '
         'trata da recuperação da infraestrutura de TI e dos sistemas.'],
        ['Sites alternativos',
         'Hot site: ambiente pronto e atualizado, com retomada quase imediata. Warm site: parcialmente equipado, exige carga de '
         'dados e configuração. Cold site: espaço e infraestrutura básica, com retomada mais lenta e de menor custo.'],
        ['Regra 3-2-1 de backup',
         'Manter três cópias dos dados, em duas mídias diferentes, com uma cópia fora do local (offsite).'],
    ],
    'tip': ['RPO Fala de Dados, RTO Fala de Tempo de Retomada',
            'RPO define quanto dado se aceita perder (define a frequência de backup ou replicação). RTO define em quanto tempo o '
            'serviço precisa voltar. Replicação síncrona tende a RPO próximo de zero; backups diários implicam RPO de até um dia.']})
S.append({
    'title': '13. Gestão de Incidentes: NIST SP 800-61 e ISO/IEC 27035',
    'content': ('Evento de segurança é uma ocorrência que indica possível violação da política ou falha de controles. Incidente de '
                'segurança é um ou mais eventos identificados que podem comprometer ativos ou operações. Nem todo evento é incidente.'),
    'bullets': [
        ['NIST SP 800-61 Rev. 2 (Computer Security Incident Handling Guide)',
         'Quatro fases: (1) Preparação; (2) Detecção e Análise; (3) Contenção, Erradicação e Recuperação; (4) Atividade Pós-Incidente '
         '(lições aprendidas). A Rev. 3, de 2025, reorganiza o guia em torno do NIST CSF 2.0; o edital do CE 2026 cita a Rev. 2.'],
        ['ISO/IEC 27035-1:2023',
         'Princípios e processo de gestão de incidentes de segurança da informação, em cinco fases: preparar, detectar e relatar, '
         'avaliar e decidir, responder e aprender com as lições.'],
        ['Modelo SANS (seis etapas)',
         'Preparação, Identificação, Contenção, Erradicação, Recuperação e Lições Aprendidas.'],
        ['Contenção antes da erradicação',
         'Conter isola o problema e limita o dano (por exemplo, isolar o host da rede) antes de eliminar a causa e restaurar o '
         'serviço. Preservar evidências é parte do processo.'],
    ],
    'tip': ['Fases Diferentes Conforme o Modelo',
            'O NIST agrupa contenção, erradicação e recuperação em uma única fase, enquanto o SANS as separa. Leia o enunciado para '
            'saber qual modelo a questão adota.']})
S.append({
    'title': '14. Defesa em Profundidade e Zero Trust',
    'content': ('Defesa em profundidade é a estratégia de empregar várias camadas de controles independentes (físicos, de perímetro, '
                'de rede, de host, de aplicação, de dados e de pessoas e processos), de modo que a falha de um controle não exponha o '
                'ativo. Zero Trust (confiança zero) parte da premissa de que nenhuma rede, usuário ou dispositivo é confiável por '
                'padrão: "nunca confie, sempre verifique".'),
    'bullets': [
        ['Zero Trust segundo a NIST SP 800-207',
         'O modelo desloca a defesa do perímetro de rede para os recursos. Nenhuma confiança é concedida apenas pela localização na '
         'rede; cada acesso é autenticado e autorizado antes de ser permitido.'],
        ['Princípios (tenets) da NIST SP 800-207',
         'Todas as fontes de dados e serviços são recursos; toda comunicação é protegida, independentemente da localização na rede; '
         'o acesso é concedido por sessão; o acesso é decidido por política dinâmica (identidade, estado do dispositivo e '
         'comportamento); a integridade e a postura de segurança dos ativos são monitoradas; autenticação e autorização são '
         'dinâmicas e rigorosamente aplicadas antes do acesso; o máximo de informação sobre o estado dos ativos é coletado para '
         'melhorar a postura de segurança.'],
        ['Componentes lógicos',
         'Policy Engine (PE, decide a concessão), Policy Administrator (PA, estabelece ou encerra o caminho de comunicação) e Policy '
         'Enforcement Point (PEP, aplica a decisão). PE e PA formam o Policy Decision Point (PDP).'],
        ['Microssegmentação',
         'Divide a rede em segmentos pequenos com políticas próprias, limitando a movimentação lateral de um invasor. É uma técnica '
         'comum de implantação de Zero Trust.'],
    ],
    'tip': ['Zero Trust Não é um Produto',
            'Zero Trust é uma abordagem de arquitetura e de políticas, e não um produto único. Estar na rede interna não concede '
            'confiança. VPN, por si só, não implementa Zero Trust.']})
S.append({
    'title': '15. Operações de Segurança: SIEM, SOC, EDR, WAF, NAT e Vulnerabilidades',
    'content': ('Ferramentas e práticas que sustentam o monitoramento contínuo e a resposta a ameaças no dia a dia da segurança da '
                'informação.'),
    'bullets': [
        ['SIEM e SOC',
         'SIEM (Security Information and Event Management) coleta, normaliza e correlaciona logs e eventos de várias fontes e gera '
         'alertas. SOC (Security Operations Center) é a equipe, os processos e as tecnologias que monitoram, analisam e respondem a '
         'incidentes. O SIEM é ferramenta; o SOC é a função que a utiliza.'],
        ['EDR',
         'Endpoint Detection and Response: coleta telemetria dos endpoints, detecta comportamento suspeito e permite investigar e '
         'responder (por exemplo, isolar a máquina). Vai além do antivírus baseado só em assinaturas.'],
        ['WAF',
         'Web Application Firewall: filtra e monitora o tráfego HTTP/HTTPS na camada de aplicação, ajudando a bloquear ataques como '
         'injeção e XSS. Complementa, mas não substitui, o desenvolvimento seguro.'],
        ['NAT',
         'Network Address Translation: traduz endereços IP entre redes, muito usado para compartilhar endereços públicos. Não é, por '
         'si só, um controle de segurança.'],
        ['CVE e CVSS',
         'CVE é o identificador público de uma vulnerabilidade conhecida. CVSS é o sistema de pontuação de severidade de 0,0 a 10,0: '
         'baixa (0,1 a 3,9), média (4,0 a 6,9), alta (7,0 a 8,9) e crítica (9,0 a 10,0). CVSS mede a severidade técnica, não o risco '
         'para a organização.'],
        ['Ciclo de gestão de vulnerabilidades',
         'Descobrir ativos, varrer vulnerabilidades, priorizar (severidade, exposição e exploração ativa), remediar (correção ou '
         'mitigação) e verificar. Varredura de vulnerabilidades identifica fragilidades; teste de intrusão (pentest) tenta explorá-las.'],
    ],
    'tip': ['Ferramenta Detecta, Processo Resolve',
            'SIEM e EDR detectam e correlacionam; a resposta depende de processo e pessoas (SOC e plano de resposta a incidentes). '
            'Prioridade de correção não é só CVSS: considere exposição e exploração ativa.']})
S.append({
    'title': '16. Segurança em Nuvem (ISO/IEC 27017) e IA em Segurança',
    'content': ('A ABNT NBR ISO/IEC 27017:2016 é um código de práticas com controles de segurança da informação para serviços em '
                'nuvem, baseado na ISO/IEC 27002. A inteligência artificial atua tanto como ferramenta de defesa quanto como alvo e '
                'meio de ataque.'),
    'bullets': [
        ['ISO/IEC 27017',
         'Complementa a ISO/IEC 27002 com orientações específicas para provedores e clientes de nuvem, incluindo a divisão de papéis '
         'e responsabilidades entre eles, a segregação de ambientes virtuais e a gestão de ativos do cliente na nuvem.'],
        ['Responsabilidade compartilhada',
         'O provedor responde pela segurança da nuvem (infraestrutura); o cliente responde pela segurança na nuvem (dados, identidades '
         'e configurações). A fatia do cliente cresce de SaaS para PaaS e para IaaS.'],
        ['IA como alvo e meio de ataque',
         'Ataques a sistemas de IA: injeção de prompt (prompt injection), envenenamento de dados de treino, exemplos adversariais e '
         'extração ou inversão de modelo. IA como ferramenta de ataque: phishing mais convincente e conteúdo sintético (deepfakes).'],
        ['IA como ferramenta de defesa',
         'Detecção de anomalias e de malware por aprendizado de máquina, priorização de alertas e apoio à triagem em SOC. Exige '
         'governança, pois modelos podem errar (falsos positivos e falsos negativos) e ser alvo de manipulação.'],
        ['Referências de IA (conferir na fonte)',
         'OWASP Top 10 for LLM Applications; NIST AI Risk Management Framework 1.0 (funções Governar, Mapear, Medir e Gerenciar); '
         'NIST AI 100-2, taxonomia de ataques de aprendizado de máquina adversarial.'],
    ],
    'tip': ['Nuvem: Quem é Responsável pelo Quê',
            'Contratar nuvem não transfere a responsabilidade pelos dados e pelo acesso. Identidades, configuração e classificação de '
            'dados continuam sendo do cliente em qualquer modelo de serviço.']})
S.append({
    'title': '17. Referências e Conferência',
    'content': ('Conferência realizada em 21/09/2026. Fontes consultadas ou citadas nesta apostila; os itens indicados como conferir '
                'dependem de texto pago (normas ISO/ABNT) ou de versão vigente.'),
    'bullets': [
        ['Normas e guias',
         'ABNT NBR ISO/IEC 27001:2022; 27002:2022; 27005:2023; 27017:2016; 27035-1:2023; ABNT NBR ISO 22301:2020; ISO 31000:2018; '
         'NIST SP 800-61 Rev. 2; NIST SP 800-207; NIST SP 800-131A; OWASP Top 10:2025 (owasp.org/Top10/2025).'],
        ['Legislação e ICP-Brasil',
         'Lei nº 13.709/2018 (LGPD); MP nº 2.200-2/2001; Lei nº 14.063/2020; DOC-ICP-04 (prazos de validade: A1 de 1 ano, A3 de até '
         '5 anos).'],
        ['Corrigido nesta revisão',
         '3DES não é mais seguro; efeito avalanche (cerca de metade dos bits); NF-e usa RSA com SHA-1; assinatura ICP-Brasil não é '
         'descrita em lei como equiparada a firma reconhecida; SQL Injection: consulta parametrizada é defesa primária, não única; '
         'OWASP Top 10:2025 incluída.'],
        ['A conferir',
         'Rótulos e quantidades de controles das normas ISO citadas seguem o conteúdo público conhecido; verificar no texto oficial '
         'da ABNT ao estudar. Possível mudança de nomenclatura de certificados ICP-Brasil anunciada em 2025: consultar o ITI.'],
    ],
    'tip': ['Regra de Conteúdo', 'Este material não afirma nada sem fonte. Se encontrar divergência com a norma vigente, a norma prevalece.']})

ap['subtitle'] = ('ISO 27001/27002, Riscos (31000/27005), Continuidade, Incidentes, Zero Trust, Criptografia, ICP-Brasil, Redes, '
                  'Malwares, OWASP Top 10, Nuvem e LGPD')
json.dump(dados, open(ARQ, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('Segurança atualizada: %d seções.' % len(S))
