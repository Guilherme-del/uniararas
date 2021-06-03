#Escreva um programa que receba uma lista com 07 números. Coloque em ordem crescente e exiba na tela. Coloque em ordem decrescente e exiba na tela
print ("="*69)
print ("\t \t \t Teste de conhecimento 5 - Exercicio 1")
print ("="*69)


lista = [1,2,3,4,5,6,7]
lista.sort()

print ("="*69)
print (" Ordem crescente do array: ",lista)
print ("="*69)

lista.sort(reverse=True)
print ("="*69)
print (" Ordem decrescente do array: ",lista)
print ("="*69)