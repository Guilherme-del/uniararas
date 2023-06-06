// PONTEIRO PARA STRUCT

#include <iostream>
using namespace std;

struct alunoFHO
{
  int raAluno;
  float notaAluno;
}

int
main()
{
  alunoFHO cleberMoreno; // variavel dso tipo aluno;
  alunoFHO *ponteiroPa;  // ponteiro para a struct;

  ponteiroPa = &cleberMoreno; // ponteiro "PA" aponta para a variavel cleberMoreno;

  //Alterações indiretas de uma struct.
  ponteiroPa->raAluno = 123;   // o campo raAluno da scruct apontada por ponteiroPa será alterado.
  ponteiroPa->notaAluno = 9.3; // o campo notaAluno da scruct apontada por ponteiroPa será alterado.

}