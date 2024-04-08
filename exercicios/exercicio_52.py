#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
print('Analisador de números primos')
num = int(input('Insira o número: '))
total = 0

for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end = '')
        total += 1
    else:
        print('\033[m', end = '')
    print('{} '.format(c), end = '')
print('\n\033[mO número {}, foi divisível \033[34m{}\033[m vezes'.format(num, total))

if total == 2:
    print('Esse número é \033[34mPRIMO\033[m')
else:
    print('Esse número \033[34mNÃO É PRIMO\033[m')
    
    
 