#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import requests

def verificarSite(url):
    try:
        response = requests.get(url, timeout=55)
        if response.status_code == 200:
            print('O site está acessível.')
        else:
            print('O site não está acessível, retornou o status:', response.status_code)
    except requests.ConnectionError:
        print('Erro de conexão com o site.')
    except requests.Timeout:
        print('Erro! A página demorou demais para responder.')
    except requests.RequestException as e:
        print(f'Erro! Não foi possível acessar o site {url}: {e}')

# Teste com o site Pudim
url = input('Insira o link do site: ')
verificarSite(url)
