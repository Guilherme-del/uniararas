#ifndef ELEVADOR_H
#define ELEVADOR_H

class Elevador {
private:
    int andarAtual;
    int totalAndares;
    int capacidade;
    int pessoasPresentes;

public:
    Elevador(); // Construtor padrão
    Elevador(int capacidade, int totalAndares); // Construtor com parâmetros

    void inicializa(); // Inicializa o elevador
    void entra(); // Acrescenta uma pessoa no elevador
    void sai(); // Remove uma pessoa do elevador
    void sobe(); // Sobe um andar
    void desce(); // Desce um andar

    // Métodos para obter os dados armazenados
    int getAndarAtual() const;
    int getTotalAndares() const;
    int getCapacidade() const;
    int getPessoasPresentes() const;
};

#endif // ELEVADOR_H
