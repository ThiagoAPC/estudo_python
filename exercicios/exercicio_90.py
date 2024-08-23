#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
#No final, mostre o conteúdo da estrutura na tela.

dados_aluno = {}
dados_aluno['Nome'] = str(input('Insira o nome do aluno: '))
dados_aluno['Média'] = float(input('Insira a média do aluno: '))
if dados_aluno['Média'] < 6.0 and dados_aluno['Média'] >= 5.0:
    dados_aluno['Situação'] = 'Recuperação'
elif dados_aluno['Média'] < 5.0:
    dados_aluno['Situação'] = 'Reprovado'
else:
    dados_aluno['Situação'] = 'Aprovado'
print('=-'*30)

for k, v in dados_aluno.items():
    print(f'{k} é {v}')