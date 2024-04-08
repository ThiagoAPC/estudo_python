#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Insira o seu sexo[M/F]: '))

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Valor inválido, digite da maneira correta [M/F]: '))
print('O seu sexo é {}'.format(sexo))