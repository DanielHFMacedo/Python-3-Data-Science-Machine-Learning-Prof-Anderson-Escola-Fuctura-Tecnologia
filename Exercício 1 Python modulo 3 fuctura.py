import numpy as np
import pandas as pd
"""
Autor: Daniel Macêdo 
Data 29/04/2022
"""

print("01 - Crie uma matriz de dimensões (50,50) com valores aleatórios entre 0 e 1.\n Imprima as duas últimas linhas da matriz.\n")

matriz=np.random.randint(0,2,2500)
matriz=matriz.reshape(50,50)
print("Matriz:\n",matriz)
print("\nFormato da matriz:\n",matriz.shape)
print("\nÚltimas duas linhas da matriz:\n",matriz[-2:])

print("\n02 - Utilize o array de números aleatórios da questão anterior e apresente a soma de cada coluna.\nEm seguida, apresente a soma de cada linha.\n")
i=0
j=0
for i in range(50):
    soma=0
    j=0
    for j in range(50):
        soma=soma+matriz[j,i]
    print("Coluna:",i,"soma:",soma)  # soma de cada coluna
    print("Linha:",i,"soma:",np.sum(matriz[i]))


print("\n03 - Crie dois arrays de 30 elementos contendo números aleatórios entre 1 e 5.")
print("Utilize os dois arrays para derivar um novo array contendo uma comparação entre os valores")
print("de forma a indicar 'True' caso os elementos em uma mesma posição apresentam o mesmo valor e 'False' caso contrário.\n")

ar1=np.random.randint(1,6,30)
ar2=np.random.randint(1,6,30)
print("Array 1:\n",ar1,"Size 1",ar1.shape)
print("Array 2:\n",ar2,"Size 2",ar2.shape)

ar3= ar1==ar2
print("Array 3:\n",ar3)

print("\n 04 - Import o NumPy e o conjunto de dados Iris.csv e utilize ele para separar cada coluna numérica em uma variável:var1, var2, var3 e var4.\n Para cada coluna calcule a média, o desvio padrão e a variância e imprima na tela.\nImprima também a soma, o maior valor e o menor valor de cada coluna.\n")

data=pd.read_csv("iris.csv")
print("Data: \n:",data)

vr1=data["sepal_length"]
print("\nMédia Vr1:",vr1.mean(),"\nVar vr1:",vr1.var(),"\nStd vr1:",vr1.std(),"\nSoma:",vr1.sum(),"\nMaior valor:",vr1.max(),"\nMenor valor:",vr1.min())
vr2=data["sepal_width"]
print("\nMédia Vr2:",vr2.mean(),"\nVar vr2:",vr2.var(),"\nStd vr2:",vr2.std(),"\nSoma:",vr2.sum(),"\nMaior valor:",vr2.max(),"\nMenor valor:",vr2.min())
vr3=data["petal_length"]
print("\nMédia Vr3:",vr3.mean(),"\nVar vr3:",vr3.var(),"\nStd vr3:",vr3.std(),"\nSoma:",vr3.sum(),"\nMaior valor:",vr3.max(),"\nMenor valor:",vr3.min())
vr4=data["petal_width"]
print("\nMédia Vr4:",vr4.mean(),"\nVar vr4:",vr4.var(),"\nStd vr4:",vr4.std(),"\nSoma:",vr4.sum(),"\nMaior valor:",vr4.max(),"\nMenor valor:",vr4.min())

print(" \n 05-Para a última coluna do conjunto de dados Iris que representa o nome das flores, crie uma varíavel nome e insira todos eles.\nConte quantas vezes aparece o nome setosa, versicolor e virginica.\n")

nome=data["species"]
print(nome)
j=0
setosa=0
virginica=0
versicolor=0

for j in range(len(nome)):
    if nome[j]=="setosa":
        setosa=setosa+1
    elif nome[j]=="versicolor":
        versicolor=versicolor+1
    elif nome[j]=="virginica":
        virginica=virginica+1

print("setosa=",setosa)
print("virginica=",virginica)
print("versicolor=",versicolor)