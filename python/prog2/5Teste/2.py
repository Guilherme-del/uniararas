#Escreva um programa que receba uma lista com 10 elementos e exiba: quantidade de positivos, quantidade de negativos, quantidade de pares e a quantidade de ímpares. Obs.: Só os e ímpares números positivos são testados em pares
print ("="*69)
print ("\t \t \t Teste de conhecimento 5 - Exercicio 2")
print ("="*69)

valores = [1,2,3,4,5,-1,-2,-3,-4,-5]

impares = list()
pares = list()

for c in valores:
    if c % 2 != 0:
        impares.append(c)
    else:
        pares.append(c)

print('os numeros impares são: ',impares)
print('os numeros positivos são: ',pares)


negativos = list()
positivos = list()

for i in valores:
    if i < 0  :
        negativos.append(i)
    else:
        positivos.append(i)

print('os numeros negativos são: ',negativos)
print('os numeros positivos são: ',positivos)