import moeda

v = float(input('Insira um valor monetário: '))
print(f'{moeda.formatar(v)} aumentado em 10% vale {moeda.aumentar(v, True)}')
print(f'{moeda.formatar(v)} descontado 10% vale {moeda.diminuir(v, True)}')
print(f'{moeda.formatar(v)} tem seu dobro valendo {moeda.dobro(v, True)}')
print(f'{moeda.formatar(v)} tem como sua metade valendo {moeda.metade(v, True)}')
