#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

lista = []
for lista_nao_ordenada in range(1,6):
    peso = float(input('Insira o peso da {} pessoa: '.format(lista_nao_ordenada)))
    lista.append(peso)
lista.sort()
print(lista)
print('O maior peso é {} Kg e o menor peso é {} Kg'.format(lista[4], lista[0]))