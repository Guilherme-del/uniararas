print ("="*69)
print ("\t \t \t Questão 5")
print ("="*69)

from datetime import date
anonasc = float(input("Qual o ano de seu nascimento? "))
idade = float(2020 - anonasc)
ano = date.today().year

passou = idade -18 
falta = 18-idade  

if idade== 18:
    print ("Esta na hora de fazer o alistamento militar")
elif idade > 18:
    print ("ja passou da hora de se alistar, se passaram ", passou," anos da idade correta")
elif idade < 18:
    print ("falta ",falta,"anos para sua inscrição")