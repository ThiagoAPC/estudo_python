lista_pessoa = []
lista_geral = []
continuar = 'S'
contador = 0
maior = menor = 0

while continuar.upper() == 'S':
    nome = str(input('Insira o nome da pessoa: '))
    peso = float(input('Insira o peso da pessoa: '))
    lista_pessoa.append(nome)
    lista_pessoa.append(peso)
    
    if len(lista_geral) == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    
    lista_geral.append(lista_pessoa[:])  # Cria uma cópia da lista_pessoa para armazenar na lista_geral
    lista_pessoa.clear()
    contador += 1
    continuar = input('Deseja continuar [S/N]: ')

# Exibe a quantidade de pessoas cadastradas
print(f'Foram cadastradas: {contador} pessoas')

# Exibe a lista geral de pessoas
print(f'Lista de pessoas: {lista_geral}')

# Exibe as pessoas com o maior peso
print(f'O maior peso é: {maior} kg. Peso de ', end='')
for pessoa in lista_geral:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}] ', end='')

print()

# Exibe as pessoas com o menor peso
print(f'O menor peso é: {menor} kg. Peso de ', end='')
for pessoa in lista_geral:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}] ', end='')

print()
