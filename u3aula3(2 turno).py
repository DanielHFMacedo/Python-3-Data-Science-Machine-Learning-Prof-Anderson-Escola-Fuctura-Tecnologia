import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk
import colorsys
plt.style.use('seaborn-talk')
import warnings
warnings.filterwarnings('ignore')

# link do colab aula 3 https://drive.google.com/file/d/1JCrFtynp0ltIZpTIsRL_P9HyCqfQCjDT/view?usp=sharing

# •Conjunto de dados (Pesquisa
# Salarial realizada pelo site https://www.freecodecamp.com/
# com programadores de software nos EUA que frequentaram treinamentos Bootcamp):
# https://drive.google.com/file/d/1I8WM2JxRiZI6TISVGvtIZqC-F0BwnW1z/view?usp=sharing


dados=pd.read_csv('Dados-Pesquisa.csv')
print(dados)
print(dados.head(10))
print(dados.describe())
print(list(dados)) # printa os nomes das colunas
idade=dados.Age # igual a dados.Age - Isso não pode ser utilizado quando o nome da coluna tem espaços

plt.hist(idade,bins=100, label='Idades',color='g')
plt.xlabel("Idades")
plt.ylabel("Quantidade de pessoas")
plt.title("Distribuição por idade")
plt.grid()
plt.legend()
plt.show()

gender=dados.Gender.value_counts()
print(gender)
fatias,texto=plt.pie(gender, startangle=90, explode=(0,0.1,0,0,0))
plt.legend(fatias, dados.Gender.value_counts().index, bbox_to_anchor=(1,1))
plt.show()

interest=dados.JobRoleInterest.value_counts()

fatias, texto=plt.pie(interest,startangle=90)
plt.legend(fatias, interest.index, bbox_to_anchor=(1.2,1)) # bbox faz a legenda andar
plt.show()

empregabilidade=dados.EmploymentField.value_counts()
fatias, texto =plt.pie(empregabilidade, startangle=90)
plt.legend(fatias,  empregabilidade.index, bbox_to_anchor=(1.1,1))
plt.show()

dados2=dados.copy()

bins=[0,20,30,40,50,60,100]

dados2['FaixaEtaria']=pd.cut(dados2['Age'],bins,labels=["<20","20-30","30-40","40-50","50-60",">60"])

#cruzar dados de Faixa Etaria com Jobpref

df2=pd.crosstab(dados2['FaixaEtaria'],dados2['JobPref']).apply(lambda r: r/r.sum(), axis=1)

# Grafico de barras empilhado
df2.plot(kind='bar', stacked=True)
plt.legend(bbox_to_anchor=(1.3,1))
plt.show()

