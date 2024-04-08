#Faça um programa que calcule a soma entre  todos os números que são
#múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('''
A soma dos valores é: {}
Foram somados {} numeros'''.format(soma, cont))