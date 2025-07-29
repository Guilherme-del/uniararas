#include <iostream>
#include <fstream>
#include <string>

int main(int argc, char* argv[]) {
    std::string size = argc > 1 ? argv[1] : "small";
    std::string path = "../datasets/" + size + "/halting_" + size + ".json";
    std::ifstream file(path);
    std::string line;
    int halted = 0, total = 0;
    while (getline(file, line)) {
        if (line.find("HALT") != std::string::npos) halted++;
        if (line.find("program") != std::string::npos) total++;
    }
    std::cout << halted << " de " << total << " programas halting (" << size << ")" << std::endl;
    return 0;
}
