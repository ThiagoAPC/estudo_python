#Nesta aula vamos entender um pouco melhor sobre tuplas
#As tuplas ficam entre parenteses porém ela funciona também fora do parenteses

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2]) #Lembrar que o python sempre ignora o último elemento
print(lanche[-3:])
print(lanche)
#ou
for comida in lanche:
    print(f'Eu vou comer: {comida}')
print('Enchi o bucho!')
print('-----------------')
#ou
for comida in range(0, len(lanche)):
    print(f'Eu vou comer: {comida}')
print('Enchi o bucho!')
print('-----------------')
#ou
for comida in range(0, len(lanche)):
    print(f'Eu vou comer: {lanche[comida]}')
print('Enchi o bucho!')
print('-----------------')
#ou
for comida in range(0, len(lanche)):
    print(f'Eu vou encher o bucho de {lanche[comida]}, na posição {comida}')
print('Enchi o bucho!')
print('-----------------')
#ou
for pos, comida in enumerate(lanche):
    print(f'Eu vou encher o bucho de {comida} na posição {pos}')
print('Enchi o bucho!')
print('-----------------')
#ou
print(sorted(lanche))
print(lanche)
print('Enchi o bucho!')
print('-----------------')

#AS TUPLAS SÃO IMUTÁVEIS ENQUANTO O PROGRAMA ESTÁ EM USO!
#Soma de tuplas significa concatenação de tuplas e não soma em si, as operações são diferentes

