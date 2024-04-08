#Faça um programa que leia 3 números e mostre qual o maior e qual o menor 
a = int(input('Insira o primeiro numero: '))
b = int(input('Insira o segundo numero: '))
c = int(input('Insira o terceiro numero: '))

maior = a
menor = a

if b > maior:
    maior = b
if c > maior:
    maior = c

if b < menor:
    b = menor
if c < menor:
    c = menor

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))


