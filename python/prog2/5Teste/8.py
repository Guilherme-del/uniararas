print ("="*69)
print ("\t \t \t Teste de conhecimento 5 - Exercicio 8")
print ("="*69)
import time

print('='*45)
print('Novo sistema o Boteco do Pai')
print('='*45)

lista=[]

itens = [10.00 ,15.00 , 4.00]

for i in range (1):
    print('Item: litrão aguado')
    print('Preço antigo:R$10.00')
    nv=float(input('Informe o novo valor:  '))
    lista.append(nv)
    
    time.sleep(1)
    
    print('Item: Catuaba selvagem')
    print('Preço antigo:R$15.00')
    nv=float(input('Informe o novo valor:  '))
    lista.append(nv)
    
    time.sleep(1)
    
    print('Item: Corotin')
    print('Preço antigo:R$4.00')
    nv=float(input('Informe o novo valor:  '))
    lista.append(nv)
    
for i ,v in enumerate(lista):
    print('='*45)
    print('Novos valores:  ')
    print('Litrão aguado,Catuaba Selvagem, Corotin ')
    print('R$' ,lista)
    break
 