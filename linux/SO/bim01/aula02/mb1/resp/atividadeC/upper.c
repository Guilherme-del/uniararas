#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Erro: Número de parâmetros incorreto!\n");
        return 1;
    }
    char *word = argv[1];
    int length = strlen(word);
    for (int i = 0; i < length; i++) {
        if (word[i] >= 'a' && word[i] <= 'z') {
            word[i] -= 32;
        }
    }
    printf("%s\n", word);

    return 0;
}