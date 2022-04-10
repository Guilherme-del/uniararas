#Crie um programa que leia dois valores fornecidos pelo usuário e exiba um menu na tela :[1] SOMAR[2] MULTIPLICAR[3] MAIOR QUE[4] NOVOS NÚMEROS[5] SAIR Seu programa deverá realizar a operação selecionada pelo usuário e só deve encerrar o programa quando a opção 5 for selecionada *

#import math
import time

print('='*45)
print('\t\t Desafio galera')
print('='*45)


num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print (''' 
    O que você deseja fazer com os valores fornecidos ? 
    [1] Somar 
    [2] Multiplicar
    [3] Maior que
    [4] Novos números
    [5] Sair  ''')

    opcao = int(input('Qual é sua opção? '))
    if opcao == 1 :
       soma =  (num1 + num2)
       print('='*45)
       print ( 'O resultado da soma de:',num1,'+',num2,'é: ',soma) 
       print('='*45)
       time.sleep(2)      
    elif opcao == 2:
        multiplica = (num1 * num2)
        print('='*45)
        print ( 'O resultado da multiplicação de:',num1,'x',num2,'é: ',multiplica) 
        print('='*45)
        time.sleep(2)     
    elif opcao == 3:
        if num1 > num2:           
            print('='*45)
            print (num1,'é maior que: ',num2 ) 
            print('='*45)
        else:
            print('='*45)
            print (num2,'é maior que: ',num1 ) 
            print('='*45)
            time.sleep(2)    
    elif opcao == 4:
        print ('Informe novamente os valores: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
        time.sleep(1) 
    elif opcao ==5:
        print('='*45)
        print('Saindo.......')
        print('='*45)
        time.sleep(2) 
    else:
        print('='*45)
        print('⚡Erro 404 not found⚡')
        print('='*45)
        time.sleep(1) 
print('='*45)
print ('Programa Finalizado com sucesso , Volte sempre ❤️ ')
print('='*45)