print ("="*69)
print ("\t \t \t Questão 2")
print ("="*69)

salario = float(input("Qual o seu salario? "))
if salario <= 1250:
    Aumento = salario+(salario*15/100)
    print ("seu novo salário é de R$: ",Aumento)
else :
    Aumento = salario+(salario*10/100)
print ("Seu novo salario é de R$",Aumento)