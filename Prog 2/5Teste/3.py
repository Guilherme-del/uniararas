#Leia uma lista com 06 números e os exiba da seguinte maneira: num[índice] = valor

print ("="*69)
print ("\t \t \t Teste de conhecimento 5 - Exercicio 3")
print ("="*69)

num = []
numero = 0

for c in range(6):
        num.append(c)
        print('num','[',numero,']' ,'=', num[c])
        numero+= 1 #incremento
