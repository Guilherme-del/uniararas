import java.io.*;
import java.util.*;
import java.nio.file.Files;
import java.nio.file.Paths;

class Item {
    int weight;
    int value;
    Item(int weight, int value) {
        this.weight = weight;
        this.value = value;
    }
}

public class NpCompleto {
    public static int knapsack(List<Item> items, int capacity) {
        int[] dp = new int[capacity + 1];
        for (Item item : items) {
            for (int w = capacity; w >= item.weight; w--) {
                dp[w] = Math.max(dp[w], dp[w - item.weight] + item.value);
            }
        }
        return dp[capacity];
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
        System.out.println("Valor máximo para " + items.size() + " itens (" + size + "): " + result);
    }
}
