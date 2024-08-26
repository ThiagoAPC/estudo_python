def saudacao(nome, mensagem="Olá"):
    """
    Exibe uma saudação personalizada.

    Parâmetros:
    nome (str): O nome da pessoa para quem a saudação é dirigida.
    mensagem (str, opcional): A mensagem de saudação. O padrão é "Olá".

    Retorna:
    None: Esta função não retorna nada, apenas exibe a saudação.

    Exemplo de Uso:
    >>> saudacao("Maria")
    Olá, Maria!

    >>> saudacao("João", "Bom dia")
    Bom dia, João!
    """
    print(f"{mensagem}, {nome}!")


def soma(a, b=0):
    """
    Retorna a soma de dois números.

    Parâmetros:
    a (int, float): O primeiro número a ser somado.
    b (int, float, opcional): O segundo número a ser somado. O padrão é 0.

    Retorna:
    int, float: A soma de a e b.

    Exemplo de Uso:
    >>> soma(5)
    5

    >>> soma(5, 3)
    8
    """
    return a + b


# Demonstrando o uso do Interactive Help
def exemplo_interactive_help():
    """
    Este exemplo mostra como utilizar o Interactive Help no Python.

    Para utilizar o Interactive Help no Python, siga os seguintes passos:

    1. Abra o interpretador Python (no terminal, digite `python` e pressione Enter).
    2. Digite `help()` e pressione Enter para abrir o menu de ajuda interativa.
    3. Para obter ajuda sobre uma função específica, como `saudacao`, digite `help(saudacao)`.
    4. O Python exibirá a docstring associada à função, que explica como usá-la.

    Exemplo:
    >>> help(saudacao)
    """
    pass  # Este é apenas um exemplo de docstring; não há necessidade de código aqui.


# Exemplo de uso das funções
if __name__ == "__main__":
    saudacao("Maria")           # Usa o valor padrão de 'mensagem'
    saudacao("João", "Bom dia") # Sobrescreve o valor padrão de 'mensagem'
    
    print(soma(5))              # Usa o valor padrão de 'b'
    print(soma(5, 3))           # Sobrescreve o valor padrão de 'b'

    # Demonstrando como usar o help diretamente no código
    print("\nInteractive Help para a função saudacao:\n")
    help(saudacao)
