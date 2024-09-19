# Integrantes do grupo

| Nome | Ra |
| ------------- | ------------- |
| Wayner Moraes  | 109097  |
| Guilherme Cavenaghi | 109317 |
| Vinicius Rossi | 110273 |
| Valter Chieregatto | 109049 |
| Rafael Souza | 109680 |

# Projeto de Classificação com RandomForest

Este projeto utiliza um modelo de [RandomForest](https://didatica.tech/o-que-e-e-como-funciona-o-algoritmo-randomforest) para classificação. O código está organizado seguindo os princípios POO para garantir manutenibilidade e escalabilidade.

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

- [Python 3.7+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Execução

### Passo 1: Preparar os dados

Coloque os arquivos de dados \`treino.csv\` e \`teste.csv\` na pasta \`input/\`. Certifique-se de que os arquivos estão no formato correto.

### Passo 2: Executar o script principal

Execute o script principal para treinar o modelo e gerar as previsões:

python index.py

### Passo 3: Verificar a saída

O arquivo de submissão \`submissao.csv\` será gerado na pasta \`working/\`. Além disso, o F1 Score no conjunto de validação será exibido no console.

## Explicação do Projeto

- main: Script principal que carrega os dados, treina o modelo e gera as previsões.
- data_handler: Classe responsável pelo carregamento e preparação dos dados.
- model_trainer: Classe responsável pelo treinamento, previsão e avaliação do modelo.
