'''
Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint

n = m = cont = soma = 0
opcao = ''

print('~-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('~-' * 20)

while True:
    m = randint(0, 10)  
    n = int(input('Insira um valor: '))
    opcao = str(input('Insira se a soma vai dar par ou ímpar [P/I]: ')).upper()
    soma = n + m
    if soma % 2 == 0 and opcao == 'P':
        print('--' * 20)
        print(f'Você jogou {n}, o computador jogou {m}, a soma deu {soma} esse valor é par!')
        print('Você ganhou!')
        print('--' * 20)
        cont += 1
    elif soma % 2 != 0 and opcao == 'I':
        print('--' * 20)
        print(f'Você jogou {n}, o computador jogou {m}, a soma deu {soma} esse valor é ímpar!')
        print('Voce ganhou!')
        print('--' * 20)
        cont += 1
    elif soma % 2 != 0 and opcao == 'P':
        print('--' * 20)
        print(f'Você jogou {n}, o computador jogou {m}, a soma deu {soma} esse valor é ímpar!')
        print('Você perdeu!')
        print('--' * 20)
        break
    elif soma % 2 == 0 and opcao == 'I':
        print('--' * 20)
        print(f'Você jogou {n}, o computador jogou {m}, a soma deu {soma} esse valor é par!')
        print('Voce perdeu!')
        print('--' * 20)
        break
print('~-' * 20)
print(f'Fim de jogo, você ganhou {cont} vezes!')
print('~-' * 20)



