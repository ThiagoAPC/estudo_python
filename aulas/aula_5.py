#O objetivo dessa aula é entender um pouco melhor como fucniona a Manipulando Texto
#É importante lemabrar que a String ocupam espaços na memória e que eles devem ser identificados apartir de 0
frase = ' Manipulação de String em Python '
print('Frase original: ',frase)
#Lembrar que a posição na memória começa sempre do 0, ou seja se colocar 3, vai contar 0, 1, 2, 3
print('Quarta letra da frase: ', frase[3])
print('Frase pulando de dois em dois espaços na memória: ', frase[::2])
print('Fatiando de uma parte da frase até outra: ', frase[25:31])
print('Fatiamento pulando de dois em dois: ', frase[1:31:2])

#Você pode de maneira fácil printar na tela textos com quebra de linha usando aspas triplas(""")

print('O número de letras "i" na frase é: ', frase.count('i'))
#Abaixo, antes de contar quantos P, ele transforma em maiúsculo a frase e depois conta, o mesmo pode valer pra lower
print('Ao mudar a frase inteira pra maiúscula e em seguida contar o número de letras "P" chagamos a: ', frase.upper().count('P'))
#Abaixo usamos len para contar quantos caracteres tem a frase(lembrando que os espaços contam)
print('O numero de caracteres da frase é: ', len(frase))
#Para poder remover os espaços antes e dpois da frase, e contar, se usa strip
print('O numero de caracteres da frase sem espaços é: ', len(frase.strip()))
#Para poder trocar uma palavra da frase por outra se usa replace
print(frase.replace('Python', 'Android'))
#Verificar se uma palavra esta dentro da frase
print('Python' in frase)
#Verificar em que posição começa uma palavra, caso ela exista dentro da frase
print(frase.find('String'))
#Mostrar a frase separada( cria uma lista e põe as palavras dentro das posições)
print(frase.split())
#Armazena a frase em uma variável e manipula ela conforme a necessidade
dividido = frase.split()
print(dividido[4])
#Pega a string, identifica a palvra e ve a letra que ocupa a posição na memória
print(dividido[4][1])