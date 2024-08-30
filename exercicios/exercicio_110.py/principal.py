from moeda import resumo

v = float(input('Insira um valor monetário: '))
aumento_percentual = float(input('Insira a porcentagem de aumento: '))
reducao_percentual = float(input('Insira a porcentagem de redução: '))
resumo(v, aumento=aumento_percentual, reducao=reducao_percentual, format=True)
