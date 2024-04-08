#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. 
print('\033[34mAnalisando Palíndromos\033[m')
frase = str(input('Insira a frase ou palavra: ')).strip().upper()
palavras = frase.split()
junta = ''.join(palavras)
inversa = ''
print('Você digitou a frase: {}'.format(junta))

for letra in range(len(junta)-1, -1, -1):
    inversa = inversa + junta[letra]
print('A frase invertida fica: {}'.format(inversa))

if inversa == junta:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')



    









