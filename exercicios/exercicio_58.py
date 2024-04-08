#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar,
#mostrando no final quantos palpites foram necessários para vencer.

import random
num_aleatorio = random.randint(0,10)
tentativas = 0

print('Bem vindo ao jogo da advinhação V2!')
print('Dê um palpite sobre qual número estou pensando!')
num_usuario = int(input('Seu palpite: '))

while num_usuario != num_aleatorio:
    if num_usuario > num_aleatorio:
        print('O número pensado é menor que esse')
        num_usuario = int(input('Seu palpite: '))
    else:
        print('O número pensado é maior que esse')
        num_usuario = int(input('Seu palpite: '))
    tentativas += 1
print('Acertou! Você precisou de {} palpites para acertar que o numero era {}'.format(tentativas, num_aleatorio))
