#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_NUMBERS 100000

// Função para fatorar e consumir os fatores (sem exibir todos)
void fatorar(long long n) {
    if (n < 2) return;
    for (long long i = 2; i <= sqrt(n); i++) {
        while (n % i == 0) {
            n /= i;
        }
    }
}

// Função principal
int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Uso: %s <small|medium|large>\n", argv[0]);
        return 1;
    }

    char *tamanho = argv[1];
    char caminho[256];
    snprintf(caminho, sizeof(caminho), "datasets/%s/factoring.json", tamanho);

    FILE *fp = fopen(caminho, "r");
    if (!fp) {
        fprintf(stderr, "Erro ao abrir o arquivo: %s\n", caminho);
        return 1;
    }

    // Lê o arquivo inteiro para memória
    fseek(fp, 0, SEEK_END);
    long fsize = ftell(fp);
    rewind(fp);

    char *json_content = malloc(fsize + 1);
    fread(json_content, 1, fsize, fp);
    json_content[fsize] = '\0';
    fclose(fp);

    // Extrai números da lista JSON
    long long numeros[MAX_NUMBERS];
    int count = 0;

    char *start = strchr(json_content, '[');
    char *end = strchr(json_content, ']');
    if (start && end && end > start) {
        char *token = strtok(start + 1, ",");
        while (token && count < MAX_NUMBERS) {
            numeros[count++] = strtoll(token, NULL, 10);
            token = strtok(NULL, ",");
        }
    }
    free(json_content);

    // Fatora todos os números
    for (int i = 0; i < count; i++) {
        fatorar(numeros[i]);
    }

    printf("Fatorados %d números do dataset %s.\n", count, tamanho);
    return 0;
}
