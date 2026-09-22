"""Aplica a auditoria da Apostila de Engenharia de Software (Fase 1) e acrescenta as seções de desenvolvimento e
arquiteturas do programa SEFAZ-CE 2026 (B02) e do edital SEFAZ-BA 2022 (inclui Análise de Pontos de Função). Idempotente.
Relatório: dados/auditoria_apostilas/07_desenvolvimento.md
Uso (na pasta do app): python dados/auditoria_apostilas/aplicar_07_desenvolvimento.py
"""
import json
import os
import sys

APP = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARQ = os.path.join(APP, 'apostilas_conteudo.json')
dados = json.load(open(ARQ, encoding='utf-8'))
ap = next(a for a in dados if 'Engenharia_Software' in a['filename'])
S = ap['sections']

if any(s['title'].startswith('11.') for s in S):
    print('Apostila de Engenharia de Software já atualizada; nada a fazer.')
    sys.exit(0)


def bul(sec, inicio):
    return next(b for b in sec['bullets'] if b[0].strip().startswith(inicio))


def trocar(txt, velho, novo):
    assert velho in txt, 'trecho não encontrado: ' + velho[:70]
    return txt.replace(velho, novo)


# ---- Seção 3: UML ----
b = bul(S[2], 'Diagramas Estruturais')
b[1] += ' Também são estruturais o diagrama de estrutura composta e o diagrama de perfil, totalizando 7.'
b = bul(S[2], 'Diagramas Comportamentais')
b[1] += (' Também são comportamentais o diagrama de comunicação, o de visão geral de interação e o de tempo, totalizando 7. Nos casos de '
         'uso, a seta de <<include>> vai do caso base para o incluído, e a de <<extend>> vai do caso que estende para o caso base. '
         'Fragmentos combinados do diagrama de sequência (alt, opt, loop, par, ref) representam alternativas, repetições e paralelismo.')
S[2]['content'] = trocar(S[2]['content'], 'A UML 2.5 divide seus 14 diagramas', 'A UML (versão atual 2.5.1) divide seus 14 diagramas')

# ---- Seção 4: SOLID ----
S[3]['content'] = trocar(S[3]['content'], 'Alto Acoplamento Coesivo e Baixo Acoplamento',
                         'Alta Coesão e Baixo Acoplamento')
b = bul(S[3], 'D - Dependency Inversion')
b[1] = ('Módulos de alto nível não devem depender de módulos de baixo nível; ambos devem depender de ABSTRAÇÕES. Abstrações não '
        'devem depender de detalhes; detalhes devem depender de abstrações. O DIP é o princípio; a injeção de dependências (DI) é uma '
        'técnica para aplicá-lo (as dependências são fornecidas de fora), e a inversão de controle (IoC) é o conceito mais amplo, '
        'presente em contêineres como o do Spring.')

# ---- Seção 5: GoF ----
b = bul(S[4], 'Padrões Comportamentais')
b[1] = trocar(b[1], '(define uma dependência um-para-muitos entre objetos para que, quando um mude de estado, todos os dependentes sejam '
              'notificados automaticamente - padrão Pub/Sub)',
              '(define uma dependência um-para-muitos entre objetos para que, quando um mude de estado, todos os dependentes sejam '
              'notificados automaticamente; é parecido com publicação e assinatura, mas no Observer o sujeito conhece seus observadores, '
              'enquanto no Pub/Sub há um intermediário que desacopla emissor e receptores)')

# ---- Seção 7: REST ----
S[6]['content'] = trocar(S[6]['content'], 'que utiliza o protocolo HTTP nativo para comunicação síncrona e interoperável entre sistemas '
                         'distribuídos', 'normalmente implementado sobre HTTP, para comunicação interoperável entre sistemas distribuídos')
b = bul(S[6], 'Os 6 Princípios')
b[1] = trocar(b[1], '4. Interface Uniforme (identificação de recursos por URIs, manipulação por representações JSON/XML e mensagens '
              'autoexplicativas)',
              '4. Interface Uniforme (identificação de recursos por URIs, manipulação por representações JSON/XML, mensagens '
              'autoexplicativas e HATEOAS, isto é, hipermídia como motor do estado da aplicação)')

# ---- Seção 8: testes ----
b = bul(S[7], 'A Pirâmide de Testes')
b[0] = 'A Pirâmide de Testes'
b[1] = ('Conceito de Mike Cohn, difundido por Martin Fowler. ' + b[1])
b = bul(S[7], 'Testes Caixa-Preta')
b[1] = trocar(b[1], 'onde ocorre a maioria dos erros', 'onde os defeitos são mais frequentes')
b = bul(S[7], 'Complexidade Ciclomática')
b[1] = ('Métrica que indica o número de caminhos linearmente independentes no grafo de fluxo de controle. V(G) = E - N + 2P, onde E é o '
        'número de arestas, N o de nós e P o de componentes conexos (P = 1 para um único programa). Equivale a V(G) = número de nós '
        'predicados (if, while, for, cada condição) + 1, quando as decisões são binárias. É também o número mínimo de casos de teste para '
        'cobrir todos os ramos independentes.')
S[7]['tip'] = ['Cálculo Rápido da Complexidade Ciclomática',
               'Conte as decisões binárias (cada if, while, for e cada condição composta separada por AND ou OR) e some 1. Um trecho '
               'sem nenhuma decisão tem V(G) = 1.']

# ---- Seção 10 ----
S[9]['title'] = '10. Armadilhas Conceituais Recorrentes em Engenharia de Software'
S[9]['content'] = ('Pontos conceituais que costumam gerar erro em questões de Engenharia de Software. Servem de revisão rápida; a base '
                   'de cada ponto está nas seções anteriores.')
for i, bl in enumerate(S[9]['bullets']):
    if bl[0].startswith('Pegadinha 3'):
        S[9]['bullets'][i] = ['Pegadinha 3: Complexidade Ciclomática = Predicados + 1',
                              'A complexidade ciclomática é o número de decisões binárias mais um, que também indica o número mínimo de '
                              'casos de teste para cobrir os caminhos independentes.']
S[9]['tip'] = ['Síntese Final de Engenharia de Software',
               'POST não é idempotente; include é obrigatório e extend, opcional; complexidade é predicados mais 1; a arquitetura limpa '
               'aponta para o centro; no TDD o teste nasce vermelho.']


def sec(t, c, bl, tip):
    S.append({'title': t, 'content': c, 'bullets': bl, 'tip': tip})


sec('11. Outros Modelos de Processo e Agilidade',
    'Além de cascata, espiral e RUP, há modelos incrementais, orientados a prototipação e os métodos ágeis.',
    [['Incremental e iterativo',
      'No incremental, o sistema é entregue em partes (incrementos), cada uma funcional. No iterativo, o trabalho é repetido em ciclos '
      'para refinar o produto. Muitos processos combinam os dois.'],
     ['Prototipação',
      'Constrói uma versão preliminar para esclarecer requisitos. Protótipo descartável (throwaway) serve só para explorar e é jogado '
      'fora; protótipo evolutivo vira a base do produto final.'],
     ['Modelo em V',
      'Relaciona cada fase de desenvolvimento a um nível de teste: requisitos a testes de aceitação, projeto de alto nível a testes de '
      'sistema, projeto detalhado a testes de integração e codificação a testes unitários. Enfatiza verificação e validação.'],
     ['Manifesto Ágil',
      'Quatro valores: indivíduos e interações mais que processos e ferramentas; software funcionando mais que documentação abrangente; '
      'colaboração com o cliente mais que negociação de contratos; responder a mudanças mais que seguir um plano. Os itens à direita '
      'também têm valor, mas os da esquerda valem mais. São 12 princípios.'],
     ['Extreme Programming (XP)',
      'Valores: comunicação, simplicidade, feedback, coragem e respeito. Práticas: programação em par, TDD, integração contínua, '
      'refatoração, propriedade coletiva do código, releases pequenos, jogo do planejamento e padrão de codificação.'],
     ['ISO/IEC/IEEE 12207',
      'Norma de processos do ciclo de vida de software: define processos de aquisição, fornecimento, desenvolvimento, operação, '
      'manutenção e suporte, com base para modelos de maturidade como o MPS.BR.']],
    ['Incremento Entrega Partes, Iteração Refina',
     'Incremental: acrescenta funcionalidades a cada entrega. Iterativo: revisita e melhora o que já existe. Os métodos ágeis são '
     'iterativos e incrementais.'])
sec('12. Requisitos em Profundidade: Elicitação, Priorização e Qualidade',
    'Complementa a seção 2 com técnicas de levantamento, priorização, critérios de aceitação e o modelo de qualidade ISO/IEC 25010.',
    [['Técnicas de elicitação',
      'Entrevistas, questionários, observação e etnografia (útil para requisitos do trabalho real), oficinas e JAD (Joint Application '
      'Design), brainstorming, cenários e casos de uso, prototipação, análise de documentos e personas.'],
     ['Priorização',
      'MoSCoW: Must (deve ter), Should (deveria ter), Could (poderia ter) e Won\'t (não desta vez). Modelo Kano: requisitos básicos, de '
      'desempenho (quanto mais, melhor), atrativos (encantadores) e indiferentes. Value Proposition Canvas: perfil do cliente (tarefas, '
      'dores e ganhos) e mapa de valor.'],
     ['Hierarquia ágil',
      'Épico (grande demanda), feature (funcionalidade), história de usuário e tarefa. Mapeamento de histórias organiza o trabalho pela '
      'jornada do usuário. Definição de Pronto (DoD) vale para todo item; critérios de aceite valem para cada história.'],
     ['Critérios de aceite e BDD',
      'BDD (desenvolvimento guiado por comportamento) descreve exemplos no formato Gherkin: Dado (Given) um contexto, Quando (When) uma '
      'ação, Então (Then) um resultado. Serve de documentação e de teste automatizado.'],
     ['Design Thinking e Lean Inception',
      'Design Thinking (etapas da d.school de Stanford): empatizar, definir, idear, prototipar e testar. Lean Inception (Paulo Caroli) é '
      'uma oficina curta para alinhar visão, personas, funcionalidades e o MVP (produto mínimo viável).'],
     ['ISO/IEC 25010:2011',
      'Modelo de qualidade de produto com oito características: adequação funcional, eficiência de desempenho, compatibilidade, '
      'usabilidade, confiabilidade, segurança, manutenibilidade e portabilidade.'],
     ['Documento de requisitos',
      'A especificação de requisitos de software (SRS) é orientada pela ISO/IEC/IEEE 29148. Rastreabilidade liga requisitos a projeto, '
      'código e testes.']],
    ['MoSCoW Ordena Entregas, Kano Mede Satisfação',
     'MoSCoW classifica o que entra na entrega. O modelo Kano explica como cada tipo de requisito afeta a satisfação do cliente.'])
sec('13. GRASP, Coesão, Acoplamento e Outros Princípios',
    'Complementam o SOLID com padrões de atribuição de responsabilidades e critérios de qualidade do projeto.',
    [['GRASP (Larman): os nove padrões',
      'Especialista na Informação (a responsabilidade vai para quem tem a informação); Criador (quem cria instâncias); Controlador '
      '(recebe eventos da interface e coordena); Baixo Acoplamento; Alta Coesão; Polimorfismo; Fabricação Pura (classe artificial '
      'para preservar coesão); Indireção (intermediário para reduzir acoplamento); Variações Protegidas (proteger pontos de mudança '
      'por interfaces).'],
     ['Tipos de coesão (da melhor à pior)',
      'Funcional, sequencial, comunicacional, procedural, temporal, lógica e coincidental.'],
     ['Tipos de acoplamento (do menor ao maior)',
      'De dados, de carimbo (stamp), de controle, externo, comum (dados globais) e de conteúdo (um módulo acessa o interior de outro).'],
     ['Outros princípios',
      'DRY (não repita a si mesmo), KISS (mantenha simples), YAGNI (você não vai precisar disso: não construa o que não é necessário) e '
      'Lei de Deméter (fale só com seus vizinhos imediatos). Preferir composição a herança.'],
     ['Pilares da orientação a objetos',
      'Abstração, encapsulamento, herança e polimorfismo.']],
    ['Especialista na Informação, Criador é Outro Padrão',
     'Quem tem a informação recebe a responsabilidade de usá-la (Especialista). Quem cria instâncias de uma classe segue o padrão '
     'Criador. Não confundir.'])
sec('14. Padrões GoF Complementares',
    'Completam os 23 padrões do GoF: 5 criacionais, 7 estruturais e 11 comportamentais.',
    [['Estruturais restantes',
      'Bridge (separa abstração e implementação para variarem de forma independente) e Flyweight (compartilha objetos pequenos para '
      'economizar memória). Os cinco vistos na seção 5 (Adapter, Facade, Decorator, Composite, Proxy) completam os sete.'],
     ['Comportamentais restantes',
      'Iterator (percorre uma coleção sem expor sua estrutura), Mediator (centraliza a comunicação entre objetos), Memento (guarda e '
      'restaura o estado de um objeto), State (o comportamento muda com o estado), Visitor (adiciona operações sem alterar as classes) '
      'e Interpreter (representa e interpreta uma gramática).'],
     ['Singleton: cuidados',
      'Garante uma instância e um ponto global de acesso. Em ambientes com várias threads, exige inicialização segura. É criticado por '
      'criar estado global e dificultar testes.'],
     ['Builder e Factory',
      'Builder constrói objetos complexos passo a passo (útil com muitos parâmetros opcionais). Factory Method delega a criação a '
      'subclasses; Abstract Factory cria famílias de objetos relacionados.'],
     ['Proxy: variações',
      'Proxy virtual (adia a criação de objetos caros), remoto (representa um objeto em outro espaço de endereçamento) e de proteção '
      '(controla o acesso).'],
     ['Padrões de arquitetura de integração',
      'Os padrões de integração corporativa (EIP: canais, roteamento e transformação) estão na apostila de Middleware e Mensageria.']],
    ['Decorator Acrescenta, Proxy Controla, Adapter Converte',
     'Os três envolvem outro objeto, mas com objetivos distintos: Decorator adiciona comportamento, Proxy controla o acesso e Adapter '
     'adapta a interface.'])
sec('15. Estilos de Arquitetura: Camadas, MVC, SOA e Arquitetura Orientada a Eventos',
    'Complementa a seção 6 com estilos clássicos e a comparação entre SOA e microsserviços.',
    [['Arquitetura em camadas',
      'Apresentação, aplicação (ou negócio), persistência e banco de dados. Cada camada usa a inferior. Facilita a manutenção, mas '
      'pode gerar dependências rígidas e sobrecarga.'],
     ['MVC, MVP e MVVM',
      'MVC: Model (dados e regras), View (interface) e Controller (recebe entradas e coordena). MVP: o Presenter intermedia a View e o '
      'Model. MVVM: o ViewModel expõe dados e comandos à View, com vinculação de dados (data binding), usado em Angular e em '
      'aplicações móveis.'],
     ['SOA versus microsserviços',
      'SOA (arquitetura orientada a serviços): serviços de negócio reutilizáveis integrados em nível corporativo, muitas vezes por um '
      'barramento (ESB) e por SOAP. Microsserviços: serviços menores, independentes e implantáveis separadamente, com dados próprios, '
      'comunicação leve (HTTP e mensagens) e lógica nas pontas ("endpoints inteligentes, tubos simples").'],
     ['Arquitetura orientada a eventos',
      'Produtores emitem eventos e consumidores reagem, geralmente por um broker. Padrões descritos por Martin Fowler: notificação de '
      'evento, transferência de estado carregada pelo evento, event sourcing e CQRS.'],
     ['Domain-Driven Design (DDD)',
      'Modelagem centrada no domínio (Eric Evans): linguagem ubíqua, contextos delimitados (bounded contexts), entidades, objetos de '
      'valor, agregados, repositórios e eventos de domínio. Os contextos delimitados orientam a divisão em microsserviços.'],
     ['Atributos de qualidade',
      'Escalabilidade, disponibilidade, desempenho, segurança, modificabilidade e testabilidade. Decisões de arquitetura equilibram esses '
      'atributos, e um ganho em um pode custar outro.']],
    ['Microsserviço Não é Só "Serviço Pequeno"',
     'O que caracteriza microsserviços é a independência de implantação e de dados por contexto de negócio, não apenas o tamanho.'])
sec('16. Microsserviços: BFF, CQRS, Saga, Resiliência e Migração',
    'Padrões usados para construir e operar sistemas de microsserviços, citados no programa de TI.',
    [['API Gateway e BFF',
      'API Gateway: ponto único de entrada (roteamento, autenticação, limites de uso). BFF (Backend for Frontend): um backend por tipo '
      'de cliente (web, mobile), que adapta as respostas às necessidades de cada interface.'],
     ['CQRS',
      'Separa o modelo de comandos (escrita) do de consultas (leitura), que podem usar armazenamentos distintos, otimizados para cada '
      'função. Traz consistência eventual entre os dois lados.'],
     ['Event Sourcing',
      'O estado é guardado como a sequência de eventos que o produziram, e não apenas o valor atual. Permite auditoria e '
      'reconstrução do estado por reaplicação; costuma andar junto com CQRS.'],
     ['Saga',
      'Transação distribuída como sequência de transações locais, com ações compensatórias em caso de falha. Coreografia: cada serviço '
      'reage a eventos. Orquestração: um coordenador central dirige os passos.'],
     ['Circuit Breaker e resiliência',
      'O circuit breaker tem três estados: fechado (chamadas passam), aberto (falha rápida, sem chamar o serviço) e semiaberto (testa se '
      'o serviço se recuperou). Outros padrões: timeout, retentativa com espera crescente e jitter, bulkhead (isolamento de recursos), '
      'limitação de taxa e fallback.'],
     ['Service mesh',
      'Camada de infraestrutura (como Istio e Linkerd) com proxies sidecar ao lado de cada serviço, que cuidam de mTLS, roteamento, '
      'retentativas e telemetria sem alterar o código.'],
     ['Strangler Fig e outbox',
      'Strangler Fig: migra um monolito aos poucos, desviando funcionalidades para novos serviços. Outbox: grava o evento na mesma '
      'transação do dado e o publica depois (veja a apostila de Middleware).'],
     ['Doze fatores (12-factor app)',
      'Base de código única; dependências explícitas; configuração no ambiente; serviços de apoio como recursos anexos; separação '
      'entre build, release e run; processos sem estado; exposição por porta; concorrência por processos; descartabilidade; '
      'paridade entre desenvolvimento e produção; logs como fluxo de eventos; tarefas administrativas como processos pontuais.']],
    ['Saga Compensa, Não Reverte',
     'Como não há transação ACID única entre serviços, a saga desfaz efeitos com ações compensatórias (por exemplo, cancelar a reserva '
     'feita). O resultado é consistência eventual.'])
sec('17. APIs e Segurança Web: CORS, CSRF, XSS, SSO e Certificados',
    'A segurança de aplicações e APIs web envolve o navegador, o servidor e a identidade.',
    [['Política de mesma origem e CORS',
      'O navegador aplica a política de mesma origem (esquema, host e porta). O CORS (Cross-Origin Resource Sharing) permite que um '
      'servidor autorize origens diferentes por cabeçalhos como Access-Control-Allow-Origin. Requisições "não simples" fazem antes uma '
      'requisição prévia (preflight) com o método OPTIONS. CORS é uma proteção do navegador; não substitui autenticação nem autorização.'],
     ['CSRF',
      'Falsificação de requisição entre sites: o navegador envia cookies automaticamente e um site malicioso induz o usuário autenticado a '
      'executar uma ação. Defesas: tokens anti-CSRF, cookies SameSite e verificação de origem. APIs que usam tokens no cabeçalho '
      'Authorization são menos expostas.'],
     ['XSS',
      'Injeção de scripts que executam no navegador da vítima. Defesas: codificação de saída conforme o contexto, validação de entradas, '
      'Content Security Policy (CSP) e cookies HttpOnly (não acessíveis por script).'],
     ['API Gateway, SSO e tokens',
      'O gateway centraliza autenticação, autorização e limites. SSO (login único) permite um só login para vários sistemas, por SAML ou '
      'OpenID Connect. Tokens JWT carregam declarações assinadas; validar assinatura, emissor, validade e público (veja a apostila de '
      'Segurança).'],
     ['Certificados digitais',
      'TLS com certificados X.509 protege o canal. TLS mútuo (mTLS) autentica também o cliente, comum entre serviços. Certificados '
      'ICP-Brasil autenticam pessoas e organizações e assinam documentos.'],
     ['JSON, XML, REST e SOAP',
      'JSON é leve e comum em REST. XML é verboso e tem esquema (XSD). SOAP é um protocolo baseado em XML com contrato WSDL e '
      'extensões (WS-Security). O modelo de maturidade de Richardson descreve os níveis de REST: 0 (um endpoint), 1 (recursos), 2 '
      '(verbos HTTP) e 3 (hipermídia).'],
     ['Boas práticas de API',
      'Versionamento, paginação, respostas de erro padronizadas, códigos de status corretos (como 409 para conflito, 422 para entidade '
      'não processável, 429 para excesso de requisições), cache com ETag e Cache-Control, documentação com OpenAPI e chaves de '
      'idempotência para POST.']],
    ['CORS Protege o Navegador, Não a API',
     'O CORS é imposto pelo navegador. Um cliente que não é navegador ignora CORS, então a API precisa de sua própria autenticação e '
     'autorização.'])
sec('18. Testes Avançados, Qualidade de Código e Ferramentas',
    'Complementa a seção 8 com tipos de teste, dublês, métricas de qualidade e as ferramentas citadas no programa.',
    [['Tipos de teste',
      'Regressão (garante que mudanças não quebraram o que funcionava), fumaça (smoke: verificação rápida do essencial), aceitação '
      '(validação pelo usuário), e não funcionais: carga, estresse, pico (spike) e resistência (soak), além de segurança e usabilidade.'],
     ['Dublês de teste',
      'Dummy (preenche parâmetros), stub (respostas fixas), spy (registra chamadas), mock (verifica interações esperadas) e fake '
      '(implementação simplificada funcional, como um banco em memória).'],
     ['Cobertura',
      'Instruções, ramos (decisões), condições e MC/DC (cada condição influencia de forma independente a decisão), exigida em software '
      'crítico. Cobertura alta não garante testes bons; teste de mutação avalia a qualidade dos testes.'],
     ['Testes de segurança',
      'SAST (análise estática do código), DAST (teste dinâmico da aplicação em execução), IAST (instrumentação em tempo de execução) e '
      'SCA (análise de dependências de terceiros).'],
     ['SonarQube',
      'Ferramenta de análise estática que reporta bugs, vulnerabilidades, pontos de atenção de segurança (security hotspots), code '
      'smells, duplicações e cobertura, com perfis de qualidade e portões de qualidade (quality gates) que bloqueiam a integração se as '
      'metas não forem atendidas.'],
     ['JUnit e Mockito (Java)',
      'JUnit 5: anotações como @Test, @BeforeEach e @AfterEach e asserções. Mockito cria mocks e configura comportamentos com when e '
      'thenReturn, e verifica interações com verify.'],
     ['Jest e Playwright',
      'Jest: testes em JavaScript e TypeScript com describe, it e expect, mocks e testes de snapshot. Playwright: automação de testes '
      'ponta a ponta em navegadores (Chromium, Firefox e WebKit), com espera automática.']],
    ['Mock Verifica Interação, Stub Fornece Resposta',
     'Stub devolve dados prontos para o teste seguir. Mock também confere se as chamadas esperadas aconteceram.'])
sec('19. Linguagens e Frameworks: Java e Spring Boot, Python, TypeScript, Angular e React Native',
    'O programa cita linguagens e frameworks de uso corporativo. Aqui estão os conceitos centrais de cada um.',
    [['Paradigmas e tipagem',
      'Imperativo, procedural, orientado a objetos, funcional, declarativo e orientado a eventos. Tipagem estática (tipos verificados '
      'na compilação, como Java e TypeScript) ou dinâmica (verificados na execução, como Python); forte ou fraca conforme as '
      'conversões implícitas.'],
     ['Java',
      'Compilado para bytecode e executado na JVM (com compilação JIT e coleta de lixo). Exceções verificadas (checked) e não verificadas. '
      'Recursos modernos: lambdas, streams e records. Contêineres e servidores de aplicação (veja a apostila de Middleware).'],
     ['Spring Boot',
      'Simplifica o Spring com autoconfiguração, starters (dependências agrupadas), servidor embutido (Tomcat por padrão), '
      'configuração em application.properties ou YAML, perfis e o Actuator (métricas e saúde). O contêiner do Spring faz injeção de '
      'dependências. Spring Data simplifica o acesso a dados.'],
     ['Python',
      'Linguagem dinâmica e interpretada, com tipagem forte. Na implementação CPython, o GIL limita a execução paralela de threads em '
      'código dependente de CPU (conferir a versão). Muito usada em automação, dados e IA.'],
     ['TypeScript',
      'Superconjunto tipado do JavaScript, que é transpilado para JavaScript. Tipos estáticos, interfaces e genéricos ajudam a detectar '
      'erros antes da execução.'],
     ['Angular',
      'Framework baseado em TypeScript para aplicações de página única (SPA). Componentes com templates, diretivas, serviços com '
      'injeção de dependências, roteamento, formulários e RxJS (observáveis) para fluxos assíncronos. Angular CLI gera e constrói projetos.'],
     ['React Native',
      'Framework para aplicativos móveis multiplataforma com JavaScript ou TypeScript e React; renderiza componentes nativos de cada '
      'plataforma. Mantido pela Meta.']],
    ['Tipagem Estática Detecta Antes, Dinâmica Detecta ao Executar',
     'Em Java e TypeScript, muitos erros de tipo aparecem na compilação. Em Python, aparecem em tempo de execução (a menos que se use '
     'verificadores de tipo à parte).'])
sec('20. Persistência: Hibernate, Redis, MongoDB, Flyway e Liquibase',
    'Tecnologias de persistência e de evolução de esquemas citadas no programa.',
    [['Hibernate e JPA',
      'JPA é a especificação de mapeamento objeto-relacional (ORM) do Jakarta EE; o Hibernate é sua implementação mais conhecida. '
      'Entidades mapeadas em tabelas; consultas em JPQL ou HQL. Carregamento preguiçoso (lazy) e ansioso (eager). Problema N+1: uma '
      'consulta principal mais N consultas adicionais, resolvido com junções de busca (fetch join) ou carga em lote. Cache de primeiro '
      'nível (sessão) e de segundo nível (opcional). Bloqueio otimista com campo de versão.'],
     ['Redis',
      'Armazenamento chave-valor em memória, com estruturas como strings, hashes, listas, conjuntos, conjuntos ordenados e streams. '
      'Suporta expiração (TTL), publicação e assinatura, e persistência por snapshot (RDB) ou log (AOF). Replicação, Sentinel (failover) '
      'e Cluster, com 16.384 slots de hash. Porta padrão 6379. Usos: cache, sessões, filas e limitação de taxa.'],
     ['MongoDB',
      'Banco de documentos (BSON). Conjuntos de réplicas (um primário e secundários, com eleição) e fragmentação (sharding) por chave de '
      'shard. Índices e pipeline de agregação. Porta padrão 27017.'],
     ['Flyway',
      'Versiona migrações de banco: scripts SQL nomeados por versão (como V1__criar_tabela.sql) executados em ordem e registrados em uma '
      'tabela de histórico, com verificação de checksum para detectar alterações. Há migrações repetíveis (prefixo R__).'],
     ['Liquibase',
      'Descreve mudanças em changelogs (XML, YAML, JSON ou SQL) formados por changesets, identificados por id, autor e arquivo e '
      'registrados em tabela de controle. Suporta reversão (rollback) e vários bancos.'],
     ['Boas práticas',
      'Migrações versionadas e revisadas, mudanças compatíveis com versões anteriores (para implantar sem parada), e ambientes de '
      'homologação parecidos com a produção.']],
    ['Flyway por Versão de Script, Liquibase por Changeset',
     'Ambos versionam o esquema do banco. Flyway é centrado em scripts numerados; Liquibase, em changesets com id e autor, e suporta '
     'formatos declarativos.'])
sec('21. DevOps no Desenvolvimento: Git Avançado, Gitflow, Jenkins, Tekton e SonarQube',
    'Complementa a seção 9 com estratégias de ramificação e ferramentas de pipeline citadas no programa.',
    [['Fluxos de ramificação',
      'Gitflow: ramos main (produção) e develop (integração), mais feature, release e hotfix. GitHub Flow: main sempre implantável, com '
      'ramos curtos e pull requests. Trunk-based development: integração frequente em um tronco com ramos muito curtos e feature flags.'],
     ['Comandos e cuidados',
      'git fetch baixa sem alterar; git pull é fetch mais merge (ou rebase). git reset move o ponteiro (soft, mixed, hard); git revert cria um '
      'commit que desfaz outro, seguro em histórico compartilhado. Regra de ouro: não reescreva (rebase) histórico já publicado. '
      'Fast-forward avança o ponteiro sem commit de mesclagem.'],
     ['Jenkins',
      'Servidor de automação com controlador e agentes. O pipeline como código é descrito em um Jenkinsfile (sintaxe declarativa ou '
      'com script), com etapas (stages), passos (steps) e plugins.'],
     ['Tekton',
      'Framework de CI/CD nativo do Kubernetes. Recursos: Task (passos executados em contêineres), Pipeline (encadeia tarefas), '
      'TaskRun e PipelineRun (execuções). Roda no cluster e é declarativo.'],
     ['Portões de qualidade no pipeline',
      'Etapas típicas: compilar, testes unitários, análise estática (SonarQube com quality gate), varredura de dependências e de '
      'imagens, empacotamento (imagem Docker), implantação e testes ponta a ponta. Helm empacota a implantação no Kubernetes (veja '
      'Middleware).'],
     ['Estratégias de liberação',
      'Blue-green, canário, implantação gradual (rolling) e feature flags, que ativam ou desativam funcionalidades sem nova implantação.']],
    ['Feature Flag Separa Implantação de Liberação',
     'Com feature flags, o código pode estar em produção desligado e ser ativado depois, reduzindo o risco. Isso é diferente de '
     'implantar uma nova versão.'])
sec('22. Métricas de Software e Análise de Pontos de Função (APF)',
    'A APF mede o tamanho funcional do software sob a ótica do usuário, independentemente da tecnologia. O edital SEFAZ-BA 2022 '
    'para a área de TI cita a Análise de Pontos de Função e o planejamento e controle de métricas de projeto.',
    [['Tipos de função (IFPUG)',
      'Funções de dados: ALI (arquivo lógico interno, mantido pela aplicação) e AIE (arquivo de interface externa, mantido por outra '
      'aplicação). Funções transacionais: EE (entrada externa, altera dados), SE (saída externa, com processamento) e CE (consulta '
      'externa, só recuperação).'],
     ['Complexidade',
      'Cada função é classificada em baixa, média ou alta pela quantidade de tipos de dados (DER) e de tipos de registros (RLR) nos '
      'arquivos, ou de arquivos referenciados (ALR) nas transações.'],
     ['Passos da contagem',
      'Definir o tipo de contagem, o escopo e a fronteira da aplicação; contar as funções de dados e as transacionais; obter os pontos de '
      'função não ajustados (PFNA); aplicar o fator de ajuste (opcional); obter os pontos de função ajustados (PFA).'],
     ['Fator de ajuste (VAF)',
      'São 14 características gerais do sistema, cada uma com nota de 0 a 5. VAF = 0,65 + 0,01 x soma das notas, variando de 0,65 a 1,35. '
      'PFA = PFNA x VAF.'],
     ['Outras métricas',
      'SNAP mede requisitos não funcionais. NESMA e COSMIC são outros métodos de medição de tamanho funcional. Pontos de história '
      '(story points) são estimativa relativa das equipes ágeis, e a velocidade é a quantidade entregue por iteração.'],
     ['Uso',
      'Estimativa de esforço e prazo (produtividade em horas por ponto de função), contratação de fábrica de software por resultado, '
      'acompanhamento de escopo e benchmarking.']],
    ['Função de Dados é Arquivo Lógico, Transacional é Fluxo',
     'ALI e AIE são dados. EE, SE e CE são transações. A diferença entre ALI e AIE é quem mantém o arquivo: a própria aplicação (ALI) '
     'ou outra (AIE).'])
sec('23. Referências e Conferência',
    'Conferência realizada em 21/09/2026.',
    [['Referências',
      'Sommerville, Engenharia de Software; Pressman, Engenharia de Software; Gamma et al. (GoF), Padrões de Projeto; Robert C. Martin, '
      'Clean Code e Clean Architecture; Fowler (Patterns of Enterprise Application Architecture, e artigos sobre microsserviços, CQRS, '
      'Event Sourcing e Strangler Fig); Newman, Building Microservices; Evans, Domain-Driven Design; Larman, Applying UML and Patterns; '
      'Fielding (dissertação sobre REST) e RFC 9110; Manual de Práticas de Contagem do IFPUG; documentação de Spring, Angular, '
      'Hibernate, Redis, MongoDB, Flyway, Liquibase, Jenkins, Tekton, SonarQube, JUnit, Mockito, Jest e Playwright; Edital SEFAZ-CE '
      '2026 (FCC), Anexo VI, e Edital SEFAZ-BA 2022 (FGV), Anexo I.'],
     ['Corrigido nesta revisão',
      'Fórmulas em LaTeX (V(G)) reescritas; "Alto Acoplamento Coesivo" para Alta Coesão; DIP separado de injeção de dependências e '
      'IoC; Observer distinguido de Pub/Sub; Pirâmide de Testes atribuída a Mike Cohn e difundida por Fowler; "a maioria dos erros" nos '
      'valores limite suavizado; REST "sobre HTTP nativo e síncrono" reformulado e HATEOAS incluído; diagramas UML completados (7 + 7); '
      'seção de armadilhas atribuída às bancas sem evidência.'],
     ['A conferir',
      'Detalhes de versões de Spring Boot, Angular e ferramentas; regras de contagem da APF na versão do manual do IFPUG adotada; '
      'comportamento do GIL na versão do Python usada.']],
    ['Regra de Conteúdo', 'Este material não afirma nada sem fonte. Se houver divergência com a documentação oficial, ela prevalece.'])

ap['subtitle'] = ('Processos e Ágil, Requisitos, UML 2.5, SOLID e GRASP, Padrões GoF, Arquiteturas e Microsserviços (BFF, CQRS, Saga), '
                  'REST e Segurança Web, Testes e SonarQube, Java/Spring, Angular, Persistência, Git, CI/CD e Pontos de Função')
json.dump(dados, open(ARQ, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('Engenharia de Software atualizada: %d seções.' % len(S))
