#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#Quantidade de notas
#A menor nota
#A media da turma
#Situação (opcional)

def notas(*n, situacao=False):
    """
    Função para analisar notas e situações de vários alunos.
    
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """

    resultado = dict()
    resultado['Quantidade de notas'] = len(n)
    resultado['Maior nota'] = max(n)
    resultado['Menor nota'] = min(n)
    resultado['Média da turma'] = sum(n)/len(n)

    if situacao:
        if resultado['Média da turma'] >= 7:
            resultado['Situação'] = 'Boa'
        elif resultado['Média da turma'] >= 5:
            resultado['Situação'] = 'Regular'
        else:
            resultado['Situação'] = 'Ruim'
    return resultado

def exibir_resultado(dados):
    """
    Função para exibir o resultado de forma formatada e agradável.
    """
    print("\n--- Resultados ---")
    print(f"Quantidade de notas: {dados['Quantidade de notas']}")
    print(f"Maior nota: {dados['Maior nota']:.2f}")
    print(f"Menor nota: {dados['Menor nota']:.2f}")
    print(f"Média da turma: {dados['Média da turma']:.2f}")
    if 'Situação' in dados:
        print(f"Situação: {dados['Situação']}")
    print("-------------------\n")

# Solicitando as notas do usuário
notas_usuario = []
while True:
    nota = input("Digite uma nota (ou 'parar' para finalizar): ")
    if nota.lower() == 'parar':
        break
    if nota.replace('.', '', 1).isdigit():
        notas_usuario.append(float(nota))
    else:
        print("Valor inválido, por favor digite uma nota válida.")

# Solicitando se o usuário deseja incluir a situação
incluir_situacao = input("Deseja incluir a situação da turma? (S/N): ").strip().upper()
situacao = True if incluir_situacao == 'S' else False

# Chamando a função e exibindo o resultado
resultado = notas(*notas_usuario, situacao=situacao)
exibir_resultado(resultado)




