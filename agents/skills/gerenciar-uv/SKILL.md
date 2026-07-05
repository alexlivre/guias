---
name: gerenciar-uv
description: Gerencia, inicializa e configura ambientes Python isolados (.venv) e dependências de forma ultra-rápida utilizando a ferramenta 'uv'.
license: MIT
compatibility: claude-code, opencode, custom-agents
---

## Quando me usar (Gatilhos de Ativação)

Você deve ativar e executar esta skill IMEDIATAMENTE se o usuário expressar qualquer uma das intenções abaixo (seja de forma explícita ou implícita):

1. **Criação Direta de Ambiente:** "cria um ambiente", "configurar venv", "inicializar python 3.10", "prepara a pasta", "coloca o ambiente na pasta".
2. **Criação de Nova Aplicação:** "vou criar um app", "vamos começar um projeto python", "cria um script novo", "iniciar projeto web".
3. **Manutenção de Aplicação Existente:** Se o usuário pedir para instalar pacotes ("bota o pandas aí", "instala o fastapi") ou rodar o projeto, mas a pasta ainda **não tiver** um diretório `.venv`.

## O que eu faço (Instruções do Agente)

Sempre que ativada, você deve seguir este fluxo rigoroso no terminal do projeto:

### Passo 1: Descobrir a Versão do Python
- Pergunte ou deduza a versão do Python. Se o usuário não especificar (ex: apenas disser "cria o ambiente"), assuma **3.10** como padrão ou use a versão mais estável atual (ex: 3.12/3.13), dependendo do contexto da aplicação.

### Passo 2: Inicializar o Projeto e o Ambiente
Rode em sequência os comandos no terminal da pasta do projeto:

1. `uv init` (Apenas se a pasta estiver completamente vazia, para criar o `pyproject.toml`).
2. `uv python pin <versao_escolhida>` (Cria o arquivo `.python-version` na raiz).
3. `uv venv` (Cria a pasta `.venv` local com o Python isolado).

### Passo 3: Configurar o Cursor/VS Code (.cursorrules)
Para garantir que o fluxo de Vibe Coding continue 100% automático, crie um arquivo chamado `.cursorrules` na raiz do projeto com o seguinte conteúdo:

```markdown
Sempre use o `uv` para este projeto. Comandos: `uv add <pacote>` para instalar e `uv run <script.py>` para rodar. Nunca sugira pip ou venv tradicional.
```

### Passo 4: Instalar Dependências (se solicitado)
Se o usuário pedir para instalar pacotes:

```bash
uv add <pacote1> <pacote2>
```

Para requirements.txt existente:

```bash
uv pip install -r requirements.txt
```

### Passo 5: Rodar Scripts (se solicitado)
Para rodar scripts Python:

```bash
uv run <script.py>
```

Para rodar comandos no ambiente:

```bash
uv run <comando>
```

## Comandos de Referência Rápida

| Ação | Comando |
|------|---------|
| Criar pyproject.toml | `uv init` |
| Fixar versão Python | `uv python pin 3.10` |
| Criar .venv | `uv venv` |
| Instalar pacote | `uv add <pacote>` |
| Instalar de requirements | `uv pip install -r requirements.txt` |
| Rodar script | `uv run <script.py>` |
| Listar pacotes | `uv pip list` |
| Desinstalar pacote | `uv remove <pacote>` |

## Restrições

- **NUNCA** use `pip` ou `venv` tradicional — sempre `uv`
- **NUNCA** instale pacotes globalmente — sempre no `.venv` do projeto
- Se `uv` não estiver instalado, instale com: `pip install uv` ou `curl -LsSf https://astral.sh/uv/install.sh | sh`
