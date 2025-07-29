#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <string>

void merge(std::vector<int>& arr, int l, int m, int r) {
    std::vector<int> left(arr.begin() + l, arr.begin() + m + 1);
    std::vector<int> right(arr.begin() + m + 1, arr.begin() + r + 1);
    int i = 0, j = 0, k = l;

    while (i < left.size() && j < right.size())
        arr[k++] = (left[i] <= right[j]) ? left[i++] : right[j++];

    while (i < left.size()) arr[k++] = left[i++];
    while (j < right.size()) arr[k++] = right[j++];
}

void mergeSort(std::vector<int>& arr, int l, int r) {
    if (l < r) {
        int m = (l + r) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

std::vector<int> read_json_array(const std::string& path) {
    std::ifstream file(path);
    std::string line, content;
    while (getline(file, line)) content += line;
    std::vector<int> result;
    std::stringstream ss(content);
    std::string token;
    while (getline(ss, token, ',')) {
        token.erase(remove(token.begin(), token.end(), '['), token.end());
        token.erase(remove(token.begin(), token.end(), ']'), token.end());
        result.push_back(std::stoi(token));
    }
    return result;
}

int main(int argc, char* argv[]) {
    std::string size = argc > 1 ? argv[1] : "small";
    std::string path = "../datasets/" + size + "/merge_sort_" + size + ".json";
    std::vector<int> data = read_json_array(path);
    mergeSort(data, 0, data.size() - 1);
    std::cout << "Ordenado " << data.size() << " elementos (" << size << ")" << std::endl;
    return 0;
}
