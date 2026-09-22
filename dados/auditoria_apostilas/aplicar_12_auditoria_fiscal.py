"""Aplica a auditoria da Apostila de Auditoria Fiscal e Contábil (Fase 1) e acrescenta o que faltava do programa SEFAZ-CE 2026
(Auditoria: NBC TA 230, 240, 265, 300, 315, 320, 500, 501, 505, 530, 540, 610, 620, 700; auditoria de estoque; papéis de
trabalho) e a base legal da fiscalização tributária. Idempotente. Relatório: dados/auditoria_apostilas/12_auditoria_fiscal.md
Uso (na pasta do app): python dados/auditoria_apostilas/aplicar_12_auditoria_fiscal.py
"""
import json
import os
import sys

APP = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARQ = os.path.join(APP, 'apostilas_conteudo.json')
dados = json.load(open(ARQ, encoding='utf-8'))
ap = next(a for a in dados if a['filename'] == 'Apostila_Auditoria_Fiscal.pdf')
S = ap['sections']

if any(s['title'].startswith('11.') for s in S):
    print('Apostila de Auditoria Fiscal já atualizada; nada a fazer.')
    sys.exit(0)


def bul(sec, inicio):
    return next(b for b in sec['bullets'] if b[0].strip().startswith(inicio))


def trocar(txt, velho, novo):
    assert velho in txt, 'trecho não encontrado: ' + velho[:70]
    return txt.replace(velho, novo)


# ---- Seção 1 ----
b = bul(S[0], 'Postulados da Auditoria Fiscal')
b[0] = 'Fundamentos da Fiscalização Tributária'
b[1] = ('A fiscalização tributária é atividade administrativa vinculada e obrigatória (CTN, art. 142, parágrafo único): o agente fiscal '
        'verifica a ocorrência do fato gerador, determina a matéria tributável, calcula o tributo, identifica o sujeito passivo e '
        'propõe a penalidade cabível, sob pena de responsabilidade funcional. A base legal dos poderes de fiscalização está nos arts. '
        '194 a 200 do CTN (seção 16). Não se confunde com a auditoria independente, que emite opinião sobre demonstrações contábeis.')

# ---- Seção 5 ----
b = bul(S[4], 'Prazo de Montagem')
b[0] = 'Prazo de Montagem e Guarda dos Papéis de Trabalho'
b[1] = ('A orientação da NBC TA 230 é concluir a montagem final do arquivo de auditoria em prazo apropriado após a data do relatório do '
        'auditor, em geral não superior a 60 dias. A retenção da documentação segue o controle de qualidade do auditor (NBC PA 01): '
        'período suficiente para atender às exigências, não inferior a cinco anos a partir da data do relatório; a regulação da CVM '
        'também exige cinco anos para auditores de companhias abertas. Confira o texto vigente.')

# ---- Seção 6 ----
S[5]['content'] = trocar(S[5]['content'], 'de modo que todas as unidades de amostragem tenham a mesma chance de serem selecionadas',
                         'de modo que todas as unidades de amostragem tenham chance de serem selecionadas')
S[5]['tip'][0] = 'Qual Risco de Amostragem Mais Preocupa'

# ---- Seção 7 ----
b = bul(S[6], 'Tipos de Fraude')
b[1] = trocar(b[1], 'apropriação indevida de políticas contábeis', 'aplicação indevida de políticas contábeis')

# ---- Seção 9 ----
b = bul(S[8], 'Auditoria de Estoques e Apuração')
b[1] = ('Verificação do Bloco K (Controle da Produção e do Estoque) e do Bloco H (Inventário). Fórmula fundamental: Estoque Inicial + '
        'Compras = Estoque Final + Vendas ou Consumo. As diferenças podem indicar omissão de saídas ou de entradas (veja a seção 17). Na '
        'Bahia, a Lei nº 7.014/1996, art. 4º, §4º, autoriza a presunção de omissão de saídas de mercadorias tributáveis quando a '
        'escrituração indica saldo credor de caixa, suprimentos de caixa não comprovados, manutenção no passivo de obrigações já pagas ou '
        'inexistentes, entradas de mercadorias não registradas ou declarações de vendas por meio de cartão de crédito ou débito em valor '
        'inferior ao informado pelas administradoras, entre outras hipóteses (confira a redação vigente).')
S[8]['tip'] = ['Presunção Legal de Omissão: é Relativa',
               'Na Lei nº 7.014/1996 (art. 4º, §4º), a presunção de omissão de saídas é relativa: ressalva-se ao contribuinte a prova da '
               'improcedência da presunção. Ela inverte o ônus da prova, mas não impede a defesa. O lançamento exige processo regular '
               'e o direito ao contraditório.']

# ---- Seção 10 ----
S[9]['title'] = '10. Armadilhas Conceituais Recorrentes em Auditoria'
S[9]['content'] = ('Pontos conceituais que costumam gerar erro em questões de Auditoria Fiscal e Contábil. Servem de revisão rápida; a base '
                   'de cada ponto está nas seções anteriores.')
for i, bl in enumerate(S[9]['bullets']):
    if bl[0].startswith('Pegadinha 8'):
        S[9]['bullets'][i] = ['Pegadinha 8: Papéis de Trabalho',
                              'Os papéis de trabalho pertencem ao auditor (ou à firma de auditoria), sujeitos ao sigilo profissional, e '
                              'devem ser retidos por no mínimo cinco anos a partir da data do relatório (NBC PA 01).']
S[9]['tip'] = ['Síntese Final de Auditoria',
               'A auditoria fornece segurança razoável, não absoluta. O auditor planeja procedimentos para detectar distorções relevantes, '
               'inclusive por fraude, mas a responsabilidade primária pela prevenção e detecção é da administração. Distorção relevante '
               'localizada leva à ressalva; generalizada, à opinião adversa; e limitação de escopo generalizada, à abstenção.']


def sec(t, c, bl, tip):
    S.append({'title': t, 'content': c, 'bullets': bl, 'tip': tip})


sec('11. Afirmações, Riscos de Distorção e Respostas do Auditor (NBC TA 315 e 330)',
    'O auditor avalia o risco de distorção relevante por afirmações e define procedimentos de auditoria que respondem a esses riscos.',
    [['Afirmações sobre classes de transações e eventos',
      'Ocorrência (as transações ocorreram e pertencem à entidade), integridade (todas foram registradas), exatidão (valores e dados '
      'corretos), corte (registradas no período certo) e classificação (nas contas adequadas).'],
     ['Afirmações sobre saldos de contas',
      'Existência, direitos e obrigações (a entidade tem os direitos sobre os ativos e as obrigações), integridade e valorização ou '
      'alocação (o valor está adequado e os ajustes, corretamente registrados).'],
     ['Afirmações sobre apresentação e divulgação',
      'Ocorrência e direitos e obrigações, integridade, classificação e compreensibilidade, e exatidão e valorização.'],
     ['Riscos significativos',
      'Riscos identificados que exigem atenção especial da auditoria, como os de fraude e os de estimativas complexas. Exigem obter '
      'entendimento dos controles relacionados e resposta específica.'],
     ['Respostas gerais e procedimentos adicionais (NBC TA 330)',
      'Respostas em nível geral (supervisão, imprevisibilidade, ceticismo) e procedimentos adicionais em nível de afirmação: testes de controles '
      'e procedimentos substantivos (testes de detalhes e procedimentos analíticos substantivos), com natureza, época e extensão ligadas '
      'ao risco avaliado.'],
     ['Testes de controles versus substantivos',
      'Testes de controles avaliam a eficácia operacional dos controles. Procedimentos substantivos detectam distorções nas afirmações. Se '
      'o risco é significativo, é preciso realizar procedimentos substantivos; testes de controles isolados não bastam.']],
    ['Para Cada Risco, uma Afirmação e um Procedimento',
     'Estoque inexistente (afirmação de existência) pede contagem física. Passivo omitido (integridade) pede confirmações e busca de '
     'passivos não registrados. Venda em período errado (corte) pede teste de corte na data-base.'])
sec('12. Outras NBC TA do Programa: 265, 501, 540, 550, 560, 570, 580, 610, 620 e 720',
    'Resumo de normas de auditoria que aparecem no programa e em provas.',
    [['NBC TA 265: deficiências de controle interno',
      'O auditor comunica por escrito, tempestivamente, as deficiências significativas de controle interno aos responsáveis pela governança '
      'e à administração.'],
     ['NBC TA 501: considerações específicas',
      'Estoques: se os estoques são relevantes, o auditor deve estar presente à contagem física, observar a contagem e testá-la. Litígios '
      'e reclamações: indagar a administração e, em regra, os assessores jurídicos, e obter confirmação por escrito quando necessário.'],
     ['NBC TA 540: estimativas contábeis',
      'Avalia métodos, dados e premissas das estimativas, o risco de viés da administração e as divulgações. Estimativas envolvem incerteza e '
      'julgamento; considera-se um intervalo de resultados razoáveis.'],
     ['NBC TA 550: partes relacionadas',
      'Exige entender as relações e transações com partes relacionadas e avaliar os riscos, inclusive de fraude, e a divulgação adequada.'],
     ['NBC TA 560: eventos subsequentes',
      'Eventos que fornecem evidência de condições que já existiam na data do balanço exigem ajuste; os que refletem condições surgidas '
      'depois exigem apenas divulgação, se relevantes.'],
     ['NBC TA 570: continuidade operacional',
      'O auditor avalia se o uso da base de continuidade é apropriado e se há incerteza relevante. Havendo incerteza adequadamente '
      'divulgada, o relatório inclui seção sobre incerteza relevante, sem modificar a opinião; se a divulgação for inadequada, a opinião '
      'é modificada.'],
     ['NBC TA 580: representações formais',
      'A carta de representação da administração confirma declarações e reduz mal-entendidos, mas não substitui evidência de auditoria '
      'apropriada e suficiente.'],
     ['NBC TA 610: uso do trabalho da auditoria interna',
      'O auditor externo avalia objetividade, competência e sistematização do trabalho da auditoria interna. Pode usar o trabalho ou '
      'a assistência direta, mas a responsabilidade pela opinião é exclusivamente do auditor externo.'],
     ['NBC TA 620: especialistas do auditor',
      'O auditor avalia competência, capacidade e objetividade do especialista e a adequação do trabalho, e mantém a responsabilidade '
      'pela opinião. O relatório com opinião não modificada não faz referência ao especialista.'],
     ['NBC TA 720: outras informações',
      'O auditor lê as outras informações que acompanham as demonstrações e considera se há inconsistência relevante com as demonstrações '
      'ou com o conhecimento obtido na auditoria.']],
    ['Responsabilidade pela Opinião é Sempre do Auditor',
     'Mesmo usando o trabalho de auditores internos (TA 610) ou de especialistas (TA 620), o auditor externo mantém a responsabilidade '
     'exclusiva pela opinião e não a divide.'])
sec('13. Fraude em Detalhe: Procedimentos Obrigatórios e Presunções (NBC TA 240)',
    'Complementa a seção 7 com o que a norma exige do auditor diante do risco de fraude.',
    [['Discussão da equipe e indagações',
      'A equipe discute a suscetibilidade das demonstrações à fraude. O auditor indaga a administração e outros sobre riscos, e sobre '
      'a existência de denúncias ou suspeitas.'],
     ['Presunção de risco na receita',
      'A norma presume que há risco de fraude no reconhecimento de receita. O auditor avalia quais tipos de receita, transações ou '
      'afirmações originam esse risco. A presunção pode ser afastada com justificativa documentada.'],
     ['Desrespeito de controles pela administração',
      'O risco de desrespeito de controles pela administração (management override) existe em toda entidade. Procedimentos obrigatórios: '
      'testar lançamentos contábeis e outros ajustes, revisar estimativas contábeis em busca de viés e avaliar a racionalidade de '
      'transações significativas fora do curso normal.'],
     ['Sinais de alerta',
      'Pressões para atingir metas, controles fracos, rotatividade da alta administração, transações complexas com partes relacionadas, '
      'documentos ausentes, alterações tardias em registros e explicações evasivas.'],
     ['Comunicação e limitações',
      'O auditor comunica a fraude ou suspeita à administração e aos responsáveis pela governança, e, quando exigido por lei, às '
      'autoridades. A auditoria tem limitação inerente: fraude com conluio e falsificação é mais difícil de detectar que erro.']],
    ['Receita e Controles Burlados: Riscos Sempre Presentes',
     'Toda auditoria trata o reconhecimento de receita como risco presumido de fraude e considera o desrespeito de controles pela '
     'administração. Lançamentos manuais fora de padrão são alvo dos testes.'])
sec('14. Amostragem em Detalhe: Distorção Tolerável, Projeção e Avaliação (NBC TA 530)',
    'Complementa a seção 6 com os elementos que determinam e avaliam a amostra.',
    [['Distorção tolerável',
      'Valor fixado pelo auditor, a partir da materialidade de execução, que é o máximo de distorção que o auditor aceita na população '
      'sem concluir que ela contém distorção relevante. Quanto menor a distorção tolerável, maior a amostra.'],
     ['Fatores que aumentam o tamanho da amostra',
      'Maior risco de distorção relevante, menor distorção tolerável, maior distorção esperada, maior confiança desejada e população '
      'muito heterogênea (a estratificação reduz a amostra).'],
     ['Unidade de amostragem',
      'Item, linha ou unidade monetária. Na amostragem por unidade monetária (MUS), cada real é uma unidade, o que dá maior chance de seleção '
      'aos itens de maior valor.'],
     ['Avaliação dos resultados',
      'O auditor projeta as distorções encontradas na amostra para a população e compara com a distorção tolerável. Se a projeção '
      'excede ou se aproxima da tolerável, o risco de a população conter distorção relevante é inaceitável, e o auditor amplia os testes '
      'ou solicita ajuste.'],
     ['Desvios e distorções',
      'Nos testes de controles, o que se conta são desvios (falhas do controle) e a taxa de desvio tolerável. Nos testes de detalhes, são '
      'distorções em valor. Itens anômalos (distorções claramente não representativas) podem ser excluídos da projeção, com justificativa.'],
     ['Estratificação',
      'Separar itens de valor elevado (testados 100%) dos demais (amostrados) reduz a variabilidade e o tamanho da amostra.']],
    ['Menor Tolerância, Maior Amostra',
     'A distorção tolerável e o tamanho da amostra variam em sentidos opostos: quando o auditor aceita menos distorção, precisa testar '
     'mais itens.'])
sec('15. Relatório do Auditor: Estrutura e Comunicações (NBC TA 700, 701, 705, 706)',
    'Complementa a seção 8 com a estrutura do relatório e as comunicações relacionadas.',
    [['Estrutura do relatório (NBC TA 700)',
      'Título e destinatário; Opinião (primeira seção); Base para opinião; incerteza relevante de continuidade operacional (quando '
      'houver); Principais Assuntos de Auditoria (quando aplicável); Outras informações; responsabilidades da administração e dos '
      'responsáveis pela governança; responsabilidades do auditor; assinatura, local e data. A data do relatório não pode ser anterior à '
      'obtenção de evidência apropriada e suficiente.'],
     ['Base para opinião nas modificações',
      'Quando a opinião é modificada, o relatório inclui a seção "Base para opinião com ressalva", "Base para opinião adversa" ou "Base '
      'para abstenção de opinião", que descreve a razão da modificação.'],
     ['PAAs (NBC TA 701)',
      'Descrevem os assuntos mais significativos da auditoria, por que foram considerados e como foram tratados. Exigidos para '
      'companhias abertas; não substituem a opinião e não são uma opinião separada.'],
     ['Ênfase e outros assuntos (NBC TA 706)',
      'O parágrafo de ênfase refere-se a assunto divulgado nas demonstrações e é fundamental para o entendimento. O de outros assuntos '
      'refere-se a assunto não divulgado nas demonstrações. Nenhum deles modifica a opinião.'],
     ['Comunicação com a governança (NBC TA 260)',
      'O auditor comunica às pessoas responsáveis pela governança o alcance e a época da auditoria, achados significativos e '
      'deficiências de controle. A comunicação é tempestiva e, em regra, por escrito quando relevante.']],
    ['Opinião Primeiro, Base Depois',
     'No relatório atual, a seção de opinião vem primeiro, seguida da base para opinião. A modificação da opinião vem descrita na base '
     'para opinião modificada.'])
sec('16. Fiscalização Tributária: Base Legal Nacional (CTN, LC 105/2001 e Lei 8.137/1990)',
    'Fundamentos legais dos poderes e limites da fiscalização, essenciais ao Auditor Fiscal.',
    [['CTN, art. 142: lançamento',
      'O lançamento é o procedimento administrativo que verifica o fato gerador, determina a matéria tributável, calcula o tributo, '
      'identifica o sujeito passivo e, se for o caso, propõe a penalidade. É atividade vinculada e obrigatória, sob pena de '
      'responsabilidade funcional.'],
     ['CTN, arts. 194 a 196: competência e poderes',
      'Art. 194: a legislação tributária regula a competência e os poderes das autoridades administrativas em matéria de fiscalização. '
      'Art. 195: não se aplicam disposições legais que excluam ou limitem o direito de examinar mercadorias, livros, arquivos, documentos, '
      'papéis e efeitos comerciais ou fiscais; os livros obrigatórios e seus comprovantes devem ser conservados até a prescrição dos '
      'créditos tributários. Art. 196: a autoridade lavra os termos para documentar o início do procedimento, e a legislação fixa prazo '
      'máximo para sua conclusão.'],
     ['CTN, art. 197: dever de informar',
      'Tabeliães, bancos e instituições financeiras, empresas de administração de bens, corretores, inventariantes, síndicos e '
      'outros são obrigados a prestar informações. Não abrange fatos sob segredo profissional por cargo, ofício, função, ministério, '
      'atividade ou profissão.'],
     ['CTN, arts. 198 e 199: sigilo e troca de informações',
      'Art. 198: veda a divulgação, pela Fazenda e seus servidores, de informação obtida sobre a situação econômica ou financeira do sujeito '
      'passivo ou de terceiros e sobre a natureza e o estado de seus negócios ou atividades, com exceções (requisição judicial e '
      'solicitações da Administração em processo administrativo regularmente instaurado). Art. 199: as Fazendas públicas prestam mútua '
      'assistência e permutam informações, na forma da lei ou de convênio.'],
     ['CTN, art. 138: denúncia espontânea',
      'Exclui a responsabilidade por infrações se acompanhada do pagamento do tributo devido e dos juros de mora. Não é espontânea a '
      'denúncia apresentada após o início de qualquer procedimento administrativo ou medida de fiscalização relacionados com a infração.'],
     ['CTN, arts. 149, 150, §4º, e 173: lançamento de ofício e prazos',
      'O lançamento é feito de ofício nas hipóteses do art. 149 (por exemplo, quando não prestada a declaração ou comprovada falsidade). '
      'No lançamento por homologação, o prazo decadencial é de cinco anos contados do fato gerador, salvo dolo, fraude ou simulação '
      '(art. 150, §4º); nos demais casos, aplica-se o art. 173.'],
     ['LC nº 105/2001, art. 6º: exame de dados bancários',
      'Autoridades e agentes fiscais tributários dos Estados podem examinar documentos, livros e registros de instituições financeiras, '
      'inclusive de contas de depósitos e aplicações, quando houver processo administrativo instaurado ou procedimento fiscal em curso e '
      'o exame for considerado indispensável pela autoridade administrativa competente. O resultado é conservado em sigilo.'],
     ['Lei nº 8.137/1990 e Súmula Vinculante 24',
      'A Lei nº 8.137/1990 define crimes contra a ordem tributária. Pela Súmula Vinculante 24 do STF, não se tipifica crime material '
      'contra a ordem tributária (art. 1º, I a IV) antes do lançamento definitivo do tributo.']],
    ['Denúncia Espontânea: Antes de Qualquer Procedimento',
     'Iniciado o procedimento fiscal, a denúncia deixa de ser espontânea, e o contribuinte perde o benefício da exclusão de responsabilidade '
     'por infrações do art. 138.'])
sec('17. Auditoria Fiscal de Estoques: Levantamento Quantitativo',
    'Técnica de fiscalização que compara o movimento de mercadorias com os estoques para revelar omissões.',
    [['Lógica do levantamento',
      'Estoque final calculado = estoque inicial + entradas (com nota) - saídas (com nota). Compara-se com o estoque final real, apurado '
      'no inventário (Bloco H da EFD).'],
     ['Estoque real menor que o calculado',
      'Indica saídas sem documento fiscal: omissão de saídas de mercadorias tributáveis.'],
     ['Estoque real maior que o calculado',
      'Indica entradas não registradas: omissão de entradas. A ocorrência de entradas sem documentação autoriza a presunção de omissão '
      'de saídas anteriores (por exemplo, na Bahia, pela Lei nº 7.014/1996, art. 4º, §4º), salvo prova em contrário.'],
     ['Cuidados na apuração',
      'Uniformizar unidades de medida e códigos de itens, considerar perdas, quebras, bonificações, devoluções e transferências, '
      'respeitar o período e permitir que o contribuinte apresente justificativas. Falhas de escrituração do contribuinte podem gerar '
      'diferenças aparentes.'],
     ['Bloco K e produção',
      'Em indústrias, o Bloco K (controle da produção e do estoque) permite comparar consumo de insumos e produção, e identificar '
      'divergências entre insumo consumido, produto acabado e vendas.'],
     ['Regulamentação estadual',
      'Cada Estado disciplina os roteiros de auditoria de estoques. Na Bahia, confira a norma que regula o levantamento quantitativo por espécie '
      'de mercadorias (a Portaria SEFAZ nº 445/1998 é citada na literatura; confirme a norma vigente).']],
    ['Menos no Real, Saída sem Nota; Mais no Real, Entrada sem Nota',
     'Se falta mercadoria no estoque real em relação ao calculado, houve saída não documentada. Se sobra, houve entrada não registrada.'])
sec('18. Referências e Conferência',
    'Conferência realizada em 21/09/2026.',
    [['Referências',
      'NBC TA 200, 230, 240, 260, 265, 300, 315 (R2), 320, 330, 500, 501, 505, 520, 530, 540, 550, 560, 570, 580, 610, 620, 700, 701, 705, 706 e '
      '720; NBC PA 01; NBC TI 01; Lei nº 5.172/1966 (CTN), arts. 138, 142, 149, 150, 173 e 194 a 200; LC nº 105/2001; Lei nº '
      '8.137/1990; Súmula Vinculante 24; Lei nº 7.014/1996 (BA), art. 4º, §4º; COSO 2013; Edital SEFAZ-CE 2026 (FCC), Anexo VI.'],
     ['Corrigido nesta revisão',
      'Referência a um "Art. 54 da COTEB" removida (a presunção está na Lei nº 7.014/1996, art. 4º, §4º); presunção de omissão descrita '
      'como "absoluta" corrigida para relativa; "independência funcional do Auditor Fiscal" trocada pelo fundamento do art. 142 do CTN; '
      '"mesma chance" na amostragem para "chance"; "apropriação indevida de políticas contábeis" para "aplicação indevida"; retenção dos '
      'papéis de trabalho atribuída à norma correta; título da seção de armadilhas sem atribuição a bancas; síntese final reescrita.'],
     ['A conferir',
      'Texto vigente da Lei nº 7.014/1996, art. 4º, §4º, e da norma estadual de auditoria de estoques; numeração e revisões das NBC TA; '
      'prazos de guarda da CVM e do CFC; se o edital da SEFAZ-BA cobrará auditoria contábil (NBC TA) ou apenas fiscalização tributária.']],
    ['Regra de Conteúdo', 'Este material não afirma nada sem fonte. Se houver divergência com a norma vigente, a norma prevalece.'])

ap['subtitle'] = ('Normas NBC TA, Riscos e Afirmações, Planejamento, Evidências, Amostragem, Fraude, Relatórios, SPED, Fiscalização Tributária '
                  '(CTN 194 a 200) e Auditoria de Estoques')
json.dump(dados, open(ARQ, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('Auditoria Fiscal atualizada: %d seções.' % len(S))
