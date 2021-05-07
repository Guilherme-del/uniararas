import random
print('='*45)
print('\t\tJogo da adivinhação!')
print('='*45)


sorteio = random.randint(0,10)
chute = int(input('Tente acertar um valor entre 0 e 10:'))

while chute != sorteio :
    print('Você errou ! Tente novamente !')
    if chute > sorteio :
        print("Tente um valor menor!")
    else:
        print("Tente um valor maior!")
    chute = int(input('Tente acertar um valor entre 0 e 10:'))

print("Parabéns, você acertou!")