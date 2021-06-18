#Escreva um programa que receba uma lista com N elementos e logo após a finalização da inserção, crie uma nova lista, onde cada item desta nova lista, é a SOMA dos valores anteriores até a sua posição atual. 

print('='*69)
print('\t\t \t P2 - EXC4')
print('='*69)

from random import randrange

print ("="*69)
print ("\t \t \t Teste de conhecimento 5 - Exercicio 5")
print ("="*69)
 


lista = []
NovaLista = []

for i in range (randrange(3,10)):
    lista.append(randrange(10))
print('a sua lista é :',lista)

for c,v in enumerate (lista) :
   # print('valor',v,'esta na posição', c)
    NovaLista.append(v+c)
print('a sua nova lista é: ',NovaLista)