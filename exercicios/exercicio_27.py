#Escreva um programa que leia um nome completo e mostre o primeiro e útlimo nome
nome_completo = str(input('Insira o seu nome completo: '))
nome = nome_completo.split()

print(nome)
print('O seu primeiro nome é: {}'.format(nome[0]))

#Aqui uma coisa importante é notar que o -1 funciona como um indicador para dizer pra exibir o ultimo elemento da lista
print('O seu último nome é: {}'.format(nome[len(nome)-1]))

