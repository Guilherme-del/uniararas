/*
4) implemente uma classe pilha utilizando vector. 
Voce deve criar a pilha vazia inserir elementos na pilha (push) e remover elementos da pilha (pop). 
Tambem deve retornar o numero de elementos. Lembre-se que a classe vector possui métodos prontos , porém o protocolo da pilha deve ser respeitado na implementação.
*/
class Pilha {
    private:
        int *pilha;
        int tamanho;
        int topo;
    public:
        Pilha(int tamanho);
        void push(int elemento);
        int pop();
        int size();
};

Pilha::Pilha(int tamanho) {
    this->tamanho = tamanho;
    this->topo = -1;
    this->pilha = new int[tamanho];
}

void Pilha::push(int elemento) {
    if(this->topo < this->tamanho - 1) {
        this->topo++;
        this->pilha[this->topo] = elemento;
    }
}

int Pilha::pop() {
    int elemento = this->pilha[this->topo];
    this->topo--;
    return elemento;
}

int Pilha::size() {
    return this->topo + 1;
}

