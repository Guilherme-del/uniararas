#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

struct Item {
    int weight;
    int value;
};

int knapsack(const std::vector<Item>& items, int capacity) {
    std::vector<int> dp(capacity + 1, 0);
    for (const auto& item : items) {
        for (int w = capacity; w >= item.weight; --w) {
            dp[w] = std::max(dp[w], dp[w - item.weight] + item.value);
        }
    }
    return dp[capacity];
}

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
    std::cout << "Valor máximo para " << items.size() << " itens (" << size << "): " << result << std::endl;
    return 0;
}
