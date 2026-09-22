# Auditoria 11: Apostila de Estatística e Raciocínio Lógico-Matemático

Data: 21/09/2026. Escopo: as 10 seções originais (conferidas, com recálculo dos exemplos) e lacunas frente ao programa SEFAZ-CE 2026 (Matemática Financeira, Estatística e Raciocínio Lógico) e ao edital SEFAZ-BA 2022 (RLM: lógica, conjuntos, números, porcentagem, proporcionalidade, medidas, estrutura lógica, contagem, probabilidade, geometria básica e noções de estatística; e Estatística: distribuições, inferência, regressão, amostragem, análise multivariada e séries temporais).

## Conteúdo conferido e mantido
Princípios da lógica clássica; conectivos e tabelas; tautologia, contradição e contingência; equivalências (contrapositiva, disjuntiva), negação da condicional e De Morgan; negação de quantificadores; validade, modus ponens e tollens; PFC, permutações, arranjo, combinação e combinação com repetição; probabilidade (Laplace, união, condicional, independência, total e Bayes); média, mediana, moda, quartis e IQR; variância, desvio-padrão, CV, covariância e correlação; Bernoulli, binomial e Poisson; normal, erro padrão e t, qui-quadrado e F; IC, hipóteses, erros Tipo I e II, poder, valor-p; regressão e R2.

## Correções
| # | Trecho original | Problema | Correção |
|---|---|---|---|
| 1 | "[mu - 2 sigma, mu + 2 sigma] (mais precisamente Z = 1,96): contém exatamente 95%" | 2 desvios-padrão contêm cerca de 95,45%; 95% corresponde a 1,96 desvio-padrão | Corrigido e valores críticos (90%, 95%, 99%) listados |
| 2 | 68,26% em 1 sigma | O valor arredondado é 68,27% | Corrigido |
| 3 | Z de 99% = 2,575 | O valor é 2,576 (2,5758) | Corrigido |
| 4 | Exemplo de permutação com repetição "SEFAZ ou BANCO" | Essas palavras não têm letras repetidas | Exemplo BANANA (60 anagramas) |
| 5 | "Combinação: C(n, p) = C(n, p) = ..." | Redundância de conversão | Fórmula limpa e exemplo |
| 6 | Média "SEMPRE" maior que a mediana na assimetria à direita | Regra prática, com exceções | "Em geral" |
| 7 | "Média 4 e variância 4: inequivocamente Poisson" | Igualdade é compatível com a Poisson, mas não a demonstra | Reformulado |
| 8 | "Média das amostras terá distribuição perfeitamente normal" | O TCL é uma aproximação | "Aproximadamente normal" |
| 9 | Aproximação Binomial por Poisson e "n >= 30" como regras fixas | Regras práticas que variam entre autores | Rotuladas como regras práticas |
| 10 | Erro Tipo II como "aceitar H0 falsa" | Tecnicamente, "não rejeitar" | Corrigido |
| 11 | Seção 10 "armadilhas... exploradas pelas bancas" | Alegação sem evidência | Renomeada |

## Seções acrescentadas (11 a 20)
11 Lógica: complementos (linhas da tabela-verdade, recíproca e inversa, silogismos, falácias, verdades e mentiras, conjuntos com inclusão e exclusão); 12 Porcentagem, razão, proporção, regra de três, PA e PG; 13 Geometria básica, unidades e medidas; 14 Matemática financeira (juros simples e compostos, taxas equivalentes, nominais e reais, descontos, capitalização contínua, anuidades, SAC, Price, SAM, VPL e TIR); 15 Distribuições de frequência, dados agrupados (média, mediana e moda de Czuber), assimetria, médias geométrica e harmônica e gráficos; 16 Amostragem (probabilística e não probabilística), tamanho da amostra e qui-quadrado; 17 Inferência em detalhe (z e t, proporção, unilateral e bilateral, IC, poder); 18 Regressão em detalhe (MQO, SQT, SQR, SQE, exemplo completo, múltipla, ANOVA); 19 Séries temporais, médias móveis, números-índices e análise multivariada; 20 Referências.

## Verificação numérica
Recalculados em Python: BANANA = 60; C(5,2) = 10; PA: termo 10 = 32 e soma 185; PG 700, 770 e 847: soma 2.317; 1% a.m. = 12,6825% a.a.; taxa real 4,76%; PMT Price = 482,54; SAC: 520, 480 e 440; IC = [46,08; 53,92]; n = 384,16; regressão: b1 = 0,6, b0 = 2,2, r = 0,7746, R2 = 0,6; normal: 68,27%, 95,45% e 99,73%; z90 = 1,645, z95 = 1,96, z99 = 2,576.

## A conferir
Regras práticas variam entre autores (n >= 30, n >= 100 e p <= 0,01, número de classes de Sturges); notação de cada banca.
