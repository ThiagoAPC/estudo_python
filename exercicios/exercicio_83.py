'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá 
analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

exp = input('Digite a expressão: ')

pilha = []

for simb in exp:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(simb)
            break

if len(pilha) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida')
