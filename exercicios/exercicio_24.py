#Faça um programa que leia o nome de uma cidade e veja se a primeira palvara é SANTO
nome_cidade = str(input('Insira o nome da sua cidade: ')).strip()  
print(nome_cidade[:5].upper() == 'SANTO')   