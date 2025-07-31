#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

#define MAX_VARS 1000

bool evaluate_clause(int *clause, int assignment[]) {
    for (int i = 0; i < 3; i++) {
        int lit = clause[i];
        int var = abs(lit);
        bool val = assignment[var];
        if ((lit > 0 && val) || (lit < 0 && !val)) return true;
    }
    return false;
}

// Força bruta para pequenas instâncias!
bool is_satisfiable(int **clauses, int num_clauses, int num_vars) {
    if(num_vars > 22) return -1; // Sinaliza para não tentar

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

    int **clauses = malloc(sizeof(int*) * 200000);
    int count = 0;
    int max_var = 0;

    char *tok = strtok(buffer, "[\n,]");
    while (tok) {
        int *clause = malloc(3 * sizeof(int));

        clause[0] = atoi(tok);
        if (abs(clause[0]) > max_var) max_var = abs(clause[0]);
        tok = strtok(NULL, "[\n,]");
        if (!tok) { free(clause); break; }

        clause[1] = atoi(tok);
        if (abs(clause[1]) > max_var) max_var = abs(clause[1]);
        tok = strtok(NULL, "[\n,]");
        if (!tok) { free(clause); break; }

        clause[2] = atoi(tok);
        if (abs(clause[2]) > max_var) max_var = abs(clause[2]);
        clauses[count++] = clause;

        tok = strtok(NULL, "[\n,]");
    }

    int result = is_satisfiable(clauses, count, max_var);
    if (result == -1) {
        printf("SAT (%s): Instância com %d variáveis é grande demais para força bruta em C. Use MiniSat ou outro solver real!\n", size, max_var);
    } else if (result) {
        printf("SAT (%s): Satisfatível\n", size);
    } else {
        printf("SAT (%s): Insatisfatível\n", size);
    }

    for (int i = 0; i < count; i++) free(clauses[i]);
    free(clauses);
    free(buffer);
    return 0;
}
