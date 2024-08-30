#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome, gols=0):
    print('-'*30)
    print(f'Nome do Jogador: {nome} \nGols Marcados: {gols}')
    print('-'*30)

# Solicitação dos dados
nome = str(input('Insira o nome do jogador: ')).strip()
gols = input('Insira quantos gols o jogador marcou: ')

# Verificação e conversão de valores
if gols.isdigit():
    gols = int(gols)
else:
    gols = 0

# Chamada da função
ficha(nome if nome != '' else '<desconhecido>', gols)
