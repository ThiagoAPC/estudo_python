#Elabore um algoritmo que leia a largura e a altura de uma parede em metros, calcule a sua área e quantidade
#de tinta necesseária para pinta-la sabendo que sabendo que cada litro de tinta pinta 2 metros quadrados

a = float(input('Insira a altura em metros: '))
l = float(input('Insira a largura em metros: '))

area = a * l
tinta = area / 2 

print('Uma parede de {} metros quadrados precisa de {} litros de tinta para ser pintada'.format(area, tinta))