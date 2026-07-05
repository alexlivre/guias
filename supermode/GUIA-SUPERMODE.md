# Super Mode — Visão Geral

## O que é o Super Mode

Super Mode é um **modo de operação persistente** que combina comandos e skills para garantir excelência em cada tarefa. Ele não é um único comando — é um **ecossistema** de peças que trabalham juntas.

## Peças do Super Mode

### Comandos (agents/commands/)

| Comando | Trigger | Função |
|---------|---------|--------|
| **Super Mode** | `/supermode` | Ativa o modo persistente com auto-verificação contínua |
| **Pesquisa** | `/pesquisa` | Pesquisa progressiva em 3 rodadas + plano de implementação |
| **Perguntas** | `/perguntas` | Análise somente leitura (diagnóstico sem modificar código) |

### Skills (agents/skills/)

| Skill | Função |
|-------|--------|
| **gerenciar-uv** | Gerencia ambientes Python isolados (.venv) com `uv` |

## Como Funciona

```
Super Mode Ativado (/supermode)
│
├── Tarefa recebida
│   ├── Descobrir skills relevantes (ex: gerenciar-uv)
│   ├── Descobrir MCPs disponíveis
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

## Regras do Super Mode

1. **Antes de qualquer ação:** Carregar skills relevantes + descobrir MCPs
2. **Em pontos de decisão:** Usar `sequential-thinking` para raciocínio estruturado
3. **Antes de modificar código:** Criar plano + obter autorização
4. **Durante implementação:** Usar subagents sempre que possível
5. **Após toda implementação:** Executar verification step
6. **Em todas as respostas:** Prefixo + auto-verificação

## Compatibilidade entre Comandos

- `/pesquisa` funciona **dentro** do Super Mode (mantém regras ativas)
- `/supermode` reconhece `/pesquisa` como sub-comando válido
- `/perguntas` pode ser usado isoladamente ou dentro do Super Mode

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

## Quando Usar Super Mode

| Cenário | Usar Super Mode? |
|---------|------------------|
| Criar projeto do zero | ✅ Sim |
| Implementar feature complexa | ✅ Sim |
| Debugar problema difícil | ✅ Sim |
| Fazer pergunta rápida | ❌ Não (use `/perguntas`) |
| Pesquisar algo específico | ⚠️ Opcional (use `/pesquisa`) |
|修改 uma linha de código | ❌ Não (não precisa de Super Mode) |

## Ativar / Desativar

| Ação | Comando |
|------|---------|
| Ativar | `/supermode` |
| Desativar | "desativar supermode", "sair do supermode", "modo normal" |
