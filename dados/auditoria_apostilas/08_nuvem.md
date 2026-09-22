# Apostila 08 (nova): Computação em Nuvem (AWS, Azure e Google Cloud)

Data: 21/09/2026. Apostila criada do zero, sem versão anterior a auditar. Fonte do escopo: programa SEFAZ-CE 2026 (FCC), área B02, bloco "Computação em Nuvem": modelos de serviço e de implantação, multicloud, SOA e microsserviços, sistemas distribuídos resilientes, serverless e event-driven, balanceamento e autoescalonamento, contêineres e orquestração, VPN, sub-redes, gateways, grupos de segurança, IAM, RBAC, MFA, criptografia em trânsito e em repouso com TLS e KMS, Zero Trust, conectividade site-to-site, Direct Connect, ExpressRoute, governança e custos (tagueamento, cotas, limites, FinOps), conformidade (ISO/IEC 27001, NIST 800-53 e LGPD), plataformas AWS, Azure e GCP, e dados em nuvem (objeto, bloco e arquivo, data lakes, processamento distribuído, Big Data e IA).

## Seções (15, 18 páginas)
1 Fundamentos, modelos de adoção e pilares (responsabilidade compartilhada, os "Rs" de migração, Well-Architected); 2 Híbrida, multicloud, lock-in, residência e transferência internacional de dados (LGPD arts. 33 a 36); 3 Redes (VPC e VNet, sub-redes, gateways, grupos de segurança versus NACL, peering, endpoints privados, balanceamento, DNS e CDN); 4 Conectividade (VPN site-to-site, Direct Connect, ExpressRoute, Interconnect, criptografia nos links dedicados, BGP); 5 Computação (VMs, autoescalonamento, modelos de compra, contêineres gerenciados); 6 Serverless e arquitetura orientada a eventos; 7 Armazenamento e bancos (objeto, bloco, arquivo, camadas, durabilidade, data warehouse e data lake); 8 Identidade e acesso (AWS IAM, Entra ID e Azure RBAC, Google Cloud IAM, RBAC e ABAC); 9 Criptografia e KMS (envelope, HSM, BYOK); 10 Segurança, Zero Trust e conformidade; 11 IaC, GitOps e governança de contas (Terraform, landing zone, políticas, tags, cotas); 12 Custos e FinOps; 13 Alta disponibilidade, DR e migração; 14 Mapa de equivalência de serviços; 15 Referências.

## Pontos em que o cuidado foi maior
- Links dedicados (Direct Connect, ExpressRoute e Interconnect): descritos como privados, mas não cifrados por padrão; a proteção vem de VPN IPsec ou MACsec.
- Avaliação de políticas do AWS IAM (negação explícita prevalece) e função das SCPs (limitam, não concedem).
- Nomes de serviços que mudam: Azure AD virou Microsoft Entra ID; Azure Synapse evolui para o Microsoft Fabric. Registrados como "conferir".
- Serviços de migração com disponibilidade recente incerta (AWS Migration Hub e Snowball): substituídos por opções estáveis (Application Migration Service e "família AWS Snow", com aviso).
- Nenhuma alegação de "cobrado em prova" e nenhuma atribuição a bancas.

## A conferir
Nomes de serviços, limites (como o tempo máximo do Lambda e cotas) e preços; regulamentação vigente da ANPD sobre transferência internacional; evolução do Synapse e do Fabric; disponibilidade dos dispositivos de transferência física; normas do órgão sobre uso de nuvem.

## Ligação com o banco de questões
Cobre os conceitos dos itens 117 a 120 da SEFAZ-CE 2021 (nuvens pública e privada, serviço medido e pool de recursos) e a questão 55 do TRF1 (resource pooling), cujas explicações já foram reescritas.
