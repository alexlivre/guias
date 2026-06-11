# Guia Definitivo: hexgrad/kokoro-82m via OpenRouter

## Sobre o Modelo

**Kokoro 82M** é um modelo TTS (text-to-speech) leve e open-weight da hexgrad. Com apenas 82 milhões de parâmetros, ele suporta **8 idiomas** incluindo **português brasileiro**, usando 54 vozes pré-definidas organizadas por idioma e gênero.

| Característica | Valor |
|---|---|
| Preço | **$0.62 / milhão de caracteres** |
| Idioma | 🇧🇷 Português, 🇺🇸 Inglês, 🇪🇸 Espanhol, 🇫🇷 Francês, 🇮🇹 Italiano, 🇯🇵 Japonês, 🇭🇰 Chinês, 🇮🇳 Hindi |
| Vozes PT-BR | `pf_dora` (feminino), `pm_alex` (masculino), `pm_santa` (masculino) |
| Formato de saída | MP3 ou PCM |
| Contexto | 4K caracteres por requisição |
| Provedor | OpenRouter (roteamento automático) |

## endpoint

```
POST https://openrouter.ai/api/v1/audio/speech
```

## Código Funcional

```python
import requests

API_KEY = "sk-or-v1-sua-chave-aqui"

response = requests.post(
    "https://openrouter.ai/api/v1/audio/speech",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    },
    json={
        "model": "hexgrad/kokoro-82m",
        "input": "Olá! Este é um teste de síntese de voz em português.",
        "voice": "pf_dora",
        "response_format": "mp3",
    },
)

with open("output.mp3", "wb") as f:
    f.write(response.content)
```

## Vozes Disponíveis

### Português (pf = portuguese female, pm = portuguese male)

| Voz | Gênero |
|-----|--------|
| `pf_dora` | Feminino |
| `pm_alex` | Masculino |
| `pm_santa` | Masculino |

### Outros idiomas (prefixos)

| Prefixo | Idioma |
|---------|--------|
| `af_*`, `am_*` | Inglês americano |
| `bf_*`, `bm_*` | Inglês britânico |
| `ef_*`, `em_*` | Espanhol |
| `ff_*` | Francês |
| `hf_*`, `hm_*` | Hindi |
| `if_*`, `im_*` | Italiano |
| `jf_*`, `jm_*` | Japonês |
| `pf_*`, `pm_*` | Português |
| `zf_*`, `zm_*` | Chinês |

## Custo

### Precificação

- **$0.62 por milhão de caracteres** de entrada
- Apenas o texto de entrada é cobrado (sem custo de saída)
- Não há custo por segundo de áudio gerado

### Exemplos reais (testados)

| Duração | Caracteres | Custo real |
|---------|-----------|-----------|
| ~30 seg | ~500 | **$0.0003** |
| ~1 min | ~1.000 | **$0.0006** |
| ~5 min | ~5.000 | **$0.0031** |
| **~10 min** | **~9.900** | **$0.0061** |
| ~1 hora | ~60.000 | **~$0.037** |
| ~10 horas | ~600.000 | **~$0.37** |

### Comparação com outros modelos

| Modelo | Preço/M chars | 1 hora |
|--------|-------------|--------|
| **kokoro-82m** | **$0.62** | **~$0.04** |
| zonos-v0.1-hybrid | $7.00 | ~$0.42 |
| gemini-3.1-flash-tts | $1 + $20 (out) | ~$1.75 |
| grok-voice-tts-1.0 | $15.00 | ~$0.90 |
| mai-voice-2 | $22.00 | ~$1.32 |

## Gerando Áudios Longos

O Kokoro tem limite de ~4K caracteres por requisição, gerando ~20-25s de áudio cada. Para áudios longos, divida o texto em segmentos e concatene:

```python
import requests, subprocess

API_KEY = "sk-or-v1-sua-chave-aqui"

textos = [
    "Primeiro parágrafo do seu texto aqui...",
    "Segundo parágrafo do seu texto...",
    # adicione quantos segmentos precisar
]

# Gera cada segmento
for i, texto in enumerate(textos, start=1):
    r = requests.post(
        "https://openrouter.ai/api/v1/audio/speech",
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        json={"model": "hexgrad/kokoro-82m", "input": texto, "voice": "pf_dora", "response_format": "mp3"},
        timeout=90,
    )
    if r.ok:
        with open(f"seg_{i}.mp3", "wb") as f:
            f.write(r.content)

# Concatena com ffmpeg
segs = [f"seg_{i}.mp3" for i in range(1, len(textos) + 1)]
subprocess.run([
    "ffmpeg", "-y", "-i", "concat:" + "|".join(segs),
    "-acodec", "copy", "audio_final.mp3"
])
```

### Estimativa de segmentos

- **1 minuto:** ~1.000 chars (~4-5 segmentos de 200-250 chars)
- **10 minutos:** ~9.900 chars (~50-60 segmentos)
- Cada segmento de ~200 chars gera ~10-12s de áudio

## Parâmetros da API

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `model` | string | Sim | `hexgrad/kokoro-82m` |
| `input` | string | Sim | Texto a ser sintetizado |
| `voice` | string | Sim | Identificador da voz |
| `response_format` | string | Não | `mp3` (padrão) ou `pcm` |
| `max_tokens` | int | Não | Limite máximo de tokens gerados |

## Boas Práticas

- **MP3** para armazenamento e playback geral
- **PCM** para streaming em tempo real (baixa latência)
- Divida textos longos em segmentos de ~200-300 caracteres
- Use `timeout=(15, 90)` no requests para evitar travamentos
- Monitore os custos no dashboard do OpenRouter

## Referências

- [Kokoro no OpenRouter](https://openrouter.ai/hexgrad/kokoro-82m)
- [API Quickstart](https://openrouter.ai/hexgrad/kokoro-82m/api)
- [Documentação TTS OpenRouter](https://openrouter.ai/docs/guides/overview/multimodal/tts)