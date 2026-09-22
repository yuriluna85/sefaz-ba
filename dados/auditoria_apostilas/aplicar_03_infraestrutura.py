"""Aplica a auditoria da Apostila de Infraestrutura, Cloud e DevOps (Fase 1) e acrescenta as seções de infraestrutura
do programa SEFAZ-CE 2026 (B02) e SEFAZ-BA 2022 que faltavam. Idempotente.
Relatório: dados/auditoria_apostilas/03_infraestrutura.md
Uso (na pasta do app): python dados/auditoria_apostilas/aplicar_03_infraestrutura.py
"""
import json
import os
import sys

APP = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARQ = os.path.join(APP, 'apostilas_conteudo.json')
dados = json.load(open(ARQ, encoding='utf-8'))
ap = next(a for a in dados if 'Infra' in a['filename'])
S = ap['sections']

if any(s['title'].startswith('11.') for s in S):
    print('Apostila de Infraestrutura já atualizada; nada a fazer.')
    sys.exit(0)


def bul(sec, inicio):
    return next(b for b in sec['bullets'] if b[0].strip().startswith(inicio))


def trocar(txt, velho, novo):
    assert velho in txt, 'trecho não encontrado: ' + velho[:70]
    return txt.replace(velho, novo)


# ---- Seção 1: datacenter ----
b = bul(S[0], 'Níveis de Classificação TIER')
b[1] = trocar(b[1], 'TIER I (Básico,', 'Valores de disponibilidade usados como referência (informativos, atribuídos ao Anexo da TIA-942; o Uptime Institute '
              'certifica a topologia, não um percentual): TIER I (Básico,')
b = bul(S[0], 'Salas Seguras')
b[1] = ('Salas seguras oferecem proteção modular contra fogo, água, poeira e acesso indevido. Salas-cofre são estruturas '
        'certificadas conforme a ABNT NBR 15247 por ensaios de laboratório (fogo, impacto e outros), com classes de resistência que '
        'limitam a temperatura e a umidade internas durante o ensaio. Os valores dependem da classe: conferir na norma.')
b = bul(S[0], 'Sistemas Complementares')
b[1] = ('Contenção de corredores quentes e frios (Hot/Cold Aisle Containment); detecção precoce de fumaça por aspiração (ASD; '
        'exemplo comercial: VESDA); extinção de incêndio por agentes limpos, que não deixam resíduo: gases inertes (como o IG-541, '
        'mistura de nitrogênio, argônio e CO2) e agentes químicos halogenados (como o FM-200, ou HFC-227ea, e o Novec 1230). '
        'FM-200 não é gás inerte. Os projetos seguem normas como a NFPA 2001 e as concentrações de projeto para áreas ocupadas.')

# ---- Seção 4: NOC/SOC (sem mudança factual) e Seção 5: nuvem ----
S[4]['content'] = ('A publicação especial NIST SP 800-145 é o referencial técnico mais citado para conceituar serviços em nuvem.')

# ---- Seção 10: Linux ----
S[9]['tip'] = ['Sticky Bit em Diretórios',
               'Com o Sticky Bit (representado por "t", como em drwxrwxrwt no /tmp), só o proprietário do arquivo, o proprietário do '
               'diretório ou o root podem renomear ou excluir o arquivo, mesmo que o diretório permita escrita a todos.']

# ---- Seções novas ----
S.append({
    'title': '11. Linux (Red Hat): Pacotes, LVM, Sistemas de Arquivos, SELinux e Firewall',
    'content': ('O programa de TI cita administração de servidores Linux, como Red Hat Enterprise Linux. Estes são os pontos '
                'centrais de administração que costumam ser cobrados.'),
    'bullets': [
        ['Gerenciamento de pacotes',
         'Na família Red Hat, o formato de pacote é o RPM (comando rpm). O gerenciador de pacotes com resolução de dependências é o '
         'DNF, que substituiu o YUM (o comando yum permanece como alias do dnf nas versões atuais). Na família Debian, usa-se dpkg e apt.'],
        ['LVM (Logical Volume Manager)',
         'Camadas: volumes físicos (PV), grupos de volumes (VG) e volumes lógicos (LV). Comandos típicos: pvcreate, vgcreate, '
         'lvcreate, lvextend. Permite redimensionar volumes e criar snapshots sem depender do particionamento fixo do disco.'],
        ['Sistemas de arquivos',
         'XFS é o sistema de arquivos padrão do RHEL (desde a versão 7): alto desempenho e boa escalabilidade; pode crescer online '
         '(xfs_growfs), mas não pode ser reduzido. Ext4 é amplamente usado e pode ser reduzido com o volume desmontado.'],
        ['Inicialização e serviços',
         'Sequência: firmware (BIOS/UEFI), carregador GRUB2, kernel, initramfs e systemd (PID 1). O systemd usa unidades e alvos '
         '(targets): multi-user.target (modo texto) e graphical.target (modo gráfico). Logs pelo journalctl.'],
        ['Contas e privilégios',
         'Contas em /etc/passwd, senhas com hash em /etc/shadow, grupos em /etc/group. O sudo delega privilégios conforme o '
         '/etc/sudoers, editado com visudo.'],
        ['SELinux',
         'Controle de acesso obrigatório (MAC) baseado em rótulos e políticas, além das permissões tradicionais. Modos: enforcing '
         '(aplica e bloqueia), permissive (apenas registra) e disabled. Comandos: getenforce e setenforce.'],
        ['firewalld',
         'Firewall dinâmico do RHEL, organizado em zonas, administrado com firewall-cmd, com regras em tempo de execução ou '
         'permanentes.'],
    ],
    'tip': ['XFS Cresce, Não Encolhe',
            'Um volume XFS pode ser ampliado, mas não reduzido. Para reduzir, é preciso recriar o sistema de arquivos e restaurar os '
            'dados. Snapshot de LVM não substitui backup.']})
S.append({
    'title': '12. Windows Server e Active Directory (Domain Services)',
    'content': ('O Active Directory Domain Services (AD DS) é o serviço de diretório do Windows Server: armazena objetos (usuários, '
                'grupos, computadores) e centraliza autenticação, autorização e políticas.'),
    'bullets': [
        ['Estrutura lógica',
         'Floresta (limite de segurança e de esquema), árvores e domínios. Unidades Organizacionais (OUs) organizam objetos e servem '
         'para delegar administração e aplicar políticas. Sites representam a topologia física de rede e orientam a replicação.'],
        ['Controladores de domínio e replicação',
         'A replicação é multimestre (qualquer controlador de domínio aceita alterações), exceto no controlador somente leitura '
         '(RODC). O Catálogo Global (GC) mantém uma cópia parcial de todos os objetos da floresta e apoia consultas e logon.'],
        ['Funções FSMO (cinco)',
         'Por floresta: Mestre de Esquema (Schema Master) e Mestre de Nomeação de Domínio (Domain Naming Master). Por domínio: Mestre '
         'de RID (RID Master), Emulador de PDC (PDC Emulator) e Mestre de Infraestrutura (Infrastructure Master).'],
        ['Autenticação',
         'Kerberos é o protocolo padrão de autenticação no domínio, baseado em tíquetes emitidos pelo KDC (nos controladores de '
         'domínio): TGT e tíquete de serviço. NTLM é o protocolo legado usado como alternativa. Kerberos usa a porta 88.'],
        ['LDAP e DNS',
         'LDAP é o protocolo de consulta ao diretório (porta 389; LDAPS na 636; catálogo global nas portas 3268 e 3269). O AD depende '
         'do DNS: os controladores de domínio se anunciam por registros SRV.'],
        ['Group Policy (GPO)',
         'Distribuição centralizada de configurações. Ordem de aplicação, do primeiro ao último: Local, Site, Domínio e OU (LSDOU); '
         'a política aplicada por último prevalece, salvo o uso de "Enforced" (imposição) e "Block Inheritance" (bloqueio de herança).'],
        ['Outros papéis comuns',
         'DNS, DHCP, servidor de arquivos, WSUS (atualizações), IIS (web), Hyper-V, AD CS (certificados) e AD FS (federação). '
         'Administração por console e por PowerShell, com cmdlets no formato verbo-substantivo (Get-ADUser, por exemplo).'],
    ],
    'tip': ['FSMO: Duas na Floresta, Três no Domínio',
            'Schema Master e Domain Naming Master são únicas na floresta. RID Master, PDC Emulator e Infrastructure Master são '
            'únicas em cada domínio. Total: cinco funções.']})
S.append({
    'title': '13. Virtualização: VMware vSphere e Hyper-V em Detalhe',
    'content': ('A virtualização consolida servidores e aumenta flexibilidade e disponibilidade. Os dois ecossistemas mais cobrados '
                'são o VMware vSphere e o Microsoft Hyper-V.'),
    'bullets': [
        ['VMware vSphere HA e FT',
         'vSphere HA reinicia as VMs em outro host quando um host falha; monitora hosts por batimentos de rede e de datastore, e '
         'possui controle de admissão para reservar capacidade e monitoramento de VM e de aplicações (painel Falhas e Respostas). '
         'vSphere Fault Tolerance (FT) mantém uma VM secundária idêntica em sincronia, sem interrupção quando o host primário falha.'],
        ['vMotion, DRS e vSAN',
         'vMotion migra VM ligada entre hosts sem parada; Storage vMotion migra os discos entre datastores; DRS balanceia carga do '
         'cluster; vSAN é o armazenamento definido por software que agrega os discos locais dos hosts (base da hiperconvergência).'],
        ['Hyper-V (Windows Server)',
         'Hipervisor Tipo 1 habilitado como papel do Windows Server. Recursos: Live Migration (migração de VM ligada), Hyper-V '
         'Replica (replicação assíncrona de VMs para outro local), clusters de failover com Volumes Compartilhados de Cluster (CSV), '
         'checkpoints, memória dinâmica e Storage Spaces Direct (armazenamento definido por software). O formato VHDX substituiu o '
         'VHD e suporta discos de até 64 TB; as VMs de geração 2 usam UEFI e Secure Boot.'],
        ['Conceitos comuns',
         'Sobrealocação (overcommit) de CPU e memória permite mais capacidade virtual que física, com risco de contenção. Ballooning '
         'e compressão de memória são técnicas de recuperação de memória. P2V converte servidor físico em virtual. Snapshot é ponto '
         'de retorno de curta duração, não é backup.'],
    ],
    'tip': ['HA Reinicia, FT Não Interrompe',
            'vSphere HA tem breve interrupção (a VM reinicia em outro host). vSphere FT mantém uma cópia em sincronia e não interrompe. '
            'Snapshot não protege contra falha do storage.']})
S.append({
    'title': '14. Backup, Replicação, Deduplicação e Recuperação',
    'content': ('Backup é a cópia de dados para recuperação. A estratégia é definida pelos objetivos de recuperação (RPO e RTO) e '
                'combina tipos de backup, mídias, locais e testes de restauração.'),
    'bullets': [
        ['Tipos de backup',
         'Completo (full): copia todos os dados selecionados. Incremental: copia o que mudou desde o último backup de qualquer tipo; '
         'backup rápido, restauração mais lenta (precisa do completo e de todos os incrementais). Diferencial: copia o que mudou '
         'desde o último completo; restauração precisa do completo e do último diferencial. Atenção: alguns materiais definem o '
         'incremental como "desde o último completo"; siga a definição da questão.'],
        ['Rotação e retenção',
         'Esquema Avô-Pai-Filho (GFS): backups diários (filho), semanais (pai) e mensais (avô) com retenções crescentes. Regra 3-2-1: '
         'três cópias, duas mídias, uma fora do local. Cópias imutáveis (WORM) e isoladas (air gap) protegem contra ransomware.'],
        ['Replicação',
         'Síncrona: a gravação só é confirmada após ocorrer nos dois locais; RPO próximo de zero, com impacto na latência e limite de '
         'distância. Assíncrona: confirma no local e replica depois; menor impacto, mas pode perder dados recentes (RPO maior que zero).'],
        ['Snapshots',
         'Pontos de retorno de curta duração no storage ou na VM; rápidos e eficientes em espaço. Ficam no mesmo sistema, então não '
         'substituem backup.'],
        ['Deduplicação e compressão',
         'Deduplicação elimina blocos repetidos, guardando um e referenciando os demais. Pode ser feita na origem (antes de enviar) '
         'ou no destino, em linha (inline, durante a gravação) ou pós-processamento. Compressão reduz o tamanho dos dados; as duas '
         'técnicas economizam espaço e banda.'],
        ['Mídias e testes',
         'Disco, fita (por exemplo, LTO, boa para arquivamento de longo prazo e custo por capacidade) e nuvem. Backup que nunca foi '
         'restaurado em teste não é confiável: testes periódicos de restauração fazem parte da estratégia.'],
    ],
    'tip': ['Incremental Rápido para Salvar, Diferencial Rápido para Restaurar',
            'Incremental grava menos e restaura com mais passos. Diferencial grava mais e restaura só com o completo mais o último '
            'diferencial. RAID e snapshot não são backup.']})
S.append({
    'title': '15. Tipos de Storage, SAN, Zoning e Virtualização de Armazenamento',
    'content': ('Complementa a seção 2 com os tipos de armazenamento e com conceitos de SAN e de armazenamento definido por '
                'software.'),
    'bullets': [
        ['Bloco, arquivo e objeto',
         'Bloco: volumes brutos acessados como discos (SAN, iSCSI, Fibre Channel). Arquivo: hierarquia de pastas e arquivos por NFS '
         'ou SMB (NAS). Objeto: dados com metadados e identificador único em espaço plano, acessados por API HTTP (como a API S3); '
         'escala massiva e boa para dados não estruturados, backups e data lakes.'],
        ['Zoning e LUN masking',
         'Em SAN Fibre Channel, o zoning no switch define quais portas ou WWNs (World Wide Names) podem se enxergar; pode ser por '
         'porta (hard) ou por WWN (soft). O LUN masking, no storage, define quais servidores enxergam cada LUN (Logical Unit Number).'],
        ['Camadas de mídia e NVMe',
         'HDD tem maior capacidade por custo; SSD tem menor latência e mais IOPS; NVMe usa o barramento PCIe e reduz a latência em '
         'relação a SATA e SAS. O tiering move dados entre camadas conforme a frequência de acesso (quentes em SSD, frios em HDD).'],
        ['Definido por software e hiperconvergência',
         'Armazenamento definido por software (SDS) separa o controle do hardware. A infraestrutura hiperconvergente (HCI) integra '
         'computação, armazenamento e rede virtualizados em nós x86 gerenciados por software, como vSAN e Storage Spaces Direct.'],
        ['Eficiência de capacidade',
         'Thin provisioning aloca espaço sob demanda; deduplicação e compressão reduzem o volume gravado; snapshots e clones '
         'compartilham blocos. Sobrealocação com thin provisioning exige monitorar o espaço real.'],
        ['RAID',
         'RAID protege contra falha de disco, não contra exclusão, corrupção ou ransomware. Na reconstrução (rebuild) de um disco, o '
         'desempenho cai e o risco de segunda falha aumenta, o que pesa em discos muito grandes.'],
    ],
    'tip': ['Zoning no Switch, Masking no Storage',
            'Zoning controla a visibilidade entre portas e WWNs na rede SAN. LUN masking controla, no storage, qual servidor acessa '
            'qual LUN. Os dois se complementam.']})
S.append({
    'title': '16. Cálculos de Disponibilidade e Confiabilidade',
    'content': ('Questões de infraestrutura pedem cálculos de disponibilidade, tempo de parada e associação de componentes em série '
                'e em paralelo.'),
    'bullets': [
        ['Fórmulas básicas',
         'Disponibilidade A = MTBF / (MTBF + MTTR). Indisponibilidade = 1 menos A. Tempo de parada por ano = (1 menos A) x 365 dias.'],
        ['Tabela dos noves (ano de 365 dias)',
         '99% = cerca de 3,65 dias de parada por ano; 99,9% = cerca de 8,76 horas; 99,99% = cerca de 52,6 minutos; 99,999% = cerca '
         'de 5,26 minutos.'],
        ['Componentes em série',
         'Se todos precisam funcionar, a disponibilidade do conjunto é o produto das disponibilidades: A = A1 x A2 x ... A cadeia '
         'fica menos disponível que o pior componente.'],
        ['Componentes em paralelo (redundância)',
         'Se basta um funcionar, a indisponibilidade é o produto das indisponibilidades: A = 1 menos [(1 - A1) x (1 - A2) x ...]. Dois '
         'componentes de 99% em paralelo dão 1 - 0,01 x 0,01 = 99,99%.'],
        ['MTBF, MTTF e MTTR',
         'MTBF: tempo médio entre falhas em itens reparáveis. MTTF: tempo médio até a falha em itens não reparáveis. MTTR: tempo '
         'médio para reparar e restaurar o serviço.'],
    ],
    'tip': ['Série Reduz, Paralelo Aumenta',
            'Em série multiplicam-se as disponibilidades (o resultado cai). Em paralelo multiplicam-se as indisponibilidades e '
            'subtrai-se de 1 (o resultado sobe). Exemplo: 0,99 x 0,99 = 98,01% em série; 99,99% em paralelo.']})
S.append({
    'title': '17. Referências e Conferência',
    'content': ('Conferência realizada em 21/09/2026. Os itens indicados como conferir dependem de norma paga ou de versão do produto.'),
    'bullets': [
        ['Referências',
         'ANSI/TIA-942; ABNT NBR 15247; NFPA 2001; NIST SP 800-145; documentação oficial Red Hat (RHEL), Microsoft (Active Directory, '
         'Hyper-V, Group Policy) e VMware (vSphere); RFCs de LDAP e Kerberos; SNIA (armazenamento); Edital SEFAZ-CE 2026 (FCC), '
         'Anexo VI, e Edital SEFAZ-BA 2022 (FGV), Anexo I.'],
        ['Corrigido nesta revisão',
         'FM-200 descrito como gás inerte (é agente químico halogenado); valores da sala-cofre da NBR 15247 removidos (dependem da '
         'classe); percentuais de disponibilidade dos TIERs marcados como referência informativa; Sticky Bit incluiu o proprietário '
         'do diretório; afirmação de que o NIST SP 800-145 é "exigido em editais" retirada.'],
        ['A conferir',
         'Valores exatos da NBR 15247 por classe; origem exata dos percentuais de disponibilidade citados para os TIERs; comportamento de recursos VMware e Hyper-V na versão em uso; portas e detalhes '
         'de protocolos no texto oficial.'],
    ],
    'tip': ['Regra de Conteúdo', 'Este material não afirma nada sem fonte. Se houver divergência com a norma vigente, a norma prevalece.']})

ap['subtitle'] = ('Datacenter TIA-942, Storage SAN/NAS/RAID, Backup, Alta Disponibilidade, Linux Red Hat, Windows Server e Active '
                  'Directory, Virtualização VMware e Hyper-V, Nuvem NIST SP 800-145, Docker, Kubernetes e CI/CD')
json.dump(dados, open(ARQ, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('Infraestrutura atualizada: %d seções.' % len(S))
