import streamlit as st
import pandas as pd
import numpy as np
#Cabeçalho
st.header("Minha dashboard")

#Textos
st.text("Textos Informativos")

#sidebar
st.sidebar.text("Textos no Side bar")

#Markdown
st.markdown("~~Textos Riscado~~")

#Legenda
st.caption("Minha Legenda")

#Imprime qualquer informação dentro da tela(mais genérico), seja markdown, estrutura de dados e outros
#em formato de json ou dicioanrio.
st.text("Modelo de dados em formato JSON ou dicionário")
dados_pessoas=[{'Nome':'José', 'Idade': 22}, {'Nome':'João', 'Idade': 33}]
st.write("# Pessoas", dados_pessoas)

# Trabalhando com Dados

# Pandas:

#Crinado um conjunto de dados com linhas e colunas.
#criando linhas e colunas em duas dimenssões, eixos X(horizontal) e Y(vertical)

df = pd.DataFrame(
    #algo aleátório (linhas, colunas), cada linhas com um numero de colunas.
    np.random.rand(10,3),
    #colunas do eixo X:
    columns=['Preço','Taxa de Ocupação','Taxa de Inadimplência']
)

df_preco = df['Preço']
df_txo = df['Taxa de Ocupação']

st.caption("Data Frame com dados aleatórios usando 'write'")
st.write("#Dados:", df)
st.caption("Data Frame com dados aleatórios usando 'table'")
st.table(df)
st.caption("Data Frame com dados aleatórios usando 'dataframe'")
st.dataframe(df)#a pessoa pode mexer na tabela.

# Gráficos:

# Em linha
st.caption("Graficos em linhas")
st.line_chart(df)
# Em barras
st.caption("Graficos em Barras")
st.bar_chart(df)

#Interação do Usuário:

#Colocando botão na side bar e mostrar com click
#Usando Button (Botão)
st.sidebar.text("Click para mostrar o gráfico.")
if st.sidebar.button("Mostrar Gráfico"):
    st.caption("Mostrando Graficos em Barras após click no botão")
    st.bar_chart(df)

#usando checkbox, dentro da sidebar:
st.sidebar.caption("Usando Chekbox para uma ação")
check = st.sidebar.checkbox("Aceito")
if check:
    st.write("Marcado com aceito")

# Radio:

st.sidebar.caption("Usando Radio Buttom para uma ação")
opcao = st.sidebar.radio(
    #escreveendo um descrição
    "selecione uma opção",
    ("Opção 1", "Opção 2", "Tabela de Preço", "Gráfico de Preço")
)

if opcao == "Opção 1":
    st.sidebar.text("selecionei a opção 01")
elif opcao == "Opção 2":
    st.sidebar.text("selecionei a opção 02")
elif opcao == "Tabela de Preço":
    st.caption("Tabela de Preços vi Radio")
    st.table(df_preco)
elif opcao == "Gráfico de Preço via Radio":
    st.caption("Tabela de Preços")
    st.line_chart(df_preco)

# Selectbox:

st.sidebar.caption("Usando SelectBox para uma ação")
opcao_select = st.sidebar.selectbox(
    #escreveendo um descrição
    "selecione uma opção no SelectBox",
    ("Tabela de Taxa de Ocupação", "Gráfico de Taxa de Ocupação")
)

if opcao_select == "Tabela de Taxa de Ocupação via SelectBox":
    st.caption("Tabela de Taxa de Ocupação")
    st.table(df_txo)
elif opcao_select == "Gráfico de Taxa de Ocupação Via SelectBox":
    st.caption("Gráfico de Taxa de Ocupação")
    st.bar_chart(df_txo)

# Multiselect:
# Não esta rodando bem. Ajustar
st.sidebar.caption("Usando MultiSelect para uma ação")
opcao_multi = st.sidebar.multiselect(
    #escreveendo um descrição
    "selecione uma opção no MultiSelect",
    ("Preço","Gráfico de Preço","Tabela de Taxa de Ocupação", "Gráfico de Taxa de Ocupação"),
    # escolhendo uma opção com default
    ('Preço')
)

if "Preço" in opcao_multi:
    st.caption("Tabela de Preço via MultiSelect")
    st.table(df_preco)
elif "Gráfico de Preço" in opcao_multi:
    st.caption("Gráfico de Taxa de Ocupação via MultiSelect")
    st.bar_chart(df_preco)
elif "Tabela de Taxa de Ocupação" in opcao_multi:
    st.caption("Tabela de Taxa de Ocupação via MultiSelect")
    st.table(df_txo)
elif "Gráfico de Taxa de Ocupação" in opcao_multi:
    st.caption("Gráfico de Taxa de Ocupação via MultiSelect")
    st.bar_chart(df_txo)

