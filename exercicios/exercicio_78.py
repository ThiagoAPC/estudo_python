'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
lista = []
maior = 0
menor = 0

for p in range(0, 5):
    lista.append(int(input(f'Insira um valor para a posição {p+1}: ')))
print('=-'*30)
print(f'Voce adicionou os valores: {lista}')
lista.sort()

maior = lista[-1]
menor = lista[0]

print(f'O maior valor da lista é: {maior}')
print(f'O menor valor da lista é: {menor}')




