# Guias Definitivos para Construção de Aplicações com IA

Repositório com guias práticos, código-fonte e testes automatizados contra APIs reais de IA.

## Estrutura

```
guias/
├── guias-openrouter/                # Guias OpenRouter
│   └── guia-kokoro-openrouter.md    # Guia TTS Kokoro 82M
│
├── guia-minimax/                    # Projeto Python completo
│   ├── src/                         # Código-fonte (7 módulos)
│   ├── tests/                       # 38 testes automatizados
│   ├── guia/                        # Guia gerado (1359 linhas)
│   └── ...
│
└── commands/                        # Comandos personalizados OpenCode CLI
    ├── commands_maker.md            # Meta-comando: cria outros comandos
    ├── perguntas.md                 # Análise somente leitura
    ├── pesquisa.md                  # Pesquisa progressiva + plano
    └── supermode.md                 # Modo persistente de excelência
```

---

## Guias Disponíveis

### Kokoro TTS via OpenRouter

Guia completo do modelo TTS (text-to-speech) Kokoro 82M.

| Característica | Valor |
|---|---|
| Modelo | `hexgrad/kokoro-82m` |
| Preço | $0.62 / milhão de caracteres |
| Idiomas | 8 (incluindo Português Brasileiro) |
| Vozes | 54 pré-definidas |
| Formato | MP3 ou PCM |
| Contexto | 4K caracteres por requisição |

**Arquivo:** [`guias-openrouter/guia-kokoro-openrouter.md`](guias-openrouter/guia-kokoro-openrouter.md)

---

### MiniMax API Completa (Projeto Python)

Projeto com **38 testes automatizados** contra a API real da MiniMax, gerando um guia completo baseado em resultados comprovados.

| Módulo | Testes | Status |
|---|---|---|
| Texto (Anthropic SDK) | 5 | ✅ |
| Texto (OpenAI SDK) | 8 | ✅ |
| Streaming | 3 | ✅ |
| Tool Use | 4 | ✅ |
| Caching | 2 | ✅ |
| Multimodal | 1 | ✅ |
| Performance (TPS) | 4 | ✅ |
| Imagem — T2I | 7 | ✅ |
| Imagem — I2I | 4 | ✅ |

**Modelos testados:** `MiniMax-M3`, `MiniMax-M2.7`, `MiniMax-M2.7-highspeed`

**Guia gerado:** [`guia-minimax/guia/guia-minimax-api.md`](guia-minimax/guia/guia-minimax-api.md) (1359 linhas)

#### Setup do Projeto Python

```bash
cd guia-minimax
pip install -r requirements.txt
cp .env.example .env
# Edite .env com sua MINIMAX_API_KEY
```

#### Executar Testes

```bash
# Todos os testes (38)
pytest tests/ -v

# Apenas imagem (T2I + I2I)
pytest tests/test_image.py -v

# Apenas texto
pytest tests/test_anthropic.py tests/test_openai.py -v

# Pular benchmarks lentos
pytest tests/ --ignore=tests/test_performance.py -v
```

> ⚠️ **Atenção:** Todos os testes chamam a API real e consomem quota.

---

## Comandos OpenCode CLI

Comandos personalizados para uso com [OpenCode CLI](https://opencode.ai).

| Comando | Trigger | Descrição |
|---------|---------|-----------|
| **Commands Maker** | `/criar-comando` | Cria novos comandos `.md` prontos para uso |
| **Perguntas** | `/perguntas` | Análise somente leitura (diagnóstico sem modificar código) |
| **Pesquisa** | `/pesquisa` | Pesquisa progressiva em 3 rodadas + plano de implementação |
| **Super Mode** | `/supermode` | Modo persistente com auto-verificação contínua |

### Compatibilidade entre comandos

- `/pesquisa` funciona dentro do `/supermode` (mantém regras do Super Mode ativas)
- `/supermode` reconhece `/pesquisa` como sub-comando válido

---

## Requisitos

- Python 3.10+
- [MiniMax API Key](https://platform.minimax.io)
- [OpenRouter API Key](https://openrouter.ai) (para Kokoro TTS)

## Links Úteis

- [Documentação MiniMax](https://platform.minimax.io/docs/llms.txt)
- [Console MiniMax](https://platform.minimax.io)
- [Kokoro no OpenRouter](https://openrouter.ai/hexgrad/kokoro-82m)
- [OpenCode CLI](https://opencode.ai)

---

*Guias criados através de testes práticos e documentação de descobertas reais.*
