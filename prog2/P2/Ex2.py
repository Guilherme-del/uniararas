#A professora Larissa gostaria de criar uma rotina que seja capaz de calcular a nota de seus alunos referente a N1. Suponha que os alunos realizem 6 avaliações . Os testes de 1 a 4 sua média tem peso 0,7 e as atividades 5 e 6 tem peso 0.1 e 0.2 respectivamente. Receba as notas e exiba ao final do programa a nota calculada.
print('='*69)
print('\t\t \t P2 - EXC2')
print('='*69)

notas = []
soma = 0
try:
    for i in range(6): 
        soma+= 1
        mensagem = 'Qual a nota da prova ' , soma , '?'
        notas.append(float(input(mensagem)))      
except ValueError:
    print("Apenas numeros são aceitos")
    raise

nota1 = notas[0]*0.7
nota2 = notas[1]*0.7
nota3 = notas[2]*0.7
nota4 = notas[3]*0.7

nota5 = notas[4]*0.1
nota6 = notas[5]*0.2

notareal = []
notareal.append(float(round(nota1,2)))  
notareal.append(float(round(nota2,2))) 
notareal.append(float(round(nota3,2))) 
notareal.append(float(round(nota4,2))) 
notareal.append(float(round(nota5,2))) 
notareal.append(float(round(nota6,2))) 

print ('Notas', notareal)


