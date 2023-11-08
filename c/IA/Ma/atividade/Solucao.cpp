
#include "Solucao.h"
#include <iostream>
#include <stack>

Solucao::Solucao(const Estado &estadoInicial) : estadoInicial(estadoInicial) {}

void Solucao::encontrarSolucao()
{
    if (buscarSolucao(estadoInicial))
    {
        imprimirSolucao();
    }
    else
    {
        std::cout << "Nao foi possivel encontrar uma solucao." << std::endl;
    }
}

bool Solucao::buscarSolucao(const Estado &estadoAtual)
{
    // Verifique se o macaco já está segurando a banana
    if (estadoAtual.estaSegurandoBanana())
    {
        solucao.push_back(estadoAtual);
        return true;
    }

    // Use uma pilha para realizar a busca em profundidade
    std::stack<Estado> pilha;
    pilha.push(estadoAtual);

    while (!pilha.empty())
    {
        Estado estado = pilha.top();
        pilha.pop();

        // Verifique se o macaco já está segurando a banana
        if (estado.estaSegurandoBanana())
        {
            solucao.push_back(estado);
            return true;
        }

        // Andar para a direita
        acaoAndarDireita(estado);
        acaoAndarDireita(estado);
        acaoAndarDireita(estado);
        acaoAndarDireita(estado);
        //subir na caixa
        acaoSubirSobreCaixa(estado);
        //ando para a esquerda
        acaoAndarEsquerda(estado);
        acaoAndarEsquerda(estado);
        //dá no pé;
        acaoAndarDireita(estado);
        acaoAndarDireita(estado);

        // Executa a solucao e verifica se pegou a bana
        if (estado.estaSegurandoBanana())
        {
            solucao.push_back(estado);
            return true;
        }
    }

    return false; // Não foi encontrada uma solução a partir deste estado
}

void Solucao::acaoAndarEsquerda(Estado &estado)
{
    int novoMacacoX = estado.getMacacoX();
    int novoMacacoY = estado.getMacacoY() - 1;
    Estado novoEstado(novoMacacoX, novoMacacoY, estado.getCaixaX(), estado.getCaixaY(), estado.getBananaX(), estado.getBananaY(), estado.estaSegurandoBanana());

    if (novoEstado.ehValido())
    {
        solucao.push_back(novoEstado);
    }
}

void Solucao::acaoAndarDireita(Estado &estado)
{
    int novoMacacoX = estado.getMacacoX();
    int novoMacacoY = estado.getMacacoY() + 1;
    Estado novoEstado(novoMacacoX, novoMacacoY, estado.getCaixaX(), estado.getCaixaY(), estado.getBananaX(), estado.getBananaY(), estado.estaSegurandoBanana());

    if (novoEstado.ehValido())
    {
        solucao.push_back(novoEstado);
    }
}

void Solucao::acaoSubirSobreCaixa(Estado &estado)
{
    int novoMacacoX = estado.getMacacoX() - 1;
    int novoMacacoY = estado.getMacacoY();
    Estado novoEstado(novoMacacoX, novoMacacoY, estado.getCaixaX(), estado.getCaixaY(), estado.getBananaX(), estado.getBananaY(), estado.estaSegurandoBanana());

    if (estado.getMacacoX() == estado.getCaixaX() + 1 &&
        abs(estado.getMacacoY() - estado.getCaixaY()) <= 1 &&
        novoEstado.ehValido())
    {
        solucao.push_back(novoEstado);
    }
}

void Solucao::acaoDescerDaCaixa(Estado &estado)
{
    int novoMacacoX = estado.getMacacoX() + 1;
    int novoMacacoY = estado.getMacacoY();
    Estado novoEstado(novoMacacoX, novoMacacoY, estado.getCaixaX(), estado.getCaixaY(), estado.getBananaX(), estado.getBananaY(), estado.estaSegurandoBanana());

    if (estado.getMacacoX() == estado.getCaixaX() && estado.getMacacoY() == estado.getCaixaY() - 1 &&
        novoEstado.ehValido())
    {
        solucao.push_back(novoEstado);
    }
}

void Solucao::acaoPuxarCaixa(Estado &estado)
{
    int novoMacacoX = estado.getMacacoX();
    int novoMacacoY = estado.getMacacoY() - 1;
    int novaCaixaX = estado.getCaixaX();
    int novaCaixaY = estado.getCaixaY() - 1;
    Estado novoEstado(novoMacacoX, novoMacacoY, novaCaixaX, novaCaixaY, estado.getBananaX(), estado.getBananaY(), estado.estaSegurandoBanana());

    if (estado.getMacacoY() > estado.getCaixaY() &&
        novoEstado.ehValido())
    {
        solucao.push_back(novoEstado);
    }
}

void Solucao::acaoEmpurrarCaixa(Estado &estado)
{
    int novoMacacoX = estado.getMacacoX();
    int novoMacacoY = estado.getMacacoY() + 1;
    int novaCaixaX = estado.getCaixaX();
    int novaCaixaY = estado.getCaixaY() + 1;
    Estado novoEstado(novoMacacoX, novoMacacoY, novaCaixaX, novaCaixaY, estado.getBananaX(), estado.getBananaY(), estado.estaSegurandoBanana());

    if (estado.getMacacoY() < estado.getCaixaY() &&
        novoEstado.ehValido())
    {
        solucao.push_back(novoEstado);
    }
}

void Solucao::imprimirSolucao() const
{
    for (const Estado &estado : solucao)
    {
        estado.imprimir();
    }
}