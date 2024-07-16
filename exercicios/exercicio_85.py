'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma 
lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.
'''
lista_geral = [[], []]
valor = 0

for c in range(0,7):
    valor = int(input(f'Digite o {c+1}º valor da lista: '))
    if valor % 2 == 0:
        lista_geral[0].append(valor)
    else:
        lista_geral[1].append(valor)
lista_geral[0].sort()
lista_geral[1].sort()
print(f'Os valores pares da lista são: {lista_geral[0]}')
print(f'Os valores ímpares da lista são: {lista_geral[1]}')