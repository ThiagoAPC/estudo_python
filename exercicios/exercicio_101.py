#Funções
def votar(idade):
    if idade < 16:
       return print('Não possuí idade suficiente')
    elif 16 <= idade < 18:
       return print('Voto opcional')
    else:
        print('Voto obrigatório!')

#Programa principal

idade = int(input('Insira sua idade: '))
votar(idade)