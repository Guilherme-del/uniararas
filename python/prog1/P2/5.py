print ("="*69)
print ("\t \t \t Questão extra")
print ("="*69)

from random import randint 
itens = ['Pedra','Papel','Tesoura']

computador = randint(0,2)

jogador = int(input('''
[0] Pedra
[1] Papel
[2] Tesoura
Escolha: '''))

print('Você escolheu',{itens[jogador]})
print('Computador escolheu', {itens[computador]})


if computador == 0:

    if jogador == 2:
        print('COMPUTADOR VENCEU!')
        
    elif jogador == 1:
        print('VOCÊ VENCEU!')
        
    elif jogador == 0:
        print('EMPATE')
        
if computador == 1:

    if jogador == 0:
        print('COMPUTADOR VENCEU!')
        
    elif jogador == 2:
        print('VOCÊ VENCEU!')
        
    elif jogador == 1:
        print('EMPATE')

if computador == 2:

    if jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('EMPATE')