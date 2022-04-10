print ("="*179)
print ("                                                                                 Bem vindo à agenda eletronica")
print ("="*179)
Nome= input("Qual seu nome?")
RG= input("Forneça seu RG?")
CPF= input("Forneça seu CPF?")
CEL= input("Forneça o número do seu Celular?")
Email=input("Qual seu email?")
print ("Deseja saber seus dados")
acao = int(input("Digite '1' para sim e digite '2' para não: "))
if(acao==1):
    print("Seu nome é:",Nome,",Seu RG é:",RG,",Seu CPF é:",CPF,",O numero do seu celular é:",CEL,"e seu email é:",Email)
else:
    if(acao==2):
        print("None")
    else:
        print("None")




#Feito no compiler online
