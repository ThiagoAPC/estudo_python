'''
Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''

print('Insira os dois valores')
valor1 = float(input('Insira o valor 1: '))
valor2 = float(input('Insira o valor 2: '))

operacao = 0

while operacao != 5:
    print('''
Selecione uma das opções abaixo:          
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    
    print('Voce informou os valores {} e {}, o que quer fazer com eles?'.format(valor1, valor2))
    operacao = int(input('Sua opção: '))
    if operacao == 1:
        resultado = valor1 + valor2
        print('{} + {} = {}'.format(valor1, valor2, resultado))
    elif operacao == 2:
        resultado = valor1 * valor2
        print('{} x {} = {}'.format(valor1, valor2, resultado))
    elif operacao == 3:
        if valor1 > valor2:
            print('O maior valor é {}'.format(valor1))
        elif valor1 < valor2:
            print('O maior valor é {}'.format(valor2))
        else:
            print('Os valores são iguais')
    elif operacao == 4:
            print('Informe os novos valores: ')
            valor1 = float(input('Insira o valor 1: '))
            valor2 = float(input('Insira o valor 2: '))
    else:
        print('Fim!')



