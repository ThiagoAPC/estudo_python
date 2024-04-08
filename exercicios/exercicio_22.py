nome = str(input('Insira o seu nome completo: '))

#Nome em maiúscula
print('Seu nome em maiúsculas, apenas fica: {}'.format(nome.upper()))

#Nome em minúscula
print('Seu nome em minúsculas, apenas fica: {}'.format(nome.lower()))

#Contar o número de caracteres do nome sem considerar os epaços
print('Seu nome tem {} letras'.format(len(nome.replace(' ',''))))

#Contar quantas letras tem o primeiro nome
dividido = nome.split()
print('O seu primeiro nome tem {} letras'.format(len(dividido[0])))






