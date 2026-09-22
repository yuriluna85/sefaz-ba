"""Cria a Apostila de Inglês Técnico para TI (nova), a partir do programa SEFAZ-CE 2026 (B02: Inglês Técnico).
Textos de treino são originais (escritos para esta apostila) e cada item cita o trecho que o sustenta. Idempotente.
Relatório: dados/auditoria_apostilas/10_ingles.md
Uso (na pasta do app): python dados/auditoria_apostilas/aplicar_10_ingles.py
"""
import json
import os
import sys

APP = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARQ = os.path.join(APP, 'apostilas_conteudo.json')
dados = json.load(open(ARQ, encoding='utf-8'))
NOME = 'Apostila_Ingles_Tecnico_TI.pdf'
if any(a['filename'] == NOME for a in dados):
    print('Apostila de Inglês já existe; nada a fazer.')
    sys.exit(0)

S = []


def sec(t, c, bl, tip):
    S.append({'title': t, 'content': c, 'bullets': bl, 'tip': tip})


sec('1. Estratégias de Leitura de Textos Técnicos em Inglês',
    'Em provas de concurso, o inglês costuma ser de leitura: um texto (notícia técnica, documentação, artigo) seguido de itens de '
    'julgamento ou de múltipla escolha. O objetivo é compreender, não traduzir palavra por palavra.',
    [['Leitura panorâmica (skimming) e localizada (scanning)',
      'Skimming: passar os olhos pelo título, pela primeira e pela última frase de cada parágrafo para captar o assunto e a '
      'estrutura. Scanning: procurar no texto uma informação específica (número, nome, data, palavra-chave) citada no item.'],
     ['Palavras cognatas e contexto',
      'Muitas palavras técnicas têm forma parecida com o português (server, network, protocol, database, security). Palavras '
      'desconhecidas podem ser deduzidas pelo contexto, pela classe gramatical e por prefixos e sufixos. Cuidado com os falsos cognatos '
      '(seção 7).'],
     ['Ideia principal e detalhes',
      'A ideia principal costuma estar no início do texto ou de cada parágrafo. Itens sobre detalhes exigem localizar o trecho exato. '
      'Itens de inferência pedem uma conclusão que decorra do texto, sem acrescentar informação externa.'],
     ['Tipos de itens mais comuns',
      'Compreensão geral, informação específica, referência de pronomes, sentido de palavra ou expressão no contexto, inferência, '
      'propósito do autor e verdadeiro ou falso (certo ou errado).'],
     ['Julgar certo ou errado',
      'Compare o item com o texto, e não com o que você sabe sobre o assunto. Desconfie de itens com palavras absolutas (always, never, '
      'only, all, none, every) quando o texto usa palavras moderadas (usually, may, some, often). Observe inversões de sentido '
      '(por exemplo, "reduce" por "increase") e troca de sujeito.'],
     ['Ordem de trabalho sugerida',
      'Leia o comando; passe rapidamente pelo texto; leia cada item e volte ao trecho correspondente; marque a resposta apoiada no '
      'texto; se não houver apoio, o item tende a ser errado.']],
    ['O Texto Manda, Não o Seu Conhecimento',
     'Mesmo que o item seja verdadeiro no mundo real, se o texto não o sustenta, ele não deve ser tomado como certo. Da mesma forma, '
     'se o texto diz algo diferente do que você conhece, vale o texto.'])
sec('2. Conectivos, Palavras de Referência e Estrutura do Parágrafo',
    'Os conectivos mostram a relação entre as ideias: adição, contraste, causa, consequência, condição e exemplo. Entendê-los é '
    'decisivo para julgar itens.',
    [['Adição',
      'and, also, moreover, furthermore, in addition, besides, as well as.'],
     ['Contraste e concessão',
      'but, however, yet, nevertheless, nonetheless, although, though, even though, whereas, while, despite, in spite of, on the '
      'other hand, instead. Depois de "although" e "despite", a ideia seguinte costuma contrastar com a anterior.'],
     ['Causa e consequência',
      'because, since, as, due to, owing to, thanks to (causa); so, therefore, thus, hence, as a result, consequently (consequência).'],
     ['Condição',
      'if, unless (a menos que), provided that, as long as, in case, otherwise (caso contrário).'],
     ['Exemplo, ênfase e resumo',
      'for example, for instance, such as, e.g. (por exemplo), i.e. (isto é), in particular, indeed, in short, in summary, overall.'],
     ['Palavras de referência',
      'Pronomes e determinantes retomam termos anteriores: it, they, them, this, that, these, those, which, who, whose, the former (o '
      'primeiro), the latter (o último), such. Em "these tools", "these" retoma o que foi listado antes. Para achar a referência, '
      'procure o substantivo compatível em número e gênero na frase anterior.'],
     ['Ordem e sequência',
      'first, second, then, next, after that, finally, meanwhile, previously, subsequently.']],
    ['However Contrasta, Therefore Conclui',
     'Após "however", espere uma ideia contrária à anterior. Após "therefore" ou "as a result", espere uma consequência do que '
     'foi dito. Errar essa relação inverte o sentido do item.'])
sec('3. Tempos Verbais e Voz Passiva em Textos Técnicos',
    'Textos técnicos usam poucos tempos verbais e muita voz passiva. Reconhecê-los evita erros de sentido.',
    [['Presente simples',
      'Fatos, funcionamento e regras gerais: "The server stores the logs." "This command deletes the file." Terceira pessoa do singular '
      'leva -s: "it runs".'],
     ['Presente contínuo e passado',
      'Presente contínuo (is/are + verbo-ing): ação em andamento ou tendência ("The team is migrating the database."). Passado simples: '
      'ação concluída ("The patch fixed the bug."). Verbos regulares terminam em -ed; há verbos irregulares (run, ran; build, built; '
      'write, wrote).'],
     ['Presente perfeito',
      'have/has + particípio passado: ação que começou no passado e tem relação com o presente ("Version 2.0 has been released."; '
      '"The team has worked on it since 2020.").'],
     ['Futuro',
      'will + verbo (previsão ou decisão): "The support will end in 2027." Going to: plano ou evidência: "The system is going to '
      'restart." O presente contínuo também indica agendamento.'],
     ['Voz passiva',
      'be + particípio passado: "The data is encrypted." "The bug was fixed." "The tool has been deprecated." Foca no que é feito, '
      'não em quem faz. Com by, indica o agente: "The report was written by the security team."'],
     ['Formas em -ing e -ed como adjetivos',
      '-ing: quem causa ("an interesting result", "the running process"). -ed: quem sofre ("an encrypted file", "a failed login", '
      '"the affected users"). São muito comuns em nomes técnicos.'],
     ['Verbos de ação frequentes',
      'run, execute, deploy, install, configure, monitor, restart, fail, crash, retrieve, store, delete, update, upgrade, rollback, '
      'scale, migrate, connect, authenticate, encrypt, detect, prevent, ensure, require, allow, enable, disable.']],
    ['Was Fixed é Passado Passivo, Has Been Fixed é Presente Perfeito Passivo',
     '"The bug was fixed" indica um fato passado. "The bug has been fixed" indica que já foi corrigido, com relevância agora. Ambos '
     'usam a voz passiva; note o tempo verbal.'])
sec('4. Verbos Modais e a Linguagem das Normas (RFC 2119)',
    'Modais expressam obrigação, recomendação, possibilidade e proibição. Em documentos técnicos e normativos, a força de cada modal '
    'importa.',
    [['Possibilidade e capacidade',
      'can (capacidade ou possibilidade), could (possibilidade menor ou passado de can), may (permissão ou possibilidade), might '
      '(possibilidade menor). "The service may fail" indica possibilidade, e não certeza.'],
     ['Obrigação',
      'must (obrigação forte), have to (obrigação externa ou necessidade), need to (necessidade), shall (obrigação em documentos '
      'formais). "Users must change the password" indica dever.'],
     ['Recomendação',
      'should e ought to (recomendação ou expectativa), had better (recomendação forte). "You should back up the data" recomenda, mas '
      'não obriga.'],
     ['Proibição e ausência de obrigação',
      'must not e cannot (proibido), mas don\'t have to e needn\'t (não é necessário, ou seja, é opcional). "You must not share the '
      'key" proíbe; "You don\'t have to share the key" não obriga a compartilhar.'],
     ['Palavras-chave da RFC 2119',
      'A RFC 2119 define o significado de termos em maiúsculas nas normas da Internet: MUST, REQUIRED e SHALL (obrigatório); MUST NOT '
      'e SHALL NOT (proibido); SHOULD e RECOMMENDED (recomendado, com exceções justificadas); SHOULD NOT e NOT RECOMMENDED '
      '(desaconselhado); MAY e OPTIONAL (opcional).'],
     ['Modais com verbo perfeito',
      'may have, might have, could have (possibilidade no passado), should have (crítica ou lamento: "should have updated"), must have '
      '(dedução: "must have been a network failure").']],
    ['Must Obriga, Should Recomenda, May Permite',
     'Trocar um modal por outro muda o valor do item. "Should" nunca equivale a "must". "May" indica possibilidade ou permissão, e '
     'não obrigação.'])
sec('5. Comparativos, Condicionais, Quantificadores e Orações Relativas',
    'Estruturas que aparecem com frequência em textos técnicos e que alteram o sentido dos itens.',
    [['Comparativos e superlativos',
      'Comparativo: faster than, more secure than, as fast as, less expensive than. Superlativo: the fastest, the most secure. '
      '"The more data, the better the model" (quanto mais... melhor).'],
     ['Condicionais',
      'Zero: if + presente, presente (fatos: "If the disk is full, the write fails."). Primeira: if + presente, will (possibilidade '
      'real: "If the test fails, the deployment will stop."). Segunda: if + passado, would (hipótese: "If we had more servers, we would '
      'scale."). Terceira: if + had + particípio, would have (hipótese no passado).'],
     ['Quantificadores',
      'many/few (contáveis), much/little (incontáveis), a few/a little (alguns, o suficiente) versus few/little (poucos, quase nenhum). '
      'some e any, enough, too, several, most, all, no, none, each e every. "Data" e "software" são tratados como incontáveis '
      '("much data", "a piece of software").'],
     ['Orações relativas',
      'who (pessoas), which (coisas), that (pessoas ou coisas, restritivo), whose (posse). "The tool that monitors the network" '
      'restringe o sentido; a oração entre vírgulas com which acrescenta informação adicional.'],
     ['Palavras negativas e limitadoras',
      'not, no, never, neither, nor, hardly, barely, only, just, merely, at least, at most, up to. "At least 8 characters" é mínimo; '
      '"up to 8 characters" é máximo.'],
     ['Números e proporções',
      'double, triple, half, twice as many, by 50%, from 10 to 20, more than, less than, approximately, nearly, about. "Increased by '
      '20%" é aumento de 20%; "increased to 20%" é chegar a 20%.']],
    ['At Least É Mínimo, Up To É Máximo',
     'Preste atenção às palavras que limitam quantidades. "By" e "to" também mudam o sentido: "grew by 5%" (cresceu 5%) e "grew to '
     '5%" (chegou a 5%).'])
sec('6. Formação de Palavras: Prefixos, Sufixos, Compostos e Phrasal Verbs de TI',
    'Conhecer a estrutura das palavras ajuda a deduzir significados de termos novos.',
    [['Prefixos',
      'un-, in-, im-, non-, dis- (negação: unavailable, invalid, non-compliant, disable); re- (repetição: restart, rebuild); '
      'de- (inverso: decrypt, deploy/undeploy); mis- (erro: misconfiguration); over- e under- (excesso e falta: overload, '
      'underperform); pre- e post- (antes e depois: preprocess, postmortem); inter- (entre: interface, interoperability); sub- '
      '(abaixo: subnet); multi- (vários: multi-factor); micro- e macro-; auto- (por si: automation).'],
     ['Sufixos',
      '-able e -ible (capaz de: scalable, reliable); -er e -or (agente: server, monitor); -ness e -ity (qualidade: availability, '
      'reliability); -ment e -tion (ação ou resultado: deployment, authentication); -less (sem: stateless); -ful; -ize ou -ise (tornar: '
      'optimize, virtualize); -ware (conjunto de programas: middleware).'],
     ['Palavras compostas',
      'workflow, backup, database, dashboard, framework, plug-in, open source, real-time, cloud-based, end-to-end, single sign-on.'],
     ['Substantivo versus verbo',
      'Muitos termos mudam de forma: login (substantivo) e log in (verbo); setup e set up; backup e back up; rollout e roll out; '
      'shutdown e shut down; checkout e check out. Como verbo, a forma tem espaço.'],
     ['Phrasal verbs comuns em TI',
      'set up (configurar), log in ou sign in (entrar), log out (sair), back up (fazer cópia), roll back (reverter), roll out '
      '(implantar), shut down (desligar), boot up (iniciar), scale up e scale out (ampliar por tamanho e por quantidade), '
      'spin up (subir uma instância), tear down (desmontar), drill down (detalhar), plug in (conectar), look up (consultar), carry out '
      '(executar), find out (descobrir), turn on e turn off (ligar e desligar), pick up (retomar, captar).'],
     ['Abreviações e siglas em inglês',
      'e.g. (por exemplo), i.e. (isto é), etc., vs. (versus), FAQ, ASAP, ETA (previsão de chegada), FYI (para sua informação), N/A '
      '(não aplicável), TBD (a definir).']],
    ['Scale Up É Vertical, Scale Out É Horizontal',
     'Scale up aumenta a capacidade de uma máquina (mais CPU e memória). Scale out acrescenta mais máquinas. Em provas, "up" e "out" '
     'diferenciam vertical de horizontal.'])
sec('7. Falsos Cognatos e Armadilhas de Tradução',
    'Falsos cognatos são palavras parecidas com o português, mas com sentido diferente. São fonte comum de erro em itens de '
    'interpretação.',
    [['Falsos cognatos gerais',
      'actually (na verdade, e não "atualmente"; atualmente é currently), eventually (por fim, com o tempo, e não "eventualmente"; '
      'eventualmente é occasionally ou possibly), pretend (fingir, e não "pretender"; pretender é intend), library (biblioteca, e não '
      '"livraria"; livraria é bookstore), attend (comparecer ou participar, e não "atender"; atender é answer ou serve), '
      'resume (retomar; résumé ou CV é currículo), realize (perceber ou dar-se conta), assist (ajudar, e não "assistir"), '
      'lecture (aula ou palestra, e não "leitura"), parents (pais, e não "parentes"; parentes é relatives), college (faculdade, e '
      'não "colégio"), notice (notar ou aviso), sensible (sensato, e não "sensível"; sensível é sensitive).'],
     ['Falsos cognatos em textos técnicos',
      'support (suporte, mas também apoiar ou aceitar; "the system supports 4K" quer dizer "suporta"), comprehensive (abrangente, e não '
      '"compreensivo"), policy (política ou regra, e também apólice), application (aplicação ou aplicativo, e também candidatura), '
      'argument (argumento, mas em programação, parâmetro passado a uma função), compromise (concessão, e também comprometer), '
      'fabric (tecido, e em redes, a malha ou estrutura de interconexão), custom (costume ou hábito; personalizado em "custom '
      'build"), costume (fantasia).'],
     ['Termos com mais de um sentido',
      'patch (correção de software), bug (defeito), release (lançamento ou versão), build (compilação ou versão gerada), issue (problema '
      'ou item de acompanhamento), thread (fio de execução), stack (pilha), queue (fila), pool (conjunto), handle (tratar ou alça), '
      'resolve (resolver, e em rede, traduzir nome em endereço), commit (confirmar ou gravar), branch (ramo), fork (bifurcação), '
      'token (ficha, símbolo ou credencial), trace (rastro).'],
     ['Plural e concordância',
      '"Data" costuma ser tratado como incontável no singular ("the data is stored"), e "criteria" e "phenomena" são plurais de '
      'criterion e phenomenon. "Software", "hardware", "information", "advice" e "equipment" são incontáveis.'],
     ['Ordem dos adjetivos e nomes compostos',
      'Em inglês, o modificador vem antes: "network security policy" é "política de segurança de rede". Leia o último substantivo como '
      'o núcleo e os anteriores como modificadores.']],
    ['Actually Não é Atualmente',
     'Não traduza "actually" como "atualmente" (currently) nem "eventually" como "eventualmente" (occasionally). Esses são os '
     'falsos cognatos mais cobrados.'])
sec('8. Vocabulário Essencial de TI (Inglês e Português)',
    'Lista organizada por áreas dos termos mais frequentes em textos técnicos.',
    [['Hardware e sistemas',
      'hardware (equipamento), motherboard (placa-mãe), processor ou CPU, memory ou RAM, storage (armazenamento), hard drive ou disk, '
      'power supply (fonte), firmware, operating system (sistema operacional), kernel, driver, file system, boot (inicialização), '
      'cache, bandwidth (largura de banda), throughput (vazão), latency (latência), uptime e downtime (tempo em operação e fora dele).'],
     ['Redes',
      'network (rede), router (roteador), switch, gateway, firewall, packet (pacote), frame (quadro), protocol (protocolo), address '
      '(endereço), subnet (sub-rede), port (porta), routing (roteamento), load balancer (balanceador de carga), wireless, link, '
      'endpoint, handshake, timeout, connection refused (conexão recusada).'],
     ['Segurança',
      'security (segurança), authentication (autenticação), authorization (autorização), access control, encryption (criptografia), '
      'key (chave), certificate (certificado), password (senha), breach (violação), vulnerability (vulnerabilidade), threat '
      '(ameaça), attack, exploit, malware, phishing, patch, audit log, least privilege (privilégio mínimo).'],
     ['Dados e bancos de dados',
      'database, table (tabela), row (linha), column (coluna), query (consulta), index (índice), schema (esquema), backup, restore '
      '(restaurar), replication, transaction, join, data warehouse, data lake, dataset, pipeline, ETL.'],
     ['Desenvolvimento',
      'source code (código-fonte), developer (desenvolvedor), function, class, variable, library, framework, compile, debug '
      '(depurar), test, deploy (implantar), repository, branch, merge, pull request, code review (revisão de código), refactoring '
      '(refatoração), bug, feature (funcionalidade), requirement (requisito).'],
     ['Nuvem e DevOps',
      'cloud, instance (instância), container, cluster, scalability (escalabilidade), elasticity, availability (disponibilidade), '
      'resilience (resiliência), monitoring (monitoramento), logging, alerting, pipeline, continuous integration, infrastructure as '
      'code, incident, outage (queda do serviço), rollback.'],
     ['Gestão e governança',
      'stakeholder (parte interessada), requirement, deadline (prazo), budget (orçamento), risk (risco), compliance (conformidade), '
      'governance, policy, standard (norma), audit (auditoria), service level agreement (SLA), roadmap, milestone (marco), deliverable '
      '(entrega).'],
     ['Inteligência artificial e dados',
      'machine learning, model, training, dataset, feature, label, bias (viés), accuracy (acurácia), overfitting, prediction, '
      'neural network, prompt, inference, hallucination (alucinação), fine-tuning, embedding.']],
    ['Aprenda em Grupos, Não em Lista Solta',
     'Termos relacionados fixam melhor. Estude cada área ligada a uma apostila deste conjunto e releia as siglas do glossário.'])
sec('9. Linguagem de Documentação, Notas de Versão e Mensagens de Erro',
    'Textos técnicos reais têm vocabulário próprio: notas de versão, manuais, relatórios de incidente e mensagens de sistema.',
    [['Notas de versão (release notes)',
      'new feature (novo recurso), improvement (melhoria), bug fix (correção de defeito), security fix, patch, hotfix (correção urgente), '
      'known issue (problema conhecido), workaround (solução de contorno), deprecated (obsoleto, mantido por ora mas com remoção '
      'prevista), removed, breaking change (mudança que quebra compatibilidade), backward compatible (retrocompatível), upgrade, '
      'migration guide, end of life ou EOL (fim de vida).'],
     ['Manuais e READMEs',
      'prerequisites (pré-requisitos), installation, configuration, usage (uso), examples, troubleshooting (solução de problemas), '
      'limitations, license (licença), contributing (como contribuir), changelog, FAQ. Verbos no imperativo dão instruções: '
      '"Run the script", "Do not delete the file", "Make sure that the service is running".'],
     ['Mensagens de erro comuns',
      'permission denied (permissão negada), access denied, file not found, connection refused (recusada), connection timed out '
      '(tempo esgotado), unable to connect, failed to (falha ao), invalid (inválido), out of memory (memória esgotada), '
      'disk full, syntax error, unexpected token, null pointer, service unavailable, authentication failed.'],
     ['Relatórios de incidente',
      'incident, impact (impacto), timeline (linha do tempo), root cause (causa raiz), contributing factors, mitigation (mitigação), '
      'resolution, lessons learned, follow-up actions, postmortem, outage, degraded performance (desempenho degradado), SLA breach.'],
     ['Avisos e alertas',
      'Note (observação), Tip, Important, Warning (atenção), Caution (cuidado), Danger. "Warning" e "Caution" indicam risco de '
      'perda de dados ou de falha.'],
     ['Estilo dos textos',
      'Frases curtas, voz passiva, termos técnicos, siglas e muitos substantivos compostos. Na dúvida, localize o verbo principal e o '
      'núcleo do sintagma nominal.']],
    ['Deprecated Não é Removed',
     'Um recurso "deprecated" ainda existe, mas deve ser evitado e será removido no futuro. "Removed" significa que já foi retirado. '
     'Itens de prova exploram essa diferença.'])
sec('10. Treino 1: Textos com Itens Certo ou Errado',
    'Textos originais, escritos para esta apostila, seguidos de itens no estilo certo ou errado. O gabarito e a justificativa citam o '
    'trecho de apoio. Tente responder antes de ler a justificativa.',
    [['Texto A',
      '"Kubernetes clusters can automatically restart containers that fail health checks. However, this feature does not fix the root '
      'cause of a problem: if an application keeps crashing because of a memory leak, the platform will simply restart it again and '
      'again. Engineers should therefore monitor restart counts and investigate logs. Moreover, resource limits, although useful, must '
      'be tuned carefully; a limit that is too low may cause containers to be terminated even when the code is correct."'],
     ['Itens do Texto A',
      '1) The platform can restart containers that fail health checks. 2) Automatic restarts solve the root cause of crashes. 3) '
      'Restart counts are a signal that engineers should watch. 4) Low resource limits never affect code that is correct.'],
     ['Gabarito e justificativa do Texto A',
      '1) CERTO: "can automatically restart containers that fail health checks". 2) ERRADO: o texto diz que o recurso "does not fix '
      'the root cause". 3) CERTO: "Engineers should therefore monitor restart counts". 4) ERRADO: um limite muito baixo "may cause '
      'containers to be terminated even when the code is correct"; "never" contraria "may".'],
     ['Texto B',
      '"Multi-factor authentication (MFA) requires users to present two or more different kinds of evidence, such as a password and a '
      'code generated by a phone app. Although MFA greatly reduces the risk of account takeover, it is not perfect: attackers may '
      'still trick users into approving fraudulent prompts. Organizations that rely only on SMS codes are more exposed than those using '
      'hardware security keys, which resist phishing better."'],
     ['Itens do Texto B',
      '1) MFA requires different kinds of evidence. 2) MFA eliminates the risk of account takeover. 3) Hardware security keys resist '
      'phishing better than SMS codes. 4) The text says attackers cannot trick users into approving prompts.'],
     ['Gabarito e justificativa do Texto B',
      '1) CERTO: "two or more different kinds of evidence". 2) ERRADO: "greatly reduces" o risco, "it is not perfect". 3) CERTO: '
      'as chaves de hardware "resist phishing better", e quem usa só SMS está "more exposed". 4) ERRADO: "attackers may still trick '
      'users into approving fraudulent prompts".'],
     ['Texto C',
      '"Version 3.2 is backward compatible with 3.1, but the old export command is now deprecated and will be removed in version 4.0. '
      'Users who rely on it should migrate to the new report command. A known issue affects large files: uploads above 2 GB may '
      'fail until the next patch is released. As a workaround, split the file into smaller parts."'],
     ['Itens do Texto C',
      '1) Version 3.2 keeps compatibility with 3.1. 2) The export command has already been removed. 3) Uploads above 2 GB may fail in '
      'this version. 4) The text recommends compressing large files as a workaround.'],
     ['Gabarito e justificativa do Texto C',
      '1) CERTO: "backward compatible with 3.1". 2) ERRADO: está "deprecated" e "will be removed in version 4.0", ou seja, ainda não '
      'foi removido. 3) CERTO: "uploads above 2 GB may fail". 4) ERRADO: a solução de contorno é dividir o arquivo ("split the file '
      'into smaller parts"), e não comprimi-lo.']],
    ['Marque o Trecho Antes de Julgar',
     'Para cada item, localize e sublinhe o trecho que o sustenta ou contradiz. Se não achar apoio, o item provavelmente está '
     'errado. Preste atenção a "may" versus "will" e a "never" e "always".'])
sec('11. Referências e Conferência',
    'Conferência realizada em 21/09/2026. Apostila nova, criada a partir do programa SEFAZ-CE 2026 (FCC), que cita "Inglês Técnico" '
    'na área de Tecnologia da Informação.',
    [['Referências',
      'Gramáticas e dicionários de inglês de uso geral e técnico (por exemplo, dicionários Oxford e Cambridge); RFC 2119 (palavras-chave '
      'para indicar níveis de exigência); documentação técnica em inglês de produtos e padrões citados nas demais apostilas; Edital '
      'SEFAZ-CE 2026 (FCC), Anexo VI.'],
     ['Sobre os textos de treino',
      'Os textos e itens são originais desta apostila, escritos com base em fatos técnicos comuns. Não reproduzem provas de bancas.'],
     ['A conferir',
      'O formato e o nível do inglês nas provas da SEFAZ-BA dependem do edital e da banca (que ainda não foram publicados). Ajustar o '
      'foco quando o edital sair: FCC costuma cobrar leitura e interpretação; CEBRASPE, itens de certo ou errado sobre um texto.'],
     ['Como estudar',
      'Leia diariamente pequenos textos técnicos em inglês (documentação e notícias de tecnologia), grife conectivos, modais e '
      'palavras de referência e resolva itens de certo ou errado sempre justificando com um trecho.']],
    ['Regra de Conteúdo', 'Este material não afirma nada sem fonte. Se houver divergência com dicionários ou gramáticas de referência, '
                          'prevalecem estes últimos.'])

dados.append({
    'filename': NOME,
    'subject': 'Inglês Técnico para TI',
    'title': 'Manual: Inglês Técnico para Tecnologia da Informação',
    'subtitle': ('Estratégias de leitura, Conectivos, Tempos verbais e Voz passiva, Modais e RFC 2119, Prefixos e Sufixos, Phrasal Verbs, '
                 'Falsos Cognatos, Vocabulário de TI, Notas de Versão e Treino Certo ou Errado'),
    'sections': S})
json.dump(dados, open(ARQ, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('Apostila de Inglês criada: %d seções.' % len(S))
