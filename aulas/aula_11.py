'''
Nessa aula, vamos aprender como utilizar a instrução break e os
loopings infinitos a favor das nossas estratégias de código.
É muito importante saber usar o break no Python, 
já que em alguns casos precisamos interromper um laço no meio do caminho.

Além disso, vamos aprender como trabalhar com as novas fstrings do Python.
'''

n = s = 0
while True:
    n = int(input('Insira um valor: '))
    if n == 999:
        break #O comando break interrompe o laço de repetição
    s += n
print(f'A soma vale {s}') #colocar o f no começo é utilizar as fstrings que é uma menira mais fácil de representar os prints