#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Define a classe pessoa
class Pessoa {
private:
    string nome;
    string cpf;
public:
    // Construtor padrão
    Pessoa() {
        nome = "";
        cpf = "";
    }
    // Construtor com parâmetros
    Pessoa(string n, string c) {
        nome = n;
        cpf = c;
    }
    // Getters
    string getNome() {
        return nome;
    }
    string getCpf() {
        return cpf;
    }
};

// Define a classe ContaBancaria
class ContaBancaria {
private:
    int numero;
    double saldo;
    Pessoa titular;
    vector<string> historicoTransacoes;
public:
    // Construtor
    ContaBancaria(int n, double s, Pessoa t) {
        numero = n;
        saldo = s;
        titular = t;
    }
    // Getters
    int getNumero() {
        return numero;
    }
    double getSaldo() {
        return saldo;
    }
    Pessoa getTitular() {
        return titular;
    }
    // Métodos de operação
    void deposito(double valor) {
        saldo += valor;
        historicoTransacoes.push_back("Depósito de R$ " + to_string(valor));
    }
    void saque(double valor) {
        if (saldo < valor) {
            cout << "Saldo insuficiente!" << endl;
        }
        else {
            saldo -= valor;
            historicoTransacoes.push_back("Saque de R$ " + to_string(valor));
        }
    }
    vector<string> getHistoricoTransacoes() {
        return historicoTransacoes;
    }
};

// Define a classe Transacao
class Transacao {
private:
    int id;
    double valor;
    string descricao;
public:
    // Construtor
    Transacao(int i, double v, string d) {
        id = i;
        valor = v;
        descricao = d;
    }
    // Getters
    int getId() {
        return id;
    }
    double getValor() {
        return valor;
    }
    string getDescricao() {
        return descricao;
    }
};

int main() {
    // Cria um objeto da classe Pessoa
    Pessoa pessoa1("João da Silva", "123.456.789-00");
    // Cria um objeto da classe ContaBancaria
    ContaBancaria conta1(12345, 1000, pessoa1);
    // Realiza um depósito e um saque na conta
    conta1.deposito(600);
    conta1.saque(500);
    // Imprime o saldo atualizado da conta
    cout << "Saldo atualizado: R$ " << conta1.getSaldo() << endl;
    // Imprime o histórico de transações da conta
    vector<string> historico = conta1.getHistoricoTransacoes();
    for (int i = 0; i < historico.size(); i++) {
        cout << historico[i] << endl;
    }  
    // Cria um objeto da classe Transacao
    Transacao transacao1(1, 50, "Compra em supermercado");
    // Imprime os dados da transação
    cout << "Transação " << transacao1.getId() << ": " << transacao1.getDescricao() << " - R$ " << transacao1.getValor() << endl;
    
    return 0;
}