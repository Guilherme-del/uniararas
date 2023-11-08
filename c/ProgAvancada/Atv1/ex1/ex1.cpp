/*
1. Faça um programa capaz de realizar a leitura do seu nome completo e seu curso.
Imprima no console os respectivos inputs
 */

#include <iostream>
using namespace std;

int main()
{
    string nomeAluno;
    string nomeCurso;

    cout << "Qual seu nome ? " << endl;
    cin >> nomeAluno;
    cout << "Qual seu curso ?" << endl;
    cin >> nomeCurso;
    cout << "Ola, " << nomeAluno << " seu curso: " << nomeCurso;

    return 0;
}
