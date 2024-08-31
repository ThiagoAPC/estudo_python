import componentes.opcoes as opcoes

def menu_principal():
    largura = 50  # Aumentando a largura para deixar o menu mais espaçoso
    titulo = 'MENU PRINCIPAL'
    print('╔' + '═' * (largura - 2) + '╗')  # Bordas superiores
    print(f'║{titulo.center(largura - 2)}║')  # Centraliza o título com bordas laterais
    print('╠' + '═' * (largura - 2) + '╣')  # Linha divisória decorativa
    print(f'║{"1 - Ver pessoas cadastradas".ljust(largura - 2)}║')
    print(f'║{"2 - Cadastrar pessoa".ljust(largura - 2)}║')
    print(f'║{"3 - Sair do Sistema".ljust(largura - 2)}║')
    print('╚' + '═' * (largura - 2) + '╝')  # Bordas inferiores


def mensagem_opcao(opcao, lista_pessoa):  # Adicionando lista_pessoa como argumento
    if opcao == 1:
        print('📝 Você escolheu a opção 1 - Ver pessoas cadastradas')
        opcoes.mostrar_pessoas(lista_pessoa)  # Passa a lista_pessoa corretamente para a função
    elif opcao == 2:
        print('👤 Você escolheu a opção 2 - Cadastrar pessoa')
        opcoes.cadastrar_pessoa(lista_pessoa)  # Adiciona novos cadastros à lista existente
    elif opcao == 3:
        print('🚪 Finalizando o sistema... Até logo!')

# Programa Principal
lista_cadastrados = []  # Define a lista que será usada para armazenar os cadastros
menu_principal()
while True:
    try:
        opcao = int(input('Digite sua opção: '))
        if opcao in [1, 2, 3]:
            mensagem_opcao(opcao, lista_cadastrados)  # Passa lista_cadastrados como argumento
            if opcao == 3:
                break
        else:
            print('⚠️  Erro! Por favor, digite uma opção válida [1, 2 ou 3]')
    except (ValueError, TypeError):
        print('⚠️  Erro! Por favor, digite uma opção válida [1, 2 ou 3]')


