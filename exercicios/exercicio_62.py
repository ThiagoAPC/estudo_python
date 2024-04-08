#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerrará quando ele disser que quer mostrar 0 termos.
print('Gerador de PA')
print('-=' * 10)
n = int(input('Insira quantos termos você quer saber: '))
a1 = int(input('Insira o primeiro termo: '))
r = int(input('Insira a razão: '))
contador = 1
total = 0
mais = n

while mais != 0:
    total = total + mais
    while contador <= total:
        an = a1 + (contador - 1) * r
        print('{} -> '.format(an), end='')
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você deseja mostrar? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
print('FIM')
