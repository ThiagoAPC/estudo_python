'''
Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
'''
cont18 = contH = contM20 = 0
idade = 0
sexo = ''
continuar = 'S'

while True:
    print('-' * 20)
    print(f'CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Insira uma idade: '))
    sexo = str(input('Insira um sexo [M/F]: ')).upper() 
    
    if idade > 18:
        cont18 += 1     
    if sexo == 'M':
        contH += 1
    if sexo == 'F' and idade < 20:
        contM20 += 1 

    continuar = str(input('Deseja continuar [S/N]? ')).upper()
    if continuar != 'S':
        break
print('-' * 20)
print(f'Foram cadastrados:\n{cont18} pessoa com mais de 18 anos\n{contH} homens\n{contM20} mulheres com menos de 20 anos')
print('-' * 20)