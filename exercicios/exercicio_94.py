"""
Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média
"""
continuar = 'S'
total_pessoas = 0
media_idade = 0

lista_mulheres = list()
lista_acima_media = list()

pessoas = []

while continuar.upper() == 'S':
    pessoa = {}  # Cria um novo dicionário para cada pessoa

    # Coleta do nome
    pessoa['nome'] = str(input('Nome: '))
    
    # Verificação do sexo
    while True:
        sexo = str(input('Sexo [M/F]: ')).upper()
        if sexo in ['M', 'F']:
            pessoa['sexo'] = sexo
            if sexo == 'F':
                lista_mulheres.append(pessoa['nome'])
            break  # Sai do loop se o sexo for 'M' ou 'F'
        else:
            print('Preenchimento incorreto, apenas M ou F')

    # Verificação da idade
    while True:
        try:
            idade = int(input('Idade: '))
            if idade >= 0:
                pessoa['idade'] = idade
                break
            else:
                print('Idade inválida, favor preencher novamente')
        except ValueError:
            print('Idade inválida, favor preencher novamente')
    
    # Adiciona o dicionário da pessoa na lista
    pessoas.append(pessoa)
    
    continuar = str(input('Deseja continuar [S/N]: ')).upper()

# Calcula o total de pessoas e a média de idades
total_pessoas = len(pessoas)
media_idade = sum([p['idade'] for p in pessoas]) / total_pessoas

# Cria a lista de pessoas com idade acima da média
for pessoa in pessoas:
    if pessoa['idade'] > media_idade:
        lista_acima_media.append(pessoa['nome'])

# Exibe os resultados
print('=-'*20)
print(f'O total de pessoas cadastradas foi: {total_pessoas}')
print(f'A média de idades das pessoas é: {media_idade:.2f}')
print(f'As mulheres cadastradas foram: {lista_mulheres}')
print(f'As pessoas com idade acima da média são: {lista_acima_media}')

