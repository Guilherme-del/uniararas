/**************************

                              7. Crie um programa capaz de ler o nome do aluno, o RA, o curso e a disciplina que ele
mais gosta até o momento. Depois, leia a média da disciplina e imprima tudo no console.
Empregue a formatação que quiser e utilize um ou mais comandos print.


***************************/

#include <iostream>

using namespace std;

int main()
{
   int ra;
   string curso;
   string nome;
   string disc;
   int media;
    
   cout << "Digite Seu nome: ";
   cin >> nome;
   
   cout << "Digite seu ra: ";
   cin >> ra;
   
   cout << "Digite seu cuso: ";
   cin >> curso;
   
   cout << "Digite sua disciplina favorita: ";
   cin >> disc;
   
   cout << "Digite sua média ";
   cin >> media;
   
   cout << "Nome: " << nome << " RA: " << ra << " Curso " << curso << " Disciplina favorita " << disc << " Média " << media;
    return 0;
}