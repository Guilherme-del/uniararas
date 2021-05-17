print ("="*69)
print ("\t \t \t Teste de conhecimento 4 - Exercicio 3")
print ("="*69)

login = []
senha = []

usuario = input('Adicione um usuario : ')
password = input('Adicione uma senha para seu usuario : ')

login.append(usuario)
senha.append(password)

print ("="*69)
print ("\t \t \t Agora vamos confirmar o usuario e a senha escolhida pelo usuario. ")
print ("="*69)

loginentrada = input('confirme o usuario: ')
senhaentrada = input('corfirme a senha: ')  

#print(login)
#print(senha)

if (loginentrada == login[0]) and (senhaentrada == senha[0] )  :
    print('!!Acess garanted!!')
else: 
    while (loginentrada != login) and (senhaentrada != senha ) :       
        print ("="*69)   
        print ("\t \t \t Usuario ou senha incorreta tente novamente ")
        print ("="*69)
        loginentrada = input('confirme o usuario: ')
        senhaentrada = input('corfirme a senha: ')             
