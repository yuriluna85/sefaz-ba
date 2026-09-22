"""Aplica a auditoria da Apostila de Redes de Computadores e Telecomunicações (Fase 1) e acrescenta as seções do programa
SEFAZ-CE 2026 (B02: redes, arquitetura, endereçamento, administração, SDN, wireless, acesso remoto, comunicação segura) e do
edital SEFAZ-BA 2022 (redes, acesso remoto e wireless, noções de administração e de mobilidade). Idempotente.
Relatório: dados/auditoria_apostilas/09_redes.md
Uso (na pasta do app): python dados/auditoria_apostilas/aplicar_09_redes.py
"""
import json
import os
import sys

APP = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARQ = os.path.join(APP, 'apostilas_conteudo.json')
dados = json.load(open(ARQ, encoding='utf-8'))
ap = next(a for a in dados if 'Redes_Computadores' in a['filename'])
S = ap['sections']

if any(s['title'].startswith('11.') for s in S):
    print('Apostila de Redes já atualizada; nada a fazer.')
    sys.exit(0)


def bul(sec, inicio):
    return next(b for b in sec['bullets'] if b[0].strip().startswith(inicio))


def trocar(txt, velho, novo):
    assert velho in txt, 'trecho não encontrado: ' + velho[:70]
    return txt.replace(velho, novo)


# ---- Seção 1 ----
S[0]['tip'] = ['Alerta de Prova - OSI e TCP/IP',
               'O modelo OSI tem 7 camadas e é um modelo de referência conceitual. A arquitetura TCP/IP é o padrão de fato da Internet, '
               'com 4 camadas (ou 5 na divisão didática). A PDU do enlace é o quadro (frame) e a da rede é o pacote.']

# ---- Seção 2 ----
b = bul(S[1], 'Norma ABNT NBR 14565')
b[0] = 'Normas de cabeamento estruturado (ABNT NBR 14565 e TIA-568)'
b[1] = ('A ABNT NBR 14565 (confira a edição vigente) e a família TIA-568 padronizam o cabeamento estruturado de edifícios comerciais e '
        'data centers. Subsistemas: entrada de facilidades, sala de equipamentos, backbone de campus, backbone de edifício, sala de '
        'telecomunicações, cabeamento horizontal e área de trabalho.')
b = bul(S[1], 'Categorias de Par Trançado')
b[1] += (' Cat 7 (até 600 MHz, definida pela ISO/IEC) e Cat 8 (até 2000 MHz, 25GBASE-T e 40GBASE-T até 30 m, para enlaces curtos de '
         'data center).')
b = bul(S[1], 'Blindagens de Cabo')
b[1] = ('Nomenclatura da ISO/IEC 11801: U/UTP (sem blindagem), F/UTP (fita metálica global), S/UTP (malha global), U/FTP (fita '
        'individual em cada par) e S/FTP (fita por par mais malha global). A blindagem reduz interferência e diafonia, mas exige '
        'aterramento correto.')
b = bul(S[1], 'Fibras Ópticas')
b[1] = ('Monomodo (SMF): núcleo de cerca de 9 micrômetros (8 a 10), um único modo de luz, laser, sem dispersão modal, para longas '
        'distâncias. Multimodo (MMF): núcleo de 50 ou 62,5 micrômetros, vários modos, LED ou VCSEL, para enlaces curtos; o alcance '
        'depende da classe da fibra (OM1 a OM5) e da velocidade. Por exemplo, o 10GBASE-SR alcança cerca de 300 m em OM3 e 400 m em OM4.')
S[1]['tip'][0] = 'Limites Práticos de Cabeamento e Fibras'

# ---- Seção 4 ----
b = bul(S[3], 'Tecnologia MPLS')
b[1] = ('Comutação por rótulos: o roteador de borda (LER) coloca um rótulo e os roteadores do núcleo (LSR) comutam pelo rótulo, sem '
        'consultar a rota IP a cada salto. Cada entrada da pilha de rótulos tem 32 bits (rótulo de 20 bits, classe de tráfego de 3 bits, '
        'bit de fundo de pilha e TTL de 8 bits). Viabiliza VPNs MPLS de camada 2 e de camada 3 e engenharia de tráfego.')

# ---- Seção 6 ----
b = bul(S[5], 'Endereçamento IPv6')
b[1] = ('Endereços de 128 bits, escritos em 8 grupos de até 4 dígitos hexadecimais separados por dois-pontos. Não há broadcast: usa '
        'unicast, multicast e anycast. Reduz a necessidade de NAT e restaura o endereçamento fim a fim, mas NAT não é mecanismo de '
        'segurança e o firewall continua necessário. Suporta autoconfiguração sem estado (SLAAC).')

# ---- Seção 7 ----
b = bul(S[6], 'Padrões da Família IEEE 802.11')
b[1] = ('802.11a (5 GHz, 54 Mbps), 802.11b (2,4 GHz, 11 Mbps), 802.11g (2,4 GHz, 54 Mbps), 802.11n ou Wi-Fi 4 (2,4 e 5 GHz, MIMO, '
        'até 600 Mbps), 802.11ac ou Wi-Fi 5 (5 GHz, MU-MIMO, até cerca de 6,9 Gbps), 802.11ax ou Wi-Fi 6 (2,4 e 5 GHz, OFDMA, 1024-QAM, '
        'Target Wake Time, BSS Coloring), Wi-Fi 6E (o Wi-Fi 6 também na faixa de 6 GHz) e 802.11be ou Wi-Fi 7 (canais de até 320 MHz, '
        '4096-QAM e operação multienlace).')
b = bul(S[6], 'Padrão WPA3')
b[1] = ('O WPA3-Personal substitui a autenticação por chave pré-compartilhada (PSK) pelo SAE (Simultaneous Authentication of Equals, '
        'baseado no Dragonfly), que resiste a ataques de dicionário offline e oferece sigilo progressivo. O WPA3-Enterprise usa '
        'IEEE 802.1X com servidor RADIUS e opção de 192 bits. O OWE cifra redes abertas. O uso de quadros de gerenciamento protegidos '
        '(PMF) é obrigatório.')

# ---- Seção 9 ----
S[8]['tip'][0] = 'IntServ versus DiffServ'


def sec(t, c, bl, tip):
    S.append({'title': t, 'content': c, 'bullets': bl, 'tip': tip})


sec('11. Modelo OSI em Detalhe, Equipamentos, ARP e ICMP',
    'Complementa a seção 1 associando funções e equipamentos a cada camada.',
    [['Equipamentos por camada',
      'Camada 1: repetidor e hub (regeneram bits). Camada 2: bridge, switch e ponto de acesso (comutam quadros por MAC). Camada 3: roteador '
      'e switch de camada 3 (encaminham pacotes por IP). Camadas 4 a 7: firewall com estado ou de aplicação, balanceadores de carga (L4 e '
      'L7) e proxies.'],
     ['Funções por camada',
      'Física: sinais, meio, codificação. Enlace: enquadramento, endereçamento MAC, detecção de erros, controle de acesso ao meio. Rede: '
      'endereçamento lógico, roteamento e fragmentação. Transporte: comunicação fim a fim, portas, controle de fluxo e erros. '
      'Sessão, apresentação e aplicação: diálogo, representação e serviços de usuário.'],
     ['ARP',
      'Resolve um endereço IPv4 em endereço MAC dentro da rede local: a requisição vai em broadcast e a resposta em unicast. Fica na '
      'fronteira entre enlace e rede. Ataques de envenenamento de ARP (ARP spoofing) permitem interceptar tráfego. No IPv6, o Neighbor '
      'Discovery (ICMPv6) substitui o ARP.'],
     ['ICMP',
      'Mensagens de controle e diagnóstico do IP: eco (tipos 8 e 0, usados pelo ping), destino inalcançável (tipo 3), tempo excedido (tipo '
      '11, usado pelo traceroute com TTL crescente) e redirecionamento. O ICMP não transporta dados de aplicação.'],
     ['Tamanhos e fragmentação',
      'O MTU típico do Ethernet é 1500 bytes. Se o pacote excede o MTU do enlace, o IPv4 pode fragmentar (roteador ou origem); o IPv6 só '
      'fragmenta na origem, usando descoberta do MTU do caminho (PMTUD).']],
    ['Switch Comuta por MAC, Roteador Encaminha por IP',
     'Switch de camada 2 decide pelo endereço MAC de destino. Roteador e switch de camada 3 decidem pelo endereço IP de destino. '
     'Domínio de broadcast só é dividido por roteador (ou por VLANs, que exigem roteamento entre si).'])
sec('12. Ethernet e Comutação em Profundidade: STP, LACP, PoE e Segurança de Camada 2',
    'Complementa a seção 3 com o funcionamento do STP, agregação de links, alimentação por Ethernet e proteções de camada 2.',
    [['Eleição e papéis no STP',
      'O switch com o menor identificador de ponte (prioridade mais o endereço MAC) é eleito raiz (root bridge). Cada switch escolhe uma '
      'porta raiz (melhor caminho até a raiz); cada segmento tem uma porta designada; as demais ficam bloqueadas. No RSTP, os papéis '
      'incluem porta alternativa e de backup, e os estados são descarte, aprendizado e encaminhamento (no STP clássico: bloqueio, '
      'escuta, aprendizado e encaminhamento).'],
     ['Agregação de links (LACP)',
      'O IEEE 802.1AX (antes 802.3ad) agrupa vários links físicos em um lógico, com balanceamento e redundância, negociado pelo LACP. '
      'Evita que o STP bloqueie os links agregados.'],
     ['PoE',
      'Alimentação de dispositivos (telefones IP, câmeras, pontos de acesso) pelo cabo de rede: IEEE 802.3af (cerca de 15 W), 802.3at '
      '(PoE+, cerca de 30 W) e 802.3bt (até 60 W e 90 a 100 W).'],
     ['VLAN nativa e ataques',
      'A VLAN nativa transporta quadros sem tag em um tronco 802.1Q. VLAN hopping explora troncos mal configurados (falsificação de '
      'switch e dupla marcação). Mitigação: desativar negociação de tronco em portas de acesso, não usar a VLAN 1 para dados e alterar '
      'a VLAN nativa.'],
     ['Proteções de camada 2',
      'Segurança de porta (limita e fixa endereços MAC), DHCP snooping (só portas confiáveis aceitam ofertas de DHCP e monta a tabela '
      'de associações), Dynamic ARP Inspection (valida ARP com base nessa tabela), IP Source Guard, proteção contra tempestade de '
      'broadcast (storm control), BPDU Guard e Root Guard (protegem a topologia do STP) e autenticação de porta por IEEE 802.1X.'],
     ['MACsec',
      'IEEE 802.1AE: cifra e autentica quadros em enlaces Ethernet, ponto a ponto.']],
    ['STP Bloqueia para Evitar Laços',
     'A raiz é eleita pelo menor ID de ponte. Portas redundantes ficam bloqueadas (descartando) até haver falha. O RSTP converge em '
     'segundos; o STP clássico, em 30 a 50 segundos.'])
sec('13. Endereçamento e Sub-redes: Cálculos, Endereços Especiais e IPv6 em Detalhe',
    'Complementa a seção 6 com cálculos de sub-redes, endereços especiais e a estrutura do IPv6.',
    [['Cálculo de sub-redes IPv4',
      'Hosts úteis em uma sub-rede /N: 2 elevado a (32 - N) menos 2 (endereço de rede e de broadcast). Exceções: /31 (enlace ponto a '
      'ponto, RFC 3021, sem os dois descontos) e /32 (host único). Exemplo: 192.168.10.0/26 tem máscara 255.255.255.192, blocos de 64, '
      'sub-redes 0, 64, 128 e 192, e 62 hosts úteis por sub-rede.'],
     ['Agregação de rotas (sumarização)',
      'Combina prefixos contíguos em um único: 192.168.0.0/24 e 192.168.1.0/24 resumem-se em 192.168.0.0/23. Reduz o tamanho das tabelas de '
      'roteamento.'],
     ['Endereços IPv4 especiais',
      '127.0.0.0/8 (loopback), 169.254.0.0/16 (autoconfiguração local, quando não há DHCP), 100.64.0.0/10 (espaço compartilhado para '
      'CGNAT, RFC 6598), 224.0.0.0/4 (multicast) e 255.255.255.255 (broadcast limitado).'],
     ['Notação e validade do IPv6',
      'Regras de abreviação: omitir zeros à esquerda de cada grupo e substituir uma sequência de grupos zerados por "::", uma única vez. '
      'Exemplo: 2001:0db8:0000:0000:0000:ff00:0042:8329 vira 2001:db8::ff00:42:8329. Um endereço é inválido se tiver caracteres fora de '
      '0 a 9 e A a F, grupos com mais de 4 dígitos, mais de 8 grupos ou mais de um "::". Existe a forma com IPv4 embutido '
      '(por exemplo, ::ffff:192.0.2.1 para IPv4 mapeado).'],
     ['Tipos de endereços IPv6',
      'Unicast global (2000::/3), link-local (fe80::/10, obrigatório em toda interface), local único (ULA, fc00::/7, uso privado), '
      'multicast (ff00::/8), loopback (::1) e não especificado (::). Prefixo de documentação: 2001:db8::/32. A sub-rede padrão é /64 e '
      'um site costuma receber um /48.'],
     ['Cabeçalho IPv6',
      'Fixo de 40 bytes, sem checksum, com campos de versão, classe de tráfego, rótulo de fluxo (20 bits), tamanho da carga, próximo '
      'cabeçalho, limite de saltos, origem e destino. Recursos opcionais vão em cabeçalhos de extensão. O MTU mínimo é 1280 bytes.'],
     ['Descoberta de vizinhos e autoconfiguração',
      'O Neighbor Discovery usa mensagens ICMPv6: solicitação e anúncio de roteador (RS e RA) e de vizinho (NS e NA). O SLAAC monta o '
      'endereço com o prefixo do RA e um identificador de interface (derivado do MAC ou aleatório por privacidade). A detecção de '
      'endereço duplicado (DAD) precede o uso. O DHCPv6 pode ser com ou sem estado.'],
     ['Transição IPv4 para IPv6',
      'Pilha dupla (dual stack: IPv4 e IPv6 ao mesmo tempo), túneis (IPv6 encapsulado em IPv4) e tradução (NAT64 com DNS64 para '
      'clientes só IPv6 acessarem serviços IPv4).']],
    ['/N Define Hosts: 2 Elevado a (32 - N), Menos 2',
     'Um /24 tem 254 hosts úteis, um /26 tem 62, um /30 tem 2. Para achar o tamanho do bloco, subtraia o octeto da máscara de 256 '
     '(máscara .192 dá bloco de 64).'])
sec('14. Serviços de Rede: DNS, DHCP, HTTP, E-mail, FTP e NTP',
    'Complementa a seção 5 com o funcionamento e as portas dos principais serviços de aplicação.',
    [['DNS em detalhe',
      'Resolução recursiva (o resolvedor consulta em nome do cliente) e iterativa (os servidores indicam o próximo a consultar), com '
      'cache controlado pelo TTL. Zonas com servidor primário e secundários; a transferência de zona (AXFR e IXFR) usa TCP. Registros: A, '
      'AAAA, CNAME, MX, NS, PTR, SOA, TXT (usado por SPF e DKIM) e SRV. O DNSSEC assina os registros (RRSIG, DNSKEY e DS) e '
      'garante autenticidade e integridade, não sigilo. DNS sobre TLS (porta 853) e sobre HTTPS (443) cifram as consultas.'],
     ['DHCP',
      'Processo DORA: Discover (cliente, broadcast), Offer, Request e Acknowledge. Fornece endereço, máscara, gateway, DNS e tempo de '
      'concessão (lease). Portas UDP 67 (servidor) e 68 (cliente). Agentes de retransmissão (relay) levam as mensagens entre sub-redes.'],
     ['HTTP',
      'HTTP/1.1 usa conexões persistentes. HTTP/2 multiplexa vários fluxos em uma conexão, com compressão de cabeçalhos. HTTP/3 roda sobre '
      'QUIC, que usa UDP (porta 443) e inclui TLS 1.3. O HTTPS usa TLS. O HTTP em si não guarda estado; cookies e tokens mantêm sessão.'],
     ['E-mail',
      'SMTP envia e retransmite (porta 25 entre servidores; 587 para submissão com autenticação e STARTTLS; 465 com TLS implícito). '
      'POP3 (110 e 995) baixa mensagens; IMAP (143 e 993) mantém e sincroniza no servidor. SPF, DKIM e DMARC, publicados no DNS, '
      'combatem falsificação de remetente.'],
     ['FTP e transferência segura',
      'FTP usa duas conexões: controle (porta 21) e dados (porta 20 no modo ativo; portas altas no modo passivo). Envia credenciais em '
      'texto claro. FTPS é FTP sobre TLS; SFTP é outro protocolo, sobre SSH (porta 22). TFTP usa UDP 69.'],
     ['NTP, syslog e SNMP',
      'NTP (UDP 123) sincroniza relógios, com níveis (strata). Syslog (UDP 514; TCP ou TLS na 6514) centraliza logs. SNMP usa UDP 161 '
      '(agente) e 162 (traps). LDAP: 389 (636 com TLS). RADIUS: UDP 1812 e 1813.']],
    ['FTP: Controle na 21, Dados na 20 (Ativo)',
     'No modo ativo, o servidor abre a conexão de dados a partir da porta 20 para o cliente. No passivo, o cliente abre a conexão de '
     'dados para uma porta indicada pelo servidor, o que atravessa melhor firewalls e NAT.'])
sec('15. TCP e UDP em Profundidade',
    'Complementa a seção 5 com o cabeçalho, os estados e o controle de congestionamento do TCP.',
    [['Cabeçalho TCP',
      'Mínimo de 20 bytes: portas de origem e destino (16 bits), número de sequência e de confirmação (32 bits), tamanho do cabeçalho, '
      'flags (SYN, ACK, FIN, RST, PSH, URG), janela de recepção (16 bits, ampliada pela opção de escala de janela) e checksum. O MSS é '
      'negociado no SYN.'],
     ['Confiabilidade',
      'Confirmações cumulativas, retransmissão por temporizador (RTO, calculado a partir do RTT) e retransmissão rápida após três '
      'ACKs duplicados. A opção SACK confirma blocos recebidos fora de ordem.'],
     ['Controle de congestionamento',
      'Slow start (a janela de congestionamento, cwnd, cresce exponencialmente até o limiar ssthresh), congestion avoidance (crescimento '
      'linear) e, ao detectar perda, redução multiplicativa (AIMD: aumento aditivo, diminuição multiplicativa). Variantes: Reno, CUBIC '
      '(padrão no Linux) e BBR (baseado em largura de banda e RTT medidos). A janela efetiva é o menor valor entre a janela do receptor '
      'e a cwnd.'],
     ['Estados da conexão',
      'LISTEN, SYN_SENT, SYN_RECEIVED, ESTABLISHED, FIN_WAIT, CLOSE_WAIT e TIME_WAIT (espera por duas vezes o tempo máximo de vida do '
      'segmento, para evitar segmentos antigos em novas conexões). Um ataque de inundação de SYN esgota conexões semiabertas; SYN cookies '
      'mitigam.'],
     ['UDP',
      'Cabeçalho de 8 bytes (portas, tamanho e checksum), sem conexão, ordenação ou retransmissão. O checksum é opcional no IPv4 e '
      'obrigatório no IPv6. Indicado para DNS, voz, vídeo, jogos e protocolos que implementam a própria confiabilidade, como o QUIC.'],
     ['Produto banda-atraso',
      'Bandwidth-delay product = largura de banda x RTT: é a quantidade de dados em trânsito para manter o enlace cheio, e o tamanho de '
      'janela necessário. Enlaces de alta capacidade e alta latência exigem janelas grandes.']],
    ['Janela do Receptor Controla o Fluxo, cwnd Controla a Rede',
     'A janela anunciada pelo receptor evita sobrecarregá-lo (controle de fluxo). A cwnd, ajustada pelo emissor, evita sobrecarregar a '
     'rede (controle de congestionamento). Vale o menor dos dois.'])
sec('16. Roteamento em Profundidade: OSPF, EIGRP, BGP e Seleção de Rotas',
    'Complementa a seção 8 com o funcionamento dos protocolos e com a forma como o roteador escolhe uma rota.',
    [['Escolha da rota',
      'Primeiro vale o prefixo mais específico (longest prefix match). Entre rotas para o mesmo prefixo, vence a menor distância '
      'administrativa (por exemplo, na Cisco: conectada 0, estática 1, eBGP 20, EIGRP interno 90, OSPF 110, IS-IS 115, RIP 120, iBGP 200). '
      'Entre rotas do mesmo protocolo, vence a menor métrica. Rotas de custo igual podem ser usadas juntas (ECMP).'],
     ['OSPF: áreas e vizinhança',
      'Estado de enlace, com áreas ligadas à área 0 (backbone). ABR liga áreas; ASBR injeta rotas externas. Roteadores descobrem vizinhos '
      'por mensagens Hello (multicast 224.0.0.5) e passam pelos estados Down, Init, 2-Way, ExStart, Exchange, Loading e Full. Em redes '
      'de acesso múltiplo elegem DR e BDR (por prioridade e depois pelo maior ID de roteador; multicast 224.0.0.6). Tipos principais de LSA: '
      '1 (roteador), 2 (rede), 3 (resumo entre áreas), 4 (ASBR), 5 (externa) e 7 (externa em NSSA). Temporizadores típicos: Hello de 10 s '
      'e Dead de 40 s em redes de difusão.'],
     ['EIGRP',
      'Protocolo avançado de vetor de distância, originalmente da Cisco, com o algoritmo DUAL, que calcula rotas sem laço e mantém sucessores '
      'e sucessores viáveis para convergência rápida. A métrica composta usa, por padrão, largura de banda e atraso.'],
     ['IS-IS',
      'Protocolo de estado de enlace usado por grandes provedores, semelhante ao OSPF em conceito.'],
     ['BGP: tipos de sessão e atributos',
      'eBGP liga sistemas autônomos diferentes; iBGP distribui rotas dentro do mesmo AS e exige malha completa ou refletores de rotas. '
      'Mensagens: OPEN, UPDATE, KEEPALIVE e NOTIFICATION, sobre TCP na porta 179. Atributos: ORIGIN, AS_PATH e NEXT_HOP (bem conhecidos e '
      'obrigatórios), LOCAL_PREF (preferência dentro do AS, maior vence) e MED (sugestão a vizinhos, menor vence). O AS_PATH mais curto '
      'é critério de desempate e evita laços.'],
     ['Segurança do BGP',
      'O BGP confia nos anúncios dos vizinhos, o que permite sequestro de prefixos. A RPKI valida a origem dos prefixos anunciados.'],
     ['Multicast',
      'IGMP (IPv4) e MLD (IPv6) gerenciam a participação de hosts em grupos; o PIM roteia o tráfego multicast entre roteadores.']],
    ['Distância Administrativa Escolhe o Protocolo, Métrica Escolhe a Rota',
     'Se dois protocolos oferecem a mesma rede, vence o de menor distância administrativa. Dentro do mesmo protocolo, vence a menor '
     'métrica. Antes de tudo, prevalece o prefixo mais específico.'])
sec('17. Redes Sem Fio em Profundidade e Mobilidade',
    'Complementa a seção 7 com a arquitetura de WLAN, o roaming, a autenticação corporativa e as redes móveis.',
    [['BSS, ESS e canais',
      'BSS: um ponto de acesso (AP) e suas estações, identificado pelo BSSID (MAC do AP). ESS: vários APs interligados que compartilham o '
      'mesmo SSID, permitindo roaming. Em 2,4 GHz, os canais 1, 6 e 11 não se sobrepõem (20 MHz). Em 5 GHz há mais canais e larguras de 20, '
      '40, 80 e 160 MHz; alguns canais exigem DFS (deixar o canal se houver radar). Pesquisa de campo (site survey) planeja a '
      'cobertura.'],
     ['Arquiteturas de gerenciamento',
      'AP autônomo, AP leve gerenciado por controlador (o protocolo CAPWAP usa UDP 5246 para controle e 5247 para dados) e gerenciamento '
      'em nuvem. O controlador centraliza configuração, segurança e roaming.'],
     ['Roaming e QoS',
      '802.11r (transição rápida entre APs), 802.11k (relatórios de vizinhos) e 802.11v (orientação de transição). O 802.11e define QoS '
      'com EDCA, que dá prioridade a categorias de acesso (voz, vídeo, melhor esforço e segundo plano).'],
     ['Autenticação 802.1X',
      'Três papéis: suplicante (cliente), autenticador (AP ou switch) e servidor de autenticação (RADIUS, UDP 1812 e 1813). Métodos EAP: '
      'EAP-TLS (certificados nos dois lados, mais seguro), PEAP e EAP-TTLS (túnel TLS com credenciais). Permite atribuir VLAN e '
      'políticas dinamicamente.'],
     ['Redes móveis (4G e 5G)',
      'O 5G NR atende três cenários: banda larga móvel aprimorada (eMBB), comunicações ultraconfiáveis de baixa latência (URLLC) e '
      'IoT massiva (mMTC). Network slicing cria fatias lógicas de rede com características próprias. Handover mantém a conexão ao mudar de '
      'célula.'],
     ['Mobilidade no IP',
      'Mobile IP (RFC 5944) permite que um nó mude de rede mantendo o endereço de origem (home address), com agente de origem (home agent) '
      'e endereço de cuidado (care-of address).']],
    ['1, 6 e 11 Não se Sobrepõem em 2,4 GHz',
     'Para evitar interferência entre APs vizinhos, use canais de 20 MHz que não se sobreponham (1, 6 e 11). Em 5 GHz há mais '
     'canais livres de sobreposição, o que ajuda em alta densidade.'])
sec('18. WAN, Banda Larga, Acesso Remoto e AAA',
    'Complementa a seção 4 com serviços de operadora, acesso banda larga e mecanismos de acesso remoto seguro.',
    [['MPLS L3VPN e Metro Ethernet',
      'Na VPN MPLS de camada 3, roteadores de borda do provedor (PE) mantêm tabelas separadas por cliente (VRF) e trocam rotas por MP-BGP, '
      'usando route distinguisher e route target; o CE é o roteador do cliente. Metro Ethernet (MEF) oferece serviços E-Line (ponto a '
      'ponto), E-LAN (multiponto) e E-Tree (raiz e folhas).'],
     ['Acesso banda larga',
      'xDSL (linha telefônica de cobre, como o ADSL assimétrico), cabo coaxial (DOCSIS) e fibra até a residência (FTTH), geralmente com '
      'redes ópticas passivas (GPON, ITU-T G.984, cerca de 2,5 Gbps de descida e 1,25 Gbps de subida, com OLT no provedor, splitters '
      'passivos e ONU ou ONT no cliente).'],
     ['VPN IPsec',
      'AH (protocolo 51: integridade e autenticação, sem cifra) e ESP (protocolo 50: cifra, integridade e autenticação), nos modos '
      'transporte e túnel. O IKE negocia as associações de segurança pela porta UDP 500 (4500 com NAT traversal). No IKEv1, a fase 1 '
      'estabelece o canal seguro de gerência e a fase 2, as associações do IPsec; o IKEv2 simplifica o processo.'],
     ['Acesso remoto',
      'VPN de acesso remoto (IPsec ou TLS/SSL, este muitas vezes sem cliente), L2TP com IPsec, túneis SSH, RDP e serviços bastion (jump '
      'host). O ZTNA (acesso à rede com confiança zero) concede acesso a aplicações específicas, e não à rede inteira, após verificar '
      'identidade e postura do dispositivo.'],
     ['AAA: RADIUS e TACACS+',
      'RADIUS (UDP 1812 e 1813) combina autenticação e autorização, cifra apenas a senha, e é padrão aberto, muito usado em acesso de '
      'rede e Wi-Fi. TACACS+ (TCP 49, Cisco) separa autenticação, autorização e contabilização, cifra todo o corpo do pacote e é comum na '
      'administração de equipamentos.'],
     ['PPP e PPPoE',
      'PPP encapsula pacotes em enlaces ponto a ponto, com autenticação PAP (senha em texto claro) ou CHAP (desafio e resposta). O PPPoE '
      'leva o PPP sobre Ethernet, usado por provedores de banda larga.']],
    ['AH Não Cifra, ESP Cifra; RADIUS Cifra a Senha, TACACS+ o Corpo',
     'No IPsec, sigilo exige o ESP. No AAA, o RADIUS protege só a senha no pacote; o TACACS+ cifra todo o conteúdo e separa as três '
     'funções.'])
sec('19. SDN, NFV e Redes de Data Center',
    'Redes definidas por software e virtualização de funções de rede mudam a forma de operar redes, e o edital de TI cita SDN.',
    [['SDN',
      'Separa o plano de controle (decisões) do plano de dados (encaminhamento) e centraliza o controle em um controlador '
      'programável. APIs ao sul (do controlador aos equipamentos, como OpenFlow e NETCONF) e ao norte (das aplicações ao controlador, '
      'geralmente REST). Controladores conhecidos: OpenDaylight e ONOS.'],
     ['OpenFlow',
      'Protocolo da Open Networking Foundation em que o switch mantém tabelas de fluxo (regras com critério de casamento e ação) '
      'programadas pelo controlador. Pacotes sem regra são enviados ao controlador.'],
     ['Overlay e VXLAN',
      'O VXLAN encapsula quadros Ethernet em UDP (porta 4789) e usa identificador de rede de 24 bits (cerca de 16 milhões de segmentos, '
      'contra 4094 VLANs), estendendo redes de camada 2 sobre uma infraestrutura de camada 3 (underlay). Os pontos de terminação são os '
      'VTEPs; o EVPN distribui as informações de MAC e IP por BGP. Alternativas: NVGRE e Geneve.'],
     ['Topologia leaf-spine',
      'Cada switch leaf (acesso) liga-se a todos os switches spine (núcleo), dando o mesmo número de saltos entre servidores e '
      'caminhos múltiplos de custo igual (ECMP). Adequada ao tráfego leste-oeste entre servidores.'],
     ['NFV',
      'Virtualização de funções de rede: firewall, roteador, balanceador e outras rodam como software em servidores padrão, em vez de '
      'equipamentos dedicados. A arquitetura ETSI inclui a camada de gerenciamento e orquestração (MANO).'],
     ['Automação e SASE',
      'Automação de rede com Ansible, NETCONF e YANG (modelos de dados) e telemetria em fluxo. SASE combina SD-WAN e segurança entregue '
      'na nuvem (firewall, acesso remoto e proteção web) em um serviço.']],
    ['SDN Separa Controle de Encaminhamento',
     'Na SDN, o controle é centralizado e o encaminhamento permanece nos equipamentos. O controlador fala com os equipamentos por '
     'APIs ao sul (por exemplo, OpenFlow) e oferece APIs ao norte às aplicações.'])
sec('20. QoS e VoIP em Profundidade',
    'Complementa a seção 9 com marcação, filas, requisitos de voz e o funcionamento do SIP.',
    [['Marcação de prioridade',
      'Camada 3: DSCP de 6 bits no campo de tipo de serviço do IP (por exemplo, EF = 46 para voz, AF41 = 34 para vídeo interativo, CS3 = 24 '
      'para sinalização, 0 para melhor esforço). Camada 2: o campo PCP de 3 bits do 802.1Q (802.1p). A fronteira de confiança define '
      'onde as marcações são aceitas ou refeitas.'],
     ['Policiamento e modelagem',
      'Policiamento (policing) descarta ou remarca o tráfego que excede a taxa contratada. Modelagem (shaping) armazena o excesso em fila '
      'e o envia depois, suavizando a taxa.'],
     ['Filas e prevenção de congestionamento',
      'FIFO, fila de prioridade, WFQ, CBWFQ e LLQ (CBWFQ mais fila de prioridade estrita para voz). Descarte antecipado (RED e WRED) '
      'evita que as filas encham e reduz o descarte simultâneo de muitos fluxos.'],
     ['Requisitos de voz',
      'Diretrizes usuais: atraso unidirecional de até 150 ms (ITU-T G.114), jitter de até cerca de 30 ms e perda inferior a 1%. O '
      'buffer de jitter compensa a variação de atraso. A qualidade é estimada pelo MOS (nota de 1 a 5).'],
     ['Codecs',
      'G.711 (64 kbps, PCM), G.729 (8 kbps), G.722 (banda larga) e Opus. Com cabeçalhos, a chamada G.711 consome cerca de 80 a 90 kbps '
      'por sentido e a G.729, cerca de 25 a 32 kbps, aproximadamente.'],
     ['SIP: métodos, respostas e SDP',
      'Métodos: INVITE, ACK, BYE, CANCEL, REGISTER e OPTIONS. Respostas em classes: 1xx provisória (180 Ringing), 2xx sucesso (200 OK), '
      '3xx redirecionamento, 4xx erro do cliente, 5xx erro do servidor e 6xx falha global. O SDP descreve e negocia a mídia (codecs, '
      'portas). O RTP carrega a voz.'],
     ['NAT e voz',
      'O NAT complica o SIP e o RTP porque os endereços vão dentro das mensagens. Soluções: STUN, TURN e ICE, e o controlador de '
      'sessão de borda (SBC) na fronteira da rede.']],
    ['Marcar, Classificar, Enfileirar',
     'A QoS começa pela classificação e marcação na borda (DSCP), continua com filas por classe nos equipamentos e usa policiamento e '
     'modelagem para controlar taxas. Voz precisa de baixa latência, jitter e perda.'])
sec('21. Administração e Diagnóstico de Redes',
    'Noções de administração de redes citadas no programa: monitoramento, análise de tráfego e método de diagnóstico.',
    [['Coleta de tráfego e eventos',
      'NetFlow (Cisco), IPFIX (padrão do IETF) e sFlow (amostragem) resumem fluxos de tráfego (origem, destino, portas e volume), úteis '
      'para planejamento, detecção de anomalias e cobrança. Syslog centraliza logs, com severidades de 0 (emergência), 1 (alerta), 2 '
      '(crítico), 3 (erro), 4 (aviso), 5 (notificação), 6 (informação) e 7 (depuração).'],
     ['Polling e traps no SNMP',
      'Polling: o gerenciador consulta os agentes periodicamente. Trap: o agente notifica eventos. Combinam-se para visibilidade contínua '
      'e alerta rápido. Estabelecer linha de base (baseline) ajuda a reconhecer o que é anormal.'],
     ['Métricas',
      'Largura de banda (capacidade), vazão (throughput, o que é efetivamente transferido), goodput (dados úteis, sem sobrecarga), '
      'latência, jitter e perda de pacotes. Disponibilidade e tempo de resposta compõem os SLAs.'],
     ['Ferramentas de diagnóstico',
      'ping (ICMP), traceroute ou tracert (rota e atraso por salto), nslookup e dig (DNS), ipconfig ou ip (configuração), netstat ou ss '
      '(conexões), arp, tcpdump e Wireshark (captura de pacotes).'],
     ['Método de diagnóstico',
      'De baixo para cima (da camada física à de aplicação), de cima para baixo, ou dividir para conquistar (começar em uma camada '
      'intermediária). Verifique sempre alterações recentes, isole o problema e documente a solução.']],
    ['Comece pela Camada Física Quando Nada Funciona',
     'Sem link, cabo, porta e energia são as primeiras verificações. Sem resolução de nomes, teste o IP direto: se responder, o '
     'problema é o DNS.'])
sec('22. Comunicação de Dados: Codificação, Multiplexação, Comutação e Detecção de Erros',
    'Fundamentos da camada física e de enlace que aparecem em questões de comunicação de dados e de comutação.',
    [['Limites de capacidade',
      'Nyquist (canal sem ruído): taxa máxima = 2 x B x log2(M), com B a largura de banda e M os níveis do sinal. Shannon (canal com '
      'ruído): capacidade C = B x log2(1 + S/N).'],
     ['Modulação e multiplexação',
      'Modulação digital: ASK (amplitude), FSK (frequência), PSK (fase) e QAM (amplitude e fase). Multiplexação: FDM (por frequência), TDM '
      '(por tempo, síncrona ou estatística) e WDM (por comprimento de onda, como CWDM e DWDM em fibra).'],
     ['Códigos de linha',
      'NRZ e NRZI, Manchester (transição no meio de cada bit; usado no Ethernet de 10 Mbps; autossincronizado, mas exige o dobro da '
      'banda). 4B/5B (Fast Ethernet 100BASE-X: cada 4 bits viram 5, garantindo transições para sincronismo; sobram códigos usados como '
      'delimitadores de início e fim de quadro). 8B/10B (Gigabit Ethernet de fibra e Fibre Channel) e 64B/66B (10 Gigabit Ethernet).'],
     ['Enquadramento',
      'Contagem de caracteres; bytes de flag com inserção de bytes (byte stuffing); flags de bits com inserção de bits (HDLC usa 01111110 e '
      'insere um 0 após cinco 1 consecutivos); e violações de código da camada física, com símbolos que não ocorrem nos dados regulares.'],
     ['Detecção e correção de erros',
      'Paridade simples detecta erros de um bit (e de quantidade ímpar de bits). Paridade bidimensional (VRC e LRC) detecta mais casos, '
      'mas não é adequada a canais muito ruidosos. Checksum (soma de complemento de um, no IP, TCP e UDP) e CRC (divisão polinomial; o '
      'Ethernet usa CRC-32) detectam erros em rajada. Correção: códigos como o de Hamming e FEC (correção direta) ou retransmissão (ARQ: '
      'para-e-espera, go-back-N e retransmissão seletiva).'],
     ['Comutação',
      'Circuitos (caminho dedicado durante a conexão, como a telefonia clássica) versus pacotes (datagrama, cada pacote roteado '
      'individualmente; ou circuito virtual, caminho definido no início). ATM: células fixas de 53 bytes (5 de cabeçalho e 48 de dados), '
      'com identificadores VPI e VCI. Um caminho virtual (VPC) e um canal virtual (VCC) fim a fim são formados pela concatenação de enlaces '
      'virtuais (VPL e VCL) ao longo da rede.']],
    ['CRC e Checksum Detectam, Hamming Corrige',
     'Paridade, checksum e CRC detectam erros. Hamming e FEC corrigem. ARQ resolve erros detectados pedindo retransmissão.'])
sec('23. Referências e Conferência',
    'Conferência realizada em 21/09/2026.',
    [['Referências',
      'Kurose e Ross, Redes de Computadores e a Internet; Tanenbaum e Wetherall, Redes de Computadores; Stallings, Redes e Sistemas de '
      'Comunicação de Dados; RFCs (791, 792, 793, 768, 8200, 4861, 1918, 3021, 5798, 2328, 4271, 8446); padrões IEEE 802.3, 802.1Q, '
      '802.1D, 802.1AX, 802.11 e 802.1X; ISO/IEC 11801; TIA-568; ABNT NBR 14565; ITU-T G.114, G.984; documentação de fabricantes para '
      'distâncias administrativas e temporizadores; Edital SEFAZ-CE 2026 (FCC), Anexo VI, e Edital SEFAZ-BA 2022 (FGV), Anexo I.'],
     ['Corrigido nesta revisão',
      'Wi-Fi 6 não usa 6 GHz (isso é o Wi-Fi 6E); WPA3 substitui o PSK pelo SAE (a troca de quatro etapas permanece); nomenclatura de '
      'blindagem (F/UTP, S/FTP etc.); alcance de fibras multimodo por classe; nota sobre o rótulo MPLS de 32 bits (20 bits de rótulo); IPv6 e '
      'NAT (reduz a necessidade, mas não é segurança); NBR 14565 sem ano fixo; três títulos de dica atribuídos a bancas sem evidência; '
      'inclusão de Cat 7 e 8 e do Wi-Fi 7.'],
     ['A conferir',
      'Edição vigente da ABNT NBR 14565; distâncias administrativas e temporizadores (dependem do fabricante e da versão); limites e '
      'alcances de padrões Ethernet; disponibilidade e taxas de GPON e de 5G em cada operadora.']],
    ['Regra de Conteúdo', 'Este material não afirma nada sem fonte. Se houver divergência com a norma vigente, a norma prevalece.'])

ap['subtitle'] = ('OSI e TCP/IP, Cabeamento, Ethernet, VLAN e STP, Endereçamento IPv4/IPv6 e Sub-redes, Serviços (DNS, DHCP, E-mail), TCP e UDP, '
                  'Roteamento (OSPF, BGP), Wi-Fi 6/7 e 5G, WAN e Acesso Remoto, SDN e VXLAN, QoS, VoIP, SNMP e Comunicação de Dados')
json.dump(dados, open(ARQ, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('Redes atualizada: %d seções.' % len(S))
