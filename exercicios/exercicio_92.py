dados_pessoais = {}

# Entrada de dados
dados_pessoais['Nome'] = str(input('Insira o nome: '))
ano_nascimento = int(input('Insira o ano de nascimento: '))
dados_pessoais['Idade'] = 2024 - ano_nascimento
dados_pessoais['CPT'] = int(input('Carteira de Trabalho (se não tem coloque 0): '))

# Verifica se a pessoa tem CTPS e coleta mais dados, se necessário
if dados_pessoais['CPT'] != 0:
    dados_pessoais['Ano de Contratação'] = int(input('Ano de Contratação: '))
    dados_pessoais['Salário'] = float(input('Valor do salário: '))
    # Calcula com quantos anos a pessoa vai se aposentar (considerando 65 anos como idade de aposentadoria)
    dados_pessoais['Aposentadoria'] = dados_pessoais['Ano de Contratação'] + 35 - ano_nascimento
else:
    dados_pessoais['CPT'] = 'Não emitida'
    dados_pessoais['Aposentadoria'] = 'Não aplicável'

# Exibição dos dados
print('=-'*30)
for k, v in dados_pessoais.items():
    print(f'{k}: {v}')
