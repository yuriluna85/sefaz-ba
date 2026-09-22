# Auditoria 01: Apostila de Segurança da Informação

Data: 21/09/2026. Escopo: as 10 seções originais (conferidas afirmação por afirmação) e a lacuna em relação ao programa oficial SEFAZ-CE 2026 (FCC), área B02.

## Resultado da conferência das 10 seções originais
Conteúdo correto e mantido: tríade CID e princípios; ISO/IEC 27002:2022 com 93 controles (37 organizacionais, 8 de pessoas, 14 físicos e 34 tecnológicos); ISO 27001 como norma certificável e SoA; modos de operação de cifra (ECB, CBC, CFB, OFB, CTR, GCM); RSA, ECC (256 bits equivale a RSA de 3072), Diffie-Hellman; MD5, SHA-1, SHA-2, SHA-3; fluxo de assinatura digital; hierarquia ICP-Brasil; três fatores e MFA; DAC, MAC, RBAC e ABAC; OAuth 2.0 (autorização), OIDC (autenticação), SAML e JWT; tipos de firewall, IDS e IPS; IPsec (AH sem cifra, ESP com cifra); taxonomia de malware; engenharia social; as 10 categorias do OWASP 2021; conceitos, agentes, princípios (art. 6º) e as 10 bases legais da LGPD (art. 7º); legítimo interesse ausente do art. 11.

## Erros e imprecisões corrigidos
| # | Trecho original | Problema | Correção | Fonte |
|---|---|---|---|---|
| 1 | 3DES "seguro porém lento" | Depreciado e proibido para cifração a partir de 2024 | Marcado como obsoleto | NIST SP 800-131A |
| 2 | Efeito avalanche "altera mais de 50% do hash" | Imprecisão: em média cerca de 50% dos bits | Reescrito | Propriedade padrão de funções hash |
| 3 | "SHA-2 adotado na NF-e" | Falso: a NF-e usa assinatura RSA com SHA-1 | Removido; incluída a informação correta com aviso de versão | Manual de Orientação do Contribuinte da NF-e (nfe.fazenda.gov.br) |
| 4 | Assinatura ICP-Brasil "equiparada à assinatura de próprio punho com firma reconhecida" | Não consta de lei | Substituído por MP 2.200-2/2001, art. 10, §1º (presunção de veracidade em relação aos signatários) e Lei 14.063/2020 (assinatura simples, avançada e qualificada) | Textos legais |
| 5 | A3 "validade de até 3 ou 5 anos"; A3 em "Token, Smartcard ou HSM" | Prazo impreciso | A1: até 1 ano; A3: até 5 anos; A3 em cartão inteligente ou token | DOC-ICP-04 |
| 6 | OWASP apenas na edição 2021 | Existe o OWASP Top 10:2025 (oficial) | Incluída a lista 2025 e mantida a 2021 para comparação | owasp.org/Top10/2025 |
| 7 | SQL Injection: "única defesa 100% eficaz" e "única solução reconhecida pela OWASP" | Falso: a OWASP lista consulta parametrizada como defesa primária e cita alternativas | Reescrito (seção 8, dica e pegadinha 6) | OWASP SQL Injection Prevention Cheat Sheet |
| 8 | Ciclo de incidentes sem atribuição | Modelo SANS apresentado como "ciclo formal" | Atribuídos NIST SP 800-61 Rev. 2 e SANS | NIST SP 800-61 Rev. 2 |
| 9 | TLS 1.3 "PFS com ECDHE" | Incompleto | ECDHE ou DHE (efêmeras) | RFC 8446 |
| 10 | Seção 10 "armadilhas da FGV/CEBRASPE" | Atribuição a bancas sem evidência | Renomeada para "Armadilhas Conceituais Recorrentes" | n/a |
| 11 | Dado anonimizado sem a exceção | Omissão | Incluída a exceção do art. 12 da LGPD | Lei 13.709/2018 |

## Seções acrescentadas (lacunas do programa CE 2026)
11 Gestão de Riscos (ISO 31000:2018 e ISO/IEC 27005); 12 Continuidade (BIA, ISO 22301, RTO, RPO, MTPD, sites, regra 3-2-1); 13 Gestão de Incidentes (NIST SP 800-61, ISO/IEC 27035-1, SANS); 14 Defesa em Profundidade e Zero Trust (NIST SP 800-207); 15 Operações de Segurança (SIEM, SOC, EDR, WAF, NAT, CVE/CVSS, gestão de vulnerabilidades); 16 Nuvem (ISO/IEC 27017) e IA em Segurança; 17 Referências e Conferência. A apostila passou de cerca de 13 para 20 páginas.

## A conferir (não foi possível verificar em fonte livre)
- Textos das normas ISO/ABNT são pagos: estrutura e controles seguem o conteúdo público conhecido. Conferir no texto oficial da ABNT ao estudar.
- Fases da ISO/IEC 27035-1:2023 (cinco fases) e a citação da NIST SP 800-61 Rev. 3 (2025): conferir na fonte.
- Um resultado de busca sugere mudança de nomenclatura dos certificados ICP-Brasil a partir de 2025 (fim dos nomes A1, A2 e A3). Não confirmado; consultar o ITI.
- Lista OWASP Top 10 for LLM Applications e taxonomia NIST AI 100-2 citadas apenas como referência.
- Rótulo "cobrado em prova" não foi usado em nenhum ponto novo, porque não há questão do banco ligada a esses tópicos ainda (Fase 4).

## Próximo passo
Questões novas (verificáveis) para os tópicos das seções 11 a 16 e vínculo `topico_edital` (Fase 4).
