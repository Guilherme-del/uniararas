/*
Aula 02 - implementacao basica de classe

visual paradigm

create new -> diagram -> class diagram
*/
#include<iostream>
#include<string>

using namespace std;

class Pessoa{
//atributos
private: //operador de encapsulamento
  int idade;
  string cpf;
  float altura;

public:
  Pessoa();//construtor padrão
  Pessoa(int idade);//construtor parametrico
  Pessoa(float altura);//construtor parametrico
  Pessoa(float altura, string cpf);
  // funções
  void setIdade(int idade);
  void setCpf(string cpf);
  void setAltura(float altura);
  int getIdade();
  string getCpf();
  float getAltura();
};

Pessoa::Pessoa(){
  this->idade = 0;
  this->cpf = " ";
  this->altura = 0.0;
}

Pessoa::Pessoa(int idade){
  this->idade = idade;
  this->cpf = " ";
  this->altura = 0.0;
}

Pessoa::Pessoa(float altura){
  this->idade = 0;
  this->cpf = " ";
  this->altura = altura;
}

Pessoa::Pessoa(float altura, string cpf){
  this->idade = 0;
  this->cpf = cpf;
  this->altura = altura;
}

int Pessoa::getIdade(){
  return this->idade;
}

string Pessoa::getCpf(){
  return this->cpf;
}

 float Pessoa::getAltura(){
    return this->altura;
 }

void Pessoa::setCpf(string cpf){
    //if(validate(cpf)){
  this->cpf = cpf;
}

void Pessoa::setAltura(float altura){
  this->altura = altura;
}

void Pessoa::setIdade(int idade){
  this->idade = idade;
}

int main(){
  Pessoa P1;
  Pessoa P2(15);

  P1.setCpf("11122233344");
  P1.setIdade(30);
  P1.setAltura(1.8);
  P2.setCpf("23456789011");
  P2.setAltura(1.7);
  cout<<" A idade da pessoa P1 e:"<<P1.getIdade()<<endl;
  cout<<" O cpf de P1 e:"<<P1.getCpf()<<endl;
  cout<<" A altura da pessoa P1 e:"<<P1.getAltura()<<endl;
  cout<<" A idade da pessoa P2 e:"<<P2.getIdade()<<endl;
  cout<<" O cpf de P2 e:"<<P2.getCpf()<<endl;
  cout<<" A altura da pessoa P2 e:"<<P2.getAltura()<<endl;

  return 0;
}
