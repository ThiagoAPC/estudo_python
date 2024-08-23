#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
#Guarde esses resultados em um dicionário em Python. 
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint

resultados = {}

resultados['Jogador 1'] = randint(1, 6)
resultados['Jogador 2'] = randint(1, 6)
resultados['Jogador 3'] = randint(1, 6)
resultados['Jogador 4'] = randint(1, 6)

for jogador, resultado in resultados.items():
    print(f'O {jogador} tirou {resultado}')
print('=-'*13)

resultados_ordenados = dict(sorted(resultados.items(), key=lambda item: item[1], reverse=True))

print('= RANKING DOS JOGADORES =')
for i, (jogador, resultado) in enumerate(resultados_ordenados.items(), start=1):
    print(f'Em {i}º lugar: {jogador} com {resultado}')