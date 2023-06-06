create database EmpresaMA;
use EmpresaMA;

create table fornecedores(
codigofornecedor int primary key auto_increment,
cnjpfornecedor varchar(20),
nome varchar(50),
produto varchar(50),
tipocontrato varchar(25)
);

create table produtos(
codigoproduto int primary key auto_increment,
nome varchar(50),
preco float,
marca varchar(25),
codfornecedor int not null,

foreign key (codfornecedor) references fornecedores(codigofornecedor)
);

create table contratos(
codigocontrato int primary key auto_increment,
tipocontrato varchar (50),
codigofornecedor int not null,

foreign key (codigofornecedor) references fornecedores(codigofornecedor)
);

create table boletos(
codigoboleto int primary key auto_increment,
valor float,
vencimento date,
statusboleto varchar (20),
codigocontrato int not null,

foreign key (codigocontrato) references contratos(codigocontrato)
);
