# Auditoria 09: Apostila de Redes de Computadores e Telecomunicações

Data: 21/09/2026. Escopo: as 10 seções originais (conferidas) e lacunas frente ao programa SEFAZ-CE 2026 (B02: redes, arquitetura, endereçamento, administração, SDN, wireless, acesso remoto e comunicação segura) e ao edital SEFAZ-BA 2022 (redes, arquiteturas, acesso remoto e wireless, noções de administração e de mobilidade).

## Conteúdo conferido e mantido
OSI e TCP/IP com PDUs e encapsulamento; categorias Cat 5e, 6 e 6a; monomodo e multimodo; canal horizontal de 100 m (90 + 10); evolução do Ethernet; VLAN 802.1Q (tag de 4 bytes, VID de 1 a 4094); acesso e tronco; STP, RSTP e MSTP; L2, L3 e roteador; SD-WAN; GRE e IPsec; TCP (handshake, janela, congestionamento) e UDP; portas conhecidas; DNS; IPv4 (classes, CIDR, VLSM, RFC 1918); NAT e PAT; CSMA/CA; WEP, WPA e WPA2; IGP e EGP; RIP (15 saltos); OSPF (Dijkstra, custo); BGP (porta 179, path vector); VRRP e HSRP; SIP e RTP; G.711 e G.729; IntServ e DiffServ (DSCP); SNMP (agente, MIB, operações, v1, v2c e v3 com USM e VACM, três níveis de segurança).

## Correções
| # | Trecho original | Problema | Correção |
|---|---|---|---|
| 1 | Wi-Fi 6 "2,4, 5 e 6 GHz" | A faixa de 6 GHz é do Wi-Fi 6E | Wi-Fi 6 em 2,4 e 5 GHz; Wi-Fi 6E e Wi-Fi 7 acrescentados |
| 2 | WPA3 "substitui a troca de quatro etapas por SAE" | O SAE substitui a autenticação por PSK; o handshake de quatro etapas permanece | Reescrito; incluídos OWE, PMF e a opção de 192 bits |
| 3 | Blindagem "FTP/STP (global em fita ou malha)" | Nomenclatura confusa | Nomenclatura da ISO/IEC 11801 (F/UTP, S/UTP, U/FTP, S/FTP) |
| 4 | Fibra multimodo "até 300 a 550 metros" | O alcance depende da classe (OM1 a OM5) e da velocidade | Exemplo correto (10GBASE-SR: cerca de 300 m em OM3 e 400 m em OM4) |
| 5 | MPLS "rótulos de 32 bits" | A entrada da pilha tem 32 bits, mas o rótulo tem 20 | Esclarecido |
| 6 | IPv6 "elimina necessidade de NAT" | Reduz a necessidade; NAT não é segurança | Reformulado |
| 7 | "ABNT NBR 14565:2019" | Ano da edição não confirmado | "Confira a edição vigente" |
| 8 | Cat 6 e 6a sem Cat 7 e 8 | Omissão | Cat 7 e Cat 8 incluídas |
| 9 | Três dicas com rótulos "FGV/CEBRASPE" e "na FGV" | Atribuição sem evidência | Renomeadas |

## Seções acrescentadas (11 a 23)
11 OSI em detalhe (equipamentos por camada, ARP, ICMP, MTU e fragmentação); 12 Ethernet e comutação (papéis do STP, LACP, PoE, VLAN nativa e ataques, DHCP snooping, DAI, MACsec); 13 Endereçamento (cálculo de sub-redes, sumarização, endereços especiais, IPv6 em detalhe, NDP, SLAAC, transição); 14 Serviços de rede (DNS e DNSSEC, DHCP, HTTP/1.1, 2 e 3, e-mail, FTP, NTP, syslog, portas); 15 TCP e UDP em profundidade (cabeçalho, AIMD, estados, produto banda-atraso); 16 Roteamento (longest prefix match, distância administrativa, OSPF, EIGRP, IS-IS, BGP, RPKI, multicast); 17 Redes sem fio e mobilidade (BSS, ESS, canais, CAPWAP, roaming, 802.1X e EAP, 5G, Mobile IP); 18 WAN e acesso remoto (MPLS L3VPN, Metro Ethernet, GPON, IPsec e IKE, ZTNA, RADIUS e TACACS+, PPPoE); 19 SDN, NFV e data center (OpenFlow, VXLAN, leaf-spine, SASE); 20 QoS e VoIP (DSCP, policing e shaping, LLQ, requisitos de voz, SIP e SDP); 21 Administração e diagnóstico (NetFlow, IPFIX, syslog, métricas, ferramentas, método); 22 Comunicação de dados (Nyquist e Shannon, modulação, multiplexação, 4B/5B, enquadramento, paridade, CRC, ATM); 23 Referências.

## A conferir
Edição vigente da ABNT NBR 14565; distâncias administrativas e temporizadores (dependem do fabricante e da versão); limites e alcances de padrões Ethernet; taxas de GPON e de 5G por operadora.

## Ligação com o banco de questões
A apostila cobre os conceitos de itens já tratados: SEFAZ-CE 2021 itens 140 e 141 (paridade VRC/LRC e ATM VCL/VCC), 142 e 143 (topologia de barramento e camadas), 144 e 145 (Gigabit Ethernet e EDCA); TRF1 Analista questões 41 a 46 (código 4B/5B, 10GBase-ER, endereços IPv6, ECMP, SIP e bastião) e 59 e 60 (segurança Wi-Fi e proxy reverso).
