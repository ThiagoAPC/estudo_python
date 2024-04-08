#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
#de uma Sequência de Fibonacci.
print('--' * 10)
print('Sequência de Fibonacci')
print('--' * 10)
n_termos = int(input('Insira quantos termos você quer saber: '))
contador = 2  # O contador inicia em 2 para representar os dois primeiros termos já impressos
t1 = 0
t2 = 1
print('~-' * 10)
print(t1, '->', t2, end=' -> ')
while contador < n_termos:  #Tem que ser menor se não ele imprime um termo a mais
    ta = t1 + t2
    print(ta, end=' -> ')
    t1 = t2
    t2 = ta
    contador += 1
print('Fim')
print('~-' * 10)
