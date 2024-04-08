#Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
real = float(input('Digite quanto você tem na carteira: '))
dolar = real / 3.27

print('Com {} reais, você pode comprar {} dólares'.format(real, dolar))
