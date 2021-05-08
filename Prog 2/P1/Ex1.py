print ("="*69)
print ("\t \t \t  P1 - EXC1")
print ("="*69)

print ("="*69)
print ("\t \t \t CONDIÇÕES DE PAGAMENTO : ") 
print('\t \t \t 1 = à vista') 
print('\t \t \t 2= dinheiro/cheque')
print('\t \t \t 3= à vista no cartão ')
print('\t \t \t 4= em até 2x no cartão' ) 
print('\t \t \t 5= em até3x ou mais no cartão')
print ("="*69)

produto = float(input("Qual o valor do produto? "))
pagamento = float(input("Qual a forma de pagamento?"))


dinheiro = produto-(produto*10/100)
cartao = produto - (produto*5/100)

if pagamento == 1:
    vista = produto-(produto*0.1)
    print('O preço do produto é de  R$ ',vista)
elif pagamento == 2:
    dinheiro=produto-(produto*0.05)
    print('O preço do produto é de  R$ ',dinheiro)
elif pagamento == 3:
    print('O preço do produto é de  R$ ',produto)
elif pagamento == 4:
    cartao= produto+(poduto*0.2)
    print('O preço do produto é de  R$ ',cartao)
else:
    print('Essa não é uma forma válida de pagamento')