print('='*69)
print('\t\t \t SCHOOLNET - ATV3')
print('='*69)

import time

while True:
    print('Seja Bem vindo')        
    nome = (str(input('Qual seu nome? ')))    
    print ('Se seu nome for ',nome,'digite sim se não digite não')
    x = input('')
    if x == (('sim') or ('Sim')):
        print ('uhul!!!Só mais um passo até seu cadastro estar completo')
        time.sleep(1)
        CPF= (float(input('digite seu CPF? (somente numeros): ')))
        if CPF.is_integer():
             print ('Cadastro concluido com sucesso')
             time.sleep(1)
             break
        else:
             print ('Cpf não encontrado na base governamental reiniciando cadastro')
             time.sleep(2)
    elif x!= 'sim':       
        print ('Tente novamente')
        time.sleep(2)
                    