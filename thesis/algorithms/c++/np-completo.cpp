#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>

struct Item {
    int weight;
    int value;
};

// Algoritmo guloso: ordena por valor/peso e inclui até bater o limite
int knapsack(const std::vector<Item>& items, int capacity) {
    std::vector<Item> sorted = items;

    std::sort(sorted.begin(), sorted.end(), [](const Item& a, const Item& b) {
        double ra = (double)a.value / a.weight;
        double rb = (double)b.value / b.weight;
        return ra > rb;
    });

    int totalValue = 0;
    int currentWeight = 0;

    for (const auto& item : sorted) {
        if (currentWeight + item.weight <= capacity) {
            currentWeight += item.weight;
            totalValue += item.value;
        }
    }

    return totalValue;
}

// Leitura simplificada do JSON
std::pair<std::vector<Item>, int> read_knapsack(const std::string& path) {
    std::ifstream file(path);
    std::string line, content;
    while (getline(file, line)) content += line;

    int capacity = std::stoi(content.substr(content.find("\"capacity\":") + 11));
    std::vector<Item> items;
    std::stringstream ss(content);
    std::string token;
    while (getline(ss, token, '{')) {
        if (token.find("weight") != std::string::npos) {
            int weight = std::stoi(token.substr(token.find("weight") + 8));
            int value = std::stoi(token.substr(token.find("value") + 7));
            items.push_back({weight, value});
        }
    }
    return {items, capacity};
}

int main(int argc, char* argv[]) {
    std::string size = argc > 1 ? argv[1] : "small";
    std::string path = "datasets/" + size + "/knapsack.json";

    auto [items, capacity] = read_knapsack(path);

    int result = knapsack(items, capacity);

    std::cout << "Valor aproximado (greedy) para " << items.size()
              << " itens (capacidade " << capacity << ", " << size << "): "
              << result << std::endl;

    return 0;
}
