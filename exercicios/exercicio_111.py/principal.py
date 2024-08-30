from utilidadesCeV import moeda, dado

v = dado.leia_dinheiro('Insira um valor monetário: ')
aumento_percentual = float(input('Insira a porcentagem de aumento: '))
reducao_percentual = float(input('Insira a porcentagem de redução: '))
moeda.resumo(v, aumento=aumento_percentual, reducao=reducao_percentual, format=True)
