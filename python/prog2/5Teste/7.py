#Escreva um programa que vá recebendo itens digitados pelo usuário, e os inserindo em uma lista, e vá perguntando ao usuário se ele deseja continuar ou não, a lista termina quando o usuário não desejar mais fornecer elementos. Após isto, exiba toda a lista gerada e exiba um menu de opções e programa as ações de cada opção: 1 - para deletar o último elemento, 2 - para deletar o elemento X da lista, 3 - terminar edições e printar lista Obs.: Considere que humanos contam a partir de 1.

print ("="*69)
print ("\t \t \t Teste de conhecimento 5 - Exercicio 7")
print ("="*69)

Lista = []

while True:
    print ("="*69)
    print ("\t \t \t Digite s para continuar ")
    print ("="*69)

    pergunta = input('Deseja adicionar um valor? ')
    if pergunta == 's':
        valor = (input ("Digite um valor : "))
        Lista.append(valor)
    else:
        print ("="*69)
        print ("\t \t \t Digite 1 - para deletar o último elemento ")
        print ("\t \t \t Digite 2 - para deletar o elemento x da lista ")
        print ("\t \t \t Digite 3 - para mostrar sua lista ")
        print ("="*69)  
        pergunta2 = int(input('Qual opção deseja? '))

        if pergunta2 == 1:
            Lista.pop()
        elif pergunta2 == 2:
            for c,v in enumerate (Lista) : 
                print('valor',v,'esta na posição', c+1) 
            pergunta3 = int(input('Em qual posição se encontra o valor que deseja excluir ?'))
            Lista.pop(pergunta3-1)  
        elif pergunta2 == 3:
            print('Sua lista é:',Lista)
            break

        


