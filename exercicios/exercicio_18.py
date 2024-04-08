#Faça um programa que leia os catetos oposto e adjacente de um triângulo e mostre a hipotenusa
import math
cat_op = float(input('Digite o cateto oposto: '))
cat_aj = float(input('Digite o cateto adjacente: '))

hip = math.sqrt(pow(cat_op, 2) + pow(cat_aj, 2))

print('A soma dos catetos {} com {}, resulta em uma hipotenusa igual a: {} '.format(cat_op, cat_aj, hip))


