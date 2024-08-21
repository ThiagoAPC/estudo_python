'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de 
cada aluno individualmente.
'''
continuar = 'S'
lista_dados = list()

while continuar.upper() == 'S':
    while True:
        dados_aluno = list()
        nome = str(input('Insira o nome do aluno: '))
        dados_aluno.append(nome)
        nota1 = float(input('Insira a primeira nota do aluno: '))
        dados_aluno.append(nota1)
        nota2 = float(input('Insira a segunda nota do aluno: '))
        dados_aluno.append(nota2)
        media = (nota1 + nota2) / 2
        dados_aluno.append(media)
        lista_dados.append(dados_aluno[:])
        dados_aluno.clear()
        continuar = str(input('Deseja continuar [S/N]: '))
        if continuar != 'Ss':
            break

print('=='*30)
print(f"{'No.':<5} {'Nome':<20} {'Média':<5}")
print('=='*30)
for i, aluno in enumerate(lista_dados):
    print(f"{i+1:<5} {aluno[0]:<20} {aluno[3]:<5.2f}")
print('=='*30)

while True:
    i = int(input('Selecione o No. de um aluno para ver suas notas (999 interrompe): '))
    if i == 999:
        break
    elif 1 <= i <= len(lista_dados):
        aluno = lista_dados[i-1]
        print(f'\nNotas do Aluno: {aluno[0]}')
        print(f'Nota 1: {aluno[1]}')
        print(f'Nota 2: {aluno[2]}')
        print(f'Média: {aluno[3]}')
    else:
        print('Número inválido, tente novamente')
    