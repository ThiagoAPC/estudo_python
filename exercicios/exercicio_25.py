#Crie um programa que leia o nome de uma pessoa e verifique se tem SILVA no nome 
nome = str(input('Insira o seu nome: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
