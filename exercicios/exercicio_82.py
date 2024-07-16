'''
Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares 
e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''

lista = []
lista_par = []
lista_impar = []
continuar = 'S'

while continuar.upper() == 'S':
    num = int(input('Insira um valor pra lista: '))
    lista.append(num)
    continuar = input('Deseja continuar[S/N]: ')
for num in lista:
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
print('-=' * 30)
print(f'Você gerou a lista: {lista}')
print(f'Lista de números pares: {lista_par}')
print(f'Lista de números ímpares: {lista_impar}')

