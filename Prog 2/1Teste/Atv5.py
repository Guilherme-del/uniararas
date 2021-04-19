print('='*69)
print('\t\t \t SCHOOLNET - ATV5')
print('='*69)
import time
import math
print('Bem vindo ao calculator FHO')

print ('Insira o valor da velocidade inicial')
vo = float(input(': '))
print('Insira o valor da aceleração')
a = float(input(': '))
print('Por fim adicione a distancia')
ds = float(input(': '))


v = ((vo**2+2*a*(ds)))
raiz = math.pow(v,1/2)
print('Calculando.....')
time.sleep(2)             
print ('o valor de V é: ',raiz, 'm/s')