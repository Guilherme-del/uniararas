/*
3- Uma fila de prioridades é uma estrutura de dados do tipo fila no qual cada novo elemento
inserido é colocado segundo uma ordem crescente ou decrescente.
Exemplo: Suponha que os valores 3, 4, 1, 2, 7, 5 sejam colocado nesta ordem na fila de
prioridades. O estado da fila será:

Após o inserção do elemento de valor 3: 3
Após o inserção do elemento de valor 4: 3, 4
Após o inserção do elemento de valor 1: 1, 3, 4
Após o inserção do elemento de valor 2: 1, 2, 3, 4
Após o inserção do elemento de valor 7: 1, 3, 3, 4, 7
Após o inserção do elemento de valor 5: 1, 2, 3, 4, 5, 7

Implemente uma fila de prioridades em um vetor.
Dica: a implementação aqui é similar à implementação do INSERT das estruturas do tipo lista.
Contudo, a posição não é determinada por um valor passado pela operação de INSERT e sim
pela ordem dos elementos da fila. Basicamente, deve-se percorrer a fila do início para o fim,
ENQUANTO o valor do novo elemento for MAIOR ao valor do i-ésimo elemento da fila. Uma
vez encontrada a posição a ser inserido, deve-se “criar um buraco” no vetor para inserir o novo
elemento.
*/

#include <iostream>
using namespace std;

struct ListaSequencial
{
  int vetor[10];
  int fim;
};

void Insert(ListaSequencial &l, int novoElemento)
{
  if (l.fim == 0)
  {
    l.vetor[l.fim] = novoElemento;
  }
  else
  {
    for (int i = 0; i <= l.fim; i++)
    {
      if (novoElemento < l.vetor[i])
      {
        for (int y = l.fim; y < i; y--)
        {
          l.vetor[y] = l.vetor[y - 1];
        }
        l.vetor[i] = novoElemento;
        break;
      }
      else if (novoElemento > l.vetor[i])
      {
        for (int h = l.fim; h <= i; h--)
        {
          l.vetor[h] = l.vetor[h + 1];
        }
        l.vetor[i] = novoElemento;
        break;
      }
    }
  }
  l.fim++;
}

void printLista(ListaSequencial f)
{
  for (int i = 0; i <= f.fim; i++)
  {
    cout << f.vetor[i] << "";
  }
}

int main()
{
  ListaSequencial ListaTeste;
  ListaTeste.fim = 0;

  Insert(ListaTeste, 3);
  Insert(ListaTeste, 2);
  Insert(ListaTeste, 7);
  printLista(ListaTeste);

  return 0;
}