#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular 
# (largura e comprimento) e mostre a área do terreno.

def area(b, h):
    a = b * h
    print(f'O terreno de {b} m x {h} m, tem área igual {a} m²')

print('CONTROLE DE DIMENSÕES DE TERRENO')
print('-'*15)
print('Insira as dimensões do terreno')
b = float(input('Largura (metros): '))
h = float(input('Comprimento (metros): '))
print('-'*15)
area(b, h)