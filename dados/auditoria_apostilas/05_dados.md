# Auditoria 05: Apostila de Banco de Dados, BI e Engenharia de Dados

Data: 21/09/2026. Escopo: as 10 seções originais (conferidas) e lacunas de engenharia de dados frente ao programa SEFAZ-CE 2026 (B02) e ao edital SEFAZ-BA 2022.

## Conteúdo conferido e mantido
Arquitetura ANSI/SPARC e independências lógica e física; álgebra relacional (a projeção elimina duplicatas, o SELECT não); modelagem ER (atributos, entidade fraca, cardinalidade e participação, especialização); mapeamento N:M por tabela associativa; formas normais 1FN a 5FN e BCNF; DDL, DML, DCL e TCL; junções; WHERE versus HAVING; window functions (ROW_NUMBER, RANK, DENSE_RANK, LEAD, LAG); ACID, níveis de isolamento ANSI e anomalias; 2PL; WAL; BASE; famílias NoSQL; características do DW (Inmon); Inmon versus Kimball; ETL versus ELT; DW versus data lake (schema-on-write e schema-on-read); tabelas fato, medidas aditivas, semiaditivas e não aditivas; dimensões conformadas e degeneradas; SCD tipos 1, 2 e 3; estrela e floco de neve; operações OLAP.

## Correções
| # | Trecho original | Problema | Correção |
|---|---|---|---|
| 1 | DAMA-DMBOK "11 áreas" com Ética na lista e Governança fora | A 11ª área é Governança de Dados (no centro); a ética é tema de um capítulo próprio | Lista das 11 áreas corrigida |
| 2 | TRUNCATE "redefine sequências auto-incremento" e "é DDL" | Depende do SGBD: MySQL e SQL Server reiniciam; PostgreSQL só com RESTART IDENTITY; o padrão SQL o classifica entre comandos de dados; rollback varia (Oracle e MySQL confirmam implicitamente) | Reescrito com as diferenças |
| 3 | CAP: "nenhum sistema distribuído pode ser CA" e "garantir apenas duas das três" | Simplificação; a escolha ocorre durante a partição | Reescrito com o contexto da partição e o modelo PACELC |
| 4 | HAVING "exclusivamente sobre funções agregadas" | Também pode usar colunas do GROUP BY | Corrigido |
| 5 | UNION "executa ordenação implícita" | Pode usar ordenação ou hash | Corrigido |
| 6 | Grafos "utilizados no Fisco para rastreamento de laranjas" | Afirmação de uso sem fonte | Reescrito como cenário de aplicação |
| 7 | Trigger que falha causa "Rollback automático" da transação | Desfaz a instrução; o efeito sobre a transação depende do SGBD | Corrigido |
| 8 | Repeatable Read "no padrão ANSI pode permitir fantasma" sem nuance | Correto pelo padrão, mas PostgreSQL e InnoDB previnem fantasmas na prática | Nuance incluída |
| 9 | Surrogate key "NUNCA... obrigatoriamente" | Afirmação absoluta; é recomendação | Reescrito como recomendação |
| 10 | Mnemônico "fórmula jurídica de William Kent... que Deus nos ajude" | A variação "so help me Codd" é trocadilho | Atribuição esclarecida |
| 11 | Erro de digitação "Muitos-para-Mutos" | Digitação | Corrigido |
| 12 | Seção 10 "análise estatística das provas fiscais revela..." | Alegação estatística sem fonte | Renomeada e reescrita sem alegação |

## Seções acrescentadas (11 a 20)
11 Índices, otimização e administração de SGBDs (B-tree, hash, bitmap, clusterizado, plano de execução, junções, particionamento, PITR, Oracle, SQL Server e PostgreSQL); 12 SQL procedural (PL/SQL, T-SQL, PL/pgSQL, cursores, CTE); 13 Concorrência e recuperação (2PL estrito e rigoroso, deadlock, timestamp, MVCC, ARIES); 14 Bancos colunares e formatos (Parquet, ORC, Avro, particionamento); 15 Arquiteturas (data mart, medalhão, Lakehouse com Delta, Iceberg e Hudi, Data Mesh, Data Fabric, Lambda e Kappa); 16 Integração e ingestão (REST e SOAP, TLS, mascaramento, buffer, cargas incrementais); 17 Pipelines (ETL e ELT, Airflow, retries, checkpoints, CI/CD, linhagem); 18 Governança e qualidade de dados (seis dimensões, catálogo, papéis, MDM, deduplicação); 19 Streaming (janelas, watermarks, Spark Structured Streaming, Flink); 20 Referências e conferência.

## A conferir
Comportamento específico por SGBD e versão (TRUNCATE, isolamento, PITR); formatos de tabela abertos e suas versões; ferramentas citadas como exemplo.

## Ligação com a questão da SEFAZ-CE 2021
A apostila agora cobre os conceitos dos itens 74 (ELT), 76 (fato e dimensão), 79 (DW: não volátil e variante no tempo) e 83 (GROUP BY e HAVING) do banco de questões, cujas explicações já foram reescritas.
