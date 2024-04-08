#Faça um program que mostre se um número é par ou ímpar
num = int(input('Insira um número inteiro: '))

if num % 2 == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é ímpar'.format(num))