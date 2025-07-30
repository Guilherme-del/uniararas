using System;
using System.IO;
using System.Text.Json;
using System.Collections.Generic;

class SATSolver {
    static bool EvaluateClause(int[] clause, Dictionary<int, bool> assignment) {
        foreach (int lit in clause) {
            int var = Math.Abs(lit);
            bool value = assignment.ContainsKey(var) && assignment[var];
            if ((lit > 0 && value) || (lit < 0 && !value)) return true;
        }
        return false;
    }

    static bool IsSatisfiable(List<int[]> cnf, int numVars) {
        int totalAssignments = 1 << numVars;
        for (int mask = 0; mask < totalAssignments; mask++) {
            var assignment = new Dictionary<int, bool>();
            for (int i = 0; i < numVars; i++) {
                assignment[i + 1] = (mask & (1 << i)) != 0;
            }

            bool allSatisfied = true;
            foreach (var clause in cnf) {
                if (!EvaluateClause(clause, assignment)) {
                    allSatisfied = false;
                    break;
                }
            }

            if (allSatisfied) return true;
        }
        return false;
    }

    static void Main(string[] args) {
        string size = args.Length > 0 ? args[0] : "small";
        string path = $"datasets/{size}/sat.json";

        if (!File.Exists(path)) {
            Console.WriteLine("Arquivo não encontrado.");
            return;
        }

        var options = new JsonSerializerOptions { PropertyNameCaseInsensitive = true };
        List<int[]> cnf = JsonSerializer.Deserialize<List<int[]>>(File.ReadAllText(path), options);

        int satisfiable = IsSatisfiable(cnf, 20) ? 1 : 0;
        Console.WriteLine($"SAT ({size}): {(satisfiable == 1 ? "Satisfatível" : "Insatisfatível")}");
    }
}
