'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

lista = []
continuar = 'S'

while continuar.upper() == 'S':
    valor = int(input(f'Adicione o {len(lista) + 1}º valor da lista: '))
    
    if valor in lista:
        print('Valor já foi adicionado. Tente novamente.')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    
    continuar = input('Quer continuar [S/N]: ')

print('Os valores adicionados foram:', lista)


        
