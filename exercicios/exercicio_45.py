#Crie um programa que faça o computador jogar Jokenpô com você
from random import randint

item = ('PEDRA', 'PAPEL', 'TESOURA')
jogada_computador = randint(0, 2)

print('''JOKENPÔ     
Digite o número de uma das opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
~~~~~~~~~~~~~~~~~~''')
jogada_player = int(input('Número da sua opção: ')) - 1

if jogada_player not in [0, 1, 2]:
    print('Jogada Inválida')
else:
    print('Você escolheu: {}'.format(item[jogada_player]))
    print('O computador escolheu: {}'.format(item[jogada_computador]))
    if jogada_computador == 0: #COMPUTADOR ESCOLHEU PEDRA
        if jogada_player == 0:
            print('EMPATE!')
        elif jogada_player == 1: #JOGADOR ESCOLHEU PAPEL
            print('VITÓRIA')
        elif jogada_player == 2: #JOGADOR ESCOLHEU TESOURA
            print('DERROTA')   
    elif jogada_computador == 1: #COMPUTADOR ESCOLHEU PAPEL
        if jogada_player == 1:
            print('EMPATE')
        elif jogada_player == 0: #JOGADOR ESCOLHEU PEDRA
            print('DERROTA')
        elif jogada_player == 2: #JOGADOR ESCOLHEU TESOURA
            print('VITÓRIA')
    elif jogada_computador == 2: #COMPUTADOR ESCOLHEU TESOURA
        if jogada_player == 2:
            print('EMPATE')
        elif jogada_player == 1: #JOGADOR ESCOLHEU PAPEL
            print('DERROTA')
        elif jogada_player == 0: #JOGADOR ESCOLHEU PEDRA
            print('VITÓRIA')
