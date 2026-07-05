# MiniMax API — Guia Completo + Testes

Projeto com testes automatizados contra a API real da MiniMax (Texto LLM + Imagem `image-01`), gerando um guia prático baseado em resultados comprovados.

## Estrutura

```
├── src/
│   ├── config.py              # Config (API key, URLs)
│   ├── anthropic_client.py    # Chamadas via Anthropic SDK
│   ├── openai_client.py       # Chamadas via OpenAI SDK
│   ├── streaming.py           # Streaming (ambos SDKs)
│   ├── tool_use.py            # Function calling
│   ├── caching.py             # Prompt caching
│   ├── multimodal.py          # Imagem/video via texto
│   └── image_client.py        # Geracao de imagens image-01
├── tests/
│   ├── test_anthropic.py      # 5 testes
│   ├── test_openai.py         # 8 testes
│   ├── test_streaming.py      # 3 testes
│   ├── test_tool_use.py       # 4 testes
│   ├── test_caching.py        # 2 testes
│   ├── test_multimodal.py     # 1 teste
│   ├── test_performance.py    # 4 testes (TPS)
│   └── test_image.py          # 7 testes
├── guia/
│   └── guia-minimax-api.md    # Guia completo
├── .env.example               # Template para config
└── requirements.txt
```

## Requisitos

- Python 3.10+
- MiniMax API Key ([platform.minimax.io](https://platform.minimax.io))

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Edite .env com sua MINIMAX_API_KEY
```

## Executar testes

```bash
# Todos os testes
pytest tests/ -v

# Apenas texto
pytest tests/test_anthropic.py tests/test_openai.py tests/test_streaming.py tests/test_tool_use.py tests/test_caching.py tests/test_multimodal.py tests/test_performance.py -v

# Apenas imagem
pytest tests/test_image.py -v
```

## Resultados

**34/34 testes passando** na API real:

| Modulo | Testes | Status |
|---|---|---|
| Texto (Anthropic) | 5 | ✅ |
| Texto (OpenAI) | 8 | ✅ |
| Streaming | 3 | ✅ |
| Tool Use | 4 | ✅ |
| Caching | 2 | ✅ |
| Multimodal | 1 | ✅ |
| Performance (TPS) | 4 | ✅ |
| Imagem (image-01) | 7 | ✅ |

## Guia

O guia completo esta em `guia/guia-minimax-api.md`, dividido em:

- **Parte I:** Texto (LLMs) — Anthropic API, OpenAI API, streaming, tool use, caching, multimodal, `<think>`, performance
- **Parte II:** Imagem (`image-01`) — T2I, I2I, parametros, erros, otimizacao
- **Parte III:** Audio *(em breve)*

## Links

- [Documentacao MiniMax](https://platform.minimax.io/docs/llms.txt)
- [Console MiniMax](https://platform.minimax.io)
