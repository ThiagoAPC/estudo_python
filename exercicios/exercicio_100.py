#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai 
# mostrar a soma entre todos os valores pares sorteados pela função anterior.
import random
numeros = list()
numeros_pares = list()
contador = 0
soma = 0

def sorteia():
    numero_aleatorio = random.randint(0, 100)
    numeros.append(numero_aleatorio)

def somaPar():
    global soma
    for n in numeros:
        if n % 2 == 0:
            numeros_pares.append(n)
    soma = sum(numeros_pares)

while contador < 5:
    sorteia()
    contador += 1

somaPar()

print(f'Os números sorteados foram: {numeros}')
print(f'Os números pares são: {numeros_pares}')
print(f'A soma dos números pares dessa lista é: {soma}')
