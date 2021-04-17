print ("="*69)
print ("\t \t \t Questão 2")
print ("="*69)

primeiro = int(input('Qual o primeiro numero: '))
segundo  = int(input('Qual o segundo numero : '))
terceiro = int(input('Qual o terceiro numero: '))

maior = primeiro
if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro
    print("Maior: ",maior)
    
menor = primeiro
if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro
    print("Menor: ",menor)
