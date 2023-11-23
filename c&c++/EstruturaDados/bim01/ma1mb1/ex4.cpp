/*
4- Apresente as implementações de fila por vetores, verificando a ocorrência de erros de
estouro (UNDERFLOW / OVERFLOW).
*/

#include <iostream>
using namespace std;

struct fila
{
  int v[10];  
  int inicio; // ponteiro inicial da fila
  int fim;    // ponteiro final da fila
};

void enqueu(fila & f, int novoElemento)
{
  f.v[f.fim] = novoElemento;
  if (f.fim <= 10)
  {
    f.fim++;
  }
  else if (f.inicio > 0)
  {
    cout << "Elemento atingiu o valor maximo"; // verifica o estouro final OVERFLOW
    f.fim = 0;
  }
}

int first(fila f) //pega o primeiro elemento
{ // não passa por referencia pois não altera a estrutura
  return f.v[f.inicio];
}

void dequeue(fila &f) // tira um elemento da fila
{
  if (f.inicio++ < 10) // verifica Overflow
  {
    f.inicio++;
  }
  else
  {
    f.inicio = 0;
  }
}

bool estaVazia(fila f) // verifica se a fila esta vazia UNDERFLOW
{
  return f.inicio == f.fim;
}

bool estaCheia(fila f) // verifica se esta cheia 
{
  return f.inicio == 0 && f.fim == 9 || f.fim++ == f.inicio;
}

int main()
{
  fila fNumeros;
  fNumeros.inicio = fNumeros.fim = 0;

  enqueu(fNumeros, 3);
  enqueu(fNumeros, 5);
  enqueu(fNumeros, 9);
  enqueu(fNumeros, 2);
  dequeue(fNumeros);

  cout << first(fNumeros);
}