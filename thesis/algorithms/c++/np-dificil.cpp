#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

int simulateProgram(const std::string& code) {
    return code.find("HALT") != std::string::npos;
}

int main(int argc, char* argv[]) {
    std::string size = argc > 1 ? argv[1] : "small";
    std::string path = "datasets/" + size + "/halting.json";

    std::ifstream file(path);
    if (!file) {
        std::cerr << "Erro ao abrir " << path << std::endl;
        return 1;
    }

    std::stringstream buffer;
    buffer << file.rdbuf();
    std::string content = buffer.str();

    int halted = 0, total = 0;
    std::size_t pos = 0;

    while ((pos = content.find("\"program\"", pos)) != std::string::npos) {
        pos = content.find(":", pos);
        if (pos == std::string::npos) break;
        pos = content.find("\"", pos);
        if (pos == std::string::npos) break;
        std::size_t end = content.find("\"", pos + 1);
        if (end == std::string::npos) break;
        std::string program = content.substr(pos + 1, end - pos - 1);
        if (simulateProgram(program)) halted++;
        total++;
        pos = end + 1;
    }

    std::cout << halted << " de " << total << " programas halting (" << size << ")" << std::endl;
    return 0;
}
