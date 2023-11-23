/*
Aula de Polimorfismo
Capitulo 13 do livro do Deitel
*/
#include<iostream>
using namespace std;

class Veiculo{
private:
    int numeroRodas;
    string cor;
    float tanque;

public:
    Veiculo(int joao, string roberval, float tanque);
    int getNumeroRodas();
    string getCor();
    float getTanque();
    void setNumeroRodas(int joao);
    void setCor(string roberval);
    void setTanque(float tanque);
    //colocar os métodos virtuais agrupados
    virtual void consumo()=0;
    virtual void acelerar()=0;
};

Veiculo::Veiculo(int joao, string roberval, float tanque){
    this->numeroRodas = joao;
    this->cor = roberval;
    this->tanque = tanque;
}

int Veiculo::getNumeroRodas(){
    return this->numeroRodas;
}

string Veiculo::getCor(){
    return this->cor;
}

float Veiculo::getTanque(){
    return this->tanque;
}

void Veiculo::setNumeroRodas(int joao){
    this->numeroRodas = joao;
}

void Veiculo::setCor(string roberval){
    this->cor = roberval;
}

void Veiculo::setTanque(float tanque){
    this->tanque = tanque;
}

//polimorfimo!!!!!!!!!!!!
class Carro:public Veiculo{
public:
    Carro(int joao, string roberval, float tanque);
    void consumo();
    void acelerar();
};

Carro::Carro(int joao, string roberval, float tanque):Veiculo(joao,roberval,tanque){

}

void Carro::consumo(){
    cout<<"Este carro consome 10 km/l"<<endl;
}

void Carro::acelerar(){
    cout<<"Voce pode acelerar ate que o tanque de "<<this->getTanque()<<" litros acabe"<<endl;
}

class Caminhao:public Veiculo{
public:
    Caminhao(int joao, string roberval, float tanque);
    void consumo();
    void acelerar();
};

Caminhao::Caminhao(int joao, string roberval, float tanque):Veiculo(joao,roberval,tanque){

}

void Caminhao::consumo(){
    cout<<"Este caminhao consome 7 km/l"<<endl;
}

void Caminhao::acelerar(){
    cout<<"Voce pode acelerar ate que o tanque de "<<this->getTanque()<<" litros acabe"<<endl;
}

int main(){
    Carro C1(4,"azul",50);

    C1.consumo();
    C1.acelerar();

    Caminhao Cam1(8,"verde",200);

    Cam1.consumo();
    Cam1.acelerar();

    return 0;

}