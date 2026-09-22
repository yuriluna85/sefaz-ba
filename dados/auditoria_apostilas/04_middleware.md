# Apostila 04 (nova): Middleware, Mensageria e Observabilidade

Data: 21/09/2026. Apostila criada do zero, sem versão anterior a auditar. Fonte do escopo: programa SEFAZ-CE 2026 (FCC), área B02 (JBoss/WildFly, ActiveMQ, Kafka, Debezium, Kubernetes, Ansible, Zabbix, Prometheus, Grafana, ELK e APM), mais os tópicos de arquitetura orientada a serviços e web services do edital SEFAZ-BA 2022.

## Seções (14, 17 páginas)
1 Middleware (tipos e acoplamento); 2 Servidores Jakarta EE (WildFly e JBoss EAP: modos standalone e domain, portas 8080 e 9990, subsistemas); 3 Fundamentos de mensageria (fila e tópico, JMS, confirmação, DLQ, semânticas de entrega, idempotência); 4 Enterprise Integration Patterns; 5 ActiveMQ (Classic e Artemis); 6 Kafka: arquitetura (partições, offsets, grupos, replicação, retenção, KRaft); 7 Kafka: garantias e ecossistema (acks, Connect, Streams, Schema Registry, comparação com filas); 8 CDC e Debezium; 9 Kubernetes avançado (StatefulSet, probes, QoS, HPA, Secret, PV e PVC, RBAC, NetworkPolicy, CRI); 10 Ansible, Helm, Podman e OCI; 11 Observabilidade (três pilares, sinais dourados, RED, USE, SLI, SLO, SLA); 12 Prometheus, Grafana e Zabbix; 13 ELK, APM e OpenTelemetry; 14 Referências.

## Pontos em que o cuidado foi maior
- ZooKeeper e KRaft: descrito sem afirmar versão exata; marcado para conferir.
- Portas padrão (8080, 9990, 61616, 8161, 9092, 9090, 9100, 3000, 10050, 10051, 9200, 9300, 5601, 5044): conhecidas e estáveis, mas marcadas para conferir na versão instalada.
- Segredos no Kubernetes: descritos como codificados em base64, sem cifra por padrão.
- ActiveMQ: distinguido o Classic (5.x) do Artemis, que é o broker embutido no WildFly e no JBoss EAP.
- Nenhuma atribuição a bancas e nenhuma afirmação de "cai em prova" sem questão ligada.

## A conferir
Situação do ZooKeeper e do KRaft na versão do Kafka em uso; portas e valores padrão na versão instalada; subsistemas e arquivos de configuração do WildFly ou JBoss EAP instalado; suporte e requisitos do Debezium por banco de dados.

## Lacunas conhecidas
Microsserviços (BFF, CQRS, Saga, Circuit Breaker) vão para a apostila de Desenvolvimento e Arquiteturas; plataformas de nuvem (AWS, Azure, GCP), para a de Nuvem.

## Infraestrutura do app
O gerador de PDFs (build_all_apostilas_ptbr.py) agora atualiza sozinho a lista de contingência (STATIC_FILES) do main.js. Antes ela tinha 15 apostilas fixas e tamanhos antigos; agora reflete as 19 apostilas existentes.
