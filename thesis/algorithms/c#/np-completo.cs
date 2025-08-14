using System;
using System.Collections.Generic;
using System.IO;

class KnapsackItem {
    public int weight;
    public int value;
}

class KnapsackProgram {
    // Algoritmo guloso: ordena por valor/peso e adiciona enquanto possível
    static int Knapsack(List<KnapsackItem> items, int capacity) {
        items.Sort((a, b) => {
            double ra = (double)b.value / b.weight;
            double rb = (double)a.value / a.weight;
            return ra.CompareTo(rb);
        });

        int totalValue = 0;
        int currentWeight = 0;

        foreach (var item in items) {
            if (currentWeight + item.weight <= capacity) {
                currentWeight += item.weight;
                totalValue += item.value;
            }
        }

        return totalValue;
    }

    static void Main(string[] args) {
        string size = args.Length > 0 ? args[0] : "small";
        string path = $"datasets/{size}/knapsack.json";

        if (!File.Exists(path)) {
            Console.WriteLine("Arquivo não encontrado.");
            return;
        }

        string json = File.ReadAllText(path);

        // Obter capacidade
        int capacity = 0;
        int capIdx = json.IndexOf("\"capacity\"");
        if (capIdx != -1) {
            int start = json.IndexOf(":", capIdx) + 1;
            int end = json.IndexOf(",", start);
            string capStr = json.Substring(start, end - start).Trim();
            int.TryParse(capStr, out capacity);
        }

        // Obter itens
        List<KnapsackItem> items = new List<KnapsackItem>();
        int idx = 0;
        while ((idx = json.IndexOf("{\"weight\"", idx)) != -1) {
            int wStart = json.IndexOf(":", idx) + 1;
            int wEnd = json.IndexOf(",", wStart);
            string wStr = json.Substring(wStart, wEnd - wStart).Trim();

            int vStart = json.IndexOf(":", wEnd) + 1;
            int vEnd = json.IndexOf("}", vStart);
            string vStr = json.Substring(vStart, vEnd - vStart).Trim();

            if (int.TryParse(wStr, out int weight) && int.TryParse(vStr, out int value)) {
                items.Add(new KnapsackItem { weight = weight, value = value });
            }

            idx = vEnd + 1;
        }

        if (items.Count == 0) {
            Console.WriteLine("Erro ao ler o arquivo ou nenhum item encontrado.");
            return;
        }

        int result = Knapsack(items, capacity);
        Console.WriteLine($"Valor aproximado (greedy) para {items.Count} itens (capacidade {capacity}, {size}): {result}");
    }
}
