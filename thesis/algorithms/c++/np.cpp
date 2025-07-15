#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <cmath>
#include <map>

bool evaluate_clause(const std::vector<int>& clause, const std::map<int, bool>& assignment) {
    for (int lit : clause) {
        int var = std::abs(lit);
        bool val = assignment.at(var);
        if ((lit > 0 && val) || (lit < 0 && !val)) return true;
    }
    return false;
}

bool is_satisfiable(const std::vector<std::vector<int>>& clauses, int num_vars) {
    int total = 1 << num_vars;
    for (int mask = 0; mask < total; ++mask) {
        std::map<int, bool> assignment;
        for (int i = 0; i < num_vars; ++i)
            assignment[i + 1] = (mask >> i) & 1;

        bool all_true = true;
        for (const auto& clause : clauses) {
            if (!evaluate_clause(clause, assignment)) {
                all_true = false;
                break;
            }
        }
        if (all_true) return true;
    }
    return false;
}

std::vector<std::vector<int>> read_cnf(const std::string& path) {
    std::ifstream file(path);
    std::string line, content;
    while (getline(file, line)) content += line;

    std::vector<std::vector<int>> clauses;
    std::stringstream ss(content);
    std::string token;
    while (getline(ss, token, '[')) {
        size_t end = token.find(']');
        if (end != std::string::npos) {
            std::string clause_str = token.substr(0, end);
            std::stringstream css(clause_str);
            std::string num;
            std::vector<int> clause;
            while (getline(css, num, ',')) {
                if (!num.empty())
                    clause.push_back(std::stoi(num));
            }
            if (!clause.empty())
                clauses.push_back(clause);
        }
    }
    return clauses;
}

int main(int argc, char* argv[]) {
    std::string size = argc > 1 ? argv[1] : "small";
    std::string path = "../data/" + size + "/sat_" + size + ".json";
    auto clauses = read_cnf(path);
    bool sat = is_satisfiable(clauses, 20);
    std::cout << "SAT (" << size << "): " << (sat ? "Satisfatível" : "Insatisfatível") << std::endl;
    return 0;
}
