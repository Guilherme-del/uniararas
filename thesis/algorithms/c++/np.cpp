#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <sstream>
#include <cstring>

#define MAX_NUMBERS 100000

void fatorar(long long n) {
    if (n < 2) return;
    for (long long i = 2; i <= std::sqrt(n); i++) {
        while (n % i == 0) {
            n /= i;
        }
    }
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Uso: " << argv[0] << " <small|medium|large>\n";
        return 1;
    }

    std::string tamanho = argv[1];
    std::string caminho = "datasets/" + tamanho + "/factoring.json";

    std::ifstream file(caminho);
    if (!file.is_open()) {
        std::cerr << "Erro ao abrir o arquivo: " << caminho << "\n";
        return 1;
    }

    std::stringstream buffer;
    buffer << file.rdbuf();
    std::string json = buffer.str();

    // Remove colchetes e espaços
    size_t start = json.find('[');
    size_t end = json.find(']');
    if (start == std::string::npos || end == std::string::npos || end <= start) {
        std::cerr << "Formato de JSON inválido.\n";
        return 1;
    }

    std::string lista = json.substr(start + 1, end - start - 1);
    std::stringstream ss(lista);
    std::string token;
    std::vector<long long> numeros;

    while (getline(ss, token, ',')) {
        try {
            long long num = std::stoll(token);
            numeros.push_back(num);
        } catch (...) {
            continue;
        }
    }

    for (long long n : numeros) {
        fatorar(n);
    }

    std::cout << "Fatorados " << numeros.size() << " números do dataset " << tamanho << ".\n";
    return 0;
}
