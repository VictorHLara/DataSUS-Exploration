import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ler o arquivo, ignorando metadados iniciais
data = pd.read_csv('datasets/infecciosas_2023.csv', sep=';', encoding='latin1', skiprows=4)

# Visualizar informações básicas
print(data.info())
print(data.head())

# Renomear colunas
data.columns = ['Região', 'Capítulo', 'Óbitos']

data = data.dropna(subset=['Óbitos'])

# Criar o gráfico
sns.barplot(x='Região', y='Óbitos', data=data)
plt.xticks(rotation=45)
plt.show()