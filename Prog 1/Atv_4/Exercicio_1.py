print ("="*130)
print ("                                                                Exercicio 1")
print ("="*130)

numero=float(input("Qual o número de lados do poligono?"))
nd=numero*(numero-3)/2
if numero >2:
    print ("o numero de diagonais é igual a: ",nd)
else:
    print ("")