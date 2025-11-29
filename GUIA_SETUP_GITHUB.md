# Guia de Setup do GitHub - Passo a Passo

**Pietro, este guia vai te ajudar a configurar seu portfólio no GitHub do zero. Siga cada passo com calma!**

---

## 🎯 Objetivo

Criar um repositório profissional no GitHub que servirá como seu **portfólio técnico** para recrutadores e empresas.

---

## 📋 Pré-requisitos

- [ ] Conta no GitHub (se não tiver, crie em https://github.com/signup)
- [ ] Git instalado no seu computador
- [ ] Terminal/Prompt de Comando

---

## 🚀 Passo 1: Configurar o Git (Primeira Vez)

Se você nunca configurou o Git, execute estes comandos no terminal:

```bash
# Configurar seu nome (será visível nos commits)
git config --global user.name "Pietro Giacomin Conte"

# Configurar seu e-mail (use o mesmo do GitHub)
git config --global user.email "seu_email@example.com"

# Verificar configuração
git config --list
```

---

## 🗂️ Passo 2: Criar o Repositório no GitHub

### 2.1. Via Interface Web (Mais Fácil)

1. Acesse https://github.com
2. Clique no botão **"+"** no canto superior direito
3. Selecione **"New repository"**
4. Preencha:
   - **Repository name:** `Cybersecurity-Portfolio`
   - **Description:** `Meu portfólio técnico de Cybersecurity - Writeups, Scripts e Projetos`
   - **Visibilidade:** ✅ **Public** (para recrutadores verem)
   - **Initialize:** ❌ NÃO marque nenhuma opção (vamos fazer manualmente)
5. Clique em **"Create repository"**

---

## 💻 Passo 3: Criar a Estrutura Local

### 3.1. Criar o Diretório do Projeto

```bash
# Navegar para onde você quer criar o repositório
cd ~/Documents  # ou qualquer outro local

# Criar o diretório
mkdir Cybersecurity-Portfolio
cd Cybersecurity-Portfolio
```

### 3.2. Criar a Estrutura de Pastas

```bash
# Criar todas as pastas de uma vez
mkdir -p Writeups/TryHackMe Writeups/HackTheBox Scripts Notes Projects

# Verificar estrutura criada
tree .
# Ou no Windows:
dir /s
```

A estrutura deve ficar assim:
```
Cybersecurity-Portfolio/
├── Writeups/
│   ├── TryHackMe/
│   └── HackTheBox/
├── Scripts/
├── Notes/
└── Projects/
```

### 3.3. Copiar os Arquivos que Criei para Você

Copie os arquivos que criei para dentro do diretório `Cybersecurity-Portfolio`:

- `README.md` (arquivo principal)
- `TEMPLATE_WRITEUP.md` (template para writeups)
- `.gitignore` (arquivos a serem ignorados)

---

## 🔗 Passo 4: Inicializar o Repositório Git

```bash
# Inicializar o repositório Git
git init

# Adicionar todos os arquivos ao staging
git add .

# Fazer o primeiro commit
git commit -m "Initial commit: Estrutura do portfólio criada"
```

---

## ☁️ Passo 5: Conectar ao GitHub e Fazer Push

### 5.1. Adicionar o Repositório Remoto

Substitua `PGC13` pelo seu username do GitHub:

```bash
git remote add origin https://github.com/PGC13/Cybersecurity-Portfolio.git
```

### 5.2. Fazer o Push (Enviar para o GitHub)

```bash
# Renomear a branch para main (padrão do GitHub)
git branch -M main

# Fazer o push
git push -u origin main
```

**Se pedir usuário e senha:**
- **Usuário:** Seu username do GitHub
- **Senha:** Use um **Personal Access Token** (não a senha da conta)

---

## 🔑 Passo 6: Criar Personal Access Token (Se Necessário)

Se o GitHub pedir senha e não aceitar, você precisa criar um token:

1. Vá em https://github.com/settings/tokens
2. Clique em **"Generate new token"** → **"Generate new token (classic)"**
3. Preencha:
   - **Note:** `Git Access Token`
   - **Expiration:** `90 days` (ou mais)
   - **Scopes:** Marque apenas `repo` (acesso total aos repositórios)
4. Clique em **"Generate token"**
5. **COPIE O TOKEN** (você não vai ver ele novamente!)
6. Use esse token como "senha" quando o Git pedir

---

## ✅ Passo 7: Verificar se Funcionou

1. Acesse https://github.com/PGC13/Cybersecurity-Portfolio
2. Você deve ver:
   - ✅ Arquivo `README.md` renderizado
   - ✅ Pastas `Writeups`, `Scripts`, `Notes`, `Projects`
   - ✅ Arquivo `.gitignore`

---

## 📝 Passo 8: Workflow Diário (Adicionar Writeups)

Sempre que você resolver uma máquina/sala:

### 8.1. Criar o Writeup

```bash
# Exemplo: Você resolveu a sala "Pickle Rick" do TryHackMe
cd Writeups/TryHackMe
cp ../../TEMPLATE_WRITEUP.md PickleRick.md

# Editar o arquivo com seu editor favorito
nano PickleRick.md  # ou vim, code, etc.
```

### 8.2. Adicionar ao Git

```bash
# Voltar para a raiz do repositório
cd ~/Documents/Cybersecurity-Portfolio

# Adicionar o novo arquivo
git add Writeups/TryHackMe/PickleRick.md

# Fazer commit
git commit -m "Writeup: TryHackMe - Pickle Rick"

# Fazer push para o GitHub
git push
```

### 8.3. Atualizar o README.md

Sempre que adicionar um writeup, atualize a seção "Writeups Recentes" no `README.md`:

```markdown
## 📝 Writeups Recentes

- [TryHackMe] - [Pickle Rick](Writeups/TryHackMe/PickleRick.md)
- [TryHackMe] - [Nome da Sala 2](Writeups/TryHackMe/sala2.md)
```

Depois:
```bash
git add README.md
git commit -m "Atualizar README com novo writeup"
git push
```

---

## 🎨 Passo 9: Personalizar o README (Opcional mas Recomendado)

### 9.1. Adicionar um Banner

Crie um banner personalizado em https://www.canva.com (gratuito) com:
- Seu nome
- "Cybersecurity Portfolio"
- Elementos visuais (código, terminal, etc.)

Salve como `banner.png` e adicione ao repositório:

```bash
# Criar pasta para imagens
mkdir assets

# Adicionar o banner
git add assets/banner.png
git commit -m "Adicionar banner ao portfólio"
git push
```

No `README.md`, substitua:
```markdown
![Banner](https://via.placeholder.com/1200x300.png?text=Cybersecurity+Portfolio)
```

Por:
```markdown
![Banner](assets/banner.png)
```

### 9.2. Adicionar Badges (Opcional)

Adicione badges para suas certificações. Exemplo:

```markdown
![ESR](https://img.shields.io/badge/ESR-Teste%20de%20Invas%C3%A3o-blue)
![Desec](https://img.shields.io/badge/Desec-Pentest%20Professional-red)
![Cisco](https://img.shields.io/badge/Cisco-CyberOps%20Associate-blue)
```

---

## 🔄 Comandos Git Mais Usados (Cheat Sheet)

```bash
# Ver status dos arquivos
git status

# Adicionar arquivo específico
git add arquivo.md

# Adicionar todos os arquivos modificados
git add .

# Fazer commit
git commit -m "Mensagem descritiva"

# Enviar para o GitHub
git push

# Atualizar repositório local com mudanças do GitHub
git pull

# Ver histórico de commits
git log

# Ver diferenças antes de commitar
git diff
```

---

## ✅ Checklist Final

- [ ] Repositório criado no GitHub
- [ ] Estrutura de pastas criada localmente
- [ ] Arquivos `README.md`, `TEMPLATE_WRITEUP.md` e `.gitignore` adicionados
- [ ] Primeiro commit feito
- [ ] Push para o GitHub realizado com sucesso
- [ ] Repositório visível em https://github.com/PGC13/Cybersecurity-Portfolio
- [ ] README.md personalizado com suas informações
- [ ] Link do GitHub adicionado ao LinkedIn

---

## 🚀 Próximos Passos

1. **Resolver sua primeira sala do TryHackMe**
2. **Criar seu primeiro writeup** usando o template
3. **Fazer commit e push** para o GitHub
4. **Compartilhar no LinkedIn:** "Acabei de criar meu portfólio técnico de Cybersecurity! Confira: [link]"

---

**Pietro, seu portfólio está pronto! Agora é só alimentá-lo com writeups e projetos. Recrutadores vão AMAR ver isso!** 🚀🔒
