#Netsa aula será introduzido a programação condicional, até agora estavamos usando a sequencial
#ou seja, tudo seria executado dentro do programa, porém agora, poderemos estabelecer condições
#que, quando atendidas, executem outras funções dentro do programa

#note que a identação do python denota que tudo que estiver colado na esquerda irá ser executado e o que
#tiver com identação pode ou não ser executado
nome = str(input('Insira o seu nome: '))
n1 = float(input('Insira sua Nota 1: '))
n2 = float(input('Insira sua Nota 2: '))

#note também que pra abrir uma condição em python se usa ":" no fim da condição

if nome == 'Thiago':
    print('Seu nome é muito bonito')
else:
    print('Seu nome não é tão bonito!')
#abaixo é um exemplo de uso condicional simplificado
print('Uau, seu nome é mesmo muito bonito' if nome == 'Thiago' else 'Eu prefiro o nome Thiago')

media = (n1+ n2)/2

if media > 6:
    print('Parabéns {} você passou! Sua média foi {}'.format(nome, media))
else:
    print('Sinto muito {}, você foi reprovado! Sua média foi {}'.format(nome, media))
print('Tenha um bom dia!')