#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('Serviço de solicitação de empréstimo')
valor_casa = float(input('Insira o valor do imóvel da compra: '))
num_anos = int(input('Insira em quantos anos deseja pagar o imóvel: '))
salario = float(input('Insira o seu salário: '))

prestacao = valor_casa / (num_anos*12)

if prestacao > salario * 0.3:
    print('Sua situção financeira não é ideal, empréstimo NEGADO')
else:
    print('Sua situação finaceira é adequada, empréstimo APROVADO')
    print('O valor das prestações será de {:.2f}'.format(prestacao))


