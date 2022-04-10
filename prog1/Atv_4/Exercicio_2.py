print ("="*130)
print ("                                                                Exercicio 2")
print ("="*130)
horas= float(input("Que horas são? "))
minutos= horas*60
segundos= horas*3600
if horas <= 0 or horas >12:
    print("O valor da variável deve estar entre 1 e 12 ")
else:
    print ( minutos,"minutos",segundos,"segundos")
