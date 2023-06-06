// Exercicio de fila
#include <iostream>

using namespace std;

struct fila
{
  int v[10];
  int inicio; // ponteiro inicial da fila
  int fim;    // ponteiro final da fila
};

void enqueu(fila &f, int novoElemento)
{
  f.v[f.fim] = novoElemento;
  if (f.fim <= 10)
  {
    f.fim++;
  }
  else if (f.inicio > 0)
  {
    cout << "Elemento atingiu o valor maximo";
    f.fim = 0;
  }
}

int first(fila f)
{ // não passa por referencia pois não altera a estrutura
  return f.v[f.inicio];
}

void dequeue(fila &f)
{
  if (f.inicio++ < 10)
  {
    f.inicio++;
  }
  else
  {
    f.inicio = 0;
  }
}
// metodo não canonico
void imprimeFila(fila f)
{
  for (int i = f.inicio; i < f.fim; i++)
  {
    cout << f.v[i] << " ";
  }
  cout << endl;
}

bool estaVazia(fila f)
{
  return f.inicio == f.fim;
}

bool estaCheia(fila f)
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
  imprimeFila(fNumeros);
  dequeue(fNumeros);
  imprimeFila(fNumeros);

  cout << first(fNumeros);
}
