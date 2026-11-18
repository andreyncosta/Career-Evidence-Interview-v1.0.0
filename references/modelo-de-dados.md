# Modelo da Career Knowledge Base

A base precisa preservar fatos e evidências e permitir diferentes interpretações para vagas, sem virar um catálogo rígido de frases de currículo.

## Estrutura sugerida

career-base/
- INDEX.md
- profile/summary.md
- experiences/<id>.md
- achievements/<id>.md
- skills/<id>.md
- sources/source-log.md
- governance/open-questions.md
- governance/revisions.md

Diretórios adicionais (projects, applications, interviews) apenas quando necessários.

## Entidades e ligações

- **experience:** cargo, organização, vínculo, datas, escopo e contexto.
- **achievement:** caso associado à experiência, problema, ação, método, resultado e evidência.
- **skill:** competência, contexto, profundidade, ferramenta, recência e realizações que a sustentam.
- **source:** depoimento ou documento, localizador, data, autorização e sensibilidade.
- **claim:** afirmação ligada a uma ou mais fontes, com precisão e grau de confirmação.

Relações: experience → achievement; achievement ↔ skill; claim → source. IDs estáveis, preferencialmente kebab-case, e referências cruzadas.

## Campos de governança

- status: rascunho / revisado_pela_pessoa / verificado_externamente
- origin_type: depoimento / documento_pessoal / artefato_tecnico / fonte_externa / inferencia
- precision: exato / aproximado / desconhecido / conflitante
- ownership: individual / lideranca / colaboracao / equipe / terceiros
- estimate: sim/não, com unidade, período e denominador
- publication: privado / compartilhavel_com_revisao / publico_autorizado
- source_locator: localização real do documento ou depoimento; não inventar URLs
- revised_at e supersedes: rastreamento das alterações

## Política de atualização

1. Inspecione a base existente antes de criar um registro.
2. Reutilize IDs de realizações e experiências equivalentes.
3. Identifique fatos novos, correções e interpretações alternativas.
4. Atualize apenas os registros afetados, mantendo proveniência e histórico.
5. Não converta ausência de evidência em evidência negativa.
6. Diferencie autorização para registrar de autorização para publicar externamente.
7. Gere currículos como derivações, não como fontes canônicas.

Os templates em assets/templates/ devem ser usados como ponto de partida, nunca como barreira para novas categorias.