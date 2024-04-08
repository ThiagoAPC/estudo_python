# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time
for c in range(10, -1, -1): #Lembrando que vai até o 0, mas tem que por o -1 pois o último é ignorado
    print(c)
    time.sleep(1)#Aqui fará uma pausa de 1 segundo entre a exibição dos incrementos do contador
print('Fim!')
