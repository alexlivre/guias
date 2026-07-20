# Guia Definitivo para Criação de AGENTS.md

> **Baseado em**: paper ETH Zurich (2025), análise de 2.500+ repositórios (GitHub), documentação oficial Anthropic, 60.000+ projetos usando o formato, paper "Beyond English" (Bar-Ilan University, 2025), e experiência prática de manutenção em 38+ projetos.

---

## Índice

1. [O que é AGENTS.md](#1-o-que-é-agentsmd)
2. [Princípios Fundamentais](#2-princípios-fundamentais)
3. [Estrutura Recomendada](#3-estrutura-recomendada)
4. [O que Incluir](#4-o-que-incluir)
5. [O que NÃO Incluir](#5-o-que-não-incluir)
6. [Idioma do Arquivo](#6-idioma-do-arquivo)
7. [Formatos por Ferramenta](#7-formatos-por-ferramenta)
8. [Antepadrões Comuns](#8-antepadrões-comuns)
9. [Auditoria e Manutenção](#9-auditoria-e-manutenção)
10. [Templates Prontos](#10-templates-prontos)
11. [Checklist Final](#11-checklist-final)
12. [Referências](#12-referências)

---

## 1. O que é AGENTS.md

`AGENTS.md` é um arquivo Markdown na raiz do repositório que serve como **README para agentes de IA**. É carregado automaticamente no contexto de cada sessão de coding agent.

**Compatível com 30+ ferramentas**:
- Codex, Claude Code, Gemini CLI, Cursor, RooCode, Aider, goose, Zed, Warp, VS Code, Devin, Junie, Amp, Kilo Code, Phoenix, Semgrep, Ona, Windsurf, Augment Code, e outros.

**Especificações**:
- Markdown puro, sem campos obrigatórios
- Sem YAML frontmatter obrigatório
- Sem sintaxe especial
- Limite do Antigravity/GEMINI.md: **12.000 caracteres**
- Tamanho ideal: **<150 linhas** (paper ETH Zurich, ro14nd.de)
- Suporta **aninhamento** (AGENTS.md em subpastas — o mais próximo vence)

---

## 2. Princípios Fundamentais

### 2.1. **Menos é mais** (paper ETH Zurich 2025)

| Configuração | Mudança em success rate | Mudança em custo de inferência |
|---|---|---|
| AGENTS.md auto-gerado | **−3%** | **+20%** |
| AGENTS.md escrito por humano | **+4%** | +19% |
| Sem AGENTS.md (baseline) | 0% | 0% |

> *"Instructions ARE followed—that's the problem. Agents respect AGENTS.md instructions, but unnecessary requirements make tasks harder, increasing reasoning tokens by 14–22%."*

### 2.2. **Só coloque o que o agente NÃO consegue descobrir sozinho**

Este é o princípio mais importante. O agente já sabe ler `package.json`, `Cargo.toml`, `requirements.txt`. Não duplique.

### 2.3. **Comandos imperativos, não diretivas vagas**

❌ "Be concise"  
✅ "Responda em até 3 frases"

❌ "Use boas práticas"  
✅ "Use o linter e formatador padrão do projeto"

### 2.4. **Framing positivo (Anthropic official)**

> *"Tell Claude what to do instead of what not to do."*

❌ "Não use markdown na resposta"  
✅ "Responda em parágrafos de prosa fluida"

**Por quê**: o "Pink Elephant Problem" — tentar suprimir um pensamento o torna mais saliente. Veja paper 16x Eval blog.

### 2.5. **Use o idioma mais forte**

> *"Stilted phrasing in a second language quietly degrades outputs."* — Anthropic

Recomendação oficial: escreva no seu idioma mais forte e peça tradução na saída, se necessário.

### 2.6. **Mostre, não explique (multishot)**

Exemplos concretos superam explicações abstratas. Use 3-5 exemplos curtos.

---

## 3. Estrutura Recomendada

### 3.1. Ordem das seções (importa!)

1. **Comandos executáveis** (com flags) — primeiro, sempre
2. **Project structure** (ponteiros curtos)
3. **Code style** (geralmente omitido — deixar para linter real)
4. **Testing strategy**
5. **Workflow / PR checklist**
6. **Hard boundaries** (segurança, segredos, prohibitions)
7. **Escape hatch** (when stuck → plano ou pergunta)

### 3.2. Comandos por arquivo vs. projeto inteiro

❌ Rode `pnpm test` antes de cada edição  
✅ Rode `pnpm vitest run path/to/file.test.ts` por arquivo editado

Razão: agents fazem loops de feedback. Suite completa a cada iteração custa caro.

### 3.3. Three-tier boundaries (Matt Nigh, GitHub blog)

Separe claramente:

```
✅ **Always do**: ...
⚠️ **Ask first**: ...
🚫 **Never do**: ...
```

> *"Never commit secrets" foi o constraint mais comum em 2.500+ repos analisados.*

---

## 4. O que Incluir

| Conteúdo | Por quê |
|---|---|
| **Comandos não-óbvios** | `uv pip install -e ".[dev]"` em vez de só `pip install` |
| **Tool-specific choices** | "Use podman not docker", "Use rg not grep" |
| **Conventions contraintuitivas** | "Commit messages usam DCO sign-off: `git commit -s`" |
| **Hard invariants** | "UID no Dockerfile deve casar com runAsUser em Go" |
| **Security boundaries** | "Never commit `.env` ou `.mcp.json`" |
| **PR/checklist expectations** | "PRs precisam de aprovação de CODEOWNERS" |
| **Conventions do projeto** | caminho custom, idioma, formato de log |

**Tools mencionados em AGENTS.md são usados 160x mais** que tools não mencionadas (paper ETH Zurich).

---

## 5. O que NÃO Incluir

| Conteúdo | Por quê é ruído |
|---|---|
| Codebase overviews / lista de diretórios | Empiricamente inútil — agente lê a árvore sozinho |
| Convenções de framework (React, Express) | Está nos dados de treino do modelo |
| Conteúdo do README | Agente lê README.md sozinho |
| Listas de dependências | Está em `package.json` etc |
| Descrição arquivo-por-arquivo | Agente explora conforme necessário |
| **Style guides** (linting, naming) | **Use o linter real — mais rápido, barato e determinístico** |
| Task-specific instructions (que aplicam só às vezes) | Dilui foco; agent só precisa de ~150-200 instruções |
| Conteúdo auto-gerado | Prejudica mais do que ajuda (-3%) |

---

## 6. Idioma do Arquivo

### Recomendação: **Híbrido** (PT/ES + termos técnicos em EN)

Paper "Beyond English" (ArXiv 2502.09331, Bar-Ilan University) testou 35 idiomas e concluiu:

> *"Selective pre-translation (traduzir só termos técnicos) consistentemente supera tanto tradução completa quanto inferência direta no idioma fonte."*

### Padrão recomendado:

**No idioma forte do autor**:
- Instruções/imperativas
- Descrições de seções
- Frases explicativas
- Mensagens de erro citadas

**Em inglês (universal/técnico)**:
- Termos técnicos consagrados: lint, commit, push, hardcode, suite, line coverage, build, deploy
- Nomes de tools: pytest, vitest, jest, MCP, ESLint, ruff
- Siglas: PR, CI/CD, OWASP, SQLi, XSS, CSRF
- Nomes próprios: Antigravity, Claude, GitHub

### Para autores brasileiros:

PT-BR é **high-resource**:
- GPT-4 / Claude / Sabia: ~9.8/10 em benchmarks PT-BR
- Anthropic lidera tradução PT-BR entre frontier models
- **Pode escrever AGENTS.md em PT-BR sem perda significativa de performance**

---

## 7. Formatos por Ferramenta

| Ferramenta | Arquivo | Limite | Localização |
|---|---|---|---|
| Generic / multi-tool | `AGENTS.md` | sem limite | raiz / subpastas |
| Anthropic Claude | `CLAUDE.md` | sem limite | raiz |
| Google Gemini / Antigravity | `GEMINI.md` | **12.000 chars** | raiz + `~/.gemini/GEMINI.md` (global) |
| GitHub Copilot | `.github/copilot-instructions.md` | — | `.github/` |
| Cursor | `.cursorrules` | — | raiz |
| Aider | `.aider.conf.yml` com `read: AGENTS.md` | — | raiz |

### Dois formatos comuns (use um):

**Formato A — Numerado (regras)**:

```markdown
## [RULE-001] Idioma

- **Faça**: código em inglês.
- **Faça**: chat em português.

---

## [RULE-002] Testes

- **Faça**: rode testes antes de commit.
- **Faça**: mantenha coverage ≥ 70%.
```

**Formato B — Descritivo (seções narrativas)**:

```markdown
## Idioma

Código em inglês, chat em português.

## Testes

Rode a suite antes de commit. Mantenha line coverage ≥ 70%.
```

Ambos funcionam. O Formato B é preferido para arquivos menores, mais narrativos.

---

## 8. Antepadrões Comuns

### ❌ "Wall of Text"

500 linhas de prompt antes de qualquer coisa. Agente se perde. **Solução**: progressive disclosure — pointers para docs externas.

### ❌ "Vague helper"

```markdown
Você é um assistente prestativo. Ajude o usuário.
```

Não funciona. Substitua por persona específica:

```markdown
You are a senior backend engineer specialized in Python. 
Write production-ready code with full error handling.
```

### ❌ "Auto-generate AGENTS.md"

```bash
/init  # ou "crie um AGENTS.md"
```

Prejudica performance em 3% (paper ETH). Escreva manualmente.

### ❌ "Kitchen sink"

Misturar instruções universais com instruções específicas de ferramenta. Use `AGENTS.md` para universais, `CLAUDE.md`/`GEMINI.md` para específicas.

### ❌ "Lista enorme sem priorização"

Sem três-tier boundaries, o agente não sabe qual regra é mais crítica.

---

## 9. Auditoria e Manutenção

### Quando auditar:

1. **Ao final de cada projeto novo** — escreva AGENTS.md deliberadamente
2. **Quando o agente ignora instruções consistemente** — pode ser sinal de regra vaga
3. **A cada 6 meses** — remova regras obsoletas
4. **Após updates de framework/dependências** — atualize comandos

### Como auditar:

Pergunte-se para cada linha:
1. O agente já descobre isso sozinho? → REMOVA
2. Esta regra é vague? → REESCREVA com verbo imperativo
3. Esta regra entra em conflito com outra? → RESOLVA
4. Esta regra cobre um caso raro? → MOV para doc externa ou remova
5. Esta regra é universal ou só para uma ferramenta? → MOVER para arquivo específico

### Verificação de qualidade:

```bash
# Tamanho
wc -l AGENTS.md          # ideal < 150 linhas
wc -c AGENTS.md          # ideal < 6000 chars (1/2 do limite Antigravity)

# Negações (should be minimized)
grep -c "Não\|never\|don't\|do not" AGENTS.md
```

---

## 10. Templates Prontos

### Template Mínimo (Universal)

```markdown
# Regras do Projeto

## Comandos

- **Faça**: use `npm test` antes de commit.
- **Faça**: type-check arquivos editados: `tsc --noEmit path/to/file.ts`

## Boundaries

✅ **Always do**: escreva testes para código novo.  
⚠️ **Ask first**: instalar dependências novas.  
🚫 **Never do**: commitar secrets, `.env` ou tokens.

## When Stuck

- Pergunte antes de assumir premissas.
- Proponha um plano curto antes de mudanças grandes.
```

### Template para Projeto Python

```markdown
# Regras do Projeto Python

## Comandos

- **Faça**: rode `pytest path/to/test_file.py::test_name` por arquivo (não suite completa).
- **Faça**: type-check com `mypy path/to/file.py`.
- **Faça**: formate com `ruff format` antes de commit.

## Boundaries

✅ **Always do**: escreva type hints em funções públicas.  
✅ **Always do**: adicione docstrings a funções complexas.  
🚫 **Never do**: commitar `.env`, `.venv/`, `__pycache__/`.

## When Stuck

- Pergunte antes de assumir requisitos.
- Proponha plano antes de refatorar > 3 arquivos.
```

### Template para Frontend (React/Next)

```markdown
# Regras do Projeto Frontend

## Comandos (file-scoped)

- **Faça**: `npm run lint --fix path/to/file.tsx`
- **Faça**: `npm run test path/to/file.test.tsx`
- **Faça**: `tsc --noEmit path/to/file.tsx`

## Project Structure

- Components: `src/components/`
- Hooks: `src/hooks/`
- API routes: `src/app/api/`
- Estado global: stores em `src/stores/`

## Boundaries

✅ **Always do**: use componentes de `@acme/ui`.  
⚠️ **Ask first**: adicione dependências > 100KB.  
🚫 **Never do**: `console.log` em PR.

## When Stuck

- Concorde com os design tokens antes de UI nova.
```

---

## 11. Checklist Final

Antes de finalizar seu AGENTS.md:

- [ ] **Tamanho**: < 150 linhas (~6KB)
- [ ] **Sem auto-geração**: escrito por humano deliberadamente
- [ ] **Sem codebase overview**: removido
- [ ] **Sem style guide** (linting deferido ao linter real)
- [ ] **Sem README duplicado**
- [ ] **Comandos primeiro**, com flags específicas
- [ ] **Three-tier boundaries** (always/ask/never)
- [ ] **Framing positivo** (zero "Não faça" ou minimizado)
- [ ] **Idioma híbrido**: termo técnico em EN, resto em idioma nativo
- [ ] **Exemplos concretos** quando precisar
- [ ] **When stuck**: escape hatch definido
- [ ] **PR checklist**: itens curtos
- [ ] **CodeGraph não tocado**: se existir, preservar

---

## 12. Referências

### Papers acadêmicos

- **Mondshine et al. (Bar-Ilan University, 2025)** — *"Beyond English: The Impact of Prompt Translation Strategies across Languages and Tasks in Multilingual LLMs"*. ArXiv:2502.09331. URL: https://arxiv.org/html/2502.09331v1
- **ETH Zurich (2025)** — *"Evaluating AGENTS.md"* (paper por trás dos dados de redução de performance)
- **García-Ferrero et al. (2023)** — *"This is not a Dataset: A Large Negation Benchmark to Challenge Large Language Models"*. EMNLP 2023. ArXiv:2310.15941.

### Documentação oficial

- **Antigravity / Gemini docs** — https://antigravity.google/docs/rules-workflows
- **Anthropic prompt engineering best practices** — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- **agents.md (oficial)** — https://agents.md/

### Análises práticas

- **Nigh, Matt (GitHub Blog, 2025)** — *"How to write a great agents.md: Lessons from over 2,500 repositories"*. URL: https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/
- **Schmid, Philipp (2026)** — *"Writing a Good AGENTS.md"* (Google Vertex AI). URL: https://www.philschmid.de/writing-good-agents
- **Huß, Roland (2026)** — *"What Goes in AGENTS.md (and What Doesn't)"*. URL: https://ro14nd.de/what-goes-in-agents-md/
- **Liang, Zhu / 16x Eval (2025)** — *"The Pink Elephant Problem: Why 'Don't Do That' Fails with LLMs"*. URL: https://eval.16x.engineer/blog/the-pink-elephant-negative-instructions-llms-effectiveness-analysis
- **Build Better (2026)** — *"AGENTS.md Complete Guide for Engineering Teams"*. URL: https://blog.buildbetter.ai/agents-md-complete-guide-for-engineering-teams-in-2026/

### Skills superpowers disponíveis

- `python-clean-code` — Clean Code catalog completo para Python
- `typescript-clean-code` — Clean Code catalog completo para TS/JS
- `clean-tests` — Quality de testes (fast, boundary, one assert)
- `clean-names`, `clean-functions`, `clean-comments`, `clean-general` — Clean Code skills específicos

> **Nota**: essas skills cobrem automaticamente o que estaria em style guides. Não duplique em AGENTS.md.

---

**Versão**: 1.0  
**Data**: Julho 2026  
**Fontes**: 9 fontes (3 papers, 3 docs oficiais, 4 análises práticas)
