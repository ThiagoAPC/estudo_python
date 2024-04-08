#Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.
nome = str(input('Insira o seu nome: '))

#Você pode utilizar quantos elif quiser, e dizemos que essas estruturas estão aninhadas
if nome == 'Thiago':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é legalzinho')
elif nome in 'Armando Paracampos Correa':
    print('Nomes espetacular!!!')
else: 
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}!'.format(nome))