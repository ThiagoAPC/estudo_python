#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1 
# b) de 10 até 0, de 2 em 2 
# c) uma contagem personalizada

def contador(inicio, fim, passo):
    # Ajuste para passo negativo se for contagem decrescente
    if passo == 0:
        passo = 1
    if inicio > fim and passo > 0:
        passo = -passo

    lista = list()
    
    if inicio < fim:
        # Contagem crescente
        pos = inicio
        while pos <= fim:
            lista.append(pos)
            pos += passo
    else:
        # Contagem decrescente
        pos = inicio
        while pos >= fim:
            lista.append(pos)
            pos += passo
    
    print(f"Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}: {lista}")

# Realizar as três contagens solicitadas

# a) de 1 até 10, de 1 em 1
contador(1, 10, 1)

# b) de 10 até 0, de 2 em 2
contador(10, 0, 2)

# c) uma contagem personalizada
inicio = int(input("Início da contagem: "))
fim = int(input("Fim da contagem: "))
passo = int(input("Passo da contagem: "))
contador(inicio, fim, passo)




