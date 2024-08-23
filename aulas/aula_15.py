"""
Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em  Python. 
Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
acessíveis por chaves literais.
"""

# Introdução aos Dicionários em Python

# Em Python, um dicionário é uma coleção de pares chave-valor. 
# Cada chave é única dentro do dicionário e é usada para acessar o valor correspondente.

# Criando um dicionário básico
meu_dicionario = {
    'nome': 'João',
    'idade': 25,
    'cidade': 'São Paulo'
}

# Acessando valores em um dicionário
# Você pode acessar os valores no dicionário usando as chaves:
print(meu_dicionario['nome'])  # Saída: João
print(meu_dicionario['idade']) # Saída: 25

# Adicionando um novo par chave-valor ao dicionário
meu_dicionario['profissao'] = 'Engenheiro'
print(meu_dicionario)  # Saída: {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo', 'profissao': 'Engenheiro'}

# Atualizando um valor existente
meu_dicionario['idade'] = 26
print(meu_dicionario['idade'])  # Saída: 26

# Removendo um par chave-valor
del meu_dicionario['cidade']
print(meu_dicionario)  # Saída: {'nome': 'João', 'idade': 26, 'profissao': 'Engenheiro'}

# Iterando sobre um dicionário
# Você pode iterar sobre as chaves do dicionário usando um loop for:
for chave in meu_dicionario:
    print(chave, meu_dicionario[chave])
# Saída:
# nome João
# idade 26
# profissao Engenheiro

# Verificando se uma chave existe no dicionário
if 'nome' in meu_dicionario:
    print('Nome está no dicionário')

# Usando o método get() para acessar valores
# O método get() permite acessar valores de forma segura, evitando erros se a chave não existir:
print(meu_dicionario.get('nome'))  # Saída: João
print(meu_dicionario.get('endereco', 'Não encontrado'))  # Saída: Não encontrado

# Obtendo apenas as chaves, valores ou pares chave-valor
print(meu_dicionario.keys())   # Saída: dict_keys(['nome', 'idade', 'profissao'])
print(meu_dicionario.values()) # Saída: dict_values(['João', 26, 'Engenheiro'])
print(meu_dicionario.items())  # Saída: dict_items([('nome', 'João'), ('idade', 26), ('profissao', 'Engenheiro')])

# Exemplo prático de uso de dicionários: Contagem de palavras em uma frase
frase = "um dois tres um dois um"
contagem_palavras = {}
palavras = frase.split()

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)  # Saída: {'um': 3, 'dois': 2, 'tres': 1}
