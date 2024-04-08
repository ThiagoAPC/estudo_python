#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
preco = float(input('Insira o preço atual: '))

precoD = preco - (preco * 5/100)

print('O produto que tinha preço {} reais, agora com desconto de 5% custa: {} reais'.format(preco, precoD))
