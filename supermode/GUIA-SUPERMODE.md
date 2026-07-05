# Super Mode — Visão Geral

## O que é o Super Mode

Super Mode é um **modo de operação persistente** que combina comandos e skills para garantir excelência em cada tarefa. Ele não é um único comando — é um **ecossistema** de peças que trabalham juntas.

---

## Peças do Super Mode

### Comandos

| Comando | Trigger | Função |
|---------|---------|--------|
| **Super Mode** | `/supermode` | Ativa o modo persistente com auto-verificação contínua |
| **Pesquisa** | `/pesquisa` | Pesquisa progressiva em 3 rodadas + plano de implementação |
| **Perguntas** | `/perguntas` | Análise somente leitura (diagnóstico sem modificar código) |

### Skills

| Skill | Função | Onde é usada |
|-------|--------|--------------|
| **gerenciar-uv** | Gerencia ambientes Python isolados (.venv) com `uv` | [`supermode.md:40`](agents/commands/supermode.md#L40), [`pesquisa.md:13`](agents/commands/pesquisa.md#L13), [`pesquisa.md:54`](agents/commands/pesquisa.md#L54) |

### MCPs

| MCP | Função | Onde é usado |
|-----|--------|--------------|
| **MiniMax_web_search** | Busca web geral (títulos + snippets + links) | [`supermode.md:48`](agents/commands/supermode.md#L48), [`pesquisa.md:18`](agents/commands/pesquisa.md#L18), [`pesquisa.md:25`](agents/commands/pesquisa.md#L25) |
| **webfetch / fetch_fetch** | Download de conteúdo de páginas web | [`supermode.md:49`](agents/commands/supermode.md#L49), [`pesquisa.md:19`](agents/commands/pesquisa.md#L19), [`pesquisa.md:25`](agents/commands/pesquisa.md#L25) |
| **github_search_repositories** | Busca repositórios no GitHub | [`supermode.md:50`](agents/commands/supermode.md#L50), [`pesquisa.md:20`](agents/commands/pesquisa.md#L20) |
| **github_search_code** | Busca código no GitHub | [`supermode.md:51`](agents/commands/supermode.md#L51), [`pesquisa.md:20`](agents/commands/pesquisa.md#L20) |
| **github_search_issues** | Busca issues no GitHub | [`supermode.md:52`](agents/commands/supermode.md#L52), [`pesquisa.md:20`](agents/commands/pesquisa.md#L20) |
| **sequential-thinking** | Raciocínio estruturado em etapas | [`supermode.md:53`](agents/commands/supermode.md#L53), [`supermode.md:66-67`](agents/commands/supermode.md#L66), [`pesquisa.md:21`](agents/commands/pesquisa.md#L21), [`pesquisa.md:31`](agents/commands/pesquisa.md#L31), [`pesquisa.md:46`](agents/commands/pesquisa.md#L46), [`pesquisa.md:59`](agents/commands/pesquisa.md#L59) |
| **MCP de análise de imagens** | Análise de imagens (quando disponível) | [`supermode.md:54`](agents/commands/supermode.md#L54), [`supermode.md:58-63`](agents/commands/supermode.md#L58) |

---

## Como Funciona

```
Super Mode Ativado (/supermode)
│
├── Tarefa recebida
│   ├── Descobrir skills relevantes (ex: gerenciar-uv)
│   ├── Descobrir MCPs disponíveis (MiniMax, GitHub, sequential-thinking)
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
