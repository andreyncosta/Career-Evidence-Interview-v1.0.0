# Career Evidence Interview

**Skill reutilizável para entrevistas de carreira baseadas em evidências.** Ajuda qualquer pessoa a reconstruir sua trajetória profissional, identificar competências técnicas e comportamentais, documentar realizações e preparar currículos direcionados — sem inventar experiências.

**Version:** 1.0.0 · **Language:** pt-BR · **License:** MIT

## O que faz

- Conduz entrevistas progressivas, experiência por experiência, com uma pergunta focada por vez.
- Investiga atividades reais: contexto, responsabilidades, autonomia, decisões, ferramentas, escala, resultados e limitações.
- Aprofunda competências técnicas por exemplos práticos, distinguindo estudos, experimentos e uso em produção.
- Separa depoimentos, documentos, estimativas, inferências e pontos que precisam de confirmação.
- Organiza uma **Career Knowledge Base** com experiências, realizações, competências e histórico de revisões.
- Reutiliza a base para currículos específicos, análise de vagas e preparação de entrevistas.

O material contém **somente exemplos fictícios**. Não inclui os dados pessoais da pessoa cuja entrevista deu origem à metodologia.

## Instalação

Esta skill segue o formato [Agent Skills](https://agentskills.io/specification) com `SKILL.md` na raiz do diretório da skill.

**Codex**: clone este repositório para `~/.agents/skills/career-evidence-interview/` ou `.agents/skills/career-evidence-interview/` dentro do projeto.

**Claude Code**: clone para `~/.claude/skills/career-evidence-interview/` ou `.claude/skills/career-evidence-interview/` dentro do projeto.

**Outros agentes**: abra `SKILL.md` e suas referências, desde que seu ambiente suporte skills ou instruções locais. No ChatGPT web, o suporte a skills standalone depende das funcionalidades disponíveis na conta/ambiente; este repositório não é um plugin instalável automaticamente.

Exemplo usando Git:

```bash
git clone https://github.com/andreyncosta/Career-Evidence-Interview-v1.0.0.git ~/.agents/skills/career-evidence-interview
```

## Como começar

Peça ao assistente:

> Use a skill career-evidence-interview para reconstruir minha carreira. Investigue uma experiência por vez, sintetize os fatos após cada resposta e faça a próxima pergunta mais útil. Diferencie o que fiz pessoalmente, o que minha equipe fez, o que é estimativa e o que está documentalmente comprovado. Não invente métricas ou tecnologias.

Depois, para aprofundar:

> Agora investigue minhas competências e ferramentas em detalhe, com exemplos reais de implementação, autonomia, complexidade, validação e experiência de produção.

E para consolidar:

> Crie uma matriz de competências × realizações × evidências, com pendências de verificação, e indique quais partes são adequadas para um currículo público.

## Arquivos

```text
SKILL.md
README.md
LICENSE
references/
  roteiro-entrevista.md
  entrevista-tecnica.md
  rubrica-evidencia.md
  modelo-de-dados.md
  testes-de-aceitacao.md
assets/templates/
  experiencia.md
  realizacao.md
  competencia.md
  matriz-consolidada.md
  registro-fontes.md
  historico-revisoes.md
examples/
  sessao-ficticia.md
scripts/
  init_workspace.py
  validate_skill.py
```

## Validação local (opcional)

Requer Python 3, sem dependências externas:

```bash
python scripts/validate_skill.py .
python scripts/init_workspace.py ./minha-career-base
```

O primeiro comando valida a estrutura da skill; o segundo prepara uma base local a partir dos modelos. Nenhum desses scripts envia informações à rede.

## Privacidade e rigor

- Depoimento é fonte de relato, não confirmação externa.
- Não atribua resultados coletivos exclusivamente ao entrevistado.
- Não converta automaticamente correlação em causalidade.
- Não publique dados internos de empregadores, clientes, salários ou sistemas sem autorização.
- Preserve correções, incertezas e origem das afirmações.

A Career Knowledge Base é a fonte de evidências; um currículo é apenas uma seleção de informações apropriadas a determinada vaga.

## Licença

[MIT License](LICENSE). Copyright (c) 2026 Andrey Costa.
