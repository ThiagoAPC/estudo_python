'''
Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o 
programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
'''

#Cabeçalho do programa
print('-' * 20)
print('CAIXA ELETRÔNICO')
print('-' * 20)

#Inicialização de variáveis

saque = 0
cont_50 = 0
cont_20 = 0 
cont_10 = 0
cont_1 = 0

saque = int(input('Insira o valor que quer sacar: R$'))
total = saque

#Loop principal
while True: 
#Calculo para numero de notas de 50
    if saque >= 50:
        saque -= 50
        cont_50 +=1
#Calculo para numero de notas de 20
    elif saque >= 20:
        saque -= 20
        cont_20 += 1
#Calculo para numero de notas de 10
    elif saque >= 10:
        saque -= 10
        cont_10 += 1
#Calculo para numero de notas de 1
    elif saque >= 1:
        saque -= 1
        cont_1 += 1
    else:
        break

#Exibição dos valores
print('-' * 20)
print(f'Valor a ser sacado: R${total}')
print(f'O número de cédulas de 50 será: {cont_50}')
print(f'O número de cédulas de 20 será: {cont_20}')
print(f'O número de cédulas de 10 será: {cont_10}')
print(f'O número de cédulas de 1 será: {cont_1}')
print('-' * 20)
print('FIM DO PROGRAMA')
