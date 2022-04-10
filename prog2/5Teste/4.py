#Faça um programa que requisite ao usuário inserir 10 valores, e os armazene em uma lista.Após isto: Exiba a lista, exiba a média.

print ("="*69)
print ("\t \t \t Teste de conhecimento 5 - Exercicio 4")
print ("="*69)
 
 
lista = []

for i in range (10):
    valor = input ("Digite um valor : ")
    lista.append(valor)
    
print(lista)