#Escreva um programa que faça o computador "pensar" em numero inteiro de 0 a 5 e peça para o usuário tentar
#advinhar qual o número que foi escolhido pelo computador
import random

num_aleatorio = random.randint(0, 5)
print('Bem vindo ao Jogo da Advinhação!')
num_usuario = int(input('Tente advinhar o número: '))

if num_usuario == num_aleatorio:
    print('Parabéns você acertou!!!')
else:
    print('Não foi dessa vez, você errou! O numero era {}'.format(num_aleatorio))
print('Fim de Jogo!')

