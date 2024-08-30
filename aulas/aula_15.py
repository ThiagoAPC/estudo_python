#Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python. 
# Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.

pessoas = {'nome': 'Thiago', 'sexo': 'Masculino', 'idade': '22'} # <- um dicionário é declarado com chaves {}
print(pessoas['nome']) # É possível acessar os valores de um dicionário pelo índice que foi definido, nesse caso o índice é 'nome' e seu valor é 'Thiago'
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #Ao referenciar os nomes dos índices para consumir suas informações, devemos nos atentar ao uso das aspas duplas 
print(pessoas.keys()) #Acessar as keys implica em acessar os índices do dicionário, ou seja, o nome dado para as categorias/colunas etc...
print(pessoas.values())#Values implica na exibição dos valores aos quais os índices categorizam
print(pessoas.items())#O items busca tanto os índices como os valores

#É possível acessar os índices e valores por laços
for k in pessoas.keys(): #mostra os índices
    print(k)

for v in pessoas.values(): #mostra os valores
    print(v)

for i in pessoas.items(): #mostra ambos
    print(i)

del pessoas['sexo'] #Podemos utilizar o comando del para poder apagar items do dicionário

print(pessoas.items())