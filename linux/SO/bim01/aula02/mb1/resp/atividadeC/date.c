#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 4 && argc != 5) {
        printf("Erro: Número de parâmetros incorreto!\n");
        return 1;
    }

    int day = atoi(argv[1]);
    int month = atoi(argv[2]);
    int year = atoi(argv[3]);

    if (argc == 4 || (argc == 5 && strcmp(argv[1], "-e") == 0)) {
        printf("%d / %d / %d\n", day, month, year);
    } else {
        printf("%d / %d / %d\n", month, day, year);
    }

    return 0;
}