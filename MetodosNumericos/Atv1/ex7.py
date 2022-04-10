""""
Exercício 7 
Exercício 7: Crie um código em que dado um valor x, ele imprime na tela se este valor é poisitivo, negativo ou nulo. 
GERAR SEQUÊNCIA NUMÉRICA 
Uma maneira muito simples de gerar uma sequência numérica em Python é por meio do comando range(). Para a sua utilização, temos de maneira geral que: 
range(valor_início, valor_término, incremento) 
sendo 
valor inicio : 
 indica em que valor começa a sequência. Trata-se de um parâmetro opcional (quando não inserido, o padrão é iniciar do zero). 
valor termino : 
 a sequência finaliza no primeiro valor antes do valor de término. Este é um parâmetro obrigatório. 

incremento :
 indica de quanto em quanto a sequência será construída. Este é um parâmetro opcional (quando não inserido, será 

utilizado o incremento 1). 
Uma forma de observar o que o range construiu é transformá-lo em uma lista e pedir para imprimí-la, ou seja, utilizando o comando: 
https://colab.research.google.com/drive/1iXfNKrt6rjH1t4kmAXLPAggF-M6xmUrG#scrollTo=R2_E6DdVHDCH&printMode=true 7/28 
07/03/2022 09:22 ALUNOS1_Revisão_Python.ipynb - Colaboratory 
list(range(estrutura_desejada)) 
"""


x = float(input('Digite um número para saber se é positivo ou negativo:'))

if x > 0:
  print('seu valor é positivo')
elif x<0:
  print('seu valor é negativo')
else:
  print('seu valor é nulo')