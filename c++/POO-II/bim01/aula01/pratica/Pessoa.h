/*O #ifndef Garante que não haverá duplicidade na hora de "usar" o arquivo ao longo da compilação/execução. 
  Evita duplicar tipos, e demais estruturas presentes.
  É UMA BOA PRÁTICA NA PROGRAMAÇÃO OOP EM C++.
*/
#ifndef _PESSOA_H_
#define _PESSOA_H_

#include <iostream>

using namespace std;

class Pessoa
{
private:
    string Nome;
    int Idade;
    float Altura;

public:
    Pessoa();
    void setNome();
    string getNome();
    void setIdade();
    int getIdade();
    void setAltura();
    float getAltura();
    void visualizarDados();
};

#endif