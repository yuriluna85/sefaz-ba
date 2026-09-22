# Auditoria 03: Apostila de Infraestrutura, Cloud e DevOps

Data: 21/09/2026. Escopo: as 10 seções originais (conferidas) e lacunas de infraestrutura em relação ao programa SEFAZ-CE 2026 (B02) e ao edital SEFAZ-BA 2022. Middleware, mensageria, observabilidade e Kubernetes avançado ficam para a apostila seguinte.

## Conteúdo conferido e mantido
Classificação TIER I a IV e o conceito de manutenção concorrente; DAS, NAS e SAN; Fibre Channel, FCoE e iSCSI (porta 3260); RAID 0, 1, 5, 6 e 10; multipathing, thin provisioning e snapshots; clusters ativo/passivo e ativo/ativo; MTBF, MTTF, MTTR e A = MTBF / (MTBF + MTTR); RPO e RTO; NOC e SOC; Zabbix e pilha ELK; as cinco características, os modelos de serviço e de implantação do NIST SP 800-145; hipervisores Tipo 1 e Tipo 2; vMotion, Storage vMotion, DRS e HA; formatos VMDK, VHD/VHDX e QCOW2; namespaces e cgroups; componentes e Dockerfile; componentes do Kubernetes e tipos de Service (NodePort de 30000 a 32767); CI/CD e Ansible (sem agente, idempotência); FHS, systemd, permissões POSIX, AD DS, Kerberos e GPO.

## Correções
| # | Trecho original | Problema | Correção |
|---|---|---|---|
| 1 | "agentes limpos (gases inertes FM-200, Novec 1230)" e "não danificam equipamentos nem asfixiam operadores" | FM-200 (HFC-227ea) e Novec 1230 são agentes químicos, não gases inertes; gases inertes (como o IG-541) reduzem o oxigênio e exigem projeto para áreas ocupadas | Separados os dois grupos; citada a NFPA 2001; removida a afirmação absoluta |
| 2 | Sala-cofre "abaixo de 55 °C e 85% de umidade" | Valores dependem da classe da NBR 15247 e não foram confirmados | Valores removidos, com aviso de conferir |
| 3 | Percentuais de disponibilidade dos TIERs apresentados como parte da classificação | São valores de referência informativos; o Uptime Institute certifica topologia | Marcados como referência informativa |
| 4 | Sticky Bit: "somente o proprietário do arquivo ou root" | Também o proprietário do diretório | Corrigido |
| 5 | NIST SP 800-145 "exigido em editais" | Afirmação sem fonte | Reescrita ("mais citado") |

## Seções acrescentadas
11 Linux Red Hat (RPM e DNF, LVM, XFS e ext4, boot e systemd, contas e sudo, SELinux, firewalld); 12 Windows Server e Active Directory (floresta, OU, sites, replicação multimestre, RODC, Catálogo Global, cinco funções FSMO, Kerberos e NTLM, LDAP e portas, LSDOU, papéis do servidor); 13 Virtualização (vSphere HA e FT, vMotion, DRS, vSAN, Hyper-V com Live Migration, Replica, CSV e VHDX, overcommit, ballooning, snapshot); 14 Backup (completo, incremental, diferencial, GFS, 3-2-1, replicação síncrona e assíncrona, deduplicação, testes de restauração); 15 Tipos de storage (bloco, arquivo, objeto, zoning e LUN masking, NVMe, SDS, hiperconvergência, riscos do RAID); 16 Cálculos de disponibilidade (tabela dos noves, série e paralelo); 17 Referências e conferência.

## A conferir
Valores exatos da NBR 15247 por classe; origem exata dos percentuais de disponibilidade citados para os TIERs; comportamento de recursos VMware e Hyper-V na versão em uso; portas e detalhes de protocolos no texto oficial.

## Observação sobre backup incremental
A definição de incremental varia entre fontes (desde o último backup de qualquer tipo, ou desde o último completo). Foi mantida a definição mais comum, com aviso na apostila. A questão da SEFAZ-CE 2021 (item 33) usou a segunda; o gabarito oficial é CERTO.
