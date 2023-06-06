print ("="*69)
print ("\t \t \t Questão 2")
print ("="*69)

Peso = float(input("Peso: "))
Altura= float(input("Altura: "))
IMC = Peso/Altura**2

if IMC <= 18.5:
    print("Abaixo do peso")
elif IMC > 18.5 and IMC<= 25:
    print ("Peso Ideal")
elif IMC > 25 and IMC<= 40:
    print("Sobrepeso")
elif IMC > 40:
    print ("Obesidade Mórbida")

    