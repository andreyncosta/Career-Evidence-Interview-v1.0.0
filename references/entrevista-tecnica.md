# Inventário técnico e avaliação de competências

Para cada competência, separar **contexto**, **fundamentação**, **execução**, **complexidade**, **autonomia**, **produção**, **recência** e **evidências**. Uso frequente não significa automaticamente domínio profundo; não conhecer uma técnica não invalida competências correlatas.

## SQL e dados relacionais

- Dialetos e ambientes: produção, laboratório, estudo, legado.
- JOINs e cardinalidade: chaves, granularidade, muitos-para-muitos, duplicação, valores nulos.
- CTEs, subconsultas, funções analíticas e agregações; recursão como competência separada.
- Otimização: EXPLAIN, filtros antecipados, partições, staging, materialização, índices, estatísticas, limites computacionais.
- Cargas incrementais: chaves, watermark, deduplicação, idempotência, upsert, falhas e recomposição.
- Modelagem: OLTP/OLAP, normalização, fatos/dimensões, SCD, integridade, esquema estrela.
- SQL distribuído: partições, movimentação de dados, formatos e limitações de memória.

Pergunta de aprofundamento: descreva uma consulta real lenta, por que era lenta, o que mudou e o resultado.

## Python e desenvolvimento

- Scripts, notebooks, pipelines, APIs, web e serviços.
- Bibliotecas utilizadas efetivamente; diferenciação entre estudos e produção.
- Organização de projetos, tipagem, testes, logging, erros, retries, timeouts, autenticação e dependências.
- Desempenho, uso de memória, vetorização, concorrência e execução por lotes.
- Uso de IA para código: autoria da arquitetura, revisão, testes, implantação e manutenção.

## R, estatística e econometria

- Pacotes e ambientes reais, transformação e visualização de dados.
- Regressões, inferência, hipóteses, diagnósticos, erros-padrão e vieses.
- Séries temporais: tendência, sazonalidade, defasagens, picos, mudanças e validação temporal.
- Inferência causal: identificação, contrafactual, comparação observacional, testes randomizados, DiD, matching, IV e RDD.
- Economia aplicada: concentração HHI, cenários de mercado, substituição de produtos, elasticidades e projeções.

## Machine Learning

- Unidade de análise, variável-alvo, rótulo e origem dos dados.
- Divisão treino/validação/teste; prevenção de leakage; validação temporal.
- Algoritmo realmente usado, features, hiperparâmetros, métricas e calibração.
- Dados desbalanceados, interpretação, estabilidade, deployment, monitoramento e drift.
- Separar regra de negócio, scoring ponderado e modelos estatísticos treinados.

## Engenharia de dados e BI

- Origem, extração, tratamento, validação, armazenamento, disponibilização e consumidores dos dados.
- Orquestração, agendamento, dependências, qualidade, linhagem, segurança e manutenção.
- Power BI: Power Query, DAX, modelo semântico, relacionamentos, RLS, gateways e desempenho.
- Distinguir ferramenta conhecida do que foi operado em produção.

## Software, DevOps e produtos

- REST, HTTP, backend/frontend, banco de dados, autenticação, versionamento e deploy.
- Git, Docker, CI/CD, ambientes, logs, testes e observabilidade.
- Requisitos funcionais/não funcionais, priorização, sprints, UAT, testes negativos e limites.
- Gestão direta de pessoas versus orientação técnica e contribuição individual.

## Regras

Faça uma pergunta por vez e use um caso real como evidência. Se um detalhe não for lembrado, registre desconhecido. Se o relato for corrigido, atualize a conclusão e documente a revisão.