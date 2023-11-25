#include "EstadoJogoDaVelha.h"

EstadoJogoDaVelha::EstadoJogoDaVelha(int tabuleiro[][3], bool eMax){
    // Copia o tabuleiro vindo do pai para o filho.
    this->copia(tabuleiro, this->tabuleiro);
    this->eMax = eMax;
}

void EstadoJogoDaVelha::copia(int origem[][3], int destino[][3]){
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            destino[i][j] = origem[i][j];
        }
    }
}
bool EstadoJogoDaVelha::eFolha(){
    int preenchido = 0;
    
    double h = this->heuristica();
    if(h == 3 || h == -3)
        return true;
    
    for(int i = 0; i < 3; i++)
        for(int j = 0; j < 3; j++)
            if(this->tabuleiro[i][j] != 0)
                preenchido++;
    
     return preenchido == 9;
}
double EstadoJogoDaVelha::heuristica(){
    // Jeito "porco" de somar linha de matrizes!
    int somaLinha0 = this->tabuleiro[0][0] + this->tabuleiro[0][1] + this->tabuleiro[0][2];
    int somaLinha1 = this->tabuleiro[1][0] + this->tabuleiro[1][1] + this->tabuleiro[1][2];
    int somaLinha2 = this->tabuleiro[2][0] + this->tabuleiro[2][1] + this->tabuleiro[2][2];
    
    // Jeito "porco" de somar coluna de matrizes!
    int somaColuna0 = this->tabuleiro[0][0] + this->tabuleiro[1][0] + this->tabuleiro[2][0];
    int somaColuna1 = this->tabuleiro[0][1] + this->tabuleiro[1][1] + this->tabuleiro[2][1];
    int somaColuna2 = this->tabuleiro[0][2] + this->tabuleiro[1][2] + this->tabuleiro[2][2];
    
    // Jeito "porco" de somar diagonais de matrizes!
    int somaDiagonalPrincipal = this->tabuleiro[0][0] + this->tabuleiro[1][1] + this->tabuleiro[2][2];
    int somaDiagonalSecundaria = this->tabuleiro[0][2] + this->tabuleiro[1][1] + this->tabuleiro[2][0];
    
    if(somaLinha0 == 3 || somaLinha1 == 3 || somaLinha2 == 3 || somaColuna0 == 3 || somaColuna1 == 3 ||
       somaColuna2 == 3 || somaDiagonalPrincipal == 3 || somaDiagonalSecundaria == 3)
       return 3;
       
    if(somaLinha0 == -3 || somaLinha1 == -3 || somaLinha2 == -3 || somaColuna0 == -3 || somaColuna1 == -3 ||
       somaColuna2 == -3 || somaDiagonalPrincipal == -3 || somaDiagonalSecundaria == -3)
       return -3;
    
    return 0;
}

bool EstadoJogoDaVelha::ePermitido(int linha, int coluna){
    return linha >= 0 && linha < 3 && coluna >= 0 && coluna < 3 && this->tabuleiro[linha][coluna] == 0;
}

vector<Estado *> EstadoJogoDaVelha::expandir(){
    vector <Estado *> filhos;
    
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            if(ePermitido(i, j)){
                // Copiar o pai, e setar a novo estado.
                int tabuleiroFilho[3][3];
                this->copia(this->tabuleiro, tabuleiroFilho);
                if(this->eMax){
                    tabuleiroFilho[i][j] = 1;
                    EstadoJogoDaVelha * filho = new EstadoJogoDaVelha(tabuleiroFilho, false);
                    filhos.push_back(filho);
                }else{
                    tabuleiroFilho[i][j] = -1;
                    EstadoJogoDaVelha * filho = new EstadoJogoDaVelha(tabuleiroFilho, true);
                    filhos.push_back(filho);
                }
            }
        }
    }
    
    return filhos;
}

EstadoJogoDaVelha * EstadoJogoDaVelha::jogadaHumano(){
    int linha, coluna;
    cin >> linha >> coluna;
    while(!this->ePermitido(linha, coluna)){
        cin >> linha >> coluna;
    }
    int tabuleiroHumano[3][3];
    this->copia(this->tabuleiro, tabuleiroHumano);
    tabuleiroHumano[linha][coluna] = -1;
    return new EstadoJogoDaVelha(tabuleiroHumano, true);
}

void EstadoJogoDaVelha::imprimir(){
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++)
            if(this->tabuleiro[i][j] == 1)
                cout << " X ";
            else if(this->tabuleiro[i][j] == -1)
                cout << " O ";
            else
                cout << " . ";
        cout << endl;
    }
}