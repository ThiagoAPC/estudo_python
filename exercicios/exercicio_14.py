#Faça um algoritmo que leia o salário de um funcionário e mostre-o com 15% de aumento
salario = float(input('Insira o salário atual: '))

reajustado = salario + (salario * 15/100)

print('O seu salário era {} reais, agora com aumento de 15% é: {} reais'.format(salario, reajustado))
