#Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import
#e from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais 
#nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi.
import math
import emoji


num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))
print(emoji.emojize('Muito maneiro :ghost:'))