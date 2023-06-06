print('='*69)
print('\t\t \t SCHOOLNET - ATV8')
print('='*69)

print('Saiba se seu numero é divisivel por 3 e 5 aqui')
num= int(input('Qaul seu numero? '))
resto= (num % 3 == 0) and (num % 5==0)

if resto == True:
    print(num,'é divisivel por 3 e 5')
else:
    print(num,'não é divisivel por 3 e 5 ')