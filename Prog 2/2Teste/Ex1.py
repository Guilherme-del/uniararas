print('='*69)
print('\t\t \t Segundo teste de conhecimento - EXC1')
print('='*69)

i = 0
for c in range(0,20):
    n = int(input('digite um numero: '))
    i += n    
    if n > 0:    
        print('A soma dos números deu',i)
    else:
        print('Erro')
        break