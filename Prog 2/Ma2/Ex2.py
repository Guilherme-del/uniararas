print('='*69)
print('\t\t \t Ma2 - EXC2')
print('='*69)


Temperatura = []
mes = 0

try:
    for i in range(2): 
        mes+= 1
        mensagem = ('Qual a temperatura do mês ', mes,'? ')
        Temperatura.append(float(input(mensagem)))       
except ValueError:
    print("Apenas numeros são aceitos")
    raise

Media = sum(Temperatura)/len(Temperatura)

print ('A media anual foi de ',Media)

for m in range(0, len(Temperatura)):
    if Temperatura[m] > Media:
        mensagem2 =  (float(m+1), mes[m])  
        print (mensagem2)
