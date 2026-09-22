# Concurso SEFAZ Dashboard - Painel de Preparação Integrada

Painel de estudos e acompanhamento estratégico para o concurso da Secretaria da Fazenda do Estado da Bahia (SEFAZ-BA), focado nos cargos de Auditor Fiscal (Especialidade Tecnologia da Informação) e Agente de Tributos Estaduais.

## Principais Funcionalidades

- **Trilhas de Estudo Diferenciadas**: Trilhas completas com checklist de progresso para Auditor Fiscal (TI) e Agente de Tributos.
- **Apostilas Digitais Estruturadas**: Módulos pedagógicos em formato PDF gerados com chancela editorial YLuna85 LABs e glossário de siglas.
- **Banco de Questões e Casos Práticos**: Treinamento focado em questões de bancas examinadoras (FCC, CEBRASPE, FGV) e estudos de caso discursivos.
- **Gamificação do Aprendizado**: Sistema de XP e níveis, sequência diária de estudo (streak), conquistas (badges) e fila de revisão espaçada das questões erradas no simulado, tudo salvo localmente no navegador (localStorage), sem necessidade de backend ou login.
- **Videoaulas e Referências**: Curadoria de materiais, aulas magnas e orientações de carreira para o cargo de Auditor de TI.
- **Glossário de Siglas**: Catálogo completo de termos contábeis, fiscais e tecnológicos.

## Arquitetura e Estrutura de Arquivos

-  pp.py: Servidor Flask local que fornece a API REST para progresso, simulados, questões e listagem de apostilas.
- index.html: Interface web responsiva em estilo Bento Grid, com alternância de trilhas e controles de acessibilidade.
-  uild_all_apostilas_ptbr.py: Compilador automatizado que gera cadernos e apostilas em formato PDF na pasta Concurso SEFAZ/.
- apostilas_conteudo.json: Base de dados estruturada em JSON com 18 apostilas completas.
- harness.py: Suíte de autoteste padronizada que valida integridade documental, sintaxe e ativos web.
- static/js/gamificacao.js: Motor de gamificação (XP, níveis, streak, badges e fila de revisão espaçada), 100% client-side via localStorage.
- testar_gamificacao.py: Suíte Playwright que valida ponta a ponta o motor de gamificação (XP por tópico e por questão, badges, alerta e carregamento da fila de revisão).

## Como Executar

Para iniciar o painel localmente:

1. Execute o arquivo EXECUTAR_CONCURSO_SEFAZ_DASHBOARD.bat ou utilize o terminal:
   ```bash
   python app.py
   ```
2. Acesse o painel pelo navegador em:
   ```
   http://localhost:5000
   ```

## Log de Atualizações

### 22/09/2026 - Versão 2.17.0
- Sistema de gamificação do aprendizado (static/js/gamificacao.js): XP por tópico marcado na trilha (10 XP) e por questão de simulado respondida (15 XP acerto, 2 XP tentativa), níveis progressivos com rótulo (Iniciante a Mestre Fiscal), sequência diária de estudo (streak) com badges em 3, 7 e 30 dias, conquistas por marcos de simulado e por trilha/apostila concluída, e fila de revisão espaçada (intervalos de 1, 3, 7 e 30 dias) para questões erradas, com botão dedicado "Revisão Espaçada" na aba de Simulados. Widget de progresso na aba Painel Geral. Tudo salvo em localStorage (`sefaz_gamificacao_v1`), sem backend.
- Corrigido sidestripe (`border-left`) remanescente no item ativo do menu lateral (static/css/style.css), substituído por brilho interno sem borda lateral colorida.
- Nova suíte testar_gamificacao.py (Playwright, 6/6 verificações), validando o fluxo completo em navegador real.
### 21/09/2026 - Versão 2.16.0
- Apostila de Auditoria Fiscal e Contábil auditada (9 correções, relatório em dados/auditoria_apostilas/12_auditoria_fiscal.md) e ampliada de 10 para 18 seções: afirmações e respostas ao risco (NBC TA 315 e 330), outras NBC TA, fraude em detalhe, amostragem em detalhe, relatório do auditor, base legal da fiscalização tributária (CTN 138, 142, 149, 150, 173 e 194 a 200; LC 105/2001; Lei 8.137/1990) e auditoria fiscal de estoques; 21 páginas. Presunção de omissão de saídas corrigida para relativa (Lei 7.014/1996, art. 4º, §4º, confirmada em fonte oficial).
### 21/09/2026 - Versão 2.15.0
- Apostila de Estatística e RLM auditada (11 correções, relatório em dados/auditoria_apostilas/11_estatistica.md) e ampliada de 10 para 20 seções: complementos de lógica e conjuntos, porcentagem, PA e PG, geometria, matemática financeira (SAC, Price, VPL, TIR), dados agrupados, amostragem, inferência, regressão, séries temporais e análise multivariada; 23 páginas. Todos os exemplos numéricos foram recalculados.
### 21/09/2026 - Versão 2.14.0
- Nova apostila (21ª): Inglês Técnico para TI (11 seções, 14 páginas), com estratégias de leitura, conectivos, modais e RFC 2119, phrasal verbs, falsos cognatos, vocabulário de TI, notas de versão e treino certo ou errado com textos originais.
- Correção transversal: as fórmulas em LaTeX que apareciam literais nos PDFs foram convertidas em texto legível em todas as apostilas (dados/auditoria_apostilas/latex_para_texto.py); 21 PDFs, 349 páginas, sem resíduos. Relatório em dados/auditoria_apostilas/10_ingles_e_latex.md.
- Bloco de TI concluído (matriz: 64 de 65 tópicos cobertos; o restante é medido por palavra-chave). Próximo: auditoria de conteúdo das apostilas de conhecimentos gerais.
### 21/09/2026 - Versão 2.13.0
- Apostila de Redes de Computadores e Telecomunicações auditada (9 correções, relatório em dados/auditoria_apostilas/09_redes.md) e ampliada de 10 para 23 seções: sub-redes e IPv6 em detalhe, serviços (DNS, DHCP, HTTP, e-mail), TCP e UDP, roteamento (OSPF, EIGRP, BGP), Wi-Fi 6/6E/7 e 5G, WAN e acesso remoto, SDN e VXLAN, QoS e VoIP, administração e comunicação de dados; 26 páginas.
### 21/09/2026 - Versão 2.12.0
- Nova apostila (20ª): Computação em Nuvem (AWS, Azure e Google Cloud), 15 seções e 18 páginas: modelos e multicloud, redes (VPC, grupos de segurança, NACL), VPN, Direct Connect, ExpressRoute e Interconnect, computação e serverless, dados em nuvem, IAM, RBAC e MFA, KMS, Zero Trust, IaC, FinOps, alta disponibilidade, migração e mapa de equivalência de serviços. Relatório em dados/auditoria_apostilas/08_nuvem.md.
### 21/09/2026 - Versão 2.11.0
- Apostila de Engenharia de Software auditada (9 correções, relatório em dados/auditoria_apostilas/07_desenvolvimento.md) e ampliada de 10 para 23 seções: processos ágeis, requisitos (MoSCoW, Kano, BDD, ISO 25010), GRASP, GoF completo, estilos de arquitetura e DDD, microsserviços (BFF, CQRS, Saga, service mesh, 12-factor), CORS/CSRF/XSS/SSO, testes e SonarQube, Java/Spring Boot, Angular, persistência (Hibernate, Redis, MongoDB, Flyway, Liquibase), Gitflow/Jenkins/Tekton e Análise de Pontos de Função; 26 páginas. Fórmulas em LaTeX reescritas.
### 21/09/2026 - Versão 2.10.0
- Apostila de Ciência de Dados e Big Data auditada (13 correções, relatório em dados/auditoria_apostilas/06_ia.md) e ampliada de 10 para 20 seções: paradigmas de aprendizado, deep learning, IA generativa e LLMs (RAG, LoRA), agentes e sistemas multiagentes, MLOps, ética e governança de IA (LGPD art. 20, NIST AI RMF, ISO/IEC 42001), regressão e boas práticas, Hadoop e Spark em detalhe e Python; 23 páginas. Fórmulas em LaTeX reescritas em texto.
- Achado transversal registrado no plano: 7 apostilas ainda com LaTeX literal nos PDFs, a corrigir na Fase 1 de cada uma.
### 21/09/2026 - Versão 2.9.0
- Apostila de Banco de Dados e BI auditada (12 correções, relatório em dados/auditoria_apostilas/05_dados.md) e ampliada de 10 para 20 seções: índices e otimização, PL/SQL e SQL procedural, concorrência e recuperação (2PL estrito e rigoroso, MVCC, ARIES), colunar e formatos (Parquet, Avro), Lakehouse e Data Mesh, ingestão, pipelines, qualidade de dados e streaming; 23 páginas.
### 21/09/2026 - Versão 2.8.0
- Nova apostila (19ª): Middleware, Mensageria e Observabilidade (14 seções, 17 páginas): WildFly/JBoss EAP, mensageria e EIP, ActiveMQ, Kafka, CDC e Debezium, Kubernetes avançado, Ansible, Helm, Podman, Prometheus, Grafana, Zabbix, ELK, APM e OpenTelemetry. Relatório em dados/auditoria_apostilas/04_middleware.md.
- O gerador de PDFs atualiza automaticamente a lista de contingência de apostilas do main.js (antes desatualizada, com 15 itens).
- README: as apostilas agora são 19 (a contagem "18" da versão 2.2.0 está superada).
### 21/09/2026 - Versão 2.7.0
- Apostila de Infraestrutura, Cloud e DevOps auditada (5 correções, relatório em dados/auditoria_apostilas/03_infraestrutura.md) e ampliada de 10 para 17 seções: Linux Red Hat (LVM, SELinux, firewalld), Windows Server e Active Directory (FSMO, Kerberos, GPO), virtualização VMware e Hyper-V, backup, tipos de storage, SAN (zoning e LUN masking) e cálculos de disponibilidade; 20 páginas.
### 21/09/2026 - Versão 2.6.0
- Apostila de Gestão e Governança de TI auditada (13 correções, relatório em dados/auditoria_apostilas/02_governanca.md) e ampliada de 10 para 16 seções: PETIC/PDTIC e portfólio, contratações de TIC pela Lei 14.133/2021 (ETP, TR, SLA), gestão financeira (TCO, ROI, CAPEX/OPEX, FinOps), BPM (BPMN, DMN, BPMS) e Lean/Six Sigma; 19 páginas.
### 21/09/2026 - Versão 2.5.0
- Apostilas, Fase 0: matriz de cobertura do programa de TI (SEFAZ-CE 2026 B02, FCC, e SEFAZ-BA 2022) em dados/matriz_edital.json, gerada por gerar_matriz_edital.py (65 tópicos). Plano completo em PLANO_ATUALIZACAO_APOSTILAS.md.
- Apostilas, Fase 1: Apostila de Segurança da Informação auditada (11 correções, relatório em dados/auditoria_apostilas/01_seguranca.md) e ampliada de 10 para 17 seções (riscos ISO 31000/27005, continuidade, incidentes, Zero Trust, operações de segurança, nuvem e IA, referências); 20 páginas. OWASP Top 10:2025 incluída.
- build_all_apostilas_ptbr.py aceita um trecho do nome para gerar só uma apostila.
### 21/09/2026 - Versão 2.4.0
- Regra de conteúdo: o banco só mantém questão com fundamento verificável. Toda explicação cita norma, padrão ou conta refeita; onde não há fundamento seguro, o item fica com explicação mínima e revisao = "explicacao_minima".
- SEFAZ-CE 2021 (CEBRASPE, Auditor Fiscal de TI): as 158 questões foram reconstruídas do caderno oficial e conferidas com o gabarito oficial definitivo (59/60 básicos e 99/100 específicos; itens 29 e 81 anulados ficam de fora). Assunto e tópico foram corrigidos pelo conteúdo real (antes eram atribuídos por posição), e os textos-base foram recolocados. 8 itens ficam ocultos (dependem de figura ou têm símbolos corrompidos, ou legislação superada). Script: reconstruir_sefaz_ce_2021.py e dados/sefaz_ce_2021_itens.json.
- TRF1 2024 (FGV): o Analista (Suporte em TI) confere 40/40 com o gabarito oficial preliminar e recebeu explicações; os itens de norma do Judiciário e de Direito Penal ficam fora do escopo da SEFAZ-BA. O Técnico (TI) divergia do gabarito oficial em 28 de 40 itens (ex.: item 41, cache: 512 conjuntos e 9 bits) e a FGV retificou o gabarito definitivo, então as 40 ficam ocultas até haver gabarito verificado. Script: ajustar_trf1_2024.py.
- As 30 "variantes" em texto-molde foram substituídas por 30 questões novas (ids ylabs_001 a ylabs_030), cada uma com fundamento citado (CTN, CF/88, Lei 14.133/2021, LGPD, RFCs, Scrum Guide, ITIL 4 etc.). Script: organizar_banco.py.
- Questões antigas: rótulos "(Adaptada)" e "(Simulada)" trocados por "Inédita - elaborada por YLuna85 LABs"; marcadas revisao = "legado_nao_auditado" (auditoria factual pendente); q_gen_15 oculta (DIFAL em compra para revenda).
- Cargos por edital: cada questão tem cargos (auditor_ti, agente) e escopo (edital_ba_2022, correlato, fora), com base no edital oficial da SEFAZ-BA 2022 (FGV, Edital nº 001/2022). O edital do Auditor Fiscal 2026 ainda não foi publicado. Simulado do Auditor (TI): 317 questões; do Agente de Tributos: 79.
- Simulado: alternativas embaralhadas a cada execução (gabarito e justificativas remapeados), exceto quando o texto depende da posição ("todas as anteriores", "I e II" etc.) e nas questões Certo/Errado.
- testar_simulado.py verifica 792 respostas nos dois cargos, o remapeamento do gabarito e a ausência de itens ocultos.

### 21/09/2026 - Versão 2.3.0
- Correção crítica do simulado: 396 de 530 questões (Certo/Errado da SEFAZ-CE e itens do TRF1) tinham alternativas em lista e o gabarito nunca era reconhecido. O banco foi normalizado para o esquema único options = {"A": ...} por normalizar_questoes.py, e o front-end (main.js) ficou tolerante aos formatos antigos.
- Remoção de 128 cópias exatas entre as variantes da SEFAZ-CE (530 para 402 questões); reclassificadas as questões tec_77 e tec_80 do TRF1 (direito penal, antes em Redes); corrigidos artefatos de OCR.
- Escape de HTML nos enunciados e alternativas (antes, <main> e o XML da questão tec_71 sumiam da tela) e quebras de linha preservadas.
- Novo teste 4/4 no harness.py (esquema de questions.json) e testar_simulado.py (Playwright, 1104 respostas verificadas, 0 falhas). Backup: questions.backup_20260921.json.

### 08/09/2026 - Versão 2.2.0
- Incorporação de duas novas apostilas temáticas em formato PDF na pasta Concurso SEFAZ/ geradas pelo compilador oficial: Apostila 17 (Redes de Computadores e Telecomunicações) e Apostila 18 (Infraestrutura Cloud e DevOps), com 10 seções analíticas cada.
- Mineração factual das provas oficiais de Analista e Técnico Judiciário de TI do concurso TRF 1ª Região (FGV 2024).
- Adição de 80 novas questões de TI comentadas no simulado (questions.json), elevando o acervo de 450 para 530 questões com gabarito oficial e justificativa detalhada por alternativa.
- Validação integral e aprovação de 3/3 testes no harness.py.

### 08/09/2026 - Versão 2.1.0
- Adição da nova apostila Apostila_Auditoria_Fiscal_TI.pdf compilada a partir da transcrição completa da aula magna sobre a carreira de Auditor Fiscal de TI.
- Incorporação de 10 capítulos dedicados à carreira, gestão de sistemas críticos, fiscalização de contratos sob a Lei 14.133/2021 e método de estudos.
- Atualização da ementa de Auditoria de TI no arquivo static/js/main.js e inclusão do link direto da aula na seção de videoaulas em index.html.
- Higienização completa do README e validação de 100% de aprovação na suíte de autoteste harness.py.
