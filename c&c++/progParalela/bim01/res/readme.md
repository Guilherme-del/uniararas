# Multiplicação de Matrizes Paralela com Pthreads

Este projeto implementa a multiplicação de matrizes usando programação paralela com Pthreads em C. O programa divide o trabalho entre várias threads para acelerar a computação, fazendo uso de `mutex` para evitar condições de corrida (race conditions) em regiões críticas do código.

## Funcionalidades

- **Multiplicação de Matrizes:** Calcula a multiplicação de duas matrizes (A e B) e armazena o resultado em uma matriz C.
- **Paralelismo:** Usa Pthreads para realizar a multiplicação de forma paralela, com cada thread processando uma linha da matriz de resultado.
- **Mutex:** Utiliza `mutex` para proteger regiões críticas durante a atualização da matriz de resultado.

## Pré-requisitos

- Compilador GCC (ou similar) com suporte a Pthreads.
- Sistema operacional compatível com Pthreads (Linux, macOS ou Windows com Cygwin/MinGW).

## Como Compilar

Para compilar o programa, utilize o comando abaixo:

```bash
gcc -o matriz_mult matriz_mult.c -pthread
```
## Exemplo de saida

```
Matriz C (resultado):
30 70 110 150 
40 96 152 208 
50 122 194 266 
60 148 236 324 
```

# Integrantes do grupo
| Nome | Ra |
| ------------- | ------------- |
| Guilherme Cavenaghi | 109317 |
| Rafael Souza | 109680 |