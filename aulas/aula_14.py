'''
Continuação da aula sobre LISTAS
'''

teste = list()
teste.append('Thiago')
teste.append(22)

#Podemos adicionar listas dentro de listas 
galera = list()
galera.append(teste[:]) #É possível fazer uma cópia dos dados da lista original 

teste[0] = 'Thigas'
teste[1] = 21
galera.append(teste[:])
print(galera)