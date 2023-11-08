/*
Primerio passo:
Projeto Conceitual (DER)
Segundo Passo:
Projeto Lógico(Modelo Relacional)
Terceiro Passo:
Projeto Físico(Tabela/Chaves)
*/

/*
scripts executados:

create database fhoEstudo;
show databases;
use fhoEstudo;

create table CLIENTE (
cpf varchar(15) primary key,
nome varchar(32),
endereco varchar(32),
telefone varchar(25)
);

show tables;
describe CLIENTES;

create table COMPUTADOR (
codigo int primary key auto_increment,
modelo varchar(32),
fabricante varchar(32),
frequencia varchar(25),
dataAquisição date,
cpfClie varchar(15), 
foreign key (cpfClie) references CLIENTE(cpf)
);

describe COMPUTADOR;

create table TECNICO (
cpf varchar(15) primary key,
formacao varchar(32),
nome varchar(32),
telefone varchar(25),
endereço varchar(32) 
);

describe TECNICO;

create table MEMORIA (
codigo int primary key auto_increment,
fabricante varchar(32),
frequencia float,
capacidade float,
modelo varchar(32) 
);

create table ACESSORIO (
codigo int primary key auto_increment,
fabricante varchar(32),
modelo varchar(32),
tipo varchar(32)
);

create table PROCESSADOR (
codigo int primary key auto_increment,
frequencia float,
fabricante varchar(32),
modelo varchar(32)
);

create table COMPONENTE (
codigo int primary key auto_increment,
codComputador int,
codAcessorio int,
codMemoria int,
codPROCESSADOR int,
foreign key (codComputador) references COMPUTADOR(codigo),
foreign key (codAcessorio) references ACESSORIO(codigo),
foreign key (codMemoria) references MEMORIA(codigo),
foreign key (codPROCESSADOR) references PROCESSADOR(codigo)
)

INSERT INTO CLIENTE (
cpf,
nome,
endereço,
telefone )
values(
'367.567.258-16',
'Pedro Pessoa Filho',
'Rua da augusta',
'(19)3866-2424'
)

INSERT INTO CLIENTE (
cpf,
nome,
endereço,
telefone )
values(
'666.567.258-28',
'Joao Pessoa Filho',
'Rua da augusta 2',
'(19)3866-6969'
)

INSERT INTO COMPUTADOR (modelo,fabricante,dataAquisicao,cpfClie) values ('Asus','testado','2020-02-15','367.567.258-16');


SELECT nome,endereco FROM CLIENTE WHERE cpf = '666.567.258-28';
*/



