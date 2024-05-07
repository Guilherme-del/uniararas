# Descrição geral do dataset

## Descrição
Este conjunto de dados contém informações sobre pacientes ou casos clínicos, com atributos relacionados a diferentes aspectos médicos.

## Atributos
1. **L-CORE**: Temperatura central do corpo do paciente. Valores possíveis: "low" (baixa), "mid" (média) e "high" (alta).
2. **L-SURF**: Temperatura superficial do corpo do paciente. Valores possíveis: "low" (baixa) e "mid" (média).
3. **L-O2**: Nível de oxigênio no sangue do paciente.
4. **L-BP**: Pressão sanguínea do paciente. Valores possíveis: "low" (baixa), "mid" (média) e "high" (alta).
5. **SURF-STBL**: Estabilidade da temperatura superficial do corpo do paciente. Valores possíveis: "stable" (estável) e "unstable" (instável).
6. **CORE-STBL**: Estabilidade da temperatura central do corpo do paciente. Valores possíveis: "stable" (estável) e "unstable" (instável).
7. **BP-STBL**: Estabilidade da pressão sanguínea do paciente. Valores possíveis: "mod-stable" (moderadamente estável), "stable" (estável) e "unstable" (instável).
8. **COMFORT**: Nível de conforto do paciente ou outra métrica subjetiva relacionada ao bem-estar do paciente.
9. **ADM-DECS**: Decisões administrativas em relação ao paciente. Valores possíveis: "A" (admitido), "S" (submetido a tratamento), "I" (indeterminado) e outros.

## Instâncias
Número total de instâncias: 89

## Uso
A análise desses dados pode ser útil para entender padrões de diagnóstico, tratamento e prognóstico em um ambiente médico, e pode ser aplicada em áreas como medicina preventiva, gestão hospitalar e pesquisa clínica.

# Fase de pré-processamento

Durante a fase de pré-processamento, foram realizadas várias etapas para entender e preparar os dados para análise. Abaixo estão as características relevantes e medidas estatísticas dos dados e das classes:

### Características Relevantes:
- O conjunto de dados possui nove atributos, incluindo informações sobre temperatura, nível de oxigênio, pressão sanguínea, estabilidade e conforto do paciente, bem como decisões administrativas.
- Os atributos variam em sua natureza, incluindo variáveis categóricas (como estabilidade) e numéricas (como conforto).
- Há um total de 89 instâncias no conjunto de dados.

### Medidas Estatísticas:
- Não foram fornecidas medidas estatísticas específicas, como média, desvio padrão ou quartis para os atributos numéricos. Isso pode ser uma área a ser explorada durante a análise exploratória de dados.

  
# Limpeza e Normalização dos Dados

Durante a análise do conjunto de dados, algumas operações de limpeza e normalização foram necessárias devido a certas peculiaridades nos dados. Abaixo estão as operações realizadas:

### Valores Faltantes:
- Foram identificados valores faltantes representados pelo símbolo "?" no atributo "ADM-DECS".
- Decidiu-se remover as instâncias com valores faltantes, pois a presença de dados ausentes poderia afetar a qualidade das análises subsequentes.

### Normalização:
- Os atributos numéricos, como "COMFORT", foram normalizados para garantir que os dados estivessem na mesma escala e facilitar a comparação entre eles.
- Foi utilizada a técnica de normalização Min-Max para ajustar os valores para um intervalo específico, geralmente entre 0 e 1, preservando as relações entre os dados originais.

### Justificativa:
- A remoção de instâncias com valores faltantes foi preferida em vez de imputar valores, pois não havia muitos casos faltantes e não se comprometeria significativamente o tamanho do conjunto de dados.
- A normalização dos atributos numéricos foi realizada para evitar que diferenças nas escalas dos dados influenciassem negativamente algoritmos de aprendizado de máquina sensíveis à escala dos atributos.

Essas operações ajudaram a garantir que os dados estivessem limpos e prontos para análises posteriores.

# Fase de Análise
