import pandas as pd

# Caminho do arquivo
caminho_arquivo = 'C:/Users/tcorrea/OneDrive - Confidence Corretora de Câmbio S A/Área de Trabalho/Estudo Python/desafios/base_pivot/log.xlsx'

# Ler a planilha 'Spread BankNotes'
df_spread = pd.read_excel(caminho_arquivo, sheet_name='Spread BankNotes')

# Exibir as primeiras linhas do DataFrame para confirmar a leitura
print(df_spread.head())

# Verificar e remover colunas que começam com 'Unnamed:'
df_spread = df_spread.loc[:, ~df_spread.columns.astype(str).str.contains('^Unnamed')]

# Lista de colunas que representam as localidades
localidades = df_spread.columns[2:]  # Assumindo que as primeiras três colunas são 'Cod.', 'MOEDAS'

# Transformar as colunas de localidades em uma coluna 'PRAÇA'
df_melted = df_spread.melt(id_vars=['Cod.', 'MOEDAS'], value_vars=localidades, 
                           var_name='PRAÇA', value_name='SPREAD')

# Remover linhas onde 'SPREAD' está em branco
df_melted = df_melted.dropna(subset=['SPREAD'])

# Exibir as primeiras linhas do DataFrame após remover valores em branco
print(df_melted.head())

# Salvar a tabela transformada em um novo arquivo Excel
caminho_saida = 'C:/Users/tcorrea/OneDrive - Confidence Corretora de Câmbio S A/Área de Trabalho/Estudo Python/desafios/base_pivotado.xlsx'
df_melted.to_excel(caminho_saida, index=False)

print("Tabela transformada criada e salva com sucesso em:", caminho_saida)
