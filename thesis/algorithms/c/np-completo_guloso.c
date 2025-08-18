#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int weight;
    int value;
} Item;

// Função de comparação para qsort (valor/peso decrescente)
int compare(const void *a, const void *b) {
    double r1 = (double)((Item *)b)->value / ((Item *)b)->weight;
    double r2 = (double)((Item *)a)->value / ((Item *)a)->weight;
    return (r1 > r2) - (r1 < r2);
}

// Algoritmo guloso para knapsack
int knapsack(Item *items, int n, int capacity) {
    qsort(items, n, sizeof(Item), compare);  // Ordena os itens por valor/peso

    int totalValue = 0;
    int currentWeight = 0;

    for (int i = 0; i < n; i++) {
        if (currentWeight + items[i].weight <= capacity) {
            currentWeight += items[i].weight;
            totalValue += items[i].value;
        }
    }

    return totalValue;
}

// Função para ler arquivo JSON simplificado
int read_knapsack(const char *path, Item **items, int *capacity) {
    FILE *f = fopen(path, "r");
    if (!f) return -1;

    fseek(f, 0, SEEK_END);
    long size = ftell(f);
    rewind(f);
    char *buffer = malloc(size + 1);
    if (!buffer) {
        fclose(f);
        return -1;
    }
    fread(buffer, 1, size, f);
    fclose(f);
    buffer[size] = '\0';

    // Procurar a capacidade
    char *cap_ptr = strstr(buffer, "\"capacity\"");
    if (!cap_ptr || sscanf(cap_ptr, "\"capacity\"%*[^0-9]%d", capacity) != 1) {
        free(buffer);
        return -1;
    }

    // Inicializar array de itens dinamicamente
    int alloc = 10000;
    Item *temp = malloc(sizeof(Item) * alloc);
    if (!temp) {
        free(buffer);
        return -1;
    }

    int count = 0;
    char *p = buffer;

    while ((p = strstr(p, "\"weight\"")) != NULL) {
        int weight = 0, value = 0;
        char *value_ptr = strstr(p, "\"value\"");
        if (value_ptr &&
            sscanf(p, "\"weight\":%d", &weight) == 1 &&
            sscanf(value_ptr, "\"value\":%d", &value) == 1) {
            if (count >= alloc) {
                alloc *= 2;
                Item *new_temp = realloc(temp, sizeof(Item) * alloc);
                if (!new_temp) {
                    free(temp);
                    free(buffer);
                    return -1;
                }
                temp = new_temp;
            }
            temp[count].weight = weight;
            temp[count].value = value;
            count++;
        }
        p++;  // Evita loop infinito
    }

    *items = temp;
    free(buffer);
    return count;
}

int main(int argc, char *argv[]) {
    const char *size = (argc > 1) ? argv[1] : "small";
    char path[128];
    snprintf(path, sizeof(path), "datasets/%s/knapsack.json", size);

    Item *items;
    int capacity;
    int count = read_knapsack(path, &items, &capacity);
    if (count <= 0) {
        printf("Erro ao ler o arquivo ou nenhum item encontrado.\n");
        return 1;
    }

    int result = knapsack(items, count, capacity);
    if (result < 0) {
        printf("Erro ao calcular knapsack (memória insuficiente?).\n");
        free(items);
        return 2;
    }

    printf("Valor aproximado (greedy) para %d itens (capacidade %d, %s): %d\n", count, capacity, size, result);

    free(items);
    return 0;
}
