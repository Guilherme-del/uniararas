#include <iostream>
using namespace std;

struct produto{
    int codigo;
    char nome[50];
    float valor;
};

int main(){
    produto estoque[2];

    for(int i=0;i<2;i++){
        cout<<endl<<"Codigo: ";
        cin>>estoque[i].codigo;
        cout<<"Nome: ";
        cin>>estoque[i].nome;
        cout<<"Valor: ";
        cin>>estoque[i].valor;
    }
    for(int i=0;i<2;i++){
        //aplicar desconto de 10% nos produtos com valor menor de 1k
        if(estoque[i].valor<1000){
            float oldvalor=estoque[i].valor;
            estoque[i].valor=estoque[i].valor*0.1;
            float newvalor= oldvalor-estoque[i].valor;         
            cout<<endl<<"Produto: "<<estoque[i].nome <<" Valor com desconto: "<< newvalor;           
        }
        // mostrar apenas produtos com valor superior a 2k
        else if(estoque[i].valor>2000){
        cout<<endl<<"Codigo: ";
        cout<<estoque[i].codigo;
        cout<<endl<<"Nome: ";
        cout<<estoque[i].nome;
        cout<<endl<<"Valor: ";
        cout<<estoque[i].valor;
        }
        
    }
    
    return 0;
}