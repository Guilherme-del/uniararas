#include "Estado.h"
#include <iostream>

Estado::Estado(int macacoX, int macacoY, int caixaX, int caixaY, int bananaX, int bananaY, bool segurandoBanana)
    : macacoX(macacoX), macacoY(macacoY), caixaX(caixaX), caixaY(caixaY), bananaX(bananaX), bananaY(bananaY), segurandoBanana(segurandoBanana) {}

bool Estado::operator==(const Estado& other) const {
    return (macacoX == other.macacoX &&
            macacoY == other.macacoY &&
            caixaX == other.caixaX &&
            caixaY == other.caixaY &&
            bananaX == other.bananaX &&
            bananaY == other.bananaY &&
            segurandoBanana == other.segurandoBanana);
}

bool Estado::ehValido() const {
    // Verifique se o estado está dentro dos limites da sala (2 linhas por 5 colunas)
    return (macacoX >= 0 && macacoX < 2 &&
            macacoY >= 0 && macacoY < 5 &&
            caixaX >= 0 && caixaX < 2 &&
            caixaY >= 0 && caixaY < 5 &&
            bananaX >= 0 && bananaX < 2 &&
            bananaY >= 0 && bananaY < 5 &&
            macacoX != caixaX || macacoY != caixaY);
}

void Estado::imprimir() const {
    std::cout << "Estado: Macaco(" << macacoX << ", " << macacoY << "), Caixa(" << caixaX << ", " << caixaY << "), Banana(" << bananaX << ", " << bananaY << "), Segurando Banana(" << segurandoBanana << ")" << std::endl;
}

int Estado::getMacacoX() const {
    return macacoX;
}

int Estado::getMacacoY() const {
    return macacoY;
}

int Estado::getCaixaX() const {
    return caixaX;
}

int Estado::getCaixaY() const {
    return caixaY;
}

int Estado::getBananaX() const {
    return bananaX;
}

int Estado::getBananaY() const {
    return bananaY;
}

bool Estado::estaSegurandoBanana() const {
    return segurandoBanana;
}