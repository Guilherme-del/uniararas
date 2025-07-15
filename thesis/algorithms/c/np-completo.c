#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int weight;
    int value;
} Item;

int knapsack(Item *items, int n, int capacity) {
    int *dp = calloc(capacity + 1, sizeof(int));
    for (int i = 0; i < n; i++) {
        for (int w = capacity; w >= items[i].weight; w--) {
            int val = dp[w - items[i].weight] + items[i].value;
            if (val > dp[w]) dp[w] = val;
        }
    }
    int result = dp[capacity];
    free(dp);
    return result;
}

int read_knapsack(const char *path, Item **items, int *capacity) {
    FILE *f = fopen(path, "r");
    if (!f) return -1;
    fseek(f, 0, SEEK_END);
    long size = ftell(f);
    rewind(f);
    char *buffer = malloc(size + 1);
    fread(buffer, 1, size, f); fclose(f);
    buffer[size] = '\0';

    char *cap_ptr = strstr(buffer, "\"capacity\":");
    *capacity = atoi(cap_ptr + 11);
    char *items_ptr = strstr(buffer, "\"items\":[");

    Item *temp = malloc(sizeof(Item) * 100000);
    int count = 0;
    char *entry = strtok(items_ptr, "{");
    while (entry) {
        if (strstr(entry, "weight")) {
            int weight, value;
            sscanf(entry, "\"weight\":%d,\"value\":%d", &weight, &value);
            temp[count].weight = weight;
            temp[count].value = value;
            count++;
        }
        entry = strtok(NULL, "{");
    }
    *items = temp;
    free(buffer);
    return count;
}

int main(int argc, char *argv[]) {
    const char *size = (argc > 1) ? argv[1] : "small";
    char path[128];
    snprintf(path, sizeof(path), "../data/%s/knapsack_%s.json", size, size);
    Item *items;
    int capacity, count = read_knapsack(path, &items, &capacity);
    if (count < 0) { printf("Erro ao ler o arquivo\n"); return 1; }
    int result = knapsack(items, count, capacity);
    printf("Valor máximo para %d itens (%s): %d\n", count, size, result);
    free(items);
    return 0;
}
