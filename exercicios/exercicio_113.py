#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

#Função proposta
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Por favor, digite um número INTEIRO no formato certo com a digitação correta')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados foi interrompida pelo usuario')
            break
        else:
            return n

        

#Programa Principal
n = leiaInt('Digite um número: ')
print(f'O valor inteiro digitado foi {n}')