print('='*69)
print('\t\t \t SCHOOLNET - ATV7')
print('='*69)


produto = float(input("Qual o valor do produto? "))

if produto >= 100 and produto <= 1000:
    desconto = produto*0.1
    produto = produto - desconto
    print ('O valor do produto é de:' ,produto,'R$')
elif produto > 1000:
    desconto = produto*0.15
    produto = produto - desconto
    print ('O valor do produto é de:' ,produto,'R$')
else:
  print('O valor do produto é de:' ,produto,'R$')      
    

