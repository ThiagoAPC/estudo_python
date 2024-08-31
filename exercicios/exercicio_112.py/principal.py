#Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. 
#Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.

from utilidadesCeV import moeda, dado

v = dado.leia_dinheiro('Insira um valor monetário: ')
aumento_percentual = float(input('Insira a porcentagem de aumento: '))
reducao_percentual = float(input('Insira a porcentagem de redução: '))
moeda.resumo(v, aumento=aumento_percentual, reducao=reducao_percentual, format=True)
