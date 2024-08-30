import os

def interactive_help():
    # Determinar a largura do terminal
    largura_terminal = os.get_terminal_size().columns

    # Função para exibir uma barra colorida
    def barra_de_titulo(texto, cor_fundo="\033[44m", cor_texto="\033[97m"):
        print(cor_fundo + cor_texto + texto.center(largura_terminal) + "\033[m")

    # Função para exibir uma mensagem com fundo colorido e texto preto
    def exibir_mensagem(texto, cor_fundo="\033[47m", cor_texto="\033[30m"):
        print(cor_fundo + cor_texto + texto.ljust(largura_terminal) + "\033[m")

    # Exibir cabeçalho
    barra_de_titulo(" SISTEMA DE INTERACTIVE HELP ", cor_fundo="\033[42m")
    exibir_mensagem("Digite o nome de um comando para obter mais informações", cor_fundo="\033[47m")
    exibir_mensagem("Digite 'sair' para encerrar o Interactive Help", cor_fundo="\033[47m")

    while True:
        # Entrada do comando com fundo branco e texto preto
        comando = input("\033[47m\033[30mInsira o nome do comando ou digite 'sair' para encerrar: \033[m").strip()
        
        if comando.lower() == 'sair':
            barra_de_titulo(" ENCERRANDO O SISTEMA, ATÉ LOGO! ", cor_fundo="\033[41m")
            break
        else:
            try:
                barra_de_titulo(f" Acessando o manual do comando '{comando}' ", cor_fundo="\033[44m")
                print("\033[47m\033[30m")
                help(comando)
                print("\033[m")  # Resetar as cores após a saída do comando
            except Exception as e:
                barra_de_titulo(f" ERRO: Comando '{comando}' não encontrado ", cor_fundo="\033[41m")

# Executa o sistema de Interactive Help
interactive_help()
