# Auditoria 07: Apostila de Engenharia de Software, Desenvolvimento e Arquiteturas

Data: 21/09/2026. Escopo: as 10 seções originais (conferidas) e lacunas frente ao programa SEFAZ-CE 2026 (B02) e ao edital SEFAZ-BA 2022 (que inclui Análise de Pontos de Função, testes e documentos de teste).

## Conteúdo conferido e mantido
Cascata, espiral (4 quadrantes) e RUP (4 fases); RF e RNF (FURPS+); processo de engenharia de requisitos; INVEST; UML 2.5 (visibilidades, associação, agregação, composição, casos de uso, sequência, atividades, estados); SOLID; GoF (23 padrões em 3 categorias, os criacionais completos); monolito versus microsserviços; API Gateway, service discovery, circuit breaker e saga; Clean Architecture e a regra de dependência; seis princípios do REST; métodos HTTP e idempotência; códigos de status; pirâmide de testes; caixa-preta e caixa-branca; TDD (Red, Green, Refactor); Git (três áreas, rebase, merge, cherry-pick, stash); CI, entrega e implantação contínuas; blue-green e canário.

## Correções
| # | Trecho original | Problema | Correção |
|---|---|---|---|
| 1 | `V(G) = E - N + 2P` e outras fórmulas em LaTeX (`$...$`, `\text`) em 3 pontos | Símbolos apareciam literais no PDF | Reescritas em texto |
| 2 | "Alto Acoplamento Coesivo e Baixo Acoplamento" | Erro de termo | "Alta Coesão e Baixo Acoplamento" |
| 3 | DIP com "(Injeção de Dependências)" | DIP é o princípio; a injeção de dependências é uma técnica; IoC é o conceito mais amplo | Distinguidos |
| 4 | Observer "padrão Pub/Sub" | No Observer o sujeito conhece os observadores; no Pub/Sub há intermediário | Diferença explicada |
| 5 | Pirâmide de Testes atribuída a Martin Fowler | Conceito de Mike Cohn, difundido por Fowler | Atribuição corrigida |
| 6 | Valores limite "onde ocorre a maioria dos erros" | Afirmação empírica sem fonte | "Onde os defeitos são mais frequentes" |
| 7 | REST "usa o protocolo HTTP nativo para comunicação síncrona" | REST é um estilo, normalmente sobre HTTP, e não é necessariamente síncrono; faltava HATEOAS na interface uniforme | Reformulado; HATEOAS incluído |
| 8 | UML 2.5 com 5 diagramas estruturais e 4 comportamentais listados | Os 14 diagramas são 7 estruturais e 7 comportamentais; a versão vigente é a 2.5.1 | Completado |
| 9 | Seção 10 "armadilhas... cobradas pelas bancas" | Sem evidência | Renomeada |

## Seções acrescentadas (11 a 23)
11 Outros modelos de processo e agilidade (incremental, prototipação, modelo em V, Manifesto Ágil, XP, ISO 12207); 12 Requisitos em profundidade (elicitação, MoSCoW, Kano, BDD e Gherkin, Design Thinking, Lean Inception, ISO/IEC 25010); 13 GRASP (os nove), coesão, acoplamento, DRY, KISS, YAGNI e Deméter; 14 GoF complementares (Bridge, Flyweight, Iterator, Mediator, Memento, State, Visitor, Interpreter); 15 Estilos de arquitetura (camadas, MVC, MVP, MVVM, SOA versus microsserviços, orientada a eventos, DDD); 16 Microsserviços (BFF, CQRS, Event Sourcing, Saga, circuit breaker, service mesh, Strangler Fig, 12-factor); 17 APIs e segurança web (CORS, CSRF, XSS, SSO, mTLS, REST versus SOAP, Richardson); 18 Testes avançados (dublês, MC/DC, SAST, DAST, SonarQube, JUnit, Mockito, Jest, Playwright); 19 Linguagens e frameworks (Java, Spring Boot, Python, TypeScript, Angular, React Native); 20 Persistência (Hibernate, Redis, MongoDB, Flyway, Liquibase); 21 DevOps no desenvolvimento (Gitflow, Jenkins, Tekton, feature flags); 22 Métricas e APF (ALI, AIE, EE, SE, CE, VAF, PFNA e PFA); 23 Referências.

## A conferir
Detalhes de versões de Spring Boot, Angular e ferramentas; regras de contagem da APF na versão do manual do IFPUG adotada; comportamento do GIL do Python na versão usada.

## Ligação com o banco de questões
A apostila cobre agora os conceitos dos itens 66 a 71 da SEFAZ-CE 2021 (HTML5 main, etnografia, sequência com alt, teste de subclasses, GRASP e Django/MTV) e da questão 90 da mesma prova (EAP), com as explicações já reescritas.
