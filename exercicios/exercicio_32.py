#Monte um programa que veja se um ano inserido é bissexto ou não
ano = int(input('Insira o ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {} é bissexto'.format(ano))
else:
    ('O ano não é bissexto')



    
