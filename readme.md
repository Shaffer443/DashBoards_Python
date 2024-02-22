# Fonte do PRojeto;

- Link do video: https://youtu.be/M5xz2PS_RsE?si=k-hpQPSnIA0DLhvt
- Material de apoio: https://grizzly-amaranthus-f6a.notion.site/Streamlit-3f599bdfbb584cd1b581e748b5291c36

# Bibliotecas:
1. **Streamlit**
`pip install streamlit`

2. **Pandas**
__OBS__: Instalação do framework **pandas** para trabalhar com manipulação de dados.
`pip install pandas`
3. 
3. **Numpy**
__OBS__: Instalação do framwork **numpy** para trabalhar com algebra linear(com vetores e matrizes, etensores que são anmtrizes de multidimenssões), 
conjunto de dados, ametamática, dados e vetores.
`pip install numpy`

# Informações do Projeto:

**Importação e cabeçalho**

`import streamlit as st` <br>
`st.header("Minha dashboard")`


**Executando o servidor**

(main.py ou o nome do arquivo do script)<br>
`streamlit run dashboard.py`

__Textos__
1. Exibe um texto no navegador
`st.text('Meu texto')`

2. Exibe um texto com formatações markdown
`st.markdown('# Meu texto')`

3. Cria uma legenda
`st.caption('Balloons. Hundreds of them...')`

4. Renderiza diversos elementos
`st.write("# Ola", ['Caio', 'Sampaio'])`

5. Exibe um tiítulo
`st.title('Meu título')`

**Exibição de dados**


 
Crinado um conjunto de dados com linhas e colunas.
Criando linhas e colunas em duas dimenssões, eixos X(horizontal) e Y(vertical).

1. Criar e exibir uma tabela:
Criando dados aleátório (linhas, colunas), cada linhas com um numero de colunas.
`df = pd.DataFrame(
     np.random.randn(10, 3),
     columns=['Preço', 'Taxa de desocupação', 'Taxa inadiplencia',])`

Mostra a tabela
`st.table(df)`

2. Criar e exibir um DataFrame
`df = pd.DataFrame(
     np.random.randn(10, 3),
     columns=['Preço', 'Taxa de desocupação', 'Taxa inadiplencia',])`

Outra opção para mostrar a tabela
`st.dataframe(df)`

**Criar gráficos**

1. Gráfico de linhas
`df = pd.DataFrame(
        np.random.randn(10, 3),
        columns=['Preço', 'Taxa de desocupação', 'Taxa inadiplencia',])`

Mostra gráfico em linhas
`st.line_chart(df)`

2. Gráfico de barras
`df = pd.DataFrame(
        np.random.randn(10, 3),
        columns=['Preço', 'Taxa de desocupação', 'Taxa inadiplencia',])`

Mostra gráfico em barras
`st.bar_chart(df)`

**Interação do Usuário**

__Entrada de dados__
Toda vez que  apágina é carregada a condição do botão é 'FALSE'.
Quando clicamos, ela passa a ser 'TRUE'.
Logo, os exemplos abaixo são cosntruindo em cima deste conceito de "se for TRUE, faça.."

1. Botão:

~~~~
if st.button('MEU BOTÃO'):
     st.write('Click')
~~~~

2. Checkbox:
~~~~
check = st.checkbox('Aceito')

if check:
     st.write('Marcado')
~~~~

3. Radio:

Por padrão vem alguma opção selecionada. Geralmente a
primeira opção.

~~~~
opcao = st.radio(
 "Selecione uma opção",
 ('Opção 1', 'Opção 2'))

if opcao == 'Opção 1':
    st.write('1')
else:
    st.write("2") 
~~~~

4. Selectbox
Funções similares ao do radio.
~~~~
option = st.selectbox(
    'Selecione',
    ('Op 1', 'Op 2', 'Op 3'))

st.write('Você selecionou:', option)
~~~~

5. Multselect

Funções similares ao do selectbox, 
Porém podendo selecionar mais de uma opção,
exemplo: Preço e Taxa de Ocupação.
Podendendo tb vir uma função pré selecionada.
Configuração de forma diferente das demais

~~~~
options = st.multiselect(
     'Cor favorita',
     ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
     ['Vermelho', 'Verde'])
~~~~

Slider
values = st.slider(
'Intervalo',
0.0, 100.0, (25.0, 75.0))
​
Text
title = st.text_input('Nome', 'Caio')
​
Number
number = st.number_input('Número')
​
Date
d = st.date_input(
 "Digite uma data",
 datetime.date(2022, 2, 2))
​
