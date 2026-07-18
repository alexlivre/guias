---
description: Pesquisa progressiva com MiniMax + Fetch + GitHub MCPs + sequential-thinking nos pontos de decisão. Cria plano completo de implementação.
---

/pesquisa

A mensagem do usuário logo após o comando /pesquisa é a tarefa que deve ser analisada.

Analise cuidadosamente essa tarefa.

**Antes de qualquer ação, use a ferramenta `skill` para verificar quais skills estão disponíveis e relevantes para esta tarefa. Carregue e siga todas as skills aplicáveis.** (Ex: brainstorming, TDD, clean-code, debugging, etc.)

**Se a tarefa envolver Python** (criar projeto, script, API, etc.), carregue também a skill `gerenciar-uv` — ela cuida do ambiente isolado automaticamente.

Depois, realize uma **pesquisa progressiva em múltiplas rodadas** usando as ferramentas disponíveis:

**Ferramentas obrigatórias:**
- `MiniMax_web_search(query)` — busca web geral (títulos + snippets + links)
- `webfetch` ou `fetch_fetch` — baixa o conteúdo completo das páginas encontradas
- `github_search_code` / `github_search_issues` / `github_search_repositories` — busca no GitHub
- `sequential-thinking_sequentialthinking` — raciocínio estruturado nos pontos de decisão

**Processo (pesquisa progressiva):**

1. **Rodada 1 — Descoberta inicial:** Faça uma busca ampla no MiniMax_web_search com a query da tarefa. Obtenha os links mais promissores (top 3-5) e use `webfetch`/`fetch_fetch` para ler o conteúdo completo de cada um.

2. **Analise o conteúdo baixado:** Extraia destas páginas: novas palavras-chave, termos técnicos, bibliotecas, referências, URLs adicionais, e gaps de conhecimento que não foram cobertos.

3. **Rodada 2 — Aprofundamento:** Com base nos gaps e leads encontrados, faça novas buscas no MiniMax + GitHub. Seja mais específico. Baixe novamente as páginas mais relevantes com fetch.

4. **Decisão — Rodada 3 necessária?:** Após a Rodada 2, use `sequential-thinking_sequentialthinking` para decidir se uma Rodada 3 é necessária. Considere: gaps ainda abertos, qualidade do conteúdo obtido, profundidade das informações, e custo de contexto restante. Defina `nextThoughtNeeded: false` e retorne a decisão (sim ou não) com justificativa.

5. **Rodada 3 (se necessário) — Refinamento final:** Se decidiu que sim, faça uma última rodada com buscas ainda mais específicas. Reduza a quantidade de páginas para evitar excesso de contexto.

**Critério de parada:** Pare quando sentir que o conhecimento adquirido é suficiente para criar um plano completo e fundamentado. Máximo 3 rodadas.

Após a pesquisa progressiva, crie um **plano completo de implementação** com a seguinte estrutura:

1. **Entendimento da Tarefa**  
   (Resumo claro do que precisa ser feito)

2. **Melhores Práticas Encontradas**  
   (Resumo das melhores abordagens encontradas via pesquisa)

3. **Decisão da Abordagem Recomendada**  
   Antes de definir a abordagem, use `sequential-thinking_sequentialthinking` para explorar prós e contras de cada alternativa viável. Gere hipóteses, verifique cada uma, e só então conclua qual é a melhor.

4. **Abordagem Recomendada**  
   (Qual solução você recomenda e por quê)

5. **Plano de Implementação Detalhado**  
   (Passos em ordem, com explicação técnica de cada etapa)
   
   **Nota Python:** Se o plano envolver código Python, o primeiro passo deve ser: "Usar skill `gerenciar-uv` para criar ambiente isolado e instalar dependências".

6. **Tecnologias / Ferramentas Sugeridas**

7. **Decisão dos Riscos**  
   Antes de listar os riscos, use `sequential-thinking_sequentialthinking` para antecipar cenários de falha, impacto e probabilidade. Considere riscos técnicos, de prazo, de dependências e de adoção.

8. **Possíveis Riscos e Como Mitigar**

9. **Próximos Passos Imediatos**

10. **Verification Step**  
    Defina como verificar que a implementação está correta e completa. Inclua: comandos de teste a executar, casos de borda a validar, critérios de aceitação, e checklists de verificação. Exemplo: "Após implementar, rode `npm run test` e verifique que todos os testes passam. Valide manualmente os edge cases: X, Y, Z. Confirme que a saída está de acordo com a especificação."

Mostre o plano completo para eu avaliar.  
Só comece a implementar depois que eu disser "autorizado", "pode implementar" ou equivalente.

Seja extremamente detalhista, técnico e prático.
