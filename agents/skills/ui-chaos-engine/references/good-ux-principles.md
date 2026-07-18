# Princípios de UX Sólida — "UI Boa e Bonita"

> A skill UI Chaos Engine NUNCA sacrifica qualidade por estética. Anti-slop é necessário mas não suficiente.

---

## 🎯 Os 7 Pilares de uma UI Boa e Bonita

### 1. Clareza > Cleverness
**Princípio**: O propósito e hierarquia devem ser óbvios em 3 segundos.

**Aplicação prática**:
- Headline que diz o que o produto FAZ (não o que ele "empodera")
- Hierarquia visual com 3+ níveis distintos
- CTA principal óbvio (não competindo com 5 outros elementos)
- Microcopy que ajuda, não decora

**Anti-patterns**:
- Headlines vagos ("Build the future")
- CTAs escondidos em meio a outros elementos
- Microcopy redundante

---

### 2. Consistência > Originalidade
**Princípio**: Um sistema coerente vale mais que um truque isolado.

**Aplicação prática**:
- Design tokens aplicados consistentemente (cores, spacing, type)
- Componentes que seguem mesmas regras
- Padrões previsíveis para ações similares
- Whitespace e spacing ritmados

**Anti-patterns**:
- Cada secção com style diferente sem propósito
- Componentes que parecem de libs diferentes
- Espaçamento aleatório

---

### 3. Performance > Polish
**Princípio**: Velocidade é feature. UI bonita que demora a carregar é falha.

**Aplicação prática**:
- Imagens otimizadas (WebP, lazy loading)
- CSS animations em transform/opacity (não width/height)
- Fontes carregadas com font-display: swap
- Bundle size razoável
- LCP < 2.5s, CLS < 0.1

**Anti-patterns**:
- Heavy 3D em landing pages sem propósito
- Imagens 4K em hero
- Animações que travam scroll

---

### 4. Acessibilidade > Estética
**Princípio**: WCAG nunca é negociável. UI bonita que exclui usuários é falha.

**Aplicação prática**:
- Contraste mínimo 4.5:1 body, 3:1 large text
- Navegação completa por teclado
- ARIA labels onde necessário
- Hierarquia de headings correta (h1→h2→h3, sem skip)
- Focus states visíveis
- Screen reader friendly

**Anti-patterns**:
- Texto cinza sobre fundo cinza
- Click handlers sem keyboard equivalents
- Headings que pulam níveis
- Imagens sem alt text

---

### 5. Delight > Decoration
**Princípio**: Cada animação/micro-interação deve servir um propósito funcional ou emocional claro.

**Aplicação prática**:
- Loading states informativos (não spinners genéricos)
- Micro-interações em CTAs (feedback visual)
- Transitions que comunicam mudanças de estado
- Surpresas agradáveis em momentos-chave

**Anti-patterns**:
- Animações decorativas que distraem
- Hover effects que não fazem nada
- Easter eggs escondidos sem propósito

---

### 6. Distinctividade > Safety
**Princípio**: Esquecível é pior que feio. Ter opinião > agradar todos.

**Aplicação prática**:
- Tipografia com personalidade (não escolha por default)
- Paleta com significado semântico
- Layout com ritmo intencional (não grid uniforme)
- Voz de marca reconhecível

**Anti-patterns**:
- Escolher fonte "porque é safe / padrão da indústria"
- Layout 3-cards porque "é o padrão"
- Copy que poderia estar em qualquer produto

---

### 7. Honestidade > Marketing
**Princípio**: UI não pode fingir ser o que não é. Microcopy honest > marketing fluff.

**Aplicação prática**:
- Headlines dizem o que o produto FAZ
- Botões descrevem a ação real ("Save draft", não "Click here")
- Error states úteis (não genéricos)
- Privacy disclosures claras
- Pricing transparente

**Anti-patterns**:
- "Build the future" sem contexto
- CTAs vagos ("Learn more")
- Error messages que culpam o usuário
- Dark patterns (confirm shaming, hidden costs)

---

## ✅ Checklist de "UI Boa e Bonita"

Antes de validar qualquer output, verificar:

### Clarity ✓
- [ ] Headline explica o produto em 1 frase?
- [ ] Hierarquia visual clara (3+ níveis)?
- [ ] CTA principal óbvio?
- [ ] User sabe o que fazer em 3 segundos?

### Consistency ✓
- [ ] Cores vêm de um sistema (não aleatórias)?
- [ ] Espaçamento segue ritmo (não uniforme)?
- [ ] Componentes seguem mesmas regras?
- [ ] Tipografia hierárquica?

### Performance ✓
- [ ] Imagens otimizadas?
- [ ] Animações em GPU (transform/opacity)?
- [ ] Fonts com font-display: swap?
- [ ] LCP < 2.5s?

### Accessibility ✓
- [ ] Contraste WCAG AA?
- [ ] Navegação por teclado completa?
- [ ] ARIA labels onde necessário?
- [ ] Headings sem skip?
- [ ] Focus states visíveis?

### Delight ✓
- [ ] Loading states informativos?
- [ ] Micro-interações em CTAs?
- [ ] Transitions servem propósito?
- [ ] Surpresas intencionais (não decoração)?

### Distinctiveness ✓
- [ ] Tipografia com personalidade?
- [ ] Paleta com significado?
- [ ] Layout com ritmo intencional?
- [ ] Diferente do median AI?

### Honesty ✓
- [ ] Headlines dizem o que é?
- [ ] CTAs descrevem ação real?
- [ ] Error states úteis?
- [ ] Sem dark patterns?

---

## 🎨 Princípios Visuais que Suportam Qualidade

### Tipografia Responsável
- Body text: 16px ideal, mínimo 14px
- Line height: 1.5-1.7 para body
- Line length: max 75ch
- Hierarquia: razão mínima 1.25x entre níveis

### Cor Funcional
- Não mais que 1-2 accent colors
- Estados (hover, active, disabled) claramente diferenciados
- Dark mode (se usado) com true blacks + high contrast text
- Semantic naming (--color-action-primary, não --color-blue-500)

### Espaçamento com Ritmo
- Sistema de spacing tokens (4px, 8px, 16px, 24px, 32px, 64px)
- Tight groupings para itens relacionados (8-16px)
- Generous separations entre seções (64px+)
- Não repetir o mesmo valor sempre

### Componentes Honestos
- Cada componente resolve um problema real
- Não usar modais quando page dedicated é melhor
- Form inputs com labels, hints, error states
- Navigation que reflete hierarquia de informação

---

## 💡 Filosofia Central

> **"Anti-slop é o piso. Distinctividade é o teto. UX sólida é o alicerce."**

Uma UI pode ser distinta e bonita, mas se não for usável, falha.
Uma UI pode seguir todas as best practices, mas se for genérica, esquece.

A skill deve procurar o equilíbrio:
- **Combate AI Slop** (evita os 46 padrões)
- **Incentiva opinião** (tem taste, declara preferências)
- **Mantém qualidade** (nunca sacrifica UX por estética)