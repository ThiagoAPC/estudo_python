def aumentar(valor, format=False):
    res = valor + (valor / 10)
    return res if format is False else formatar(res)

def diminuir(valor, format=False):
    res = valor - (valor / 10)
    return res if format is False else formatar(res)

def dobro(valor, format=False):
    res = valor * 2
    return res if format is False else formatar(res)


def metade(valor, format=False):
    res = valor / 2
    return res if format is False else formatar(res)

def formatar(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')

