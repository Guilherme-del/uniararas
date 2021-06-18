#Escreva um programa que receba uma lista com 05 números. Coloque em ordem crescente e exiba na tela. Coloque em ordem decrescente e exiba na tela 

print('='*69)
print('\t\t \t P2 - EXC1')
print('='*69)

numeros = []

try:
    for i in range(5): 
        numeros.append(float(input("Digite um numero: "))) 
except ValueError:
    print("Apenas numeros são aceitos")
    raise

numeros.sort(key=float, reverse=True)  # Decrescente
print('Ordem decrescente é :',numeros)
numeros.sort(key=float, reverse=False)  # Crescente
print('Ordem crescente é :',numeros)


