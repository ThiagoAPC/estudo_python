#Estudando funçõesm pyhton
def linha():
    print('=-'*10)

def titulo(txt):
    print('=-'*10)
    print(txt)
    print('=-'*10)

def soma(*numeros):
    s= 0
    for n in numeros:
        s += n
    print(f'A soma dos valores {numeros} é igual {s}')
    
def dobra_lista(lista):
    pos = 0
    while pos < len(valores):
        valores[pos] *= 2
        pos += 1
#Programa principal
titulo('    Olá Mundo   ')
soma(4, 5)
linha()

#Entender como manipular listas e funções 

#Definir uma lista de valores
valores = [4, 3, 0, 7, 6, 1, 2]

print(f'Lista com os valores originais: {valores}')
dobra_lista(valores)
print(f'Lista com os valores dobrados: {valores}')
linha()


