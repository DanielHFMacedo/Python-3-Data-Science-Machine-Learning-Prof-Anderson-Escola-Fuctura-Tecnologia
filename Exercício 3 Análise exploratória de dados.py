import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk
from sklearn.datasets import load_iris

#Carregando o dataset Iris
iris=pd.read_csv("iris.csv")
data=load_iris()

# Imprima as primeiras linhas do Dataset Iris
print("Iris data frame: \n",iris.head(10))
print("iris table:\n",data)
# Imprima os valores numéricos da Variável target (o que queremos prever),
# uma de 3 possíveis categorias de plantas: setosa, versicolor ou virginica
categorias=np.unique(iris['species'])
print(categorias)

# Imprima os valores numéricos da Variável target (o que queremos prever),
# uma de 3 possíveis categorias de plantas: 0, 1 ou 2
y=data.target
print(y)
print(np.unique(y))

# Inclua no dataset uma coluna com os valores numéricos da variável 'target'
iris["Número"]=y
print("Iris data frame: \n",iris)

# Extraia as features (atributos) do dataset e imprima

sl=iris["sepal_length"]
print(sl)
sw=iris["sepal_width"]
print(sw)
pl=iris["petal_length"]
print(pl)
pw=iris["petal_width"]
print(pw)

# Calcule a média de cada feature para as 3 classes
df_setosa=iris.loc[iris['Número']==0]
print("df_setosa: \n",df_setosa)
print(df_setosa['sepal_length'])
print("Média da sepal_lenght tipo setosa:",df_setosa['sepal_length'].mean())
print("Média da sepal_width tipo setosa:",df_setosa['sepal_width'].mean())
print("Média da petal_lenght tipo setosa:",df_setosa['petal_length'].mean())
print("Média da petal_width tipo setosa:",df_setosa['petal_width'].mean())
print("\n")
df_versicolor=iris.loc[iris['Número']==1]
print("Média da sepal_lenght tipo versicolor:",df_versicolor['sepal_length'].mean())
print("Média da sepal_width tipo versicolor:",df_versicolor['sepal_width'].mean())
print("Média da petal_lenght tipo versicolor:",df_versicolor['petal_length'].mean())
print("Média da petal_width tipo versicolor:",df_versicolor['petal_width'].mean())
print("\n")
df_virginica=iris.loc[iris['Número']==2]
print("Média da sepal_lenght tipo virginica:",df_virginica['sepal_length'].mean())
print("Média da sepal_width tipo virginica:",df_virginica['sepal_width'].mean())
print("Média da petal_lenght tipo virginica:",df_virginica['petal_length'].mean())
print("Média da petal_width tipo virginica:",df_virginica['petal_width'].mean())

# Exploração de dados

# Imprima uma Transposta do dataset (transforme linhas e colunas e colunas em linhas)
# Dica: O Dataframe possui o atributo: .T

iris_transposta=iris.T
print("Iris transposta:\n",iris_transposta)

# Utilize a função Info do dataset para obter um resumo sobre o dataset
print("Iris info:\n",iris.info())
print("Iris T info:\n",iris_transposta.info())

# Faça um resumo estatístico do dataset
print("Resumo estatístico da Iris:\n",iris.describe())

# Verifique se existem valores nulos no dataset
print(iris.isnull())

# Faça uma contagem de valores de sepal length
print(iris["sepal_length"].value_counts())

# PLot

# Crie um Histograma da coluna: sepal length
plt.hist(iris['sepal_length'],25)
plt.show()

# Crie um Histograma de todas as features
plt.hist(iris['petal_length'],25)
plt.show()
plt.hist(iris['petal_width'],25)
plt.show()
plt.hist(iris['sepal_length'],25)
plt.show()
plt.hist(iris['sepal_width'],25)
plt.show()

y=np.arange(len(iris['sepal_length']))
print(y)
# Crie um Gráficos de Dispersão (scatter Plot) da variável sepal length versus número da linha,
# colorido por marcadores da variável target
plt.scatter(y,iris['sepal_length'])
plt.show()

# Escolha 2 colunas com Atributos (Features) e crie um Scatter Plot (um atributo em cada eixo).
# (Coloque uma cor para cada atributo)

plt.scatter(iris['petal_length'],iris['sepal_length'] )
plt.show()


