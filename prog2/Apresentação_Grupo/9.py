
#Faça um programa que conte quantas vogais existem na palavra digitada.


print('='*69)
print('\t\t \t CONTADOR DE VOGAIS')
print('='*69)

i = 0
j = 0
string = str.lower (input("Digite algo: "))
for i in string:
    if ( i == 'a'
        or i == 'e'
        or i == 'i'
        or i == 'o'
        or i == 'u'):
        j+=1
print("Temos", j, "vogais na sua palavra")

