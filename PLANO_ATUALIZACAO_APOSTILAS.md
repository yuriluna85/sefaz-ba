# Plano de atualização das apostilas (Concurso SEFAZ Dashboard)

Elaborado em 21/09/2026. Regra mestra: **todo conteúdo verdadeiro e verificável** (cada afirmação com fonte; o que não puder ser conferido não entra ou fica marcado "conferir").

## 1. Situação do edital

| Item | Situação |
|---|---|
| **SEFAZ-BA 2026** | Sem edital publicado. Última informação confirmada: 04/08/2026 (Estratégia Concursos, com base no Sindsefaz e na Comissão Organizadora). Previsão de edital: setembro ou, no máximo, outubro/2026. Banca não definida naquele momento. Provas previstas entre dez/2026 e jan/2027. 200 vagas imediatas (100 Auditor Fiscal e 100 Agente de Tributos) mais cadastro de reserva. Não consegui confirmar nada posterior a agosto; a fonte oficial é o Diário Oficial do Estado e o site da SAEB/SEFAZ. |
| **SEFAZ-CE 2026 (FCC)** | Edital nº 01/2026 publicado em 24/04/2026. Provas em 01 e 02/08/2026. Resultado preliminar em 09/09/2026 (Edital nº 06/2026). Cargo Auditor-Fiscal, área B02 - Tecnologia da Informação. **O programa oficial já foi baixado e lido**; é a melhor referência atual de conteúdo de TI. |
| Base usada até aqui | SEFAZ-BA 2022 (FGV, Agente de Tributos, edital oficial) e SEFAZ-CE **2021** (CEBRASPE). O CE 2026 ainda não foi usado. |

Hierarquia de fontes de conteúdo: (1) edital SEFAZ-BA 2026, quando sair; (2) SEFAZ-CE 2026 B02 (FCC; a SEFAZ-BA usou FCC em 2019); (3) SEFAZ-BA 2022 (FGV); (4) CE 2021 (CEBRASPE). Partes exclusivas do Ceará (Constituição, legislação e programas estaduais do CE) ficam de fora.

## 2. O programa de TI do CE 2026 (B02) em blocos
Governança, gestão e contratações de TIC (PETIC/PDTIC, Lei 14.133 com ETP/TR/SLA, TCO/ROI/CAPEX/OPEX/FinOps, ISO 31000, COBIT 2019, ITIL 4, PMBOK 7, MPS.BR, CMMI 2.0, BPMN/DMN/BPMS, Six Sigma). Segurança e cibernética (CID, defesa em profundidade, Zero Trust, ISO 27001:2022, 27002:2022, 27005:2023, 27035-1:2023, 22301:2020, 27017, NIST SP 800-61, LGPD, BIA, PCN/DRP/RPO/RTO, IAM/RBAC/SSO/MFA/OAuth 2.0/OIDC, PKI/X.509/ICP-Brasil, TLS, firewall/NGFW/IDS/IPS/WAF/VPN/SIEM/SOC/EDR, OWASP, DevSecOps). Infraestrutura (redes, SDN, Wi-Fi; Windows Server, Linux, AD, VMware, Hyper-V; backup, SAN, storage, deduplicação; JBoss/WildFly, ActiveMQ, Kafka, Debezium, Kubernetes, Ansible, Zabbix, Prometheus, Grafana, ELK, APM). Nuvem (IaaS/PaaS/SaaS, multicloud, serverless, event-driven, KMS, Direct Connect/ExpressRoute, AWS/Azure/GCP, Data Lakes). Dados (relacional/colunar/NoSQL, PL/SQL, DW, Data Lake, Lakehouse, Data Mesh, ETL, Parquet, streaming, governança de dados). Ciência de Dados e IA (Python, Hadoop, Spark, ML, deep learning, PLN, IA generativa, agentes, MLOps, ética e viés). Engenharia de software (GoF, EIP, BFF/CQRS/Saga/Circuit Breaker, Java/Python/TypeScript, Spring Boot, Angular, testes, REST, CORS/CSRF/XSS, Git/Gitflow, CI/CD, Docker/Helm). Gestão de projetos, produtos e serviços (requisitos, Scrum, Kanban, MoSCoW, Kano, Design Thinking, Lean Inception, Lean IT/Kaizen, viabilidade). Inglês técnico.
Conhecimentos gerais do Auditor: Língua Portuguesa, Matemática Financeira/Estatística/RLM, Administração e Governança Pública, Economia, Direito Constitucional, Administrativo, Civil, Penal, Financeiro, Contabilidade Geral e Pública, Auditoria (NBC TA). Específicos comuns: Direito Tributário, Reforma Tributária (EC 132, LC 214/2025, LC 227/2026), legislação tributária nacional, Contabilidade Avançada e de Custos, Finanças Públicas.

## 3. Lacunas nas 18 apostilas atuais
Confiáveis (busca por termo com resultado zero): Zero Trust, ISO 27005, ISO 31000, Apache Kafka, MLOps, BPMN/DMN, FinOps/TCO, LC 214/2025, Economia (Pareto, Ramsey, Laffer), Contabilidade Avançada (equivalência patrimonial, arrendamento), NBC TSP/MCASP e Inglês técnico. Vários outros termos são apenas citados, sem que se saiba a profundidade (a Fase 1 mede isso). Cada apostila atual tem cerca de 13 páginas e 10 seções, o que é raso para matérias como Redes, Cloud, Segurança e Engenharia de Software.

## 4. Fases

**Fase 0 - Matriz de cobertura (1 sessão).** Arquivo `dados/matriz_edital.json`: cada tópico do programa (CE 2026 B02, gerais do CE 2026, BA 2022) com apostila responsável, status (ausente, raso, adequado), fonte e prioridade. Quando o edital da BA sair, rodamos a comparação e reordenamos tudo.

**Fase 1 - Auditoria das 18 apostilas atuais (3 a 4 sessões).** Conferir cada afirmação factual com a fonte (norma, padrão, livro da biblioteca local); corrigir o que estiver errado; restaurar a acentuação em pt-BR (a Apostila 15 e outras estão sem acentos); atualizar o que mudou (por exemplo, 8.666 para 14.133; PMBOK 5 e 6 para 7; ISO 27001:2013 para 2022). Saída: relatório de erros por apostila.

**Fase 2 - Novas apostilas e aprofundamento, por prioridade.**
- P1, TI (Auditor): (a) Segurança cibernética e gestão de riscos; (b) Infraestrutura: SO, virtualização, armazenamento e backup; (c) Middleware, mensageria e observabilidade; (d) Nuvem e FinOps; (e) Engenharia de dados; (f) IA e Ciência de Dados (com IA generativa e MLOps); (g) Desenvolvimento e arquiteturas; (h) Gestão de projetos, produtos, serviços e processos; (i) Governança e contratações de TIC; (j) Inglês técnico; ampliar Redes.
- P2, gerais do Auditor: Direito Tributário e Reforma Tributária; legislação tributária nacional; Constitucional; Administrativo (14.133, LAI, LGPD, 12.846, 8.429); Contabilidade e Auditoria; Economia; Finanças Públicas e Direito Financeiro; Estatística, Matemática Financeira e RLM; Penal; Civil; Português.
- P3, Agente de Tributos: Informática Básica, Legislação Tributária da Bahia (Lei 7.014/1996, COTEB, RICMS/BA etc.), RLM. Só reforçar depois do edital, porque o 2022 é a única referência.

**Fase 3 - Padrão de qualidade de cada apostila.** Metas: 30 a 60 páginas nas matérias pesadas de TI. Cada seção com: conceito, base normativa com artigo ou cláusula, quadro comparativo, exemplo, "como a banca cobra" (só com base em questão real do banco, citando o ID), questões vinculadas por tópico e resumo. Lista de referências no fim, com data de conferência e versão da legislação. Nada sem fonte. Observação: as normas ISO/ABNT são pagas, então o texto sobre elas se limita à estrutura e aos controles publicamente documentados, com aviso.

**Fase 4 - Integração ao app.** Campo `topico_edital` nas questões (liga apostila, questão e edital), aba de estudo com progresso por seção e base para a gamificação.

**Fase 5 - Atualização quando o edital da BA sair.** Diff da matriz, ajuste de prioridades e do perfil da banca (FCC, FGV ou CEBRASPE), e revisão do escopo dos simulados.

## 5. Decisões pendentes do usuário
1. Começar pelo Auditor (TI) e deixar o Agente para depois do edital?
2. Ordem P1 sugerida: Segurança, Governança/Contratações, Infraestrutura, Dados/IA, Desenvolvimento. Confirmar.
3. Formato: manter PDF e acrescentar leitura em HTML dentro do app?
4. Ritmo: 2 a 3 apostilas por sessão, com relatório de fontes ao final de cada uma.

## 6. Achados transversais (21/09/2026)
- **Fórmulas em LaTeX literais nos PDFs** (`$...$`, `\frac`, `\times`): já corrigidas nas apostilas de Governança e de Ciência de Dados. Ainda presentes em Estatística e RLM (muitas), Auditoria Fiscal (inclusive escapes corrompidos, como tabulação + "imes"), Legislação Tributária BA, Engenharia de Software, Finanças Públicas e Contabilidade Geral. O "R$" é legítimo. Cada uma será corrigida na Fase 1 da sua apostila; o gerador de PDFs não interpreta LaTeX.
- **Rótulos "armadilhas da FGV/CEBRASPE"** com alegação estatística sem fonte: removidos das apostilas já auditadas (Segurança, Governança, Dados, Ciência de Dados); conferir nas demais.
- **Lista de contingência de apostilas** do main.js agora é regravada automaticamente pelo gerador de PDFs.

## 7. Auditoria 13 (22/09/2026): Legislação Tributária da Bahia
Apostila auditada: 6 correções (presunção de omissão indevidamente atribuída ao art. 54 do COTEB quando está na Lei nº 7.014/96; alíquota geral do ICMS desatualizada em 19%, hoje 20,5% desde 07/02/2024; tabela de alíquotas do IPVA por categoria sem confirmação em fonte primária, agora como faixa de referência a conferir; base legal e alíquotas do ITD trocadas, lei correta é a nº 14.802/2024, não a nº 14.634/2023; faltavam os artigos do PAF/BA e do IPVA). Relatório completo em `dados/auditoria_apostilas/13_legislacao_tributaria_ba.md`.

## 8. Auditoria 14 (22/09/2026): Finanças Públicas e Orçamento
Apostila auditada sem erro factual encontrado nas 10 seções originais (PPA/LDO/LOA, princípios orçamentários, créditos adicionais, receita e despesa pública, LRF e dívida pública todos conferidos contra CF, Lei 4.320/64 e LC 101/2000). Ampliada com 3 seções novas para cobrir a lacuna de Direito Financeiro: Precatórios (EC 113/2021 e EC 114/2021), Dívida dos Estados com a União (Lei 9.496/1997 e LC 148/2014) e Fundo de Compensação de Benefícios Fiscais do ICMS (LC 214/2025). Relatório completo em `dados/auditoria_apostilas/14_financas_publicas.md`.

## 9. Auditoria 15 (22/09/2026): Contabilidade Geral e de Custos
Apostila auditada: 2 correções (percentuais fechados de 10% e 50% para passivo contingente possível, que o CPC 25 não fixa numericamente; mnemônico "DEPA" incompleto para a ordem de 5 participações estatutárias, corrigido para "DEPPA" com o art. 190 da Lei 6.404/76). Ampliada com a seção de Contabilidade Aplicada ao Setor Público (NBC TSP e MCASP: 4 subsistemas contábeis, VPA/VPD e PCASP), preenchendo lacuna confirmada no item 3 deste plano. Relatório completo em `dados/auditoria_apostilas/15_contabilidade_geral.md`.

## 10. Auditoria 16 (22/09/2026): Língua Portuguesa
Apostila auditada sem erro factual encontrado nas 10 seções originais de sintaxe e redação oficial. Ampliada com a seção de Ortografia (Acordo de 1990), Acentuação e Semântica (trema, acento facultativo em forma/fôrma, regras de acentuação, homônimos, parônimos, polissemia, denotação/conotação e figuras de linguagem), preenchendo lacuna para o nível de Agente de Tributos. Relatório completo em `dados/auditoria_apostilas/16_lingua_portuguesa.md`.

## 11. Auditoria 17 (22/09/2026): Direito Constitucional
Apostila auditada sem erro factual encontrado nas 10 seções originais (teoria da Constituição, direitos fundamentais, organização do Estado, Administração Pública, processo legislativo, sistema tributário, imunidades e repartição de receitas). Ampliada com a seção de Reforma Tributária Constitucional (EC nº 132/2023: IBS, CBS e Imposto Seletivo, cronograma de transição 2026-2033), lacuna relevante que não constava no Sistema Tributário Nacional descrito. Relatório completo em `dados/auditoria_apostilas/17_direito_constitucional.md`.

## 12. Auditoria 18 (22/09/2026): Direito Administrativo
Apostila auditada: 1 correção (valores de dispensa de licitação desatualizados, corrigidos para os vigentes em 2026 pelo Decreto nº 12.807/2025: R$ 130.984,20 para obras/engenharia e R$ 65.492,11 para os demais serviços e compras). Demais 9 seções sem erro encontrado, inclusive a Lei de Improbidade reformada e o Estatuto do Servidor da Bahia (Lei 6.677/1994, número confirmado). Ampliada com a seção de LAI, LGPD e Lei Anticorrupção (Leis 12.527/2011, 13.709/2018 e 12.846/2013), lacuna apontada no programa do plano mestre. Relatório completo em `dados/auditoria_apostilas/18_direito_administrativo.md`.

## 13. Auditoria 19 (22/09/2026): Direito Tributário
Apostila auditada sem nenhuma correção necessária nas 10 seções (teoria pentapartida, obrigação e responsabilidade tributária, lançamento, suspensão, extinção, exclusão/garantias e Reforma Tributária), incluindo a confirmação da composição do Comitê Gestor do IBS (27 representantes dos Estados e DF, 27 dos Municípios, LC nº 227/2026). Nenhuma lacuna relevante identificada; apostila não foi ampliada nesta etapa. Relatório completo em `dados/auditoria_apostilas/19_direito_tributario.md`.

## 14. Auditoria 20 (22/09/2026): Igualdade Racial e de Gênero
Apostila auditada: 1 correção terminológica ("Súmula Vinculante" do TSE não existe; o instrumento correto é a Súmula nº 73 do TSE, de 2024, sobre fraude à cota de gênero, com ressalva de debate mais recente em 2026 ainda não pacificado). Demais 9 seções sem erro encontrado, inclusive a Lei da Igualdade Salarial e a natureza objetiva do feminicídio confirmadas. Apostila não foi ampliada por ausência de lacuna relevante. Relatório completo em `dados/auditoria_apostilas/20_igualdade_racial_genero.md`.

## 15. Auditoria 21 (22/09/2026): Carreira e Auditoria Fiscal na Especialidade TI
Achado principal: era a única apostila do acervo inteiramente sem acentuação gráfica (violação da regra 19 do laboratório), passando despercebida nas etapas anteriores por não ser prioridade técnica/jurídica. Reescrita integral das 10 seções com acentuação completa. Corrigidas também 4 passagens com cifras salariais e percentuais fechados sem fonte (remuneração inicial, "concurso iminente" da SEFAZ-BA sem edital publicado, percentuais de aproveitamento mínimo e de peso da discursiva), substituídas por orientação para conferir o dado exato no edital vigente. Relatório completo em `dados/auditoria_apostilas/21_auditoria_fiscal_ti.md`. Com esta etapa, encerra-se a sequência combinada de Direito Constitucional, Administrativo, Tributário, Igualdade Racial e Auditoria Fiscal TI. Todas as 21 apostilas do acervo já passaram por ao menos uma auditoria completa.

## Fase 2 - Aprofundamento

### Parte A (22/09/2026): Bloco de TI
Acrescentada 1 seção nova de aprofundamento em cada uma de 10 das 11 apostilas de TI (Banco de Dados, Ciência de Dados, Segurança, Governança, Engenharia de Software, Redes, Infraestrutura, Middleware, Nuvem e Inglês Técnico), cobrindo temas de ponta não detalhados antes (RAG e agentes de IA, Zero Trust operacional e DevSecOps, Saga/CQRS/BFF, SD-WAN/SASE/VoIP, Kubernetes avançado e SRE, arquitetura orientada a eventos e gRPC, FinOps e segurança em nuvem, estudo de caso de contratação de TIC pela Lei 14.133/2021, otimização de consultas SQL). A apostila de Auditoria Fiscal TI (carreira) ficou fora por já ter sido corrigida na etapa anterior e não ser conteúdo técnico. Todas as 21 apostilas revalidadas e regeneradas em lote. Relatório completo em `dados/auditoria_apostilas/22_aprofundamento_parte_a_ti.md`.

### Parte B (22/09/2026): Bloco de Legislação e Conhecimentos Gerais
Resolvida com fonte primária a pendência da tabela de alíquotas do IPVA/BA (art. 6º, não art. 5º, da Lei nº 6.348/1991, texto confirmado). Acrescentada 1 seção nova em 9 apostilas: Direito Constitucional (contencioso administrativo do IBS e modulação de efeitos), Direito Administrativo (sanções do art. 156 e fase de habilitação da Lei 14.133/2021), Direito Tributário (exercícios de decadência e prescrição), Legislação Tributária da Bahia (exemplo numérico de ICMS-ST), Auditoria Fiscal contábil (exercício de amostragem e caso de estoques), Finanças Públicas (exercícios de RCL e limites de pessoal), Contabilidade Geral (exercícios de DFC e ponto de equilíbrio), Estatística e RLM (intervalo de confiança e teste de hipótese) e Língua Portuguesa (banco de questões de crase e regência). A apostila de Igualdade Racial ficou sem alteração por a pendência do debate do TSE ainda estar em aberto, sem posição definitiva a registrar. Todas as 21 apostilas revalidadas e regeneradas em lote. Relatório completo em `dados/auditoria_apostilas/23_aprofundamento_parte_b_legislacao.md`. Com esta etapa, encerra-se a Fase 2 (aprofundamento) da rodada combinada com o usuário.
