#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.

n = int(input('Insira quantos termos você quer saber: '))
a1 = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão: '))

contador = 1

while contador <= n:
    an = a1 + (contador - 1)* r
    print('O {}º termo vale: {}'.format(contador, an))
    contador += 1
print('Fim')
