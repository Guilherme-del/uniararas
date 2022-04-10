print('='*69)
print('\t\t \t Ma1 - EXC2')
print('='*69)

from random import randint

op = ('Pedra', 'Papel', 'Tesoura')

maq = randint(0, 2)
print('''Suas opções:'
      [ 0 ] Pedra
      [ 1 ] Papel
      [ 2 ] Tesoura''')
jogador = int(input('Qual a sua jogada? '))
if jogador != 0 and jogador != 1 and jogador !=2:
    print('JOGADA INVALIDA \nJogue novamente')

else:
    print('O computador jogou {}'.format(op[maq]))
    print('O jogador jogou {}'.format(op[jogador]))
if maq == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
     print('JOGADA INVALIDA')

elif maq == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
      print('JOGADA INVALIDA')


elif maq == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
     print('JOGADA INVALIDA')