#Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
#o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(numero, show):
    if show == 'S':
        resultado = 1
        for i in range(1, numero+1):
            resultado *= i
            print(f'Multiplicando {i}, resultado parcial: {resultado}')
        return resultado
    else:
        resultado = 1
        for i in range(1, numero+1):
            resultado *= i
        return resultado





numero = int(input('Digite o número pra fatorial: '))
show = str(input('Deseja exibir o calculo[S/N]: ')).upper()
print(f'A fatorial de {numero} é: {fatorial(numero, show)}')