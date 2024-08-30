#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

#Função proposta
def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            print(f'\033[92mSUCESSO! Você digitou o valor {n}, este valor é um número\033[0m')
            break  
        else:
            print(f'\033[91mERRO! Você digitou o valor: {n}. Este valor não é um número, tente outra vez.\033[0m')

#Programa Principal
n = leiaInt('Digite um número: ')
