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

### 📅 05/07/2026 - Correção Ortográfica, Regeração das Apostilas e Favicon
- ✍️ **Correção Ortográfica em Lote**: Corrigidos diversos erros ortográficos, termos desacentuados e distorções de codificação (como `INTENCAO` para `INTENÇÃO`, `omissaõ` para `omissão`, `manipulaçao` para `manipulação`, `falsificaçao` para `falsificação`, `interpretacao` para `interpretação`, `matematicos` para `matemáticos`, etc.) diretamente no banco de dados [apostilas_conteudo.json](file:///G:/Meu%20Drive/APP/2.%20Projetos%20e%20Aplica%C3%A7%C3%B5es/2.2%20Aplica%C3%A7%C3%B5es%20e%20C%C3%B3digos%20(GitHub)/YLuna85%20LABs%20APPs/Concurso%20SEFAZ%20Dashboard/apostilas_conteudo.json).
- ⚙️ **Normalização de Arquivo**: Removidos caracteres de controle invisíveis e soft hyphens (`\xad` e `\u200b`) que causavam bugs de renderização no PDF.
- 📚 **Compilação e Regeração**: Executado o script [build_all_apostilas_ptbr.py](file:///G:/Meu%20Drive/APP/2.%20Projetos%20e%20Aplica%C3%A7%C3%B5es/2.2%20Aplica%C3%A7%C3%B5es%20e%20C%C3%B3digos%20(GitHub)/YLuna85%20LABs%20APPs/Concurso%20SEFAZ%20Dashboard/build_all_apostilas_ptbr.py) para regerar com sucesso todas as 15 apostilas em PDF com a ortografia e a formatação totalmente corrigidas.
- 🎨 **Favicon do Hub**: Copiado o ativo oficial da marca (`marca-yluna85-labs.jpg`) para a pasta de estáticos e adicionado o link de ícone no head do arquivo [index.html](file:///G:/Meu%20Drive/APP/2.%20Projetos%20e%20Aplica%C3%A7%C3%B5es/2.2%20Aplica%C3%A7%C3%B5es%20e%20C%C3%B3digos%20(GitHub)/YLuna85%20LABs%20APPs/Concurso%20SEFAZ%20Dashboard/index.html) para remover o ícone de página em branco padrão do navegador.

### 📅 04/07/2026 - Restauração e Enriquecimento das Apostilas Didáticas
- 📚 **Restauração de Conteúdo Completo (Anti-Nerf)**: Reconstruído o script [build_all_apostilas_ptbr.py](file:///G:/Meu%20Drive/APP/2.%20Projetos%20e%20Aplica%C3%A7%C3%B5es/2.2%20Aplica%C3%A7%C3%B5es%20e%20C%C3%B3digos%20(GitHub)/YLuna85%20LABs%20APPs/Concurso%20SEFAZ%20Dashboard/build_all_apostilas_ptbr.py) para gerar PDFs a partir do banco de dados estruturado [apostilas_conteudo.json](file:///G:/Meu%20Drive/APP/2.%20Projetos%20e%20Aplica%C3%A7%C3%B5es/2.2%20Aplica%C3%A7%C3%B5es%20e%20C%C3%B3digos%20(GitHub)/YLuna85%20LABs%20APPs/Concurso%20SEFAZ%20Dashboard/apostilas_conteudo.json). Isso recuperou o conteúdo completo de 10 a 11 páginas de cada uma das 15 apostilas originais que haviam sido sobrescritas por um modelo simplificado de 3 páginas.
- ✍️ **Enriquecimento de Língua Portuguesa**: Adicionados os conceitos de **Denotação**, **Conotação** e uma nova seção dedicada a **Figuras de Sintaxe** (com conceitos como Elipse, Zeugma, Hipérbato, Silepse, entre outros) na apostila de Língua Portuguesa, de modo a ter uma versão estendida de 11 páginas.
- ⚙️ **Automação**: Criados os scripts auxiliares [extract_all_to_json.py](file:///G:/Meu%20Drive/APP/_Scripts/extract_all_to_json.py) e [update_portuguese_and_generate.py](file:///G:/Meu%20Drive/APP/_Scripts/update_portuguese_and_generate.py) para automatizar a manutenção e o processo de regeneração segura.
- 🐛 **Correção de Busca**: Ajustado o script [update_portuguese_and_generate.py](file:///G:/Meu%20Drive/APP/_Scripts/update_portuguese_and_generate.py) para suportar busca de arquivos com acentuação, corrigindo a divergência de `'Apostila_Língua_Portuguesa.pdf'` vs `'Apostila_Lingua_Portuguesa.pdf'` e garantindo a perfeita compilação em lote das 15 apostilas.

### 📅 30/06/2026 - Estruturação de SEO & Monetização
- 🌐 **Otimização de SEO (White Hat)**: Inclusão de meta tags de indexação, dados estruturados JSON-LD e tags Open Graph (OG) para melhorar a relevância e indexação orgânica no Google.
- 💵 **Estrutura de Monetização**: Adicionados slots de publicidade responsivos (banner horizontal e lateral) compatíveis com o modo de alto contraste para Google AdSense e AdMob.

