#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

lista_numeros = list() #Lista onde serão armazenados os valores 
continuar = 'S'

def maior(*numeros): #Função que verifica o maior número
    if len(numeros) == 0:
        print('Nenhum valor foi encontrado')
    else:
        maior_numero = max(numeros) 
        print(f'O maior número encontrado foi: {maior_numero}')

while True: #Loop que coloca os valores dentro da lista 
    valor = int(input('Insira um número: '))
    lista_numeros.append(valor)
    continuar = str(input('Deseja contininuar[S/N]: ')).strip().upper()
    if continuar == 'N':
        break

maior(*lista_numeros) #Chamada da função usando a lista como parâmetro



    
