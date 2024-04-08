#Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, 
#que é uma estrutura versátil e simples de entender.
#Lembrando que ele não considera o ultimo numero então fica [0, 1, 2, 3, 4, 5]

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('FIM!')

print('-~' * 10)

s = 0

for contador in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('A soma dos valores é: {}'.format(s))
print('-~' * 10)



