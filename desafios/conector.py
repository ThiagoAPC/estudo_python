#bibliotecas utilizadas 
import pandas as pd
import requests

#chamada da requisição
requisicao = requests.get("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?@moeda=%27USD%27&@dataCotacao=%2707-08-2024%27&$format=json"
)

#caso o protocolo venha com coódigo 200 = sucesso
if requisicao.status_code == 200:
#conversao do json
    data = requisicao.json() 
    values = data['value']

df = pd.DataFrame(values)

print(df)

'''
#criação das listas onde os dados da API serão armazenados 
    paridade_compra = []
    paridade_venda = []
    cotacao_compra = []
    cotacao_venda = []
    datahora_cotacao = []
    tipo_boletim = []
    moeda = []
   
#laço for que anexa os dados nas listas criadas
    for item in values:
        paridade_compra.append(item['paridadeCompra'])
        paridade_venda.append(item['paridadeVenda'])
        cotacao_compra.append(item['cotacaoCompra'])
        cotacao_venda.append(item['cotacaoVenda'])
        datahora_cotacao.append(item['dataHoraCotacao'])
        tipo_boletim.append(item['tipoBoletim'])

#criação do data frame com as colunas requisitadas 
    df = pd.DataFrame({
        'ParidadeCompra': paridade_compra,
        'ParidadeVenda': paridade_venda,
        'CotacaoCompra': cotacao_compra,
        'CotacaoVenda': cotacao_venda,
        'DataHoraCotacao': datahora_cotacao,
        'TipoBoletim': tipo_boletim,
    })
#exibição do data frame
    print(df)

'''

