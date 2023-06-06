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
    
