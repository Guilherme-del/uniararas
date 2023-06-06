print('='*35)
print('Calculo da area do terreno retângular')
print('='*35)

print('Para isso forneça algumas informações')

base = float(input('Forneça o largura do terreno retângular em metros:'))
if base > 0 :
    altura = float(input('Forneça o comprimento do terreno retângular em metros :'))
    if altura > 0 :
        area = base * altura
        area = round(area,2)
        print('A area do terreno retângular em estudo é : ', area,'m²')
    else:
print('Erro, valor inválido! Tente novamente!')