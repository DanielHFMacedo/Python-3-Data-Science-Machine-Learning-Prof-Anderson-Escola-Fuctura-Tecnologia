import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk

# link do colab aula 3 https://drive.google.com/file/d/1JCrFtynp0ltIZpTIsRL_P9HyCqfQCjDT/view?usp=sharing

# •Conjunto de dados (Pesquisa
# Salarial realizada pelo site https://www.freecodecamp.com/
# com programadores de software nos EUA que frequentaram treinamentos Bootcamp):
# https://drive.google.com/file/d/1I8WM2JxRiZI6TISVGvtIZqC-F0BwnW1z/view?usp=sharing

# revisão do 2 exercicio

# 01 - Importe o arquivo com o Pandas
dados=pd.read_csv("dados.csv")
# 02 - Imprima as 10 primeiras linhas do DataFrame criado.
print(dados.head(10))
print(dados['bairro']) # utilizando pd['classe'] podemos imprimir uma coluna inteira
print(dados['bairro'].unique()) # utilizando o unique podemos imprimir um vez todos os nomes sem repetição
print(dados['bairro'].value_counts())
# 03 - Verifique se existe algum valor missing (NaN) no DataFrame.
print(dados.isnull().any()) # vai pesquisar em cada coluna um valor True para null
"""
04 - Crie um array com o nome dos bairros e um array com a quantidade de vezes que cada bairro aparece
e plot um gráfico de barras com o nome dos bairros no eixo x e a quantidade de apartamentos em cada bairro
no eixo y. Coloque uma legendas para os eixos e um título para o seu gráfico.
"""
bairros=dados['bairro'].value_counts().index
quantidade=dados['bairro'].value_counts().values
print(bairros)
print(quantidade)
plt.bar(bairros,quantidade, label='Bairros')
plt.xlabel("Bairros")
plt.ylabel("Quantidade de condomínios")
plt.title("Quantidade de condomínios por bairros")
plt.legend()
plt.show()

# 05 - Use a coluna de preços do arquivo para criar um Histograma.
# Coloque a cor vermelha para a barra do gráfico. Coloque um título para o seu Histograma.

preços=dados["preco"]
print("\n Preços: \n",preços)
plt.hist(preços)
plt.legend()
plt.show()

#06 - Crie um gráfico do tipo Scatter Plot contendo o preço e a área de cada condomínio.
#Crie uma legenda para o eixo x e o eixo y. Crie também um título e coloque a cor verde para o plot do gráfico.
# Coloque o tamanho da bolinha do plt = 10.

area=dados["area"]
plt.scatter(preços,area, c='g')
plt.legend()
plt.show()

"""
07 - Use a coluna com a quantidade de quartos e crie um Gráfico de Pizza (Pie Chart) com a quantidade de quartos
 presentes para os dados (o label com a quantidade de quartos deve estar presente em cada pedaço).
Coloque as seguintes cores para cada pedaço: Vermelho para 1 quarto, Preto para 2 quartos, Azul para 3 quartos
"""

quantidade_quartos=dados['quartos'].value_counts()
print(quantidade_quartos)

plt.pie(quantidade_quartos.values, labels=quantidade_quartos.index, colors=['b','k','r'],startangle=90)
plt.legend()
plt.show()

dict = {'Estado' : ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"],
        'Sigla' : ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"],
        'Capital' : ["Maceió", "Salvador", "Fortaleza", "São Luiz", "João Pessoa", "Recife", "Teresina", "Natal", "Aracaju"],
        'Área': [27848.140, 564733.177, 148920.472, 331937.450, 56469.778, 98148.323, 251577.738, 52811.047, 21915.081],
        'População': [3322820, 14812617, 9075649, 7035055, 3996496, 9496294, 3264531, 3479010, 2278308],
        'Expectativa de vida': 'NaN'}

df=pd.DataFrame(dict)
print(df)
df['Expectativa de vida']=np.random.rand(9)
print(df)

# Finalizamos a revisão do 2 exercício

# Tema da aula: Introdução a análise de dados com Python

