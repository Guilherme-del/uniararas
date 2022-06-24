#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:1. "Telefonou para a vítima?"2. "Esteve no local do crime?"3. "Mora perto da vítima?"4. "Devia para a vítima?"5. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente" *

print ("="*69)
print ("\t \t \t  Ma2 - EXC1")
print ("="*69)

resposta = []
resposta.append(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
resposta.append(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
resposta.append(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
resposta.append(input("Devia para a vítima? 1/Sim ou 0/Não: "))
resposta.append(input("Já trabalhou com a vítima? 1/Sim ou 0/Não: "))
soma = 0

for i in resposta: # soma do número de respostas
    soma+= int(i)
if (soma == 2):
    print("Suspeita")
elif (3 <= soma <= 4):
    print("Cúmplice")
elif (soma == 5):
    print("Assassino")
else:
    print('Esta dispensado, Inocente')
    
