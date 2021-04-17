print ("="*69)
print ("\t \t \t Questão 2")
print ("="*69)

casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salario? "))
fatura=float(input("Em quantos anos pretende pagar? "))
meses = fatura * 12
parcelas = casa / meses
minimo = (salario / 100) * 30

print('='*69)
print('O valor da casa dividido em', meses , 'meses é de:', parcelas,'por mes.')
print('='*69)

if parcelas < minimo:
    print('seu emprestimo foi aprovado.')
else:
    print('NÂO APROVADO , o valor das parcelas é maior que 30% do seu salário que é de',minimo)
