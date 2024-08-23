"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

ficha_jogador = {}

ficha_jogador['Nome: '] = str(input('Nome do Jogador: '))
num_partidas = int(input('Numero de jogos: '))

ficha_jogador['Gols por partida'] = []

for partida in range(1, num_partidas + 1):
    gols = int(input(f'Gols marcados na {partida}: '))
    ficha_jogador['Gols por partida'].append(gols)

ficha_jogador['Total de Gols'] = sum(ficha_jogador['Gols por partida'])

print(ficha_jogador)