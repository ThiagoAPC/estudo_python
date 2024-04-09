# Cabeçalho do programa
print('-' * 20)
print('SUPER MERCADO BARATÃO')
print('-' * 20)

# Inicialização das variáveis
total = 0  # Total gasto na compra
mais100 = 0  # Contador de produtos que custam mais de R$1000
contmenor = 0  # Contador para identificar o primeiro produto
barato = ''  # Nome do produto mais barato

# Loop principal para cadastro de produtos
while True:
    produto = str(input('Insira o nome do produto: '))
    preco = float(input('Insira o preço do produto: R$ '))
    contmenor += 1  # Incrementa contador de produtos para verificar o primeiro produto
    total += preco  # Acumula o preço do produto ao total gasto
    
    # Verifica se o produto custa mais de R$1000
    if preco > 1000:
        mais100 += 1
    
    # Verifica se é o primeiro produto ou se é mais barato que o atual mais barato
    if contmenor == 1 or preco < menor:
        menor = preco
        barato = produto

    # Loop para verificar se o usuário deseja continuar
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    
    # Verifica se o usuário não deseja continuar
    if resp == 'N':
        break

# Impressão dos resultados
print('-' * 20)
print(f'O total da compra foi: R${total:.2f}')
print(f'O número de produtos que custam mais de R$1000.00 é: {mais100}')
print(f'O produto mais barato foi {barato} custando: R${menor:.2f}')
print('{:-^40}'.format('FIM DO PROGRAMA'))
