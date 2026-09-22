# Aprofundamento Parte A: Bloco de TI (Fase 2 do plano mestre)

Data: 22/09/2026. Escopo: 10 das 11 apostilas de TI, cada uma recebendo uma seção nova de aprofundamento (a 11ª, Auditoria Fiscal TI, já havia sido corrigida na etapa 21 e não é conteúdo técnico, ficando fora desta rodada).

## Seções novas acrescentadas

| Apostila | Seção nova | Conteúdo |
|---|---|---|
| Banco de Dados e BI | Otimização de Consultas e Planos de Execução | EXPLAIN/EXPLAIN ANALYZE, regra do prefixo mais à esquerda em índices compostos, estatísticas do otimizador, Nested Loop/Hash Join/Merge Join |
| Ciência de Dados e Big Data | RAG, Agentes e Métricas de Avaliação de Modelos | Arquitetura RAG, agentes e uso de ferramentas, matriz de confusão (precisão, recall, F1), curva ROC e AUC |
| Segurança da Informação | Zero Trust na Prática e DevSecOps | Pilares do Zero Trust (NIST SP 800-207), SASE, SAST/DAST/SCA, shift left security |
| Gestão e Governança de TI | Estudo de Caso de Contratação de TIC (Lei 14.133/2021) | Sequência DOD/ETP/Análise de Riscos/TR (IN SGD/ME 94/2022), modelo de execução e gestão, IMR |
| Engenharia de Software | Padrões de Microsserviços na Prática | Saga (coreografia e orquestração), CQRS, BFF, Circuit Breaker |
| Redes de Computadores e Telecom | SD-WAN, SASE e VoIP na Prática | SD-WAN, SASE, codecs G.711/G.729, MOS, QoS para voz |
| Infraestrutura, Cloud e DevOps | Kubernetes Avançado e SRE | Operators/CRDs, Service Mesh (Istio/Linkerd), SLI/SLO/Error Budget |
| Middleware, Mensageria e Observabilidade | Arquitetura Orientada a Eventos, gRPC e Resiliência | EDA, Event Sourcing, gRPC, Circuit Breaker/Retry/Bulkhead |
| Computação em Nuvem | FinOps na Prática e Segurança em Nuvem | Rightsizing, reservadas versus spot, tagging, políticas de IAM, criptografia de envelope (KMS) |
| Inglês Técnico para TI | Treino 2: Textos com Itens Certo ou Errado | Dois novos textos originais (Zero Trust e responsabilidade compartilhada em nuvem) com gabarito comentado |

## Metodologia

Todo o conteúdo acrescentado é conhecimento técnico consolidado e amplamente documentado (padrões de arquitetura de software, práticas de SRE, conceitos de FinOps, protocolos de rede), não dependendo de fontes normativas específicas sujeitas a mudança de numeração, com exceção do estudo de caso de contratação de TIC, cuja sequência de artefatos foi conferida contra a Lei nº 14.133/2021 e a IN SGD/ME nº 94/2022 já citadas na própria apostila de Governança. Nenhuma nova pesquisa externa foi necessária para o restante do conteúdo, por se tratar de definições técnicas estáveis (Saga, CQRS, Zero Trust, RAG, FinOps, SD-WAN, VoIP, Kubernetes).

## Resultado

Todas as 21 apostilas do acervo foram revalidadas (JSON íntegro) e regeneradas em lote via `build_all_apostilas_ptbr.py`. As 10 apostilas de TI aprofundadas ganharam entre 1 e 2 páginas adicionais cada, aproximando-as da meta de 30 a 60 páginas da Fase 3 do plano mestre nas matérias mais pesadas.

## Próximos passos

Parte B do aprofundamento: bloco de Legislação e Conhecimentos Gerais (10 apostilas), a executar em sequência.
