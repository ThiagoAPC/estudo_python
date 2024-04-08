#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
import math

angulo = float(input('Insira o valor do angulo: '))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('O angulo {}, tem como:\n-Seno: {:.2f}\n-Cosseno: {:.2f}\n-Tangente: {:.2f}'.format(angulo, sen, cos, tan))


