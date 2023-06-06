#include<iostream>
#include<vector>

using namespace std;

class Time{
private:
    string nome;
    string jogadores[50];
    string presidente;
    string estado;
    int numeroJogadores;

public:
    Time();
    void setNome(string nome);
    void insereJogador(string nomeJogador);
    void setPresidente(string presidente);
    void setEstado(string estado);
    string getNome();
    string getJogador(int numero);
    string getPresidente();
    string getEstado();

};

class Campeonato{
private:
    string nome;
    int numeroTimes;
    vector <Time> participantes;//cria a composicao com time
    float premio;

public:
    Campeonato();
    void setNome(string nome);
    void insereTime(Time T1);
    void setNumeroTimes(int numeroTimes);
    void setPremio(float premio);
    string getNome();
    void getTimes();//imprime os times que estão no campeonato
    int getNumeroTimes();
    float getPremio();
};

class CBF{
private:
    string presidente;
    vector <Time> times; //cria composicao com time
    vector <Campeonato> eventos; //cria composicao com campeonatos
    int numeroTimes;

public:
    CBF();
    void setPresidente(string presidente);
    string getPresidente();
    void cadastraTime();
    void criaCampeonato();
    void insereTimeCampeonato(Time T1, string campeonato);

};

Time::Time(){
    this->nome = " ";
    this->presidente = " ";
    this->estado = " ";
    this->numeroJogadores = 0;
}

void Time::setNome(string nome){
    this->nome = nome;
}

void Time::insereJogador(string nomeJogador){
    this->jogadores[this->numeroJogadores] = nomeJogador;
    this->numeroJogadores++;
}

void Time::setPresidente(string presidente){
    this->presidente = presidente;
}

void Time::setEstado(string estado){
    this->estado = estado;
}

string Time::getNome(){
    return this->nome;
}

string Time::getJogador(int numero){
    return this->jogadores[numero-1];//considerando primeiro jogador = 1

}

string Time::getPresidente(){
    return this->presidente;
}

string Time::getEstado(){
    return this->estado;
}


 string nome;
    int numeroTimes;
    vector <Time> participantes;//cria a composicao com time
    float premio;

Campeonato::Campeonato(){
    this->nome = " ";
    this->numeroTimes = 0;
    this->premio = 0.0;
}
void Campeonato::setNome(string nome){
    this->nome = nome;
}

void Campeonato::insereTime(Time T1){
    if((participantes.size() < this->numeroTimes) && (this->numeroTimes != 0)){
        this->participantes.push_back(T1);
    }else if(this->numeroTimes <= 0){
            cout<<"Defina primeiro o numero de times"<<endl;
    }else{
        cout<<"Numero de times esgotado"<<endl;
    }
}

void Campeonato::setNumeroTimes(int numeroTimes){
    this->numeroTimes = numeroTimes;
}

void Campeonato::setPremio(float premio){
     this->premio = premio;
}

string Campeonato::getNome(){
    return this->nome;
}

void Campeonato::getTimes(){//imprime os times que estão no campeonato
   for(int i; i < participantes.size(); i++){
       cout<<participantes[i].getNome()<<endl;
   }
}

int Campeonato::getNumeroTimes(){
    return this->numeroTimes;
}

float Campeonato::getPremio(){
    return this->premio;
}


string presidente;
    vector <Time> times; //cria composicao com time
    vector <Campeonato> eventos; //cria composicao com campeonatos
    int numeroTimes;


CBF::CBF(){
    this->presidente = " ";
    this->numeroTimes = 0;
}

 void CBF::setPresidente(string presidente){
    this->presidente = presidente;
 }

 string CBF::getPresidente(){
    return this->presidente;
 }

void CBF::cadastraTime(){
Time temp;
string temps;
int tempnum;
bool controle = true;

    cout<<"Digite o nome do time"<<endl;
    cin>>temps;
    temp.setNome(temps);
    while(controle){
        cout<<"Digite o nome de um jogador"<<endl;
        cin>>temps;
        temp.insereJogador(temps);
        cout<<"Deseja inserir mais jogadores? 1 - sim 0 - nao"<<endl;
        cin>>tempnum;
        if(tempnum == 0) controle = false;
    }
    cout<<"Qual o nome do presidente do time?"<<endl;
    cin>>temps;
    temp.setPresidente(temps);
    cout<<"Qual o estado do time?"<<endl;
    cin>>temps;
    temp.setEstado(temps);

    this->times.push_back(temp);

}

void CBF::insereTimeCampeonato(Time T1, string campeonato){
int i = 0;

    for(i = 0; i < times.size(); i++){
        if(eventos[i].getNome() == campeonato) break;
    }

    this->eventos[i].insereTime(T1);

}


void CBF::criaCampeonato(){
Campeonato camptemp;
string temps;
int numero;
float tempf;
int controle = 0;

    cout<<"Digite o nome do campeonato"<<endl;
    cin>>temps;
    camptemp.setNome(temps);
    cout<<"Digite o numero de times"<<endl;
    cin>>numero;
    camptemp.setNumeroTimes(numero);
    while(numero > 0){
        if(controle == times.size()-1){
            numero = 0;
        }
        if(times[controle].getEstado() == "SP"){
            this->insereTimeCampeonato(times[controle], temps);
            numero--;
        }
        controle++;
    }
    cout<<"Digite o valor do premio"<<endl;
    cin>>tempf;
    camptemp.setPremio(tempf);

    this->eventos.push_back(camptemp);

}