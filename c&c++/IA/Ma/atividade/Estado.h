#ifndef ESTADO_H
#define ESTADO_H

class Estado {
public:
    Estado(int macacoX, int macacoY, int caixaX, int caixaY, int bananaX, int bananaY, bool segurandoBanana);
    
    bool operator==(const Estado& other) const;

    bool ehValido() const;

    void imprimir() const;

    int getMacacoX() const;
    int getMacacoY() const;
    int getCaixaX() const;
    int getCaixaY() const;
    int getBananaX() const;
    int getBananaY() const;
    bool estaSegurandoBanana() const;

private:
    int macacoX;
    int macacoY;
    int caixaX;
    int caixaY;
    int bananaX;
    int bananaY;
    bool segurandoBanana;
};

#endif