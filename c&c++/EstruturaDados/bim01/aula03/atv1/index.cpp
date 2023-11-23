//Exercicio de pilha
#include <iostream>
using namespace std;

struct pilha
{
  int v[10];
  int topo;
};

bool estaVazia(pilha &p)
{
  return p.topo < 0;
}

bool estaCheia(pilha &p)
{
  return p.topo >= 9;
}

void push(pilha &p, int novoElemento)
{
  if (estaCheia(p))
  {
    cout << "lista já atingiu o topo" << endl;
  }
  else
  {
    p.topo++;
    p.v[p.topo] = novoElemento;
  }
}

int top(pilha & p)
{
  if (estaVazia(p))
  {
    cout << "Não há topo em pilha vazia " << endl;
    return -999;
  }
  else
  {
    return p.v[p.topo];
  }
}

void pop(pilha &p) // e comercial esta usando o valor ja declarado. POR REFERENCIA
{
  if (estaVazia(p))
  {
    cout << "A pilha esta vazia" << endl;
  }
  else
  {
    p.topo--;
  }
}

int main()
{
  pilha minhaPilha;
  minhaPilha.topo = -1;

  if (estaVazia(minhaPilha))
  {
    cout << "A pilha esta vazia" << endl;
  }
  push(minhaPilha, 4);

  cout << minhaPilha.topo << endl;
  cout << top(minhaPilha) << endl;

  pop(minhaPilha);
  cout << top(minhaPilha) << endl;

  for (int i = 0; i < 15; i++)
  {
    push(minhaPilha,i)
  }
  
}
