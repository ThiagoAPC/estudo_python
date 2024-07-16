'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''

valor1 = int(input('Insira o 1º valor: '))
valor2 = int(input('Insira o 2º valor: '))
valor3 = int(input('Insira o 3º valor: '))
valor4 = int(input('Insira o 4º valor: '))

valores = (valor1, valor2, valor3, valor4)

print(valores)

print(f'O número 9 apareceu {valores.count(9)} vezes')

if 3 in valores:
    print(f'O primeiro número 3 está na posição {valores.index(3)}')
else:
    print(f'O número 3 não está presente nesta tupla')

pares = [valor for valor in valores if valor % 2 == 0]

print(f'Os valores pares são: {pares}')


