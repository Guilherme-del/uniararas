#ifndef ESTADO_H
#define ESTADO_H

#include <vector>
using namespace std;

//Interface que representa um estado genérico
class Estado
{
    public:
            virtual bool  eObjetivo() = 0;
            virtual vector <Estado *> expandir() = 0;
};

#endif // ESTADO_H