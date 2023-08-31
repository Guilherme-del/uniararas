#include <stdio.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Número de parâmetros insuficiente! Digite apenas seu nome como parâmetro do comando.\n");
    } else {
        printf("Ola %s\n", argv[1]);
    }
    return 0;
}