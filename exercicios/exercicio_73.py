'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time do Palmeiras.
'''

classificao = ('Athletico-PR', 'Flamengo', 'Botafogo', 'São Paulo', 'Bahia', 'Cruzeiro', 'Atlético-MG', 'Palmeiras', 'Internacional', 'Fortaleza', 'Red Bull Bragantino', 'Grêmio', 'Juventude', 'Criciúma', 'Atlético-GO', 'Corinthians', 'Fluminense', 'Vitória', 'Vasco da Gama', 'Cuiabá')

print(f'Os 5 primeiros colocados são: {classificao[:5]}')
print(f'Os 4 ultimos colocados são: {classificao[-4:]}')
print(f'Os times em ordem alfabética: {sorted(classificao)}')
print(f'O Palmeiras está na {classificao.index('Palmeiras')+ 1}º posição do campeonato brasileiro.')
