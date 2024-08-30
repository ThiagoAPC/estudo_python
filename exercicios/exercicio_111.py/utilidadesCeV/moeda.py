def aumentar(valor, percentual=10, format=False):
    
    res = valor + (valor * percentual / 100)
    return res if not format else formatar(res)

def diminuir(valor, percentual=10, format=False):
    res = valor - (valor * percentual / 100)
    return res if not format else formatar(res)

def dobro(valor, format=False):
    res = valor * 2
    return res if not format else formatar(res)

def metade(valor, format=False):
    res = valor / 2
    return res if not format else formatar(res)

def formatar(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')

def resumo(valor, aumento=10, reducao=10, format=True):
    print('-'*30)
    print('Resumo do Valor'.center(30))
    print('-'*30)
    print(f'O valor analisado foi: {formatar(valor) if format else valor}')
    print(f'Dobro do valor: {dobro(valor, format)}')
    print(f'Metade do valor: {metade(valor, format)}')
    print(f'{aumento}% de aumento: {aumentar(valor, aumento, format)}')
    print(f'{reducao}% de redução: {diminuir(valor, reducao, format)}')
    print('-'*30)
