#Monte um programa que pergunte o valor do salário e aplique um aumento de 10% para salários acima de R$1250,00
# e 15% para salários ATÉ R$1250,00

salario = float(input('Insira o seu salário: '))

if salario <= 1250:
    aumento = salario + (salario * 15/100)
else:
    aumento = salario + (salario * 10/100)
print('O seu salário de {:.2f}, sofreu um aumento e agora vale é: {:.2f}'.format(salario, aumento))
