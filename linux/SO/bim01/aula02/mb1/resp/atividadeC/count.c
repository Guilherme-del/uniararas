#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc == 2) {
        int start = atoi(argv[1]);
        if (start < 100) {
            for (int i = start; i <= 100; i++) {
                printf("%d ", i);
            }
            printf("\n");
        } else {
            printf("Erro: Valor inicial deve ser menor que 100.\n");
            return 1;
        }
    } else if (argc == 3) {
        int start = atoi(argv[1]);
        int end = atoi(argv[2]);
        if (start <= end) {
            for (int i = start; i <= end; i++) {
                printf("%d ", i);
            }
            printf("\n");
        } else {
            printf("Erro: Valor inicial deve ser menor ou igual ao valor final.\n");
            return 1;
        }
    } else if (argc == 4) {
        int start = atoi(argv[1]);
        int step = atoi(argv[2]);
        int end = atoi(argv[3]);
        if (start <= end && step > 0) {
            for (int i = start; i <= end; i += step) {
                printf("%d ", i);
            }
            printf("\n");
        } else {
            printf("Erro: Valores incorretos.\n");
            return 1;
        }
    } else {
        printf("Erro: Número de parâmetros incorreto!\n");
        return 1;
    }

    return 0;
}
