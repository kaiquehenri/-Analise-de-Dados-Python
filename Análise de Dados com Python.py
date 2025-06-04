'''
#Desafio:
#Você trabalha em uma grande empresa de Cartão de Crédito e o diretor da empresa percebeu que o número de clientes que cancelam seus cartões tem aumentado significativamente, causando prejuízos enormes para a empresa

#O que fazer para evitar isso? Como saber as pessoas que têm maior tendência a cancelar o cartão?

#O que temos:
#Temos 1 base de dados com informações dos clientes, tanto clientes atuais quanto clientes que cancelaram o cartão

#Download da Base de Dados: Botão na página

#Referência: https://www.kaggle.com/sakshigoyal7/credit-card-customers"
#passo 1- importar a base de dados passo 2 - visualizar e tratar base de dados passo 3 - "dar uma olhada na sua base de dados" passo 4 - contruir uma analise para identificar o motivo do cancelamento

#identificar qual o motivo ou os principais motivos dos clientes estarem cancelando o cartão de crédito.
'''



import pandas as pd 
tabela = pd.read_csv('C:/Users/Kaiqu/Documents/analise de dados python/ClientesBanco.csv', encoding="latin1")
tabela = tabela.drop("CLIENTNUM", axis=1)
print(tabela)
# vamos tratar valores vazios e exibir um resumo das colunas da base de dados
tabela = tabela.dropna()
print(tabela.info())
print(tabela.describe().round(1))
#vamos avaliar a divisão entre clientes e cancelados 
qtde_categoria = tabela["Categoria"].value_counts()
print(qtde_categoria)
#percentual
qtde_categoria_perc = tabela["Categoria"].value_counts(normalize =True)
print(qtde_categoria_perc)
'''
 temos varias formas de descobrir o motivo de cancelamento 
- podemos olhar a comparação entre Clinetes e Cancelados
em cada um caoluna da base de dados, para ver se essa informação traz
algum insight novo para a gente. 
'''
import plotly.express as px 
for coluna in tabela:
    grafico = px.histogram(tabela , x = coluna , color = "Categoria")
    grafico.show()
    '''
    informações retiradas da analise
me parece que quanto mais produtos contratados um cliente tem , menor a chence dele cancelar
e quanto mais transações e quanto maior o valor de transação, menor a chance dele cancelar.
    '''
