print ("="*69)
print ("\t \t \t Questão 5")
print ("="*69)

anonasc = float(input("Qual o ano de nascimento do nadador? "))
idade = float(2020 - anonasc)
   
if idade<= 9:
    print ("Mirim")
elif idade<= 14:
    print ("Infantil")
elif  idade<=13:
    print ('Juvenil A')
elif  idade<= 19:
    print ("junior")
elif idade<= 25:
    print("Sênior")
else:
    print ("Master")