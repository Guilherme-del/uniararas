#Escreva um programa que vá recebendo itens digitados pelo usuário, e os inserindo em uma lista, e vá perguntando ao usuário se ele deseja continuar ( Respondendo sim ou não ) ou não, a lista termina quando o usuário não desejar mais fornecer elementos. Após isto, exiba toda a lista gerada e exiba um menu de opções e programa as ações de cada opção: 1 para acessar um elemento em qualquer posição, selecionada pelo usuário exiba o valor, 2 - para deletar o índice X da lista, 3- deletar um valor qualquer , 4 - terminar edições e EXIBIR a lista editada. Obs.: Considere valores a partir de 1 .

import random
print('='*69)
print('\t\t \t P2 - EXC3')
print('='*69)


Lista = []

while True:
    print ("="*69)
    print ("\t \t \t Digite s para continuar ")
    print ("="*69)
    
    pergunta = input('Deseja adicionar um valor? ')

    if pergunta == 's':
        valor = (input (str("Digite um valor : ")))
        Lista.append(valor)
    
        print ("="*69)
        print ("\t \t \t Digite 1 - para mostrar o qualquer valor da lista")
        print ("\t \t \t Digite 2 - para deletar x valor da lista ")
        print ("\t \t \t Digite 3 - para deletar qualquer valor da lista ")
        print ("\t \t \t Digite 4 - para mostrar sua lista ")
        print ("="*69)  
        pergunta2 = int(input('Qual opção deseja? '))

        if pergunta2 == 1:
            for i,c in enumerate (Lista) : 
                print('valor',c,'esta na posição', i+1) 
            pergunta3 = int(input('Em qual posição se encontra o valor que deseja visualizar ?'))
            print(Lista[pergunta3])                   
        elif pergunta2 == 2:
            Lista.pop(random)
        elif pergunta2 == 3:
            for i,c in enumerate (Lista) : 
                print('valor',c,'esta na posição', i+1) 
            pergunta3 = int(input('Em qual posição se encontra o valor que deseja excluir ?'))
            Lista.pop(pergunta3-1)  
        elif pergunta2 == 4:
            print('Sua lista é:',Lista)
            break
    elif pergunta != 's':
        print('Programa finalizado com sucesso')
        break