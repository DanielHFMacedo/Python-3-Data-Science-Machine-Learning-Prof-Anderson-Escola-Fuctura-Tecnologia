import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

# Aula 2 30-04-2022 Matplotlib e Pandas

# Revisão da Questão 5 da aula anterior - resolução do professor

# 1- importar numpy e outras bibliotecas


ar=np.random.rand(50,50) # rand por si só já é um distribuição entre zero e um
print("Duas ultimas linhas do array:\n",ar[-2:],"\n")

filename=os.path.join("iris.csv")

var1,var2,var3,var4=np.loadtxt(filename, delimiter=',', usecols=(0,1,2,3) , skiprows=1, unpack=True)
print(var1,"\n")

print("Soma var1",np.sum(var1))
print("Media var1",np.mean(var1))
print("Var var1",np.var(var1))
print("Std var1",np.std(var1))
print("Min var1",np.min(var1))
print("Max var1",np.max(var1))

var5=np.loadtxt(filename, delimiter=',', usecols=(4) , skiprows=1, unpack=True, dtype=str)

print(" Var 5:\n",var5)

flores, quantidade =np.unique(var5, return_counts=True)
print(flores)
print(quantidade)

# Aula 2 propriamente dita

""" Pandas : Criando séries temporais
             Criando Data frames 
             Explorar dados estruturados 
            
    Matplotlib : Graficos de linha, barra, pizza
                 Gráfico 3D


Pandas é componente principal para Analise de Dados
Tambem é exelente para Data Munging/Wrangling

É utilizado na fase de preparação des dados, fase importante
e que consome tempo."""

"Estudar tutorial pandas.pydata.org"

"Pandas trabalha com Series e Data Frames."

"Série pe um array unidimensional (lista de valores) que contém um array de dados de índices"

"Data frammes eles representam uma estrutura tabular semelhante a estrutura de uma planilha do excel." \
"contendo uma coleção de colunas em que cada um apode ser de diferentes tipos de valores( int, float, str, bool. etc)" \
" "

obj=pd.Series([73,51,-15,13])
print("Objeto em pandas:\n",obj)
print(obj.values)
print(obj.index)

obj2=pd.Series([73,51,-15,13], index=['a','b','c','d'])
print(obj2)

novoobj = obj2.append(pd.Series([100,10000],index=['e','f']))
print("Novo objeto:\n",novoobj)

h=obj2[obj2>10]
print(h)

obj3=pd.Series([1,2,3,4,5,6,7,8,9,10],['a','b','c','d','e','f','g','h','i','j'])
print(obj3)

# Usando numpy com pandas para criar series

obj4=pd.Series(np.arange(1,11),index=np.arange(1,11))
print("Obj 4:\n",obj4)

# criando a partir de dicionarios

dict = {'Apple':408.25, 'Amazon': 249.25, 'Microsoft': 210.19, 'Google': 196.81, 'Samsung': 74.36}

obj5=pd.Series(dict)
print("Obj5 :\n",obj5)

empresas = ['Apple', 'Amazon', 'Microsoft', 'Google', 'Coca-Cola']

obj6 = pd.Series(dict, index=empresas)
print("Obj6:\n",obj6)

obj7 = obj6.append(pd.Series([325.7], index=['Coca-Cola']))
print("\n",obj7)

data2 = {'Estado': ['Santa Catarina', 'Paraná', 'Goiás', 'Bahia', 'Minas Gerais'],
        'Ano': [2002, 2003, 2004, 2005, 2006],
        'População': [1.5, 1.7, 3.6, 2.4, 2.9]}

df=pd.DataFrame(data2)
print("frame: \n",df)
df['Área']=np.random.randint(1,10,5)
print("novo df com area \n",df)
print(df.describe())

# Data Frames e arquivos CSV

salarios=pd.read_csv("salarios.csv")
print("\n Salarios head \n",salarios.head())

# Usando o método read_table
df = pd.read_table('salarios.csv', sep = ',')
print("\nRead table:\n",df)

# Criando um Dataframe com datas
dates = pd.date_range('20210101', periods = 10)
df = pd.DataFrame(np.random.randn(10,4), index = dates, columns = list('ABCD'))
print("\n",dates)


