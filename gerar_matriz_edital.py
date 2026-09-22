"""Gera dados/matriz_edital.json: tópicos do programa de TI (SEFAZ-CE 2026 B02, FCC, e SEFAZ-BA 2022, FGV)
e o quanto cada um é tratado nas apostilas atuais (apostilas_conteudo.json).

Status por tópico: ausente (0 menções), citado (1 menção), raso (2-3), coberto (4+). É uma medida de
presença do termo, não de correção: a correção é verificada na Fase 1 (auditoria).
Uso: python gerar_matriz_edital.py
"""
import json
import os
import re
import sys
import unicodedata

BASE = os.path.dirname(os.path.abspath(__file__))
sys.stdout.reconfigure(encoding='utf-8')


def norm(s):
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()


# (bloco, tópico, padrões regex já normalizados, origem, apostila alvo sugerida)
CE = 'CE2026'
BA = 'BA2022'
T = [
    # Governança, gestão e contratações de TIC
    ('Governança e contratações de TIC', 'Governança de TI e alinhamento estratégico', [r'governanca de ti'], f'{CE}/{BA}', 'Governança e Contratações de TIC'),
    ('Governança e contratações de TIC', 'PETIC e PDTIC', [r'\bpetic\b', r'\bpdtic\b'], CE, 'Governança e Contratações de TIC'),
    ('Governança e contratações de TIC', 'Contratações de TIC (Lei 14.133: ETP, TR, SLA)', [r'\betp\b', r'termo de referencia', r'\bsla\b'], CE, 'Governança e Contratações de TIC'),
    ('Governança e contratações de TIC', 'Gestão financeira de TI (TCO, ROI, CAPEX, OPEX, FinOps)', [r'\btco\b', r'\broi\b', r'\bcapex\b', r'\bopex\b', r'finops'], CE, 'Governança e Contratações de TIC'),
    ('Governança e contratações de TIC', 'Gestão de riscos (ISO 31000)', [r'31000'], CE, 'Segurança e Riscos'),
    ('Governança e contratações de TIC', 'COBIT 2019', [r'cobit'], f'{CE}/{BA}', 'Governança e Contratações de TIC'),
    ('Governança e contratações de TIC', 'ITIL 4', [r'\bitil\b'], f'{CE}/{BA}', 'Governança e Contratações de TIC'),
    ('Governança e contratações de TIC', 'PMBOK 7', [r'pmbok'], f'{CE}/{BA}', 'Gestão de Projetos, Produtos e Processos'),
    ('Governança e contratações de TIC', 'MPS.BR e CMMI 2.0', [r'\bmps', r'\bcmmi\b'], f'{CE}/{BA}', 'Governança e Contratações de TIC'),
    ('Governança e contratações de TIC', 'BPMN, DMN e BPMS', [r'\bbpmn\b', r'\bdmn\b', r'\bbpms\b'], f'{CE}/{BA}', 'Gestão de Projetos, Produtos e Processos'),
    ('Governança e contratações de TIC', 'Six Sigma, Lean e Value Stream Mapping', [r'six sigma', r'\blean\b', r'value stream'], CE, 'Gestão de Projetos, Produtos e Processos'),
    # Segurança
    ('Segurança da informação e cibernética', 'Pilares CID, autenticidade e não repúdio', [r'nao repudio', r'confidencialidade'], f'{CE}/{BA}', 'Segurança e Riscos'),
    ('Segurança da informação e cibernética', 'Defesa em profundidade e Zero Trust', [r'zero trust', r'defesa em profundidade'], CE, 'Segurança e Riscos'),
    ('Segurança da informação e cibernética', 'ISO/IEC 27001:2022 e 27002:2022', [r'27001', r'27002'], CE, 'Segurança e Riscos'),
    ('Segurança da informação e cibernética', 'ISO/IEC 27005, 27035-1, 22301 e 27017', [r'27005', r'27035', r'22301', r'27017'], CE, 'Segurança e Riscos'),
    ('Segurança da informação e cibernética', 'NIST SP 800-61 (resposta a incidentes)', [r'800-61', r'\bnist\b'], CE, 'Segurança e Riscos'),
    ('Segurança da informação e cibernética', 'BIA, PCN, DRP, RPO e RTO', [r'\bbia\b', r'\bpcn\b', r'\bdrp\b', r'\brpo\b', r'\brto\b'], f'{CE}/{BA}', 'Segurança e Riscos'),
    ('Segurança da informação e cibernética', 'IAM, RBAC, SSO, MFA, OAuth 2.0 e OIDC', [r'\biam\b', r'\brbac\b', r'\bsso\b', r'\bmfa\b', r'oauth', r'openid|\boidc\b'], CE, 'Segurança e Riscos'),
    ('Segurança da informação e cibernética', 'PKI, X.509 e ICP-Brasil', [r'\bpki\b', r'x\.509', r'icp-brasil'], CE, 'Segurança e Riscos'),
    ('Segurança da informação e cibernética', 'Criptografia, HTTPS e TLS', [r'\btls\b', r'criptografia'], f'{CE}/{BA}', 'Segurança e Riscos'),
    ('Segurança da informação e cibernética', 'Firewall/NGFW, IDS/IPS, WAF, VPN, NAT', [r'\bngfw\b', r'\bids\b', r'\bips\b', r'\bwaf\b', r'\bvpn\b'], CE, 'Segurança e Riscos'),
    ('Segurança da informação e cibernética', 'SIEM, SOC, EDR e logs', [r'\bsiem\b', r'\bsoc\b', r'\bedr\b'], CE, 'Segurança e Riscos'),
    ('Segurança da informação e cibernética', 'OWASP, DevSecOps e SDL', [r'owasp', r'devsecops'], CE, 'Segurança e Riscos'),
    ('Segurança da informação e cibernética', 'Gestão de vulnerabilidades e incidentes', [r'vulnerabilidade'], CE, 'Segurança e Riscos'),
    ('Segurança da informação e cibernética', 'LGPD (Lei 13.709/2018)', [r'lgpd', r'13\.709'], CE, 'Segurança e Riscos'),
    ('Segurança da informação e cibernética', 'IA em segurança (ataques e defesa)', [r'\bia\b.*seguranca|seguranca.*\bia\b'], CE, 'Segurança e Riscos'),
    # Infraestrutura
    ('Infraestrutura', 'Redes: arquitetura, endereçamento, SDN, Wi-Fi', [r'\bsdn\b', r'ipv6', r'wireless|wi-fi'], f'{CE}/{BA}', 'Redes (ampliar)'),
    ('Infraestrutura', 'Windows Server e Active Directory', [r'windows server', r'active directory'], f'{CE}/{BA}', 'Infraestrutura: SO, virtualização, storage'),
    ('Infraestrutura', 'Linux (Red Hat)', [r'\blinux\b', r'red hat'], f'{CE}/{BA}', 'Infraestrutura: SO, virtualização, storage'),
    ('Infraestrutura', 'Virtualização (VMware, Hyper-V)', [r'vmware', r'hyper-v', r'virtualizacao'], f'{CE}/{BA}', 'Infraestrutura: SO, virtualização, storage'),
    ('Infraestrutura', 'Backup, recuperação, replicação, SAN e deduplicação', [r'\bsan\b', r'deduplicacao', r'replicacao', r'\bbackup\b'], f'{CE}/{BA}', 'Infraestrutura: SO, virtualização, storage'),
    ('Infraestrutura', 'JBoss/WildFly e servidores de aplicação', [r'jboss', r'wildfly'], CE, 'Middleware, mensageria e observabilidade'),
    ('Infraestrutura', 'Mensageria e streaming (ActiveMQ, Kafka, Debezium)', [r'activemq', r'kafka', r'debezium'], CE, 'Middleware, mensageria e observabilidade'),
    ('Infraestrutura', 'Kubernetes, containers e Ansible', [r'kubernetes', r'\bdocker\b', r'ansible'], CE, 'Middleware, mensageria e observabilidade'),
    ('Infraestrutura', 'Observabilidade (Zabbix, Prometheus, Grafana, ELK, APM)', [r'zabbix', r'prometheus', r'grafana', r'\belk\b', r'\bapm\b'], CE, 'Middleware, mensageria e observabilidade'),
    # Nuvem
    ('Computação em nuvem', 'IaaS, PaaS, SaaS e modelos de implantação', [r'\biaas\b', r'\bpaas\b', r'\bsaas\b', r'multicloud'], f'{CE}', 'Nuvem e FinOps'),
    ('Computação em nuvem', 'Serverless, event-driven e microsserviços', [r'serverless', r'event-driven|orientada a eventos', r'microsservico'], CE, 'Nuvem e FinOps'),
    ('Computação em nuvem', 'Segurança em nuvem (KMS, IAM, Zero Trust, conectividade)', [r'\bkms\b', r'direct connect', r'expressroute'], CE, 'Nuvem e FinOps'),
    ('Computação em nuvem', 'Plataformas AWS, Azure e GCP', [r'\baws\b', r'azure', r'google cloud|\bgcp\b'], CE, 'Nuvem e FinOps'),
    ('Computação em nuvem', 'FinOps, tagueamento e governança de custos', [r'finops', r'tagueamento'], CE, 'Nuvem e FinOps'),
    # Dados
    ('Banco de dados e engenharia de dados', 'Relacional, colunar e NoSQL; SQL e PL/SQL', [r'\bnosql\b', r'pl/sql', r'colunar'], f'{CE}/{BA}', 'Dados e Engenharia de Dados'),
    ('Banco de dados e engenharia de dados', 'DW, Data Mart, Data Lake, Lakehouse e Data Mesh', [r'data warehouse', r'data lake', r'lakehouse', r'data mesh|data mart'], f'{CE}/{BA}', 'Dados e Engenharia de Dados'),
    ('Banco de dados e engenharia de dados', 'ETL, pipelines, Parquet e formatos (CSV, JSON, XML)', [r'\betl\b', r'parquet', r'\bjson\b'], CE, 'Dados e Engenharia de Dados'),
    ('Banco de dados e engenharia de dados', 'Governança e qualidade de dados (linhagem, catálogo, metadados)', [r'linhagem', r'catalogacao|catalogo de dados', r'metadados'], CE, 'Dados e Engenharia de Dados'),
    ('Banco de dados e engenharia de dados', 'Streaming e tempo real (Spark Streaming, particionamento)', [r'streaming', r'particionamento'], CE, 'Dados e Engenharia de Dados'),
    # IA
    ('Ciência de dados e IA', 'Python, Hadoop e Spark', [r'hadoop', r'\bspark\b', r'python'], f'{CE}/{BA}', 'IA e Ciência de Dados'),
    ('Ciência de dados e IA', 'Aprendizado de máquina (supervisionado, não supervisionado, reforço)', [r'supervisionado', r'aprendizado de maquina'], CE, 'IA e Ciência de Dados'),
    ('Ciência de dados e IA', 'Deep learning, redes neurais e PLN', [r'deep learning', r'redes neurais', r'\bpln\b|linguagem natural'], CE, 'IA e Ciência de Dados'),
    ('Ciência de dados e IA', 'IA generativa, agentes e sistemas multiagentes', [r'generativa', r'multiagente', r'\bllm\b'], CE, 'IA e Ciência de Dados'),
    ('Ciência de dados e IA', 'MLOps e deploy', [r'mlops'], CE, 'IA e Ciência de Dados'),
    ('Ciência de dados e IA', 'Ética em IA (explicabilidade, viés)', [r'explicabilidade', r'vies algoritmico|vies'], CE, 'IA e Ciência de Dados'),
    # Software
    ('Engenharia de software', 'Requisitos, qualidade, métricas e testes', [r'requisitos', r'teste unitario|testes unitarios', r'metricas'], f'{CE}/{BA}', 'Desenvolvimento e Arquiteturas'),
    ('Engenharia de software', 'Padrões GoF e EIP', [r'\bgof\b', r'singleton', r'\beip\b|enterprise integration'], CE, 'Desenvolvimento e Arquiteturas'),
    ('Engenharia de software', 'Microsserviços (BFF, CQRS, Saga, Circuit Breaker)', [r'\bcqrs\b', r'\bsaga\b', r'circuit breaker', r'\bbff\b'], CE, 'Desenvolvimento e Arquiteturas'),
    ('Engenharia de software', 'APIs e segurança web (REST, CORS, CSRF, XSS)', [r'\brest\b', r'\bcors\b', r'\bcsrf\b', r'\bxss\b'], CE, 'Desenvolvimento e Arquiteturas'),
    ('Engenharia de software', 'Git, Gitflow, CI/CD, SonarQube, Helm', [r'\bgit\b', r'ci/cd', r'sonarqube', r'\bhelm\b'], CE, 'Desenvolvimento e Arquiteturas'),
    ('Engenharia de software', 'Linguagens e frameworks (Java, TypeScript, Spring, Angular)', [r'\bjava\b', r'typescript', r'spring', r'angular'], CE, 'Desenvolvimento e Arquiteturas'),
    ('Engenharia de software', 'Persistência (Redis, MongoDB, Hibernate, Flyway)', [r'\bredis\b', r'mongodb', r'hibernate', r'flyway|liquibase'], CE, 'Desenvolvimento e Arquiteturas'),
    # Gestão
    ('Gestão de projetos, produtos e serviços', 'Scrum, Kanban e gestão híbrida', [r'\bscrum\b', r'\bkanban\b'], f'{CE}/{BA}', 'Gestão de Projetos, Produtos e Processos'),
    ('Gestão de projetos, produtos e serviços', 'Backlog e priorização (MoSCoW, Kano)', [r'moscow', r'\bkano\b'], CE, 'Gestão de Projetos, Produtos e Processos'),
    ('Gestão de projetos, produtos e serviços', 'Elicitação, Design Thinking e Lean Inception', [r'design thinking', r'lean inception', r'historias de usuario'], CE, 'Gestão de Projetos, Produtos e Processos'),
    ('Gestão de projetos, produtos e serviços', 'Gestão de incidentes/problemas e melhoria contínua (Lean IT, Kaizen)', [r'kaizen', r'gerenciamento de incidentes|gestao de incidentes'], CE, 'Gestão de Projetos, Produtos e Processos'),
    ('Gestão de projetos, produtos e serviços', 'Competências comportamentais', [r'lideranca', r'inteligencia emocional', r'negociacao'], CE, 'Gestão de Projetos, Produtos e Processos'),
    ('Gestão de projetos, produtos e serviços', 'Análise de pontos de função e métricas de projeto', [r'pontos de funcao'], BA, 'Desenvolvimento e Arquiteturas'),
    ('Inglês', 'Inglês técnico', [r'ingles tecnico', r'english'], CE, 'Inglês Técnico'),
]


def status(n):
    return 'ausente' if n == 0 else 'citado' if n == 1 else 'raso' if n <= 3 else 'coberto'


def main():
    apos = json.load(open(os.path.join(BASE, 'apostilas_conteudo.json'), encoding='utf-8'))
    corpus = {a['filename']: norm(json.dumps(a, ensure_ascii=False)) for a in apos}
    linhas = []
    for bloco, topico, pats, origem, alvo in T:
        onde, total = {}, 0
        for f, t in corpus.items():
            n = sum(len(re.findall(p, t)) for p in pats)
            if n:
                onde[f] = n
                total += n
        linhas.append({'bloco': bloco, 'topico': topico, 'origem': origem, 'apostila_alvo': alvo,
                       'mencoes': total, 'status': status(len(onde) and total),
                       'apostilas_onde_aparece': onde})
    os.makedirs(os.path.join(BASE, 'dados'), exist_ok=True)
    json.dump({'gerado_em': '2026-09-21', 'referencias': {
        CE: 'Edital 01/2026 SEFAZ-CE (FCC), Anexo VI, área B02 - Tecnologia da Informação',
        BA: 'Edital 001/2022 SEFAZ-BA (FGV), Anexo I, Agente de Tributos Estaduais - Tecnologia da Informação'},
        'topicos': linhas}, open(os.path.join(BASE, 'dados', 'matriz_edital.json'), 'w', encoding='utf-8'),
        ensure_ascii=False, indent=1)
    cont = {}
    for l in linhas:
        cont[l['status']] = cont.get(l['status'], 0) + 1
    print('tópicos:', len(linhas), cont)
    bloco_atual = None
    for l in linhas:
        if l['bloco'] != bloco_atual:
            bloco_atual = l['bloco']
            print('\n##', bloco_atual)
        print('  %-8s %3d  %s' % (l['status'], l['mencoes'], l['topico']))


if __name__ == '__main__':
    main()
