#O objetivo dessa aula é entender como utilizar cores e estilos no terminal usando o 
#formato ansi \033[style;text;backgroundm

#style
# 0     none
# 1     bold
# 4     underline
# 7     negative


#     text                    background
 
#      30       preto           40
#      31       vermelho        41
#      32       verde           42
#      33       amarelo         43
#      34       azul            44
#      35       Magenta         45
#      36       ciano           46
#      37       cinza           47
#      97       branco          107

print('\033[1;30;40mOlá Mundo!\033[0m')
print('\033[1;31;40mOlá Mundo!\033[0m')
print('\033[1;32;40mOlá Mundo!\033[0m')
print('\033[1;33;40mOlá Mundo!\033[0m')
print('\033[1;34;40mOlá Mundo!\033[0m')
print('\033[1;35;40mOlá Mundo!\033[0m')
print('\033[1;36;40mOlá Mundo!\033[0m')
print('\033[1;37;40mOlá Mundo!\033[0m')
print('\033[7;30;40mOlá Mundo!\033[0m')

print('\033[1;30;40mOlá Mundo!\033[0m')
print('\033[1;31;41mOlá Mundo!\033[0m')
print('\033[1;32;42mOlá Mundo!\033[0m')
print('\033[1;33;43mOlá Mundo!\033[0m')
print('\033[1;34;44mOlá Mundo!\033[0m')
print('\033[1;35;45mOlá Mundo!\033[0m')
print('\033[1;36;46mOlá Mundo!\033[0m')
print('\033[1;37;47mOlá Mundo!\033[0m')
print('\033[7;30;107mOlá Mundo!\033[0m')

print('----------------------------------------------')

a = 5
b = 6

print('O valor de A é \033[4;34;40m{}\033[0m e o valor de B é \033[4;35;40m{}\033[0m'.format(a, b))

#Podemos fazer isto de outro modo 

nome = 'Thiago'
print('Olá, muito prazer em te conhecer {}{}{}!!'.format('\033[4;34m',nome, '\033[m'))

#Outra última maneira de fazer isso seria

cor = {'Limpa':'\033[m', 
         'Magenta':'\033[35m', 
         'Verde': '\033[32m', 
         'PretoeBranco': '\033[7m'}

print('Olá, muito prazer em te conhecer {}{}{}!!'.format(cor['Magenta'],nome, cor['Limpa']))
print('Olá, muito prazer em te conhecer {}{}{}!!'.format(cor['Verde'],nome, cor['Limpa']))
print('Olá, muito prazer em te conhecer {}{}{}!!'.format(cor['PretoeBranco'],nome, cor['Limpa']))