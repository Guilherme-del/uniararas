print('='*69)
print('\t\t \t Ma1 - EXC1')
print('='*69)


import random


for i in range(1):
    numero = random.random()
    n = int(input('digite um numero: '))
    numero += n
    resto = numero % 2 

print('='*69)
print('\t\t \t Agora vamos para a adivinhação')
print('Digite 1 para saber se a soma dos numeros foi impar e digite 2 para par')
print('='*69)

guess = int(input('1 = PAR ou 2 = IMPAR, é impar ou par?  '))   

if resto == 0 and guess == 1 :
    print('O numero é par, e voce acertou, Parabéns.')
elif resto == 0 and guess == 1 :
    print('O numero é par, e voce errou, tente novamente.')
elif resto != 0 and guess != 1 :
    print('O numero é Impar, e voce acertou, Parabéns.')
elif resto != 0 and guess == 1 :
    print('O numero é Impar, e voce errou, tente novamente')
else:
    print('Voce digitou um numero inesperado por favor reinicie o programa e tente novamente')
