using System;
using System.IO;
using System.Collections.Generic;

class Program {
    static bool Simulate(string code) {
        return code.Trim().ToUpper() == "HALT";
    }

    static void Main(string[] args) {
        string size = args.Length > 0 ? args[0] : "small";
        string path = $"datasets/{size}/halting.json";

        if (!File.Exists(path)) {
            Console.WriteLine("Arquivo não encontrado.");
            return;
        }

        string json = File.ReadAllText(path);
        int halted = 0, total = 0;

        int idx = 0;
        while ((idx = json.IndexOf("\"program\"", idx)) != -1) {
            int start = json.IndexOf("\"", idx + 9);
            int end = json.IndexOf("\"", start + 1);
            if (start != -1 && end != -1) {
                string code = json.Substring(start + 1, end - start - 1);
                if (Simulate(code)) halted++;
                total++;
                idx = end;
            } else {
                break;
            }
        }

        Console.WriteLine($"{halted} de {total} programas halting ({size})");
    }
}
