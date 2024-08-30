def leia_dinheiro(msg):
    while True:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.replace('.', '').isdigit():
            return float(entrada)
        print(f'\033[0;31mERRO: "{entrada}" é um preço inválido!\033[m')
