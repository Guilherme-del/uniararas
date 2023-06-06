create database ODS13;
use ODS13;

Create table Estados(
	CodEstado int Primary key auto_increment,
    NomeEstado varchar(15)
);

create table Pessoas(
	CPF varchar(20) primary key,
    nome varchar(50),
    codEstado int,
	foreign key (codEstado) references Estados(CodEstado)
);


create table Afetados(
	CodAfetado int primary key auto_increment,
    nome varchar(50),
    CodEstado int,
	ano varchar(4),
	cpfPessoa varchar (20),
    foreign key (cpfPessoa) references Pessoas(CPF),
	foreign key (CodEstado) references Estados(CodEstado)
   
);

create table Instituicao(
	CodInstituicao int primary key auto_increment,
    CodEstado int,
    nome varchar(50),
    foreign key (CodEstado) references Estados(CodEstado)
);

create table Fonte(
	CodFonte int primary key auto_increment,
    CodInstituicao int,
    CodEstado int,
    Descricao varchar(50),
    foreign key (CodInstituicao) references Instituicao(CodInstituicao),
    foreign key (CodEstado) references Estados(CodEstado)
    );
    
create table Desastre(
	CodDesastre int primary key auto_increment,
    CodEstado int,
    Descricao varchar(50),
    Escala varchar(30),
    foreign key (CodEstado) references Estados(CodEstado)
);
    
    
