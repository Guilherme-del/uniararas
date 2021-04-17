print ("="*69)
print ("\t \t \t Questão 3")
print ("="*69)

x0= float(input("Qual a coordenada de lançamento inicial? (APENAS NUMEROS): "))
y0=float(input("Qual a coordenada de altura inicial (APENAS NUMEROS): ")) 
v0= float(input("Qual é a velocidade de lançamento? (APENAS NUMEROS): "))
t= float(input("Qual é o tempo? (APENAS NUMEROS): "))
g=10
x=x0+v0*t
y=y0-((g*t**2)/2)


if y>0 and y0>0 and t>0 :
    print ("ERROR")
else :
    print ("lançamento horizontal é de :", x,"m, e o ","lançamento vertical é de:",y,"m")
