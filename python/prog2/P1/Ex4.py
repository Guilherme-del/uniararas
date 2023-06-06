print ("="*69)
print ("\t \t \t P1 - EXC4")
print ("="*69)

password = 1234

for i in range(5): 
   tentativas = int(input('Informe a senha:'))
   if tentativas == password:
        print('ACESSO PERMITIDO')
        break
else:
    print("ACESSO NEGADO")