# Super Mode — Visão Geral

## O que é o Super Mode

Super Mode é um **modo de operação persistente** que combina comandos e skills para garantir excelência em cada tarefa. Ele não é um único comando — é um **ecossistema** de peças que trabalham juntas.

---

## Peças do Super Mode

### Comandos (agents/commands/)

| Comando | Trigger | Função |
|---------|---------|--------|
| **Super Mode** | `/supermode` | Ativa o modo persistente com auto-verificação contínua |
| **Pesquisa** | `/pesquisa` | Pesquisa progressiva em 3 rodadas + plano de implementação |
| **Perguntas** | `/perguntas` | Análise somente leitura (diagnóstico sem modificar código) |
| **Commands Maker** | `/criar-comando` | Cria novos comandos `.md` prontos para uso |

### Skills do Projeto (agents/skills/)

| Skill | Descrição | Quando Usar |
|-------|-----------|-------------|
| **gerenciar-uv** | Gerencia ambientes Python isolados (.venv) com `uv` | Criar projeto Python, instalar pacotes, configurar ambiente |

### Skills Instaladas no Sistema

Skills disponíveis via `npx skills` ou instaladas localmente em `~/.agents/skills/`:

| Skill | Categoria | Origem |
|-------|-----------|--------|
| **skill-creator** | Criação de skills | Superpowers |
| **brainstorming** | Design e planejamento | Superpowers |
| **test-driven-development** | Testes | Superpowers |
| **systematic-debugging** | Debug | Superpowers |
| **writing-plans** | Planejamento | Superpowers |
| **executing-plans** | Execução | Superpowers |
| **python-clean-code** | Qualidade Python | Comunidade |
| **typescript-clean-code** | Qualidade TypeScript | Comunidade |
| **frontend-design** | Design UI | Comunidade |
| **pdf** | Manipulação PDF | Comunidade |
| **docx** | Documentos Word | Comunidade |
| **pptx** | Apresentações | Comunidade |
| **xlsx** | Planilhas | Comunidade |
| **image-create** | Geração de imagens | Comunidade |
| **mcp-builder** | Criação de MCPs | Comunidade |
| **find-skills** | Descoberta de skills | Superpowers |

---

## MCPs (Model Context Protocol)

### MCPs Padrão do Sistema

MCPs que vêm configurados no OpenCode:

| MCP | Função |
|-----|--------|
| **github** | Integração completa com GitHub (repos, issues, PRs, commits) |
| **MiniMax_web_search** | Busca web geral (títulos + snippets + links) |
| **MiniMax_understand_image** | Análise de imagens via MiniMax |
| **sequential-thinking** | Raciocínio estruturado em etapas |
| **webfetch / fetch_fetch** | Download de conteúdo de páginas web |
| **omni-image-tools** | Ferramentas de imagem (visão + processamento) |

### MCPs Criados por Alex (GitHub Pessoal)

| MCP | Repositório | Status | Descrição |
|-----|-------------|--------|-----------|
| **minimax-image-mcp** | [alexlivre/minimax-image-mcp](https://github.com/alexlivre/minimax-image-mcp) | ✅ Público | Servidor MCP para geração de imagens MiniMax (image-01) |
| **omni-image-tools-mcp** | [alexlivre/omni-image-tools-mcp](https://github.com/alexlivre/omni-image-tools-mcp) | 🔒 Privado | MCP de ferramentas de imagem (visão + processamento) com múltiplos provedores |
| **pixabay-mcp** | [alexlivre/pixabay-mcp](https://github.com/alexlivre/pixabay-mcp) | 🔒 Privado | MCP para busca de imagens no Pixabay |
| **imageHub-MCP** | [alexlivre/imageHub-MCP](https://github.com/alexlivre/imageHub-MCP) | 🔒 Privado | MCP hub de imagens |
| **terminalvision-casca** | [alexlivre/terminalvision-casca](https://github.com/alexlivre/terminalvision-casca) | ✅ Público | Daemon de terminal para MCP (sessões PTY/Terminal) |

### Outros Projetos Relacionados (GitHub Pessoal)

| Projeto | Repositório | Descrição |
|---------|-------------|-----------|
| **guias** | [alexlivre/guias](https://github.com/alexlivre/guias) | Este repositório — guias e comandos |
| **guia-minimax** | [alexlivre/guia-minimax](https://github.com/alexlivre/guia-minimax) | Guias e testes para API MiniMax |
| **autonovel-minimax** | [alexlivre/autonovel-minimax](https://github.com/alexlivre/autonovel-minimax) | Pipeline de escrita autônoma com MiniMax |
| **odysseus-minimax** | [alexlivre/odysseus-minimax](https://github.com/alexlivre/odysseus-minimax) | Odysseus com suporte nativo MiniMax |
| **versatile-open-chat** | [alexlivre/versatile-open-chat](https://github.com/alexlivre/versatile-open-chat) | Chatbot multiplataforma com MiniMax |
| **chatMax** | [alexlivre/chatMax](https://github.com/alexlivre/chatMax) | Wrapper API OpenAI-compatible para MiniMax |

---

## Como Funciona

```
Super Mode Ativado (/supermode)
│
├── Tarefa recebida
│   ├── Descobrir skills relevantes (ex: gerenciar-uv)
│   ├── Descobrir MCPs disponíveis (GitHub, MiniMax, omni-image, etc.)
│   └── Classificar tipo de tarefa
│
├── Fluxo baseado no tipo
│   ├── Pesquisa → /pesquisa (3 rodadas)
│   ├── Implementação → Plano → Autorização → Subagents
│   ├── Correção → Debug → Solução
│   └── Análise → /perguntas (somente leitura)
│
└── Auto-verificação contínua
    ├── Checklist mental após cada etapa
    ├── Prefixo [🔵 Super Mode Ativo] em todas as respostas
    └── Pergunta: "Nova tarefa ou desativar Super Mode?"
```

---

## Regras do Super Mode

1. **Antes de qualquer ação:** Carregar skills relevantes + descobrir MCPs
2. **Em pontos de decisão:** Usar `sequential-thinking` para raciocínio estruturado
3. **Antes de modificar código:** Criar plano + obter autorização
4. **Durante implementação:** Usar subagents sempre que possível
5. **Após toda implementação:** Executar verification step
6. **Em todas as respostas:** Prefixo + auto-verificação

---

## Compatibilidade entre Comandos

- `/pesquisa` funciona **dentro** do Super Mode (mantém regras ativas)
- `/supermode` reconhece `/pesquisa` como sub-comando válido
- `/perguntas` pode ser usado isoladamente ou dentro do Super Mode

---

## Exemplo de Uso

```
Usuário: /supermode

Agente: [🔵 Super Mode Ativo — OpenCode CLI]
        [Auto-verificação: Super Mode ativado. Skills e MCPs prontos.]
        Qual é a tarefa que você deseja designar?

Usuário: Crie um projeto Python com FastAPI

Agente: [Auto-verificação: Skill gerenciar-uv relevante. Carregando...]
        [Auto-verificação: MCPs verificados — MiniMax_web_search, fetch_fetch disponíveis.]
        [Auto-verificação: Tipo de tarefa = Implementação. Fluxo definido.]
        
        Plano de implementação:
        1. Usar gerenciar-uv para criar ambiente Python
        2. Instalar FastAPI com uv
        3. Criar estrutura do projeto
        4. Implementar endpoints
        5. Verification step: rodar testes
        
        Autorize a implementação.
```

---

## Quando Usar Super Mode

| Cenário | Usar Super Mode? |
|---------|------------------|
| Criar projeto do zero | ✅ Sim |
| Implementar feature complexa | ✅ Sim |
| Debugar problema difícil | ✅ Sim |
| Fazer pergunta rápida | ❌ Não (use `/perguntas`) |
| Pesquisar algo específico | ⚠️ Opcional (use `/pesquisa`) |
| Modificar uma linha de código | ❌ Não (não precisa de Super Mode) |

---

## Ativar / Desativar

| Ação | Comando |
|------|---------|
| Ativar | `/supermode` |
| Desativar | "desativar supermode", "sair do supermode", "modo normal" |
