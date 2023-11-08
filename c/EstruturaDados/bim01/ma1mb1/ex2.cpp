/*
2- Faça um programa que apresente duas filas de inteiros, no programa haverá um menu que
possibilita o usuário realizar as operações em cada fila e inclusive transferir dados de uma fila
para outra.
*/

#include <iostream>
using namespace std;

struct fila
{
  int v[10];
  int inicio;
  int fim;
};

// Inserção
void enqueue(fila &f, int novoElemento)
{
  f.v[f.fim] = novoElemento;
  f.fim++;
}

// Acesso
int first(fila f)
{
  return f.v[f.inicio];
}

// Desenfileirar
void dequeue(fila &f)
{
  f.inicio++;
}

// verifica o tamanho da fila
void sizeOf(fila f1, fila f2)
{
  cout << "primeira fila tem tamanho" << f1.fim << endl;
  cout << "segunda fila tem tamanho" << f2.fim << endl;
  if (f1.fim == f2.fim)
  {
    cout << "são do mesmo tamanho" << endl;
  }
  else
  {
    cout << "Não são do mesmo atmanho" << endl;
  }
}

// copiar uma fila para outra
void realloc(fila f1, fila f2)
{
  f2.v[f2.fim] = f1.v[f1.inicio];
  f2.fim++;
  f1.inicio++;
}

int main()
{
  fila fInicial, fSecundaria;
  int filaASerUtilizada, opcaoEscolhidaFila, numeroAInserir;
  cout << "Qual a fila deseja usar: digite o numero : " << endl
       << "[1] para fila 1:"
       << "[2] para fila 2" << endl;
  cin >> filaASerUtilizada;

  if (filaASerUtilizada == 1)
  {
    cout << "Oque deseja fazer com a fila" << endl
         << "[1]:Adicionar dados. " << endl
         << "[2]:Retirar um dado. " << endl
         << "[3]:Transferir para outra fila.";
    cin >> opcaoEscolhidaFila;
    if (opcaoEscolhidaFila == 1)
    {
      cout << "Qual numero deseja inserir ?" << endl;
      cin >> numeroAInserir;
      enqueue(fInicial, numeroAInserir);
    }
    else if (opcaoEscolhidaFila == 2)
    {
      dequeue(fInicial);
    }
    else if (opcaoEscolhidaFila == 3)
    {
      realloc(fInicial,fSecundaria);
    }
    else
    {
      cout << "Opcao inválida";
    }
  }
  else if (filaASerUtilizada == 2)
  {
    cout << "Oque deseja fazer com a fila" << endl
         << "[1]: Adicionar dados. " << endl
         << "[2]:Retirar um dado. " << endl
         << "[3]: Transferir para outra fila.";
    cin >> opcaoEscolhidaFila;

    if (opcaoEscolhidaFila == 1)
    {
      cout << "Qual numero deseja inserir ?" << endl;
      cin >> numeroAInserir;
      enqueue(fSecundaria, numeroAInserir);
    }
    else if (opcaoEscolhidaFila == 2)
    {
      dequeue(fSecundaria);
    }
    else if (opcaoEscolhidaFila == 3)
    {
       realloc(fSecundaria,fInicial);
    }
  }
  else
  {
    cout << "Opcao Invalida";
  }
}