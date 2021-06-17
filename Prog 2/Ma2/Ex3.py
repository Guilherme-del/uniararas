#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

print('='*69)
print('\t\t \t Ma2 - EXC2')
print('='*69)


meses = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperatura = []

try:
    for m in range(0, len(meses)):
        temperatura.append(float(input("Digite a temperatura do mês de " + meses[m] + ": ")))
except ValueError:
    print("Apenas numeros são aceitos")
    raise

media = sum(temperatura)/len(temperatura)
print('='*69)
print ('Os meses que ficaram acima da temperatura media foram:')
for m in range(0, len(temperatura)):
    if temperatura[m] > media:
        print (str(m+1) + " - " + meses[m])
print('='*69)