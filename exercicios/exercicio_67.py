'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.
'''

n = 0

while True:
    n = int(input('Insira um número inteiro: '))
    if n < 0:
        break
    print('-' * 20)
    for c in range(0,11):
        print(f'{n} x {c} = {n*c}, ')
    print('-' * 20)
print('Acabou!')