#Crie um programa que leia um numero real qualquer no teclado e mostre sua porção inteira
import math
num = float(input('Digite um numero qualquer real: '))

print('A parte real desse numero é {}'.format(math.floor(num)))
