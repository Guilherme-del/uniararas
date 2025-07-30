#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int simulate_program(const char *code) {
    if (strstr(code, "HALT")) return 1;
    return 0; // WHILE TRUE => não para
}

int main(int argc, char *argv[]) {
    const char *size = (argc > 1) ? argv[1] : "small";
    char path[128];
    snprintf(path, sizeof(path), "../datasets/%s/halting.json", size);
    FILE *f = fopen(path, "r");
    if (!f) { printf("Erro ao abrir %s\n", path); return 1; }
    fseek(f, 0, SEEK_END);
    long sizef = ftell(f);
    rewind(f);
    char *buffer = malloc(sizef + 1);
    fread(buffer, 1, sizef, f);
    fclose(f);
    buffer[sizef] = '\0';

    int halted = 0, total = 0;
    char *ptr = buffer;
    while ((ptr = strstr(ptr, "\"program\":\"")) != NULL) {
        ptr += strlen("\"program\":\"");
        char prog[32];
        sscanf(ptr, "%[^\"]", prog);
        if (simulate_program(prog)) halted++;
        total++;
    }
    printf("%d de %d programas halting (%s)\n", halted, total, size);
    free(buffer);
    return 0;
}
