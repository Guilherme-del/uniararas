""""
Exercício 5 
p = 7 q = 5 
Exercício 5: Dados e , utilize as operações relacionais para verificar os segunites itens: 

(a)  (b)  
(p E q) > 5 (p OU q) > 5

https://colab.research.google.com/drive/1iXfNKrt6rjH1t4kmAXLPAggF-M6xmUrG#scrollTo=R2_E6DdVHDCH&printMode=true 5/28 
07/03/2022 09:22 ALUNOS1_Revisão_Python.ipynb - Colaboratory 
(c) Não (p > 3) 
ESTRUTURAS CONDICIONAIS 
As estruturas condicionais são utilizadas para tomadas de decisões do tipo "Se algo, então...". Basicamente temos a seguinte sintaxe: if <condicao>**:** 
<bloco de comandos a ser executado> 
else: 
<bloco de comandos a ser executado> 
OBS.: A identação é obrigatória em Python para indicar o que será considerado na condicional. 
Muitas vezes é necessário ter uma outra condição entre o if e o else, então uma das possibilidades é utilizar o comando elif, ou seja: if <condicao 1>**:** 
<bloco de comandos a ser executado> 
elif <condicao 2>**:** 
<bloco de comandos a ser executado> 
else: 
<bloco de comandos a ser executado> 
"""

p=7
q=5

#A
print('comparação: (maior que 5 |E|)',(p&q) > 5)
#B
print('comparação: (maior que 5 |OU|)',(p or q) > 5 )
#C
print('not in: ', not(p>5) )