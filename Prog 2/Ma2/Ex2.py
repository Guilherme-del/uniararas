#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).



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
