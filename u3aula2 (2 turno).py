import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 2 aula 2 turno

x = [1, 3, 5]             # Criando uma lista com valores do eixo x
y = [2, 5, 12]            # Criando uma lista com valores do eixo y

plt.plot(x, y)            # O método plot() define os eixos do gráfico
plt.xlabel('Variável 1')  # Definindo o eixo x
plt.ylabel('Variável 2')  # Definindo o eixo y
plt.title('Teste Plot')
plt.show()                # O método show() apresenta para o usuário o gráfico criado

# Inserindo uma legenda no gráfico
x2 = [1,  2,  3,  4,  5]
y2 = [8, 13, 15, 19, 21]

plt.plot(x2, y2, label = 'Linha') # label define o nome da legenda
plt.legend()                      # Apresentando a legenda
plt.show()

# Criar um gráfico com os dados abaixo, insira nomes para os eixos, título e legenda
x = [1,2,3,4,5,6,7,8,9,10]
y = [12,62,56,85,42,32,22,15,62,85]
plt.plot(x,y)
plt.xlabel(' Variável x')
plt.ylabel(' Variável y')
plt.title('Ex 1')
plt.show()

x = [1,2,3,4,5,6,7,8,9,10]
y = [12,62,56,85,42,32,22,15,62,85]
plt.plot(x,y, label='linha', color='g')
plt.xlabel(' Variável x')
plt.ylabel(' Variável y')
plt.title('Ex 1')
plt.legend(loc='best')
plt.show()

# scater
x = [1,2,3,4,5,6,7,8,9,10]
y = [12,62,56,85,42,32,22,15,62,85]
plt.plot(x,y, label='linha', color='g')
plt.scatter(x,y, color='purple')
plt.xlabel(' Variável x')
plt.ylabel(' Variável y')
plt.title('Ex 1')
plt.legend(loc='best')
plt.show()

# grafico de br plt.bar

x = [2, 4, 6, 8, 10]
y = [6, 7, 8, 2,  4]

# O método bar() cria um gráfico de Barras
plt.bar(x, y, label = 'Barras', color = 'r')  # color define a cor da barra
plt.legend()
plt.show()

# graficos de barra em paralelo

# Gráfico de barras em paralelo
x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]

plt.bar(x, y, label = 'Barras1', color = 'r')
plt.bar(x2, y2, label = 'Barras2', color = 'b')
plt.legend()
plt.show()

# Criando gráficos com numpy

x=np.arange(50)
y=np.random.rand(50)
plt.bar(x,y,label="gráfico de numeros aleatorios", color='g')
plt.legend()
plt.show()

