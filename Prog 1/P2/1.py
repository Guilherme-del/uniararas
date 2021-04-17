print ("="*69)
print ("\t \t \t Questão 1")
print ("="*69)

primeiro = int(input("Primeiro valor: "))
segundo = int(input("Segundo valor: "))


if (primeiro > segundo):
    print ("O primeiro é o maior")
elif(segundo>primeiro):
    print("O segundo é o maior")
elif primeiro==segundo:
    print ("Não existe valor maior, os dois são iguais")
else:
    print("ERROR")
    