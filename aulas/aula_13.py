'''
Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. 
As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves individuais.
'''
num = [2, 5, 2, 9, 1, 2]

#alterar valor em uma posição da lista [2, 5, 3, 1]
num[2] = 3
#adicionar elemento à lista [2, 5, 3, 1, 7]
num.append(7)
#ordenação da lista [1, 2, 3, 5, 7]
num.sort()
#ordenação reversa da lista [7, 5, 3, 2, 1]
num.sort(reverse = True)
#adicionar elemnto em uma posição específica [7, 5, 0, 3, 2, 1]
num.insert(2, 0)
#remoção de elementos [7, 5, 0, 3, 2]
num.pop()
#remoção de elementos específicos [7, 5, 3, 2]
num.pop(2)
#eliminando o primeiro elemento especificado que encontrar na lista [9, 7, 5, 3, 2]
num.remove(2)

print(num)
print(f'Essa lista tem {len(num)} elemntos')
print('-'*10)

valores = list()
valores.append(1)
valores.append(2)
valores.append(3)
valores.append(4)

#Marcação de posição na lista e valor do elemnto
print(valores)
for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor: {v}')

#Criar uma cópia de uma lista
A = [2, 3, 4, 5, 6]
B = A[:]
#Modificação indidvidual de listas
B[2] = 7

print(f'A lista A: {A}')
print(f'A lista B: {B}')    
