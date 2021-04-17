print('='*35)
print('\t\t SCHOOLNET - FHO')
print('='*35)

nome = input('Informe seu nome :')
ra = input('Informe o registro do aluno :')

A1 = float(input('Forneça a nota da primeira avaliação: '))

if A1 < 0 or A1 > 10 :
    print('Valor inválido , tente novamente')
else:
    A2 = float(input('Forneça a nota da segunda avaliação: ' ))
    if A2 < 0 or A2 > 10 :
        print('Valor inválido, tente novamente')
    else:
        media = (A1 + (2*A2))/3
        media = round(media,2)
    print(nome,', sua média foi ', media)
    if media <= 10 and media >= 5:
            print("Parabéns você está aprovado!")
    elif media < 5 and media >= 3:
            print('Você terá que realizar o regime especial de recuperação')
    else:
            print("Você terá que cursar novamente a disciplina")