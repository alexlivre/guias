# 46 Padrões de AI Slop — Lista de Referência Anti-Padrões

> Fonte primária: [Impeccable.style/slop](https://impeccable.style/slop/) — Paul Bakaus
> Fonte secundária: [925Studios AI Slop Design Tells](https://www.925studios.co/blog/ai-slop-design-tells)

Esta é a lista de referência completa dos padrões que caracterizam UI gerada por IA. **Use durante a geração para validar que opções NÃO violam estes padrões.**

---

## 🔴 TOP 10 TELLS (Críticos — Evitar Sempre)

Estes são os mais reconhecíveis e devem ser **evitados a todo custo**:

1. **Fontes overused como primária** — qualquer fonte que tenha virado default estatístico de AI training data (tell constante na indústria; verificar quais estão saturadas AGORA, não fixar lista)
2. **Purple-to-blue gradient** — o tell mais alto de AI Slop em 2026
3. **Layout de 3 cards idênticos** — clichê universal AI
4. **Hero com "Build the future" headline** — vague aspirational copy
5. **Marketing buzzwords** — "supercharge", "empower", "world-class", "next-generation"
6. **Glassmorphism como decoração** — usar só quando resolve layering real
7. **Side-tab accent border** — tell #1 de AI-generated UI
8. **Cream/beige como "tasteful" default** — sem propósito
9. **Hero metric trio** — 10M+ users + 99.9% uptime + 200ms p50
10. **Numbered section markers (01/02/03)** sem ser sequência real

---

## 📋 Lista Completa dos 46 Padrões (por categoria)

### Visual Details (7 regras)

| # | Padrão | Severidade | Como Evitar |
|---|--------|------------|-------------|
| 1 | **Rounded card** — border colorido grosso que conflita com border-radius | Média | Border-radius consistente com border weight |
| 2 | **Frosted glass card** — glassmorphism como decoração | Alta | Usar só quando resolve layering real |
| 3 | **Side-tab accent border** — borda colorida grossa num lado | **CRÍTICA** | Subtle accents ou nada |
| 4 | **Hairline border + wide shadow** — combinação tell | Alta | Escolher um ou outro |
| 5 | **Repeating-gradient stripes** — faixas decorativas | Média | Texturas deliberadas ou superfícies planas |
| 6 | **Extreme border-radius** — cards 24px+ viram blob | Média | Manter entre 12-16px |
| 7 | **Amateurish hand-drawn SVG** — parece rabisco amador | Baixa | Não usar SVG amador ou remover ilustração |

### Typography (10 regras)

| # | Padrão | Severidade | Como Evitar |
|---|--------|------------|-------------|
| 8 | **Flat type hierarchy** — tamanhos muito próximos | Alta | Razão mínima 1.25 entre níveis |
| 9 | **Icon tile above heading** — container arredondado acima do título | Alta | Icon side-by-side ou inline |
| 10 | **Italic serif display headline** — virou clichê AI | Alta | Serif roman ou não-serif display |
| 11 | **Hero eyebrow / pill chip** — label uppercase acima do hero | Alta | Sem eyebrow, ou como breadcrumb |
| 12 | **Repeated section kicker** — labels tiny uppercase repetidos | Alta | Estrutura mais forte |
| 13 | **Oversized hero headline** — full-sentence em display size | Média | Headlines curtas em display, longas menores |
| 14 | **Crushed letter spacing** — apertado demais | Baixa | Tracking óptico, não destrutivo |
| 15 | **Overused font** — qualquer fonte que tenha virado default estatístico de AI training data | **CRÍTICA** | Famílias com curadoria editorial e personalidade reconhecível |
| 16 | **Single font for everything** — sem hierarquia | Alta | Sempre display + body contrastante |
| 17 | **All-caps body text** | Alta | Reservar uppercase para labels curtos |

### Color & Contrast (5 regras)

| # | Padrão | Severidade | Como Evitar |
|---|--------|------------|-------------|
| 18 | **AI color palette** — purple/violet gradient + cyan-on-dark | **CRÍTICA** | Paletas distintivas com propósito |
| 19 | **Dark mode with glowing accents** — neon glow | Alta | Lighting sutil ou skip dark mode |
| 20 | **Gradient text** — texto com gradiente | Média | Cores sólidas para texto |
| 21 | **Gray text on colored background** | Média | Sombra mais escura do bg, ou white/near-white |
| 22 | **Cream/beige palette** — "tasteful" default | Média | Background de paleta deliberada |

### Layout & Space (8 regras)

| # | Padrão | Severidade | Como Evitar |
|---|--------|------------|-------------|
| 23 | **Hero metric layout** — 10M+/99.9%/200ms trio | **CRÍTICA** | Métricas específicas do produto, não genéricas |
| 24 | **Identical card grids** — same-size + icon + heading + text | **CRÍTICA** | Variação intencional, bento, assimetria |
| 25 | **Monotonous spacing** — mesmo valor sempre | Alta | Tight groupings + generous separations |
| 26 | **Nested cards** — card dentro de card | Alta | Spacing, typography, dividers |
| 27 | **Numbered section markers** — 01/02/03 sem ser sequência | Alta | Só quando é sequência real |
| 28 | **Line length too long** — >80 chars | Alta | Max-width 65ch-75ch |
| 29 | **Content overflowing** — quebra layout | Alta | Wrap, constrain widths |
| 30 | **Positioned child clipped** — tooltip cortado | Alta | overflow: visible, ou mover layer |

### Motion (3 regras)

| # | Padrão | Severidade | Como Evitar |
|---|--------|------------|-------------|
| 31 | **Bounce/elastic easing** — datado e piegas | Alta | ease-out-quart/quint/expo |
| 32 | **Layout property animation** — width/height/padding jank | Alta | transform/opacity, ou grid-template-rows |
| 33 | **Image hover transform** — scale/rotate on hover | Alta | Imagens estáticas, ou interação sutil |

### Copy (4 regras)

| # | Padrão | Severidade | Como Evitar |
|---|--------|------------|-------------|
| 34 | **Em-dash overuse** — >2 no body copy | Alta | Vírgulas, dois pontos, parênteses |
| 35 | **Marketing buzzword** — generic SaaS phrases | **CRÍTICA** | Verbos e substantivos específicos |
| 36 | **Aphoristic-cadence copy** — "Not a feature. A platform." | Alta | Voz natural, não manufactured contrasts |
| 37 | **Theater framing copy** — dismissing things as "theater" | Média | Dizer diretamente o que faz/não faz |

### Imagery (1 regra)

| # | Padrão | Severidade | Como Evitar |
|---|--------|------------|-------------|
| 38 | **Broken/placeholder image** — img tags vazias | Alta | Real images, generated assets, ou remover |

### General Quality (8 regras)

| # | Padrão | Severidade | Como Evitar |
|---|--------|------------|-------------|
| 39 | **Cramped padding** — <8px | Média | Mínimo 8px, ideal 12-16px |
| 40 | **Body text touching viewport** — flush against edge | Média | Container com padding 16px+ |
| 41 | **Justified text** — creates rivers | Média | text-align: left, ou hyphens: auto |
| 42 | **Low contrast text** — falha WCAG AA | Alta | 4.5:1 body, 3:1 large text |
| 43 | **Skipped heading level** — h1→h3 sem h2 | Alta | Hierarquia correta para screen readers |
| 44 | **Tight line height** — <1.3 | Alta | 1.5-1.7 para body |
| 45 | **Tiny body text** — <12px | Alta | Mínimo 14px, ideal 16px |
| 46 | **Wide letter spacing** — >0.05em em body | Alta | Reservar para uppercase labels |

---

## 🎯 Princípio Tipográfico Anti-Slop

**Não trate este como uma whitelist/blacklist fixa** — o que é "overused" muda constantemente. Em vez disso, aplique estes princípios durante a curadoria tipográfica:

### ❌ Evite Fontes com Estas Características
- **Tell #1 de AI**: qualquer fonte que tenha virado default estatístico em AI training data — escolha por default do Tailwind/Tailwind UI, escolhas de vibe coding tools, fontes mais frequentes em "vibe coded" landing pages
- **System defaults**: qualquer fonte que é escolha por omissão (não-deliberada) — system fonts, default de bibliotecas UI, fontes mais frequentes em vibe-coding tools sem curadoria
- **Fontes viradas-clichê**: aquela que era "fresh" há 6 meses mas já saturou (avaliar com base em uso recente em AI-generated UI)

### ✅ Prefira Fontes com Estas Características
- **Personalidade reconhecível**: formas distintivas, wanky outlines, decisões de design opinativas
- **Curadoria editorial**: tipo Foundry reputable, design award, propósito claro
- **Variable fonts**: para movimento e hierarquia tipográfica dinâmica
- **Famílias com peso e proporção distintos**: contraste extremo (100 vs 800) para hierarquia marcante
- **Fonts fora do mainstream recente**: ajustar constantemente com base no que está saturado agora

---

## 🎨 Paletas a EVITAR

### ❌ AI Color Defaults
- Purple/violet gradient (#8B5CF6 → #3B82F6)
- Cyan-on-dark (#06B6D4 em #000)
- Cream/beige como bg principal (#F5F1E8, #FAF7F2)
- Neon glows em dark mode

### ✅ Considere Em Vez
- Paletas derivadas de fotografia do produto
- Paletas com significado semântico (cor = função)
- Espectros alternativos: terra, verde-escuro, bordô, slate, mostarda, ametista
- Cores com propósito emocional claro

---

## ✍️ Copy a EVITAR

### ❌ Buzzwords Genéricos
- "supercharge", "empower", "world-class", "enterprise-grade"
- "cutting-edge", "next-generation", "streamline"
- "Build the future", "Scale without limits"
- "Your all-in-one platform"

### ❌ Cadences AI
- Em-dashes excessivos (—)
- Aphorisms manufactured ("Not a feature. A platform.")
- Theater framing ("No more X theater")
- Hedging ("may help you", "can potentially")

### ✅ Escrita Distintiva
- Específico > genérico
- Verbos concretos ("ship faster" → "deploy in 30s")
- Voz como humano real, não LinkedInfluencer
- Opinião declarada
- Referência interna ao produto real

---

## 🧠 Como Usar Esta Lista

**Durante a geração** de opções para cada categoria:
1. Mental validation: "Esta opção viola algum dos 46 padrões?"
2. Se sim, re-gerar com alternativa que respeite os princípios
3. Preferência explícita: quando há 10 opções, peso para as que demonstram mais distintividade

**Durante a validação final**:
1. Checklist obrigatório dos 10 tells críticos
2. Checklist dos 46 se o contexto permitir (mais rigoroso para projetos importantes)

**Filosofia**: Evitar estes padrões é **necessário mas não suficiente** — também é preciso ter OPINIÃO nas escolhas. Anti-slop é o piso, distintividade é o teto.