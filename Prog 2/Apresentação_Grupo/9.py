
#Faça um programa que conte quantas vogais existem na palavra digitada.


print('='*69)
print('\t\t \t CONTADOR DE VOGAIS')
print('='*69)


def cacavogais():
    i = 0
    j = 0
    string = str (input("Digite algo: "))
    for i in string:
        if (i == 'A' or i == 'a'
        or i == 'E' or i == 'e'
        or i == 'I' or i == 'i'
        or i == 'O' or i == 'o'
        or i == 'U' or i == 'u'):
             j+=1
    print("Temos", j, "vogais na sua palavra")
cacavogais()