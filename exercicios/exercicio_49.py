#Refaça o DESAFIO 9,
# mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Insira o número: '))

for c in range(0,11):
   print('{} x {} = {}'.format(num, c, num*c))
