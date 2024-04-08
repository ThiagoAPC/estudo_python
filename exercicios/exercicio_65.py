'''
Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

lista = []
n = 0
continuar = 'Ss'
contador = 0

while continuar not in 'Nn': 
    n = int(input('Insira um valor inteiro: '))
    lista.append(n)
    contador += 1
    continuar = str(input('Deseja continuar [S/N]: '))
soma = sum(lista)
media = soma / contador
lista.sort()
print('A média dos valores inseridos foi: {:.2f}'.format(media))
print('O menor valor lido foi {} e o maior valor foi {}'.format(lista[0], lista[-1]))

