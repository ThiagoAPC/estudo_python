#Escreva um programa que leia a velocidade de um carro e se for acima de 80 km/h, mostre uma mensagem dizendo
#que ele foi multado e mostre o valor da multa que corresponde a (x - 80)* 7.00

velocidade = float(input('Insira a sua velocidade: '))

if velocidade > 80.00:
    multa = (velocidade - 80.00) * 7.00
    print('Você foi multado em R${:.2f} por estar a {} km/h em uma via onde a velocidade máxima é 80 km/h'.format(multa, velocidade))
