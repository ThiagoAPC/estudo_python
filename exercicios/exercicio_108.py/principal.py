import moeda

v = float(input('Insira um valor monetário: '))
print(f'{moeda.formatar(v)} aumentado em 10% vale {moeda.formatar(moeda.aumentar(v))}')
print(f'{moeda.formatar(v)} descontado 10% vale {moeda.formatar(moeda.diminuir(v))}')
print(f'{moeda.formatar(v)} tem seu dobro valendo {moeda.formatar(moeda.dobro(v))}')
print(f'{moeda.formatar(v)} tem como sua metade valendo {moeda.formatar(moeda.metade(v))}')
