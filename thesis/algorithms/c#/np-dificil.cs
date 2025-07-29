using System;
using System.IO;
using System.Text.Json;
using System.Collections.Generic;

class HaltingSimulator {
    static bool Simulate(string code) {
        return code.Trim().ToUpper() == "HALT";
    }

    static void Main(string[] args) {
        string size = args.Length > 0 ? args[0] : "small";
        string path = $"../datasets/{size}/halting_{size}.json";

        if (!File.Exists(path)) {
            Console.WriteLine("Arquivo não encontrado.");
            return;
        }

        var options = new JsonSerializerOptions { PropertyNameCaseInsensitive = true };
        List<Dictionary<string, string>> programs = JsonSerializer.Deserialize<List<Dictionary<string, string>>>(File.ReadAllText(path), options);

        int halted = 0;
        foreach (var p in programs) {
            if (p.ContainsKey("program") && Simulate(p["program"]))
                halted++;
        }

        Console.WriteLine($"{halted} de {programs.Count} programas halting ({size})");
    }
}
