print('='*69)
print('\t\t \t SCHOOLNET - ATV9')
print('='*69)
import time
A = int(input('Insira o valor de A: ' ))
B = float(input('Insira o valor de B:' ))
C = float(input('Insira o valor de C:' ))

while True:    
    if ((A<B+C) and (B<A+C) and (C<A+B)):
        print('Calculando....')
        time.sleep(2)
        print('O perimetro do seu triangulo é de: ',A+B+C,'e a area é de: ',(((A+B)*C)/2))
        break
    else:
            print('**********error 404 not found***********')
            break
            
            