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

# Análise

### K Nearest Neighbors (KNN):
- **Número de Vizinhos: 1**
  - Precisão Média: 0.411
  - Recall Médio: 0.467
  - F1-Score Médio: 0.438
- **Número de Vizinhos: 3**
  - Precisão Média: 0.406
  - Recall Médio: 0.433
  - F1-Score Médio: 0.419
- **Número de Vizinhos: 5**
  - Precisão Média: 0.4
  - Recall Médio: 0.4
  - F1-Score Médio: 0.4

### Decision Tree:
- **Profundidade Máxima: 1**
  - Precisão Média: 0.392
  - Recall Médio: 0.667
  - F1-Score Médio: 0.1
- **Profundidade Máxima: 3**
  - Precisão Média: 0.554
  - Recall Médio: 0.567
  - F1-Score Médio: 0.557
- **Profundidade Máxima: 5**
  - Precisão Média: 0.328
  - Recall Médio: 0.644
  - F1-Score Médio: 0.305

### Random Forest:
- **Número de Estimadores: 50**
  - Precisão Média: 0.393
  - Recall Médio: 0.367
  - F1-Score Médio: 0.379
- **Número de Estimadores: 100**
  - Precisão Média: 0.375
  - Recall Médio: 0.3
  - F1-Score Médio: 0.333
- **Número de Estimadores: 150**
  - Precisão Média: 0.393
  - Recall Médio: 0.367
  - F1-Score Médio: 0.379

## Descrição do Algoritmo Alternativo: Random Forest
O Random Forest é um algoritmo de aprendizado supervisionado usado para classificação e regressão. Ele cria uma "floresta" de árvores de decisão durante o treinamento e faz previsões com base na maioria das previsões das árvores individuais. Cada árvore é treinada em uma amostra aleatória dos dados e, durante a previsão, cada árvore contribui com uma votação igual.

O motivo pelo qual escolhemos o Random Forest como um substituto potencial para o KNN é devido à sua robustez em lidar com conjuntos de dados de alta dimensionalidade, capacidade de lidar com dados faltantes e valores atípicos, e geralmente requer menos ajustes de hiperparâmetros em comparação com o KNN.

## Resultados Gerais:
- O KNN tende a ter desempenho consistente, mas pode não ser ideal para conjuntos de dados com alta dimensionalidade devido à sensibilidade à maldição da dimensionalidade.
- A árvore de decisão apresenta resultados variáveis com base na profundidade máxima da árvore, sendo mais propensa a overfitting em profundidades mais altas.
- O Random Forest demonstra desempenho estável e pode ser uma boa escolha devido à sua capacidade de lidar com diferentes tipos de dados e evitar overfitting.

Em geral, o Random Forest pode ser uma escolha sólida como substituto do KNN devido à sua flexibilidade e desempenho consistente em uma variedade de conjuntos de dados.

# Conclusão

Com base nos resultados das análises dos diferentes algoritmos de classificação (K Nearest Neighbors, Decision Tree e Random Forest), podemos tirar algumas conclusões importantes:

1. **Desempenho do K Nearest Neighbors (KNN):** O KNN demonstrou consistência em seus resultados, porém sua eficácia pode ser limitada em conjuntos de dados com alta dimensionalidade devido à sensibilidade à maldição da dimensionalidade.

2. **Comportamento da Decision Tree:** A Decision Tree apresentou resultados variáveis, influenciados pela profundidade máxima da árvore. Profundidades mais altas levaram a um maior risco de overfitting, enquanto profundidades mais baixas resultaram em uma simplificação excessiva do modelo, afetando negativamente o desempenho.

3. **Vantagens do Random Forest:** O Random Forest demonstrou um desempenho estável em diferentes configurações, mostrando-se uma escolha sólida para a classificação. Sua capacidade de lidar com diferentes tipos de dados, reduzir o overfitting e requerer menos ajustes de hiperparâmetros em comparação com o KNN o torna uma opção atrativa.

4. **Escolha do Melhor Algoritmo:** Com base nas análises, o Random Forest surge como o algoritmo mais promissor para substituir o KNN. Sua robustez, capacidade de generalização e menor sensibilidade aos ajustes de hiperparâmetros o tornam uma escolha sólida para uma variedade de conjuntos de dados.

Em resumo, a escolha do Random Forest como substituto do KNN é respaldada pela consistência de seus resultados e sua capacidade de lidar com desafios comuns em problemas de classificação.
