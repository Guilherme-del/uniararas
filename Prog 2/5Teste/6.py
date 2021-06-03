#Escreva um programa que vá recebendo itens digitados pelo usuário, e os inserindo em uma lista, e vá perguntando ao usuário se ele deseja continuar ou não, a lista termina quando o usuário não desejar mais fornecer elementos. Ao final, exiba toda a lista gerada.


print ("="*69)
print ("\t \t \t Teste de conhecimento 5 - Exercicio 6")
print ("="*69)

Lista = []

while True:
    print ("="*69)
    print ("\t \t \t s para continuar ")
    print ("="*69)

    pergunta = input('Deseja adicionar um valor? ')
    if pergunta == 's':
        valor = (input ("Digite um valor : "))
        Lista.append(valor)
    else:
        print('sua lista é: ',Lista)
        break
