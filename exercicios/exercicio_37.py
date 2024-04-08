#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer 
#e peça para o usuário escolher qual
#será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('Conversor de bases de números')

numero = int(input('Insira o número que deseja converter: '))

print('''Escolha a base para conversão: 
    (A) Binário
    (B) Octal
    (C) Hexadecimal''')

base = str(input('Insira a letra correspondente da base desejada: '))

if base == 'A':
    print('O valor {} em binário equivale a {}'.format(numero, bin(numero)[2:]))
    #Note que eu inseri esse [2:] pra ele não mostrar o tipo numérico, ele vai pular as posições que mostram isso
elif base == 'B':
    print('O valor {} em octal equivale a {}'.format(numero, oct(numero)[2:]))
elif base == 'C':
    print('O valor {} em hexadecimal equivale a {}'.format(numero, hex(numero)[2:]))
else:
    print('Insira uma opção que está na lista!')

   
