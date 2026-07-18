---
name: ui-chaos-engine
description: Use ao idealizar conceitos de UI, explorar direções visuais com restrições anti-AI-Slop, sair de bloqueios criativos ou precisar de restrições aleatórias para projetos de design. Combina randomização criativa com guardrails explícitos para combater AI Slop — produz UIs distintas, funcionais e bonitas que NÃO parecem geradas por IA.
---

# UI Chaos Engine v2.0 — Anti-AI Slop Edition

Uma ferramenta de randomização criativa para design de UI que combina o **caos** da exploração aleatória com **guardrails explícitos** contra AI Slop. Gere briefings estruturados que a IA que vai executar o design pode seguir diretamente.

**Filosofia central:** *"UIs boas e bonitas nascem de decisões deliberadas, não de randomização cega. Randomização com constraints > Randomização pura."*

---

## 🎯 Quando Usar Esta Skill

Use esta skill quando:
- Pedir um conceito de UI, direção visual ou briefing de design
- Estiver em bloqueio criativo e precisar de direções inesperadas
- Quiser sair do padrão genérico AI (purple gradient + fontes overused + 3 cards)
- Quiser randomizar direções COM constraints que combatem AI Slop
- Quiser um briefing estruturado que possa usar como prompt em AI builders

**NÃO use** para: implementar UI diretamente (esta skill produz briefings, não código).

---

## 📋 As 7 Categorias (com Anti-Slop Embutido)

Cada categoria define uma dimensão da UI. Em execução, você gera 10 opções concretas por dimensão, especificamente adaptadas ao contexto do projeto, **filtradas contra os 46 padrões de AI Slop documentados em `references/anti-slop-patterns.md`**.

### 1. Metáfora / Conceito Central
**Pipeline obrigatório de 2 etapas.** Não pule a Etapa 1.

#### Etapa 1 — Extrair Brand Profile
Antes de gerar metáforas, analise o projeto e produza:
- **Domínio**: fintech, saúde, games, B2B SaaS, social, e-commerce, educação, produtividade, devtools, entretenimento
- **Público-alvo**: developers, executives, criativos, teens, designers, enterprise, consumidores
- **Arquétipo de marca**: 12 clássicos (Sábio, Herói, Criador, Bobo, Explorador, Governante, Cuidador, Fora-da-lei, Amante, Inocente, Mago, Pessoa Comum) + alternativos (Construtor, Alquimista, Cartógrafo, Tecedor, Navegador, Hacker, Curador)
- **Dimensões visuais** (escala 1-7): Sério↔Lúdico, Tradicional↔Experimental, Minimalista↔Ornamentado, Frio↔Quente, Abstrato↔Concreto, Luxuoso↔Frugal, Orgânico↔Geométrico
- **Anti-influências**: o que evitar ativamente

#### Etapa 2 — Derivar 10 Metáforas
Cada opção deve incluir: **Domínio fonte → Domínio alvo → Mapeamento → Alinhamento**.

### 2. Paleta de Cores
Direção cromática + regras do sistema de cores. Inclui temperatura, saturação, contraste, e como cores operam em fundos/superfícies/estados.

**PROIBIÇÕES DURAS** (ver `references/anti-slop-patterns.md`):
- ❌ Purple-to-blue gradient como accent default
- ❌ Cream/beige como "tasteful" default
- ❌ Dark mode + neon glow como combo clichê
- ❌ Cyan-on-dark como paleta AI

**PREFERÊNCIAS**: Paletas semânticas (cor sinaliza função), derivadas de fotografia/cultura/restrições de marca, com propósito claro.

### 3. Tipografia
Pares de fontes, tratamento tipográfico, hierarquia visual.

**PROIBIÇÕES DURAS** (Anti-AI Slop):
- ❌ Fontes overused como primária sem justificativa deliberada (verificar quais estão saturadas AGORA — o que era fresh há 6 meses pode já ser clichê)
- ❌ Single font para tudo (sem hierarquia)
- ❌ Flat type hierarchy (tamanhos muito próximos)
- ❌ All-caps body text
- ❌ Crushed letter spacing

**PREFERÊNCIAS**:
- Famílias tipográficas com personalidade reconhecível e curadoria editorial — evitar fontes que são escolhas estatísticas por defeito da indústria
- Princípio de **contraste extremo**: pesos 100/800, jumps de 3x+ no size
- Sempre **display + body contrastante** (não single-font systems)

### 4. Layout / Estrutura
Sistema de grid, hierarquia visual, densidade, whitespace, responsividade.

**PROIBIÇÕES DURAS**:
- ❌ 3 cards idênticos em row (clichê universal AI)
- ❌ Hero metric layout (10M+ users + 99.9% uptime + 200ms p50)
- ❌ Nested cards (card dentro de card)
- ❌ Side-tab accent border (tell #1 de AI UI)
- ❌ Identical card grids repetidos
- ❌ Monotonous spacing (mesmo valor sempre)
- ❌ Numbered section markers (01/02/03) sem ser sequência
- ❌ Line length >80 caracteres

**PREFERÊNCIAS**: Assimetria, ritmo variável, grids não-óbvios (bento, magazine, newspaper, brutalist manifesto, kinetic), whitespace como elemento de design.

### 5. Animação / Interatividade
Filosofia de animação, triggers, tom emocional, micro-interações, performance.

**PROIBIÇÕES DURAS**:
- ❌ Bounce/elastic easing em elementos de interface
- ❌ Image hover transform (scale/rotate)
- ❌ Layout property animation (width/height/padding)
- ❌ Animação sem propósito funcional

**PREFERÊNCIAS**: Motion com propósito (comunica estado, dirige atenção, reforça personalidade), physics-based quando apropriado, performance-first, degrada graciosamente.

### 6. 🆕 Voz de Copy (NOVA CATEGORIA)
Tom de escrita, voz de marca, padrões de microcopy.

**PROIBIÇÕES DURAS** (ver `references/anti-slop-patterns.md`):
- ❌ Marketing buzzwords: "supercharge", "empower", "world-class", "enterprise-grade", "cutting-edge", "next-generation", "streamline"
- ❌ Vague aspirational headlines: "Build the future", "Scale without limits"
- ❌ Aphoristic cadence: "Not a feature. A platform." / "We killed X"
- ❌ Em-dash overuse (>2 no body copy)
- ❌ Theater framing: "no more growth theater", "theater of X"
- ❌ Hedging language: "may help you", "can potentially"

**PREFERÊNCIAS**: Específico > genérico, verbos concretos, fala como humano real (não LinkedInfluencer), opinião declarada, referência interna ao produto real.

### 7. 🆕 Distinctive Reference (NOVA CATEGORIA)
Referências que combatem AI Slop. Ver `references/distinctive-references.md`.

**11 Estéticas documentadas**:
1. **Technical Mono** — monospace, terminal-like, code brutalism
2. **Surveillance Aesthetic** — CCTV dystopia, high-contrast B&W, glitch
3. **Tech-Organic Fusion** — flora/fauna + tech, wood grain, botanical UIs
4. **Interface Nostalgia** — Frutiger Aero, skeuomorphic iOS6, glossy bubbles
5. **Heisei Retro** — PC-98, '90s Japanese tech, dithered graphics
6. **Lo-fi Pixel** — 8/16-bit, dithered gradients, pixel typography
7. **Y3K Hyperfuturism** — alien sleek, iridescent neon, hovering panels
8. **Dreamy Softness** — pastel, diffuse, low-contrast, uncanny
9. **Collage / Intercalated** — text overlaps image, tape/staples, zine aesthetic
10. **KidCore / Scrapbook** — mixed media, doodles + magazine textures
11. **Immersive 3D** — WebGL, 3D everywhere, depth-layered

**7 Produtos de referência**:
- **Linear** — restraint + precision + custom type
- **Stripe** — premium clarity + bespoke serif
- **Duolingo** — playful character + loud identity
- **Notion** — warm minimalism + semantic color
- **Vercel** — developer-first + custom typeface
- **Superhuman** — speed-obsessed + sharp hierarchy
- **Basecamp** — opinionated + direct voice

---

## 🔄 Fluxo de Trabalho

### Passo 1: Extrair/Inferir Brand Profile
Leia arquivos do projeto, entenda tema/diretrizes/público. Se contexto insuficiente, **PEDIR** ao usuário antes de prosseguir. Não adivinhe domínios.

### Passo 2: Carregar Referências
Sempre consultar antes de gerar:
- `references/anti-slop-patterns.md` — 46 padrões a evitar
- `references/distinctive-references.md` — 11 estéticas + 7 produtos
- `references/good-ux-principles.md` — qualidade UX sólida

### Passo 3: Gerar 10 Opções por Categoria
Baseado no Brand Profile, gere 10 opções **filtradas** para cada categoria. **Mental validation**: cada opção deve passar pelos checks anti-slop DURANTE a geração, não depois.

### Passo 4: Sortear 1 por Categoria
Use o script Python (`scripts/chaos_engine.py`) para randomizar. Use seed para resultados reproduzíveis.

```bash
echo '<JSON>' | python scripts/chaos_engine.py --stdin --seed 42
```

### Passo 5: Validar Output (Obrigatório)
Antes de entregar, verificar:
- [ ] **Anti-Slop**: nenhuma opção viola os 46 padrões?
- [ ] **UX Sound**: contraste WCAG AA, hierarquia clara, acessibilidade?
- [ ] **Distinctive**: as escolhas têm opinião declarada? Diferem do default AI?
- [ ] **Consistent**: categorias reforçam-se ou contradizem-se?
- [ ] **Beautiful**: a combinação resultaria em algo reconhecível e memorável?

### Passo 6: Compor Output Estruturado
Gerar o JSON final com todas as escolhas + implementação.

### Passo 7: Apresentar ao Usuário
Mostrar como briefing claro, com explicação do porquê de cada escolha. Incluir prompt estruturado que o usuário pode usar em AI builders.

---

## 📤 Output Estruturado

A skill produz o seguinte output (em JSON internamente, apresentado em markdown formatado):

```json
{
  "brand_profile": {
    "domain": "...",
    "audience": "...",
    "archetype": "...",
    "tone": "...",
    "anti_influences": [...]
  },
  "picks": {
    "metaphor": "...",
    "palette": "...",
    "typography": "...",
    "layout": "...",
    "animation": "...",
    "copy_voice": "...",
    "distinctive_reference": "..."
  },
  "anti_slop_checks": {
    "no_overused_fonts": true,
    "no_purple_gradient_default": true,
    "no_three_card_cliche": true,
    "no_marketing_buzzwords": true,
    "no_glassmorphism_everywhere": true,
    "no_hero_metric_trio": true,
    "no_aphoristic_cadence": true
  },
  "distinctiveness_score": "high|medium|low",
  "implementation_guidance": {
    "do": ["concrete actions"],
    "dont": ["specific pitfalls"],
    "watch_for": ["edge cases"]
  },
  "prompt_for_ai_builder": "..."
}
```

---

## 🎨 Tom e Personalidade da Skill

Esta skill tem **personalidade forte**:
- **Opinativa** — declara preferências sem hedging desnecessário
- **Confiante** — tem taste, faz escolhas deliberadas
- **Direta** — vai direto ao ponto
- **Didática** — explica o porquê de cada escolha
- **Humor sutil** —偶尔 piadas sobre AI Slop quando apropriado

A skill **NÃO é neutra** — ela prefere distintividade sobre segurança, opinião sobre median, restrições sobre vagueza.

---

## ⚙️ Usando o Script Python

### Via stdin (recomendado — zero arquivos)

```bash
echo '<JSON>' | python scripts/chaos_engine.py --stdin
echo '<JSON>' | python scripts/chaos_engine.py --stdin --seed 42
echo '<JSON>' | python scripts/chaos_engine.py --stdin --json
```

### Via arquivo

```bash
python scripts/chaos_engine.py --options path/to/options.json
```

### Estrutura do JSON de input

```json
{
  "metafora": ["opt1", ..., "opt10"],
  "paleta": [...],
  "tipografia": [...],
  "layout": [...],
  "animacao": [...],
  "copy_voice": [...],
  "distinctive_reference": [...]
}
```

Nenhuma dependência externa — usa apenas biblioteca padrão do Python.

---

## 📚 Referências Internas

- **`references/anti-slop-patterns.md`** — Lista completa dos 46 padrões de AI Slop (de Impeccable.style) + top tells (de 925Studios)
- **`references/distinctive-references.md`** — 11 estéticas anti-AI + 7 produtos de referência com exemplos
- **`references/good-ux-principles.md`** — Princípios de UX sólida que a UI deve respeitar

---

## 💡 Princípios "UI Boa e Bonita"

A skill encoraja UIs que são:

1. **Claras** — propósito óbvio, hierarquia visível
2. **Consistentes** — sistema coerente, padrões respeitados
3. **Acessíveis** — WCAG AA+, navegação por teclado, screen readers
4. **Performantes** — rápidas, responsivas, leves
5. **Delightful** — micro-interações com propósito, surpresas agradáveis
6. **Distintas** — reconhecíveis, memoráveis, com opinião
7. **Honestas** — dizem o que fazem, não fingem ser o que não são

**A skill NUNCA sacrifica qualidade por estética.** Anti-slop não significa "diferente a qualquer custo" — significa "diferente com propósito e qualidade".