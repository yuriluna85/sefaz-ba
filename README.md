# SEFAZ-BA 2026 — Hub de Estudos e Novidades
> **Projeto desenvolvido sob a chancela 🔬 YLuna85 LABs**


Um painel interativo desenvolvido em Python (Flask) e HTML/CSS/JS (com design moderno e responsivo) para organizar e gerenciar a preparação de dois irmãos para o concurso da **SEFAZ-BA 2026**.

## Estrutura do Hub

- **Trilha de Estudos - Irmão TI**: Focada no cargo de **Auditor Fiscal (Especialidade: Tecnologia da Informação)**. Contém matérias básicas (Língua Portuguesa, Raciocínio Lógico, Estatística, Direito Administrativo, Direito Constitucional, Direito Tributário, Contabilidade Geral) e específicas avançadas de TI.
- **Trilha de Estudos - Irmão Geral**: Focada no cargo de **Agente de Tributos Estaduais (Qualquer Graduação)**. Contém as matérias básicas e específicas focadas em Legislação Tributária do Estado da Bahia (ICMS, IPVA, ITD, PAF-BA), Auditoria Fiscal e Finanças Públicas.
- **Integração de Arquivos Locais**: O painel detecta automaticamente os arquivos PDF na pasta `Concurso SEFAZ` (no mesmo nível deste diretório) e os disponibiliza para download diretamente pela interface.
- **Videoaulas e Recursos**: Compilados de termos de buscas e atalhos de playlists gratuitas de alta qualidade no YouTube para as principais matérias.
- **Cronograma Semanal**: Calendário de estudos estruturado para guiar a rotina dos dois em conjunto.
- **Persistência de Progresso**: Salva o andamento das matérias de cada usuário em um arquivo `progress.json` local.

---

## Como Executar Localmente

### 1. Pré-requisitos
Certifique-se de ter o **Python 3** instalado em sua máquina.

### 2. Instalar as Dependências
Abra o terminal na pasta deste projeto e instale o Flask:
```bash
pip install flask
```

### 3. Rodar a Aplicação
Inicie o servidor local executando:
```bash
python app.py
```

### 4. Acessar no Navegador
Abra o seu navegador e acesse o endereço:
```
http://127.0.0.1:5000/
```

---

## Como Subir para o GitHub

Para publicar a sua base de estudos no GitHub, siga as etapas abaixo:

1. **Crie um repositório no seu GitHub**:
   - Vá em [github.com](https://github.com/) e crie um novo repositório público (para o GitHub Pages gratuito) ou privado (por exemplo, `sefaz-ba-2026-estudos`).

2. **Inicialize o repositório Git localmente**:
   Abra o terminal na pasta do projeto e execute:
   ```bash
   git init
   ```

3. **Crie um arquivo `.gitignore`** para evitar subir arquivos temporários ou de banco local:
   ```bash
   echo "venv/\n__pycache__/\n*.pyc\nprogress.json" > .gitignore
   ```

4. **Adicione os arquivos e faça o primeiro commit**:
   ```bash
   git add .
   git commit -m "feat: setup do painel de estudos e simulado sefaz-ba 2026"
   ```

5. **Configure a branch principal e o repositório remoto**:
   ```bash
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   ```

6. **Envie os arquivos para o GitHub**:
   ```bash
   git push -u origin main
   ```

---

## 🌐 Publicação no GitHub Pages (Modo Estático)

Como reestruturamos o projeto deixando o `index.html` na raiz e implementamos caminhos relativos com fallbacks automáticos, você pode utilizar o simulado e as trilhas online de forma 100% gratuita através do **GitHub Pages**!

Para ativar o GitHub Pages no seu repositório:
1. No seu repositório no GitHub, clique na aba **Settings** (Configurações).
2. No menu lateral esquerdo, na seção *Code and automation*, clique em **Pages**.
3. Em *Build and deployment* -> *Source*, selecione **Deploy from a branch**.
4. Em *Branch*, selecione **main** e a pasta **/ (root)**, e clique em **Save**.
5. Aguarde cerca de 1 a 2 minutos e o GitHub fornecerá o link público da sua página (ex: `https://seu-usuario.github.io/seu-repositorio/`).

> [!NOTE]  
> Quando acessado pelo link do GitHub Pages (modo estático), o painel salvará todo o progresso dos checklists de forma independente no **localStorage** do navegador de cada usuário. Os simulados de múltipla escolha (60 questões) e discursivos (6 casos de estudo) funcionam de forma integral e responsiva. Apenas a aba de materiais locais (varredura da pasta física local do computador) não exibirá os arquivos, pois este recurso de varredura depende do servidor local em Python (`python app.py`) estar ativo na máquina.


## 📜 Log de Atualizações (Changelog)

### 📅 30/06/2026 - Estruturação de SEO & Monetização
- 🌐 **Otimização de SEO (White Hat)**: Inclusão de meta tags de indexação, dados estruturados JSON-LD e tags Open Graph (OG) para melhorar a relevância e indexação orgânica no Google.
- 💵 **Estrutura de Monetização**: Adicionados slots de publicidade responsivos (banner horizontal e lateral) compatíveis com o modo de alto contraste para Google AdSense e AdMob.

