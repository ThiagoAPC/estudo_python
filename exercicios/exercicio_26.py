#Faça um program que leia uma frase e mostre:
frase = str(input('Insira uma frase: ')).strip().upper()
#Quantas letras "a" tem na frase 
print('Existem {} letras A na sua frase'.format(frase.count('A')+frase.count('Á')+frase.count('À')+frase.count('Â')+frase.count('Ã')))
#Em qual posição ela aparece pela primeira vez
print('A primeira vez que a letra A apareceu foi na posição: {}'.format(frase.find('A')+1))
#Em qual posição ela aparece pela última vez
print('A ultima vez que a letra A apareceu foi na posição: {}'.format(frase.rfind('A')+1))

