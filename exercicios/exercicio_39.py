'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

idade = int(input('Insira sua idade: '))

if idade == 18:
    print('Você deve se alistar!')
elif idade > 18:
    tempo_atrasado = idade - 18
    print('Voce deveria ter se alistado a {} anos, voce se alistou?'.format(tempo_atrasado))
elif idade < 18:
    tempo_restante = 18 - idade
    print('Ainda não está na hora de se alistar mas faltam {} anos'.format(tempo_restante))
