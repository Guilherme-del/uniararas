using System;
using System.IO;
using System.Collections.Generic;

class SATSolver
{
    static bool EvaluateClause(int[] clause, Dictionary<int, bool> assignment)
    {
        foreach (int lit in clause)
        {
            int var = Math.Abs(lit);
            bool value = assignment.ContainsKey(var) && assignment[var];
            if ((lit > 0 && value) || (lit < 0 && !value)) return true;
        }
        return false;
    }

    static bool IsSatisfiable(List<int[]> cnf, int numVars)
    {
        int totalAssignments = 1 << numVars;
        for (int mask = 0; mask < totalAssignments; mask++)
        {
            var assignment = new Dictionary<int, bool>();
            for (int i = 0; i < numVars; i++)
                assignment[i + 1] = (mask & (1 << i)) != 0;

            bool allSatisfied = true;
            foreach (var clause in cnf)
            {
                if (!EvaluateClause(clause, assignment))
                {
                    allSatisfied = false;
                    break;
                }
            }

            if (allSatisfied) return true;
        }
        return false;
    }

    static List<int[]> ParseJsonManualmente(string content)
    {
        var clauses = new List<int[]>();
        content = content.Replace("[[", "").Replace("]]", "");
        string[] rawClauses = content.Split(new[] { "],[" }, StringSplitOptions.RemoveEmptyEntries);

        foreach (string raw in rawClauses)
        {
            string[] parts = raw.Split(',');
            if (parts.Length != 3) continue; // cláusula inválida

            int[] clause = new int[3];
            for (int i = 0; i < 3; i++)
            {
                if (int.TryParse(parts[i].Trim(), out int value))
                    clause[i] = value;
                else
                    throw new FormatException($"Valor inválido: '{parts[i]}'");
            }
            clauses.Add(clause);
        }

        return clauses;
    }

    static void Main(string[] args)
    {
        string size = args.Length > 0 ? args[0] : "small";
        string path = $"datasets/{size}/sat.json";

        if (!File.Exists(path))
        {
            Console.WriteLine("Arquivo não encontrado.");
            return;
        }

        string content = File.ReadAllText(path);
        List<int[]> cnf = ParseJsonManualmente(content);

        bool satisfiable = IsSatisfiable(cnf, 20);
        Console.WriteLine($"SAT ({size}): {(satisfiable ? "Satisfatível" : "Insatisfatível")}");
    }
}
