#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Erro: Número de parâmetros incorreto!\n");
        return 1;
    }

    int n = atoi(argv[1]);
    if (n <= 0) {
        printf("Erro: O número de termos deve ser maior que zero.\n");
        return 1;
    }

    int fibo[n];
    fibo[0] = 1;
    fibo[1] = 1;

    for (int i = 2; i < n; i++) {
        fibo[i] = fibo[i - 1] + fibo[i - 2];
    }

    for (int i = 0; i < n; i++) {
        printf("%d ", fibo[i]);
    }
    printf("\n");

    return 0;
}