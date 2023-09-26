#include <iostream>
#include "Elevador.h"

int main() {
    // Crie um objeto Elevador com capacidade para 10 pessoas e 5 andares
    Elevador elevador(10, 5);

    // Inicialize o elevador
    elevador.inicializa();

    // Teste os métodos
    std::cout << "Andar atual: " << elevador.getAndarAtual() << std::endl;
    std::cout << "Total de andares: " << elevador.getTotalAndares() << std::endl;
    std::cout << "Capacidade do elevador: " << elevador.getCapacidade() << std::endl;
    std::cout << "Pessoas presentes: " << elevador.getPessoasPresentes() << std::endl;

    elevador.entra();
    elevador.entra();
    elevador.entra();

    std::cout << "Pessoas presentes: " << elevador.getPessoasPresentes() << std::endl;

    elevador.sobe();
    elevador.sobe();

    std::cout << "Andar atual: " << elevador.getAndarAtual() << std::endl;

    elevador.desce();

    std::cout << "Andar atual: " << elevador.getAndarAtual() << std::endl;

    elevador.sai();
    elevador.sai();

    std::cout << "Pessoas presentes: " << elevador.getPessoasPresentes() << std::endl;

    return 0;
}
