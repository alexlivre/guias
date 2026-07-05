# AGENTS.md — Guias IA

## O que é este repositório

Coleção de guias práticos para APIs de IA, com código-fonte e testes reais. **Não é um projeto de software tradicional** — é documentação viva gerada por testes.

## Estrutura

- `guias-openrouter/` — Guias de APIs OpenRouter (Kokoro TTS)
- `guia-minimax/` — Projeto Python com 38 testes contra API real MiniMax
- `commands/` — Comandos personalizados OpenCode CLI (em português)

## Gotcha crítico: testes custam dinheiro

Todos os testes em `guia-minimax/tests/` chamam **APIs reais** e consomem quota. Nunca rode testes sem necessidade. Para rodar:

```bash
cd guia-minimax
pip install -r requirements.txt
cp .env.example .env  # adicione MINIMAX_API_KEY
pytest tests/ -v
```

Pular benchmarks lentos: `pytest tests/ --ignore=tests/test_performance.py -v`

## Convenções

- **Idioma:** Todo o conteúdo (guias, comandos, README) é em português brasileiro
- **Comandos OpenCode:** Estão em `commands/`, usam frontmatter YAML com `description`, trigger no formato `/nome-do-comando`
- **Guia gerado:** O resultado dos testes vai para `guia-minimax/guia/guia-minimax-api.md` — atualizar quando testes verificarem nova funcionalidade
- **Não versionar:** `.env`, `.venv/`, `__pycache__/`, `img/`, `test_output/`

## Comandos OpenCode disponíveis

| Trigger | Arquivo | Função |
|---------|---------|--------|
| `/criar-comando` | `commands_maker.md` | Cria novos comandos `.md` |
| `/perguntas` | `perguntas.md` | Análise somente leitura |
| `/pesquisa` | `pesquisa.md` | Pesquisa progressiva + plano |
| `/supermode` | `supermode.md` | Modo persistente com auto-verificação |

`/pesquisa` funciona dentro do `/supermode`.

## Links úteis

- API MiniMax: https://platform.minimax.io/docs/llms.txt
- Kokoro TTS: https://openrouter.ai/hexgrad/kokoro-82m
