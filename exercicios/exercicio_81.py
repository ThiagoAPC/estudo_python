lista = []
continuar = 'S'

while continuar.upper() == 'S':
    valor = int(input('Digite um valor para a lista: '))
    lista.append(valor)
    continuar = input('Quer continuar [S/N]: ')

# Ordenando a lista em ordem decrescente
lista.sort(reverse=True)

# Verificando se o valor 5 está na lista
if 5 in lista:
    print('O valor 5 está presente na lista.')
else:
    print('O número 5 não está presente na lista.')

# Exibindo a lista em ordem decrescente
print(f'Esta foi a lista gerada em ordem decrescente: {lista}')

# Exibindo a quantidade de números digitados
print(f'O número de valores digitados na lista foi: {len(lista)}')
