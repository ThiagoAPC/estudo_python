'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caneta', 1.00,
            'Apontador', 2.50,
            'Régua', 3.00,
            'Caixa de Lápis de Cor', 124.00,
            'Lapiseira 0.5', 8.00)
print('-'* 60)
print(f'{"LISTAGEM DE PREÇOS": ^60}')
print('-'* 60)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<60}', end = '')
    else:
        print(f'R$ {listagem[pos]: >8.2f}')
print('-'* 60)

