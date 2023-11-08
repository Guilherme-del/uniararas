#include "Elevador.h"

Elevador::Elevador() {
    // Construtor padrão, inicializa os valores com 0
    andarAtual = 0;
    totalAndares = 0;
    capacidade = 0;
    pessoasPresentes = 0;
}

Elevador::Elevador(int capacidade, int totalAndares) {
    // Construtor com parâmetros, inicializa com valores fornecidos
    andarAtual = 0;
    this->totalAndares = totalAndares;
    this->capacidade = capacidade;
    pessoasPresentes = 0;
}

void Elevador::inicializa() {
    // Inicializa o elevador no térreo e vazio
    andarAtual = 0;
    pessoasPresentes = 0;
}

void Elevador::entra() {
    // Acrescenta uma pessoa no elevador se houver espaço
    if (pessoasPresentes < capacidade) {
        pessoasPresentes++;
    }
}

void Elevador::sai() {
    // Remove uma pessoa do elevador se houver alguém dentro dele
    if (pessoasPresentes > 0) {
        pessoasPresentes--;
    }
}

void Elevador::sobe() {
    // Sobe um andar se não estiver no último andar
    if (andarAtual < totalAndares) {
        andarAtual++;
    }
}

void Elevador::desce() {
    // Desce um andar se não estiver no térreo
    if (andarAtual > 0) {
        andarAtual--;
    }
}

int Elevador::getAndarAtual() const {
    return andarAtual;
}

int Elevador::getTotalAndares() const {
    return totalAndares;
}

int Elevador::getCapacidade() const {
    return capacidade;
}

int Elevador::getPessoasPresentes() const {
    return pessoasPresentes;
}
