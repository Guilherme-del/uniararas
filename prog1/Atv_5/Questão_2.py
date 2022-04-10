print ("="*69)
print ("\t \t \t Questão 1")
print ("="*69)

quilowatthora = 0.31
chuveiro = 5*quilowatthora
x=float(input("Há quantos dias o chuveiro está ligado ?(COLOQUE APENAS NUMEROS): "))
gasto = x*chuveiro

if gasto > 100 :
    print (" ALERTA CONTA DE ENERGIA ESTA MUITO ELAVADO ")
else :
    print ("R$",gasto)