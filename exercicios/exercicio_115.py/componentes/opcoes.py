from colorama import Fore, Style, init
init(autoreset=True)

# Função de cadastro de pessoas
def cadastrar_pessoa(lista_pessoa):
    """
    Solicita ao usuário algumas informações básicas sobre a pessoas que será cadastrada

    Parâmetros
    lista_pessoas(list) - Lista onde serão armazenados os dicionários que contém os dados das pessoas

    dados_pessoa(dict) - Dicionário de dados que armazena como índice as informações das pessoas abaixo:
    - Nome: nome da pessoa
    - DataNasc: data de nascimento que será utilizada pra calcular a idade
    - Sexo: sexo da pessoa [M/F]
    - Cargo: a ocupação da pessoa
    """
    print(Fore.CYAN + Style.BRIGHT + 'Siga os passos abaixo para cadastrar a pessoa:')
    
    while True:
        # Criando o dicionário para inserir as informações da pessoa e depois adicionar na lista
        dados_pessoa = dict()
        
        try:
            # Inserindo os dados da pessoa como índices
            dados_pessoa['Nome'] = str(input(Fore.YELLOW + '📝 Insira o nome: ')).strip()
            
            # Validação da Data de Nascimento
            while True:
                try:
                    ano_nasc = int(input(Fore.YELLOW + '📅 Insira o ano de nascimento (ex: 1990): '))
                    if 1900 <= ano_nasc <= 2024:
                        dados_pessoa['DataNasc'] = ano_nasc
                        dados_pessoa['Idade'] = 2024 - ano_nasc
                        break
                    else:
                        print(Fore.RED + '⚠️  Ano inválido. Por favor, insira um ano entre 1900 e 2024.')
                except ValueError:
                    print(Fore.RED + '⚠️  Erro! Por favor, insira um ano válido como número inteiro.')
            
            # Validação do Sexo
            while True:
                sexo = str(input(Fore.YELLOW + '⚤ Insira o sexo [M/F]: ')).strip().upper()
                if sexo in ['M', 'F']:
                    dados_pessoa['Sexo'] = sexo
                    break
                else:
                    print(Fore.RED + '⚠️  Erro! Por favor, insira "M" para Masculino ou "F" para Feminino.')
            
            # Inserção do Cargo
            dados_pessoa['Cargo'] = str(input(Fore.YELLOW + '💼 Insira o cargo: ')).strip()
            
            # Adicionando o dicionário na lista
            lista_pessoa.append(dados_pessoa)
            
            # Quebra ou continuidade do loop
            while True:
                continuar = str(input(Fore.GREEN + 'Deseja cadastrar outra pessoa? [S/N]: ')).strip().upper()
                if continuar in ['S', 'N']:
                    break
                else:
                    print(Fore.RED + '⚠️  Erro! Responda com "S" para sim ou "N" para não.')
            
            if continuar == 'N':
                break
        
        except KeyboardInterrupt:
            print(Fore.RED + '\n⚠️  Cadastro interrompido pelo usuário.')
            break

# Função de exibição de pessoas cadastradas
def mostrar_pessoas(lista_pessoa):
    """
    Exibe todas os dicionários de dados (dados_pessoa) armazenados na lista lista_pessoa

    Parâmetros
    lista_pessoas(list) - Lista onde estão armazenados os dicionários que contém os dados das pessoas

    A função mostra cada pessoa com suas informações em formato organizado.
    """
    # Exibindo todas as pessoas cadastradas
    print(Fore.MAGENTA + Style.BRIGHT + '\n📋 Pessoas cadastradas:')
    if not lista_pessoa:
        print(Fore.RED + 'Nenhuma pessoa cadastrada ainda.')
    else:
        for index, pessoa in enumerate(lista_pessoa, start=1):
            print(Fore.YELLOW + Style.BRIGHT + f'\n{"=" * 50}')
            print(Fore.CYAN + Style.BRIGHT + f'👤 Pessoa {index}')
            print(Fore.YELLOW + Style.BRIGHT + f'{"=" * 50}')
            for chave, valor in pessoa.items():
                print(Fore.GREEN + f'{chave}: {valor}')

# Lista para armazenar os cadastros
lista_cadastrados = []
