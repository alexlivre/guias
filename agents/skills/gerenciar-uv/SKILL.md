---
name: gerenciar-uv
description: Gerencia ambientes Python isolados e dependências usando uv — detecta SO automaticamente, instala uv se necessário, e configura projetos Python modernos.
license: MIT
compatibility: claude-code, opencode, custom-agents
---

## Quando me usar (Gatilhos de Ativação)

Você deve ativar e executar esta skill IMEDIATAMENTE se o usuário expressar qualquer uma das intenções abaixo (seja de forma explícita ou implícita):

1. **Criação Direta de Ambiente:** "cria um ambiente", "configurar venv", "inicializar python 3.10", "prepara a pasta", "coloca o ambiente na pasta".
2. **Criação de Nova Aplicação:** "vou criar um app", "vamos começar um projeto python", "cria um script novo", "iniciar projeto web".
3. **Manutenção de Aplicação Existente:** Se o usuário pedir para instalar pacotes ("bota o pandas aí", "instala o fastapi") ou rodar o projeto, mas a pasta ainda **não tiver** um diretório `.venv`.
4. **Migração de Projeto:** Se o usuário quiser migrar de pip/poetry/conda para uv.

## O que eu faço (Instruções do Agente)

Sempre que ativada, você deve seguir este fluxo rigoroso:

---

### Passo 0: Detectar SO e Garantir que uv está Instalado

Primeiro, detecte o sistema operacional do usuário e verifique se `uv` está disponível:

```bash
uv --version
```

**Se `uv` estiver instalado** — anote a versão e siga para o Passo 1.

**Se `uv` NÃO estiver instalado**, instale pelo método correto do SO:

#### Windows (PowerShell)
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Alternativa com WinGet:
```powershell
winget install --id=astral-sh.uv -e
```
Alternativa com Scoop:
```powershell
scoop install main/uv
```

#### Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Alternativa (sem curl):
```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

#### macOS
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Alternativa com Homebrew:
```bash
brew install uv
```

> **IMPORTANTE:** Após instalar, pode ser necessário abrir um novo terminal para que o `PATH` seja atualizado.

---

### Passo 1: Detectar ou Instalar Python

O `uv` detecta automaticamente Python já instalado no sistema. Não é necessário instalar Python separadamente.

**Verificar Python disponível:**
```bash
uv python list --only-installed
```

**Se o usuário especificar uma versão** (ex: "cria com Python 3.12"):
```bash
uv python install 3.12
uv python pin 3.12
```

**Se o usuário NÃO especificar versão:**
- O `uv` baixa automaticamente a versão mais recente quando necessário
- Para fixar uma versão estável recomendada: `uv python pin 3.12`

> **Nota:** O `uv` usa distribuições `python-build-standalone` — são binários pré-compilados, portáveis, e não afetam o Python do sistema.

---

### Passo 2: Criar ou Inicializar o Projeto

#### Cenário A: Criar projeto do zero
```bash
uv init nome-do-projeto
cd nome-do-projeto
```
Isso cria automaticamente:
- `pyproject.toml` (metadados do projeto)
- `.python-version` (versão do Python)
- `.gitignore`
- `README.md`
- `main.py` (script inicial)

#### Cenário B: Inicializar em pasta existente (vazia)
```bash
cd pasta-do-projeto
uv init
```

#### Cenário C: Pasta já tem código Python
Se a pasta já contém arquivos `.py`, o `uv init` vai detectar e criar apenas os arquivos de configuração faltantes.

> **NÃO** crie `.venv` manualmente com `uv venv` — o `uv` cria automaticamente no primeiro `uv add` ou `uv run`.

---

### Passo 3: Fixar Versão do Python (se não fixada)

Se ainda não rodou `uv python pin` no Passo 1:
```bash
uv python pin 3.12
```

---

### Passo 4: Instalar Dependências

#### Para novos pacotes:
```bash
uv add <pacote1> <pacote2>
```

#### Com versão específica:
```bash
uv add 'requests==2.31.0'
uv add 'fastapi>=0.100'
```

#### De um requirements.txt existente:
```bash
uv add -r requirements.txt
```

#### Remover pacote:
```bash
uv remove <pacote>
```

---

### Passo 5: Rodar Scripts e Comandos

#### Rodar script Python:
```bash
uv run <script.py>
```

#### Rodar comando no ambiente:
```bash
uv run python -c "print('hello')"
uv run flask run -p 3000
```

#### Sincronizar ambiente manualmente:
```bash
uv sync
```

---

## Fluxo Resumido (Copia Rápida)

```
# 1. Instalar uv (se necessário)
curl -LsSf https://astral.sh/uv/install.sh | sh    # Linux/macOS
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows

# 2. Criar projeto
uv init meu-projeto && cd meu-projeto

# 3. Fixar Python
uv python pin 3.12

# 4. Instalar pacotes
uv add requests fastapi uvicorn

# 5. Rodar
uv run main.py
```

---

## Tabela de Instalação do uv por SO

| SO | Método Recomendado | Comando |
|----|-------------------|---------|
| **Windows** | Standalone (PowerShell) | `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex"` |
| **Windows** | WinGet | `winget install --id=astral-sh.uv -e` |
| **Windows** | Scoop | `scoop install main/uv` |
| **Linux** | Standalone (curl) | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| **Linux** | Standalone (wget) | `wget -qO- https://astral.sh/uv/install.sh \| sh` |
| **macOS** | Standalone (curl) | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| **macOS** | Homebrew | `brew install uv` |
| **Qualquer** | pip (NÃO recomendado) | `pip install uv` |

---

## Comandos de Referência Rápida

| Ação | Comando |
|------|---------|
| Verificar versão do uv | `uv --version` |
| Atualizar uv | `uv self update` |
| Criar projeto | `uv init <nome>` |
| Fixar versão Python | `uv python pin 3.12` |
| Instalar Python | `uv python install 3.12` |
| Listar Pythons instalados | `uv python list --only-installed` |
| Instalar pacote | `uv add <pacote>` |
| Instalar de requirements | `uv add -r requirements.txt` |
| Remover pacote | `uv remove <pacote>` |
| Rodar script | `uv run <script.py>` |
| Rodar comando | `uv run <comando>` |
| Sincronizar ambiente | `uv sync` |
| Listar pacotes | `uv pip list` |
| Gerar lockfile | `uv lock` |
| Build do projeto | `uv build` |

---

## Restrições

- **NUNCA** use `pip` ou `venv` tradicional — sempre `uv`
- **NUNCA** instale pacotes globalmente — sempre no `.venv` do projeto
- **NUNCA** use `pip install uv` como método principal — use standalone installer
- **NUNCA** crie `.venv` manualmente — o `uv` cria automaticamente
- **NUNCA** edite `uv.lock` manualmente — use `uv lock` ou `uv add`
- Se `uv` não estiver instalado, instale com standalone installer (método recomendado)
- Preferência de Python: use `uv python install` em vez de pyenv ou conda
- Para requirements.txt: use `uv add -r requirements.txt` em vez de `uv pip install -r`
