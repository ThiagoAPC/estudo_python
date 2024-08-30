#Funções
def teste(b):
    global a #Quando eu coloco esse comando ele informa pra deixar de usar o valor de fora e considerar o de dentro como o novo valor global
    a = 3 #Se eu declarar o a novamente aqui, ele irá criar outra variável, dessa vez será local
    b += 1 #Se eu declarar a variável dentro de uma função, ela terá um escopo local
    c = 2
    print(f'A dentro recebe {a}, pois agora ele está pegando o valor da variável local') #Nesse caso valor de a será o valor da variável local
    print(f'B dentro recebe {b}, pois é uma variável local') #Nesse caso o valor de b é local, ele pega o valor da variável global e opera em cima dele pra dar outro valor
    print(f'C dentro recebe {c}, pois é uma variável local') #Nesse caso c foi declarado dentro sem uso de variáveis externas, ele se mantém local e terá o valor mantido

#Programa principal
a = 4 #Se eu declarar a variável fora, no programa principal, ela se tornará uma variável global
teste(a)
print(f'A fora recebe {a}, pois é uma variável global')
