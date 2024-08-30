import moeda

v = float(input('Insira um valor monetário: '))
print(f'{v} aumentado em 10% vale {moeda.aumentar(v)}')
print(f'{v} descontado 10% vale {moeda.diminuir(v)}')
print(f'{v} tem seu dobro valendo {moeda.dobro(v)}')
print(f'{v} tem como sua metade valendo {moeda.metade(v)}')
