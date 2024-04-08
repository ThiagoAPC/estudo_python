#Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que leia os nomes e sorteie um deles
import random
a = str(input('Digite o nome do 1° aluno: '))
b = str(input('Digite o nome do 2° aluno: '))
c = str(input('Digite o nome do 3° aluno: '))
d = str(input('Digite o nome do 4° aluno: '))

print(random.choice([a, b, c, d]))