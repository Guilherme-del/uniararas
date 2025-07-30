#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;
    int *L = malloc(n1 * sizeof(int));
    int *R = malloc(n2 * sizeof(int));
    for (int i = 0; i < n1; i++) L[i] = arr[l + i];
    for (int j = 0; j < n2; j++) R[j] = arr[m + 1 + j];

    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];

    free(L); free(R);
}

void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

int read_array(const char *path, int **arr) {
    FILE *f = fopen(path, "r");
    if (!f) return -1;
    fseek(f, 0, SEEK_END); long size = ftell(f); rewind(f);
    char *buffer = malloc(size + 1); fread(buffer, 1, size, f); fclose(f);
    buffer[size] = '\0';

    int *temp = malloc(sizeof(int) * 1000000);
    int count = 0;
    char *tok = strtok(buffer, "[,]");
    while (tok) {
        temp[count++] = atoi(tok);
        tok = strtok(NULL, "[,]");
    }
    *arr = temp;
    free(buffer);
    return count;
}

int main(int argc, char *argv[]) {
    const char *size = (argc > 1) ? argv[1] : "small";
    char path[128];
    printf("Ordenando %s elementos...\n", size);
    snprintf(path, sizeof(path), "datasets/%s/merge_sort.json", size);
    int *arr;
    int len = read_array(path, &arr);
    if (len < 0) { printf("Erro ao ler arquivo JSON\n"); return 1; }
    mergeSort(arr, 0, len - 1);
    printf("Ordenado %d elementos (%s)\n", len, size);
    free(arr);
    return 0;
}
