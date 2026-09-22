# Apostila 10 (nova): Inglês Técnico para TI, e correção transversal do LaTeX

Data: 21/09/2026.

## Inglês Técnico (nova, 11 seções, 14 páginas)
Fonte do escopo: programa SEFAZ-CE 2026 (FCC), área B02, que cita "Inglês Técnico".
Seções: 1 Estratégias de leitura (skimming, scanning, julgar certo ou errado); 2 Conectivos e palavras de referência; 3 Tempos verbais e voz passiva; 4 Verbos modais e RFC 2119; 5 Comparativos, condicionais, quantificadores e orações relativas; 6 Formação de palavras, phrasal verbs de TI; 7 Falsos cognatos; 8 Vocabulário de TI por área; 9 Notas de versão, READMEs, mensagens de erro e relatórios de incidente; 10 Treino com três textos originais e 12 itens certo ou errado, cada um com justificativa citando o trecho; 11 Referências.
Cuidados: os textos e itens são originais (não reproduzem provas); "exit" e "pull/push" foram retirados da lista de falsos cognatos por não serem falsos cognatos; o foco (leitura e interpretação) deve ser ajustado quando o edital e a banca da SEFAZ-BA forem conhecidos.

## Correção transversal: LaTeX literal nos PDFs
Problema: fórmulas escritas em LaTeX (`$...$`, `\frac`, `\times`, `\sum` etc.) apareciam literais nos PDFs, porque o gerador (FPDF) não interpreta LaTeX. Havia ainda escapes corrompidos em Auditoria Fiscal (`\times` gravado como tabulação seguida de "imes").
Solução: `dados/auditoria_apostilas/latex_para_texto.py`, conversor único que:
- protege o "R$" (reais);
- repara os escapes corrompidos;
- converte apenas os segmentos entre cifrões, com 25 comandos LaTeX mapeados (frac, binom, sqrt, bar, text, sum, times, símbolos gregos, relações e conjuntos);
- gera texto legível (por exemplo, `RA = (RI x RC) x RD`, `P(A|B) = (P(A inter B)) / (P(B))`, `Z(alfa/2) = 1,96`, `soma (i = 1 até k) de P(Bi) x P(A|Bi)`).
Verificação: conferido o antes e o depois dos 192 trechos antes de aplicar; corrigidos 4 defeitos de legibilidade do próprio conversor (subscritos, barra, letra grega colada a número, somatório com limites); corrigidos à mão 2 trechos danificados pela proteção do "R$" (Risco de Distorção Relevante e o limite do boxplot). Resultado: 21 PDFs, 349 páginas, 0 resíduos de LaTeX.
Apostilas afetadas: Estatística e RLM (a maior), Auditoria Fiscal, Legislação Tributária BA, Direito Administrativo, Finanças Públicas e Contabilidade Geral (as duas últimas com setas e símbolos).
Pendente nessas apostilas: a auditoria de conteúdo (Fase 1), que segue na ordem combinada.
