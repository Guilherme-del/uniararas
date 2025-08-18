import java.io.*;
import java.util.*;
import java.nio.file.Files;

class Item {
    int weight;
    int value;
    Item(int weight, int value) {
        this.weight = weight;
        this.value = value;
    }
}

public class NpCompleto {
    // Algoritmo guloso: ordena por valor/peso e adiciona enquanto possível
    public static int knapsack(List<Item> items, int capacity) {
        items.sort((a, b) -> Double.compare(
            (double)b.value / b.weight,
            (double)a.value / a.weight
        ));

        int totalValue = 0;
        int currentWeight = 0;

        for (Item item : items) {
            if (currentWeight + item.weight <= capacity) {
                currentWeight += item.weight;
                totalValue += item.value;
            }
        }

        return totalValue;
    }

    public static List<Item> readItems(String path, int[] capacityOut) throws IOException {
        String content = new String(Files.readAllBytes(new File(path).toPath()));
        int capacity = Integer.parseInt(content.split("\"capacity\":")[1].split(",")[0].trim());
        capacityOut[0] = capacity;
        List<Item> items = new ArrayList<>();
        String[] parts = content.split("\\{");
        for (String part : parts) {
            if (part.contains("weight") && part.contains("value")) {
                int weight = Integer.parseInt(part.split("weight\":")[1].split(",")[0].trim());
                int value = Integer.parseInt(part.split("value\":")[1].split("}")[0].trim());
                items.add(new Item(weight, value));
            }
        }
        return items;
    }

    public static void main(String[] args) throws IOException {
        String size = args.length > 0 ? args[0] : "small";
        String path = "datasets/" + size + "/knapsack.json";
        int[] capacity = new int[1];
        List<Item> items = readItems(path, capacity);
        int result = knapsack(items, capacity[0]);
        System.out.println("Valor aproximado (greedy) para " + items.size() +
                           " itens (capacidade " + capacity[0] + ", " + size + "): " + result);
    }
}
