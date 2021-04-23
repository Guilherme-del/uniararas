print('='*69)
print('\t\t \t P1 - EXC2')
print('='*69)

import math

H = float(input("Concentração de íons de hidrogênio: "))
ph = -(math.log10)(H)

if ph > 1*10-7:    
    print('Substancia Acida')
else:
    print('Substancia Alcalina')