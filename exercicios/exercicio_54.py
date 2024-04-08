#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

lista_ano_nasc = []
total_maiores = 0
total_menores = 0

ano_atual = int(input('Insira o ano atual: ')) 
for datas in range(1, 8):
    ano_nasc = int(input('Insira o ano de nascimento da {} pessoa: '.format(datas)))
    lista_ano_nasc.append(ano_nasc) #Adiciona as datas de nascimento em uma lista

for datas_nasc in lista_ano_nasc: #Ve todos os elementos dentro da lista datas_nasc
    if ano_atual - datas_nasc >= 18:
        total_maiores += 1 #Incrementa a variável caso seja maior de idade
    else:
        total_menores += 1 #Incrementa a variável caso seja menor de idade

print('O número de maiores de idade é: {}\nO número de menores de idade é: {}'.format(total_maiores, total_menores))
