'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados 
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
from random import randint

lista_jogos = list()
cont = 0
cont_jogos = 0

print('='*30)
print('        Jogos Mega Sena     ')
print('='* 30)
num_jogos = int(input('Insira quantos jogos você quer: '))
while cont_jogos < num_jogos:
    jogo = list()
    while len(jogo)<=5: #Este while monta uma lista com 5 valores aleatórios pra mega sena
        num = randint(1,60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    lista_jogos.append(jogo[:]) #Nessa parte ele anexa na lista_jogos uma cópia do jogo que ele gerou antes
    jogo.clear() #Aqui ele apaga o jogo original, pra lista ficar vazia e ele começar o loop novamente
    cont_jogos += 1 #Ele adiciona 1 ao contador pra que o loop gere a quantidade de jogos que foi pedida
print(f'Os jogos gerados foram:')

for i, jogo in enumerate(lista_jogos):
    print(f'{i+1}º jogo gerado: {jogo}')