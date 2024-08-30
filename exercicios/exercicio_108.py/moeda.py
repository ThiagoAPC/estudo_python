def aumentar(valor):
    res = valor + (valor / 10)
    return res

def diminuir(valor):
    res = valor - (valor / 10)
    return res

def dobro(valor):
    res = valor * 2
    return res


def metade(valor):
    res = valor / 2
    return res

def formatar(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')

