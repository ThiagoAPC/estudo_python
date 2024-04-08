#O Objetivo aqui é entender um pouco sobre operadores aritiméticos (+, -, *, /, **)

n1 = int(input('Insira um valor: '))
n2 = int(input('Insira outro valor: '))

s = n1 + n2     #soma
t = n1 - n2     #subtração
u = n1 * n2     #multiplicação
v = n1 / n2     #divisão
w = n1 // n2    #divisão inteira
x = n1 % n2     #resto da divisão
y = n1 ** n2    #potência

print('A soma é {},\nA subtração é {},\nO produto é {},\nA divisão é {},\nA divisão inteira é {},\nO resto da divisão é {},\nA potência é {}'.format(s, t, u, v, w, x, y))
