# Demonstração fictícia de entrevista adaptativa

Este exemplo é **inventado** apenas para ilustrar a metodologia. Não representa uma pessoa real, empresa real nem desempenho verificado.

**Pessoa:** “Eu cuidava de relatórios e automatizações numa distribuidora.”

**Agente:** “Você acompanhava indicadores ou desenvolveu alguma solução que mudou o funcionamento da área? Conte um caso específico.”

**Pessoa:** “As vendas chegavam em planilhas. Eu criei uma rotina SQL e Python para consolidar tudo.”

**Agente — síntese:** “Você relata ter desenvolvido uma rotina de consolidação com SQL e Python. Ainda não sabemos se era usada em produção, qual parte era sua ou o benefício medido. **Pergunta:** essa rotina substituiu algum processo manual?”

**Pessoa:** “Sim. Antes a conferência levava duas tardes e depois levava meia hora.”

**Agente:** “Registro como **estimativa retrospectiva** de tempo, não como medição auditada. **Pergunta:** como você evitava duplicar vendas caso a importação fosse repetida?”

**Pessoa:** “Não controlava. O operador zerava a planilha manualmente.”

**Agente:** “Sua experiência demonstra consolidação de dados e automação, mas ainda não comprova idempotência. Registrei essa limitação. **Pergunta:** a rotina era executada todos os dias em produção ou apenas quando você era solicitado?”

**Pessoa:** “Todos os dias.”

**Agente — resultado:** “Experiência de pipeline diário em produção; não alegar processamento resiliente a reexecução. Após completar as demais dimensões, isso pode justificar uma descrição de currículo como: Desenvolveu fluxo diário de consolidação SQL/Python com redução estimada do tempo de preparação.”

## Correção posterior

**Pessoa:** “Na verdade, a parte do Python era só experimental; a rotina em produção era SQL.”

**Agente:** “Atualizo a evidência vigente: **SQL em produção; Python experimental**. Não manterei Python como tecnologia de produção nesse projeto. Preservo a correção no histórico.”

## Nota

Observe a sequência: contexto → caso real → ação → escala → limitação → técnica → validação → linguagem profissional. O agente não transforma depoimento em prova independente nem compensa lacunas inventando detalhes.