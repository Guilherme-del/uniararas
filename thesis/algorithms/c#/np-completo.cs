using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;

class KnapsackItem {
    public int weight { get; set; }
    public int value { get; set; }
}

class KnapsackData {
    public int capacity { get; set; }
    public List<KnapsackItem> items { get; set; }
}

class KnapsackProgram {
    static int Knapsack(List<KnapsackItem> items, int capacity) {
        int[] dp = new int[capacity + 1];
        foreach (var item in items) {
            for (int w = capacity; w >= item.weight; w--) {
                dp[w] = Math.Max(dp[w], dp[w - item.weight] + item.value);
            }
        }
        return dp[capacity];
    }

    static void Main(string[] args) {
        string size = args.Length > 0 ? args[0] : "small";
        string path = $"datasets/{size}/knapsack.json";

        if (!File.Exists(path)) {
            Console.WriteLine("Arquivo não encontrado.");
            return;
        }

        KnapsackData data = JsonSerializer.Deserialize<KnapsackData>(File.ReadAllText(path));
        int result = Knapsack(data.items, data.capacity);
        Console.WriteLine($"Valor máximo para {data.items.Count} itens ({size}): {result}");
    }
}
