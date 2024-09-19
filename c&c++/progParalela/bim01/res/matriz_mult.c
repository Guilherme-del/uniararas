/*
B - 2 
O programa mostrado na saída realiza a multiplicação de matrizes usando diferentes ordens de loops para calcular o produto de duas matrizes.
A saída do programa mostra as dimensões das matrizes, 
o número de operações de ponto flutuante realizadas e o tempo de computação para cada método de multiplicação. 
Isso ajuda a identificar o método mais eficiente para multiplicação de matrizes em diferentes cenários.
*/

// B - 3
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define N1 4 // Número de linhas da matriz A e matriz resultado
#define N2 4 // Número de colunas da matriz B e matriz resultado
#define N3 4 // Número de colunas da matriz A / Número de linhas da matriz B

// Matrizes globais
int A[N1][N3], B[N3][N2], C[N1][N2];

// Mutex para proteger regiões críticas
pthread_mutex_t mutex;

void* multiply_row(void* arg) {
    int row = *(int*)arg; // Índice da linha a ser processada
    free(arg); // Libera a memória alocada para o índice da linha

    // Calcula a linha do resultado
    for (int j = 0; j < N2; j++) {
        C[row][j] = 0;
        for (int k = 0; k < N3; k++) {
            pthread_mutex_lock(&mutex); // Protege a operação com mutex
            C[row][j] += A[row][k] * B[k][j];
            pthread_mutex_unlock(&mutex); // Libera o mutex
        }
    }
    pthread_exit(0);
}

int main() {
    pthread_t threads[N1]; // Uma thread para cada linha de resultado

    // Inicializa as matrizes A e B com valores
    for (int i = 0; i < N1; i++) {
        for (int j = 0; j < N3; j++) {
            A[i][j] = i + j + 1; // Valores de exemplo
        }
    }
    for (int i = 0; i < N3; i++) {
        for (int j = 0; j < N2; j++) {
            B[i][j] = i + j + 1; // Valores de exemplo
        }
    }

    // Inicializa o mutex
    pthread_mutex_init(&mutex, NULL);

    // Cria as threads
    for (int i = 0; i < N1; i++) {
        int* row = malloc(sizeof(int));
        *row = i;
        pthread_create(&threads[i], NULL, multiply_row, row);
    }

    // Aguarda todas as threads terminarem
    for (int i = 0; i < N1; i++) {
        pthread_join(threads[i], NULL);
    }

    // Exibe a matriz resultante
    printf("Matriz C (resultado):\n");
    for (int i = 0; i < N1; i++) {
        for (int j = 0; j < N2; j++) {
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }

    // Destroi o mutex
    pthread_mutex_destroy(&mutex);

    return 0;
}
