#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
# formar um triângulo.

print('Verificando se as retas formam um triângulo')

a = int(input('Insira o valor da reta A: '))
b = int(input('Insira o valor da reta B: '))
c = int(input('Insira o valor da reta C: '))

if a + b > c and a + c > b and b + c > a:
    print('Essas retas podem formar um triângulo')
else:
    print('Essas retas não podem formar um triângulo')
    