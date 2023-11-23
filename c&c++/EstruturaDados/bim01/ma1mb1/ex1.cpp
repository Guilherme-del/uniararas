/*
1- Faça um programa que represente um controle de estoque de produtos. Cada produto
apresenta um preço, quantidade é código. No programa deve existir um menu que permita
cadastrar um novo produto, consultar pelo código, encontrar os produtos que tem quantidade
maior que um valor fornecido na própria opção, apresentar o mais caro. Implemente uma lista
de um tipo struct.
*/
#include <iostream>
using namespace std;

struct lista
{
  int v[10];
  int fim;
};

void insert(lista &l, int pos, int novoElemento)
{
  if (pos != l.fim)
  {
    for (int i = l.fim; i > pos; i--)
    {
      l.v[i] = l.v[i - 1];
    }
  }
  l.v[pos] = novoElemento;
  l.fim++;
}

void remove(lista &l, int pos)
{
  if (pos != l.fim - 1)
  {
    for (int i = pos; i < l.fim - 1; i++)
    {
      l.v[i] = l.v[i + 1];
    }
  }
  l.fim--;
}

int element(lista l, int pos)
{
  return l.v[pos];
}

int pos(lista l, int elemento)
{
  for (int i = 0; i < l.fim; i++)
  {
    if (l.v[i] == elemento)
    {
      return i;
    }
  }
  return -1;
}

void imprime(lista l)
{
  for (int i = 0; i < l.fim; i++)
  {
    cout << l.v[i] << " ";
  }
  cout << endl;
}

void menu()
{
  cout << "Menu" << endl;
  cout << "i: insere na lista" << endl;
  cout << "r: remove da lista" << endl;
  cout << "p: procura elemento" << endl;
  cout << "e: verifica uma posição" << endl;
  cout << "v: visualizar a lista " << endl;
  cout << "s: sair" << endl;
  cout << "Opção: " << endl;
}

int main()
{
  lista ml;
  ml.fim = 0;
  char op;
  int posicao, elemento;

  while (true)
  {
    menu();
    cin >> op;
    switch (op)
    {
    case 'i':
      cout << "Digite a posição que sera inserido: ";
      cin >> posicao;
      cout << "Digite o elementor a ser inserido: ";
      cin >> elemento;
      insert(ml, posicao, elemento);
      break;

    case 'r':
      cout << "Qual é a posicaoição do elemento a ser removido: ";
      cin >> posicao;
      remove(ml, posicao);
      break;
    case 'p':
      cout << "Digite o elemento a ser buscado: ";
      cin >> elemento;
      cout << "Está na posição" << pos(ml, elemento);
      break;

    case 'e':
      cout << "Digite a posicaoição do elemento a ser visualizado ";
      cin >> posicao;
      cout << "O elemento na posição: " << posicao << "é" << element(ml, posicao) << endl;
      break;
    case 'v':
      imprime(ml);
      break;
    case 's':
      return 0;
      break;
    default:
      cout << "Opção inválida!" << endl;
    }
  }
  return 0;
}