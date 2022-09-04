import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
Autor: Daniel Macêdo 
Data 02/05/2022
"""

# 01 - Importe o arquivo com o Pandas
dados=pd.read_csv("dados.csv")

# 02 - Imprima as 10 primeiras linhas do DataFrame criado.
print("\n",dados.head(10))

# 03 - Verifique se existe algum valor missing (NaN) no DataFrame.
NAN = dados.isnull().values.any()
print("\n",NAN)

"""
04 - Crie um array com o nome dos bairros e um array com a quantidade de vezes que cada bairro aparece
e plot um gráfico de barras com o nome dos bairros no eixo x e a quantidade de apartamentos em cada bairro
no eixo y. Coloque uma legendas para os eixos e um título para o seu gráfico.
"""

bairros=dados["bairro"]
print("bairros:\n",bairros)
"""bairros=np.loadtxt(dados, delimiter=',', usecols=(6) , skiprows=1, unpack=True, dtype=str)
print("Bairros :\n",bairros)"""

nomes,quantidade=np.unique(bairros, return_counts=True)
print("nome dos bairros:",nomes,"\n quantidade:",quantidade)

plt.bar(nomes, quantidade, label = 'Barras1', color = 'r')
plt.legend()
plt.show()

# 05 - Use a coluna de preços do arquivo para criar um Histograma.
# Coloque a cor vermelha para a barra do gráfico. Coloque um título para o seu Histograma.

preços=dados["preco"]
print("\n Preços: \n",preços)
plt.hist(preços,30)
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

quartos=dados["quartos"]
print("Quartos:\n",quartos)
quartos,quantidade=np.unique(quartos, return_counts=True)
print("Quartos:",quartos,"\nQuantidade:",quantidade)

plt.pie (quantidade,quartos)
plt.show()

# 08 - Utilize o dicionário abaixo e crie um DataFrame com o Pandas

dict = {'Estado' : ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"],
        'Sigla' : ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"],
        'Capital' : ["Maceió", "Salvador", "Fortaleza", "São Luiz", "João Pessoa", "Recife", "Teresina", "Natal", "Aracaju"],
        'Área': [27848.140, 564733.177, 148920.472, 331937.450, 56469.778, 98148.323, 251577.738, 52811.047, 21915.081],
        'População': [3322820, 14812617, 9075649, 7035055, 3996496, 9496294, 3264531, 3479010, 2278308],
        'Expectativa de vida': 'NaN'}

estados=pd.DataFrame(dict)
print("Data frames dos estados",estados)

estados.fillna(random.random(),inplace=False)
print("Data frames dos estados",estados)