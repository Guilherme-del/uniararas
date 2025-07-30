#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

#define MAX_VARS 20

bool evaluate_clause(int *clause, int assignment[]) {
    for (int i = 0; i < 3; i++) {
        int lit = clause[i];
        int var = abs(lit);
        bool val = assignment[var];
        if ((lit > 0 && val) || (lit < 0 && !val)) return true;
    }
    return false;
}

bool is_satisfiable(int **clauses, int num_clauses, int num_vars) {
    int total = 1 << num_vars;
    int assignment[MAX_VARS + 1];
    for (int mask = 0; mask < total; mask++) {
        for (int i = 1; i <= num_vars; i++)
            assignment[i] = (mask >> (i - 1)) & 1;
        bool all_true = true;
        for (int i = 0; i < num_clauses; i++) {
            if (!evaluate_clause(clauses[i], assignment)) {
                all_true = false;
                break;
            }
        }
        if (all_true) return true;
    }
    return false;
}

int main(int argc, char *argv[]) {
    const char *size = (argc > 1) ? argv[1] : "small";
    char path[128];
    snprintf(path, sizeof(path), "datasets/%s/sat.json", size);
    FILE *f = fopen(path, "r");
    if (!f) {
        printf("Erro ao abrir arquivo\n");
        return 1;
    }

    fseek(f, 0, SEEK_END);
    long sizef = ftell(f);
    rewind(f);
    char *buffer = malloc(sizef + 1);
    fread(buffer, 1, sizef, f);
    fclose(f);
    buffer[sizef] = '\0';

    int **clauses = malloc(sizeof(int*) * 100000); // suporte até 100k cláusulas
    int count = 0;

    char *tok = strtok(buffer, "[\n,]");
    while (tok) {
        int *clause = malloc(3 * sizeof(int));

        clause[0] = atoi(tok);
        tok = strtok(NULL, "[\n,]");
        if (!tok) { free(clause); break; }

        clause[1] = atoi(tok);
        tok = strtok(NULL, "[\n,]");
        if (!tok) { free(clause); break; }

        clause[2] = atoi(tok);
        clauses[count++] = clause;

        tok = strtok(NULL, "[\n,]");
    }

    int satisfiable = is_satisfiable(clauses, count, MAX_VARS);
    printf("SAT (%s): %s\n", size, satisfiable ? "Satisfatível" : "Insatisfatível");

    for (int i = 0; i < count; i++) free(clauses[i]);
    free(clauses);
    free(buffer);
    return 0;
}
