print ("="*69)
print ("\t \t \t Questão 1")
print ("="*69)

x = float (input("Qual o valor de x? "))
y = float (input ("Qual o valor de y? "))

if x==0 and y==0:
    print ("suas coordenadas estão na origem do quadrante ")
elif x> 0 and y>0:
    print ("suas coordenas estão no Q1 ")
elif x<0 and y<0:
    print ("suas coordenadas estão no Q3" )
elif x>0 and y<0:
    print ("suas coordenadas estão no Q4 ")
elif x<0 and y>0 :
    print ("suas coordenadas estão no Q2 ")
else :
    print ("Error")