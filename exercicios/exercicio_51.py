#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
#No final, mostre os 10 primeiros termos dessa progressão.

n = int(input('Insira quantos termos você quer saber: '))
a1 = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão: '))
an = 0

for c in range(1,n+1):
    an = a1 + (c - 1) * r
    print('O {} termo vale {}'.format(c, an))