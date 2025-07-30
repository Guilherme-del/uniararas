#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int simulate_program(const char *code) {
    return strstr(code, "HALT") != NULL;
}

char *skip_whitespace(char *s) {
    while (isspace(*s)) s++;
    return s;
}

int main(int argc, char *argv[]) {
    const char *size = (argc > 1) ? argv[1] : "small";
    char path[128];
    snprintf(path, sizeof(path), "datasets/%s/halting.json", size);
    FILE *f = fopen(path, "r");
    if (!f) {
        printf("Erro ao abrir %s\n", path);
        return 1;
    }

    fseek(f, 0, SEEK_END);
    long sizef = ftell(f);
    rewind(f);

    char *buffer = malloc(sizef + 1);
    fread(buffer, 1, sizef, f);
    fclose(f);
    buffer[sizef] = '\0';

    int halted = 0, total = 0;
    char *p = buffer;

    while ((p = strstr(p, "\"program\"")) != NULL) {
        p = strstr(p, ":");
        if (!p) break;
        p++;
        p = skip_whitespace(p);
        if (*p == '\"') {
            p++;
            char prog[128];
            int i = 0;
            while (*p && *p != '\"' && i < 127) {
                prog[i++] = *p++;
            }
            prog[i] = '\0';

            if (simulate_program(prog)) halted++;
            total++;
        }
    }

    printf("%d de %d programas halting (%s)\n", halted, total, size);
    free(buffer);
    return 0;
}
