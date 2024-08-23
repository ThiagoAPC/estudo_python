# Lista para armazenar a ficha de vários jogadores
jogadores = []

while True:
    ficha_jogador = {}  # Dicionário para armazenar os dados de um jogador
    
    ficha_jogador['Nome'] = str(input('Nome do Jogador: '))
    num_partidas = int(input(f'Número de jogos que {ficha_jogador["Nome"]} jogou: '))

    ficha_jogador['Gols por partida'] = []

    for partida in range(1, num_partidas + 1):
        gols = int(input(f'Gols marcados na partida {partida}: '))
        ficha_jogador['Gols por partida'].append(gols)

    ficha_jogador['Total de Gols'] = sum(ficha_jogador['Gols por partida'])

    jogadores.append(ficha_jogador)  # Adiciona a ficha do jogador à lista de jogadores
    
    continuar = input('Deseja cadastrar outro jogador? [S/N]: ').upper()
    if continuar == 'N':
        break

# Exibindo as fichas dos jogadores
print('=-' * 20)
print('Fichas dos Jogadores:')
print('=-' * 20)
for idx, jogador in enumerate(jogadores):
    print(f"{idx + 1}. Nome: {jogador['Nome']} - Total de Gols: {jogador['Total de Gols']}")

# Sistema de visualização de detalhes
while True:
    escolha = input('Deseja ver o detalhamento de qual jogador? (Informe o número ou digite "sair" para encerrar): ').strip()
    
    if escolha.lower() == 'sair':
        break
    
    if escolha.isdigit():
        escolha = int(escolha) - 1
        if 0 <= escolha < len(jogadores):
            jogador = jogadores[escolha]
            print(f"Detalhamento do jogador {jogador['Nome']}:")
            for i, gols in enumerate(jogador['Gols por partida']):
                print(f"  Partida {i + 1}: {gols} gols")
            print(f"  Total de Gols: {jogador['Total de Gols']}")
        else:
            print('Jogador não encontrado. Tente novamente.')
    else:
        print('Entrada inválida. Tente novamente.')
