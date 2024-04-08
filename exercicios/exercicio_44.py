'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal 
e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros
'''

print('Pagamento do Produto')

preco = float(input('Insira o preço do produto do cliente: '))

print('''Formas de Pagamento:
[ 1 }à vista dinheiro/cheque: 10% de desconto

[ 2 ] à vista no cartão: 5% de desconto

[ 3 ] em até 2x no cartão: preço formal 

[ 4 ] 3x ou mais no cartão: 20% de juros
      ''')

forma_pagamento = str(input('Digite qual opção de pagamento você deseja: '))

if forma_pagamento == '1':
    preco_total = preco - (preco * 0.1)
    print('''
VALOR TOTAL: R${:.2f}
VALOR À PAGAR: R${:.2f} '''.format(preco, preco_total))
    
elif forma_pagamento == '2':
    preco_total = preco - (preco * 0.05)
    print('''
VALOR TOTAL: R${:.2f}
VALOR À PAGAR: R${:.2f}'''.format(preco, preco_total))
    
elif forma_pagamento == '3':
    preco_total = preco/2
    print('''
VALOR TOTAL: R${:.2f}
VALOR À PAGAR: 2x de R${:.2f}'''.format(preco, preco_total))

elif forma_pagamento == '4':
    num_parcelas = int(input('Insira o número de parcelas: '))
    preco_total = (preco + (preco * 0.2)) / num_parcelas
    print('''
VALOR TOTAL: R${:.2f}
VALOR À PAGAR: {}x de R${:.2f}, com 20% de juros aplicados'''.format(preco, num_parcelas, preco_total))


else:
    print('ERRO! Selecione o número de uma das opções disponíveis!')


