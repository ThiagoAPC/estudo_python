#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

print('Analisador Completo')

somaidade = 0
mediaidade = 0
maioridade = 0
maisvelho = ''
num_mulheres = 0

for p in range (1, 5):
    print('-------{}º Pessoa-------'.format(p))
    nome = str(input('Insira o nome: ')).strip()
    idade = int(input('Insira a idade: '))
    sexo = str(input('Insira o sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm': #Ele verifica a pessoa 1, caso seja masculino o sexo, coloca nome e a idade dele
        maisvelho = nome
        maioridade = idade
    if sexo in 'Mm' and idade > maioridade: #Neste if ele compara o valor da próxima inserção com o atual e o atualiza caso atenda as condições
        maisvelho = nome
        maioridade = idade
    if sexo in 'Ff' and idade < 20: #Aqui ele verifica se sexo é feminino e se é menor de 20 e incrementa em 1 a variável num_mulheres
        num_mulheres += 1

    
mediaidade = somaidade / 4
print('-~' * 10)
print('A média de idade do grupo é: {} anos'.format(mediaidade))
print('O nome do homem mais velho é: {}'.format(maisvelho))
print('O número de mulheres com menos de 20 anos é: {}'.format(num_mulheres))

    


