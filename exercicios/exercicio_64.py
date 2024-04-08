'''
Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
contador = 0
soma = 0
n = 0
n = int(input('Insira um numero para ser somado ou digite 999 para sair: '))

while n != 999:
    soma += n
    contador += 1
    n = int(input('Insira um numero para ser somado ou digite 999 para sair: '))
print('A soma dos números deu {} e foram somados {} números'.format(soma, contador))
