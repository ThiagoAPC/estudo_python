#Faça um programa que leia um número qualquer e mostre o seu fatorial.

print('Calculando fatorial')

n = int(input('Insira o numero: '))
c = n
f = 1
print('{}! = '.format(n), end = '')

while c > 0:
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c
    c -= 1
print(f, end = '')