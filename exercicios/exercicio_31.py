#Desenvolva um programa que leia a distância de uma viagem em Km, cobrando R$0,50 por Km rodado
#em viagens de até 200 Km, e R$0,45 para viagens mais longas que isso
distancia = int(input('Insira a distância da sua viagem: '))
if distancia <= 200:
    preco = distancia * 0.50 
    print('O preço da sua viagem será: {}'.format(preco))
else:
    preco = distancia * 0.45
    print('O preço da sua viagem será {}'.format(preco))