print ("="*69)
print ("\t \t \t Questão 1")
print ("="*69)

velocidade =float(input("Qual a velocidade em km/h ? "))
multa = (velocidade - 81) * 7 +37.5

if velocidade>80:
    print ("Voce foi ultrapassou a velocidade limite da pista resultando em multa")
    print ("E terá que pagar R$",multa," ao estado")
else :
    print("Voce estava na velocidade permitida")