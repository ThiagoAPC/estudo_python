'''
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
'''

print('Analisando Triângulos v2.0')

a = int(input('Insira o valor da reta A: '))
b = int(input('Insira o valor da reta B: '))
c = int(input('Insira o valor da reta C: '))

if a + b > c and a + c > b and b + c > a and a == b or a == c or b == c:
    print('Essas retas podem formar um triângulo, esse triângulo é isóceles')
elif a + b > c and a + c > b and b + c > a and a == b and a == c and b == c:
    print('Essas retas podem formar um triângulo, esse triângulo é equilátero')
elif a + b > c and a + c > b and b + c > a and a != b and a != c and b != c:
    print('Essas retas podem formar um triângulo, esse triângulo é escaleno')
else:
    print('Essas retas não podem formar um triângulo')

