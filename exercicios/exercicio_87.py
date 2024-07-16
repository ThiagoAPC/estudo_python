'''
Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.

'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #definindo o tamanho da matriz
lista_pares = list()
lista_terceira_coluna = 0
maior_segunda_coluna = 0

for l in range(0, 3): #especificando o range de linhas e colunas da matriz
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}] da matriz: '))
        if matriz[l][c] % 2 == 0:
            lista_pares.append(matriz[l][c])
        if c == 2:  # Se for a terceira coluna, somar ao total
            lista_terceira_coluna += matriz[l][c]
        if l == 1: #verificar o maior da segunda coluna
            if matriz[l][c] > maior_segunda_coluna:
                maior_segunda_coluna = matriz[l][c]
                
print('-='*30)
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()
print('-='*30)
print(f'A soma dos valores pares é: {sum(lista_pares)}')
print(f'A soma dos valores da terceira coluna é {lista_terceira_coluna}')
print(f'O maior valor da segunda coluna é {maior_segunda_coluna}')