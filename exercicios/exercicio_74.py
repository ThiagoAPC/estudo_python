'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint

aleatorios = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)) #aqui usamos randint 5 vezes pra definir os 5 valores da tupla
print(f'A tupla com os valores aleatórios é: {aleatorios}')

ordenados = sorted(aleatorios)
print(f'A tupla com os valores ordenados fica: {ordenados}')
print(f'O menor valor da tupla é {ordenados[0]}')
print(f'O maior valor da tupla é {ordenados[-1]}')

