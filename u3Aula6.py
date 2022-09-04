import numpy as np  # Importar o NumPy
import pandas as pd # Importar o Pandas
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Tema : Deep Learning
# principal bibliotecas Keras, TensorFlow, Pythorch
# Utilizando o Pytorch precisa-se apenas conhecer orientação a objeto

# Carregando o dataset
df = pd.read_csv("pima-data.csv")
print(df.head(7))

diabetes_map = {True : 1, False : 0}
# Aplicando o mapeamento ao dataset (https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html)
df['diabetes'] = df['diabetes'].map(diabetes_map)
print(df.head(7))

# Seleção de variáveis preditoras (Feature Selection)
atributos = ['num_preg', 'glucose_conc', 'diastolic_bp', 'thickness', 'insulin', 'bmi', 'diab_pred', 'age']
# Variável a ser prevista
atrib_prev = ['diabetes']

# Criando objetos
X = df[atributos].values
Y = df[atrib_prev].values

print(X)

# Criando dados de treino e de teste
X_treino, X_teste, Y_treino, Y_teste = train_test_split(X, Y, test_size = 0.20, shuffle=True, random_state = 42)

print("\n X treino:\n",X_treino)
print(X_treino.shape)

# Retirar os valores missing ocultos
from sklearn.impute import SimpleImputer

# Criando objeto
preenche_0 = SimpleImputer(missing_values = 0, strategy = "mean")

# Substituindo os valores iguais a zero, pela média dos dados
X_treino = preenche_0.fit_transform(X_treino)
X_teste = preenche_0.fit_transform(X_teste)


# Criando o modelo preditivo com uma Multi-layer Perceptron

# Classificador Multi-layer Perceptron
from sklearn.neural_network import MLPClassifier  # https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html

# Criando o modelo preditivo
modelo = MLPClassifier(hidden_layer_sizes = (60, 40, 20), max_iter=1000, random_state=42)

# Treinando o modelo
modelo.fit(X_treino, Y_treino.ravel())

# Previsão para o conjunto de treino
pred_train = modelo.predict(X_treino)
acc_train = metrics.accuracy_score(Y_treino, pred_train)
print("Accuracy Treino: %.6f" %acc_train)

# Previsão para o conjunto de Teste
pred_test = modelo.predict(X_teste)
acc_test = metrics.accuracy_score(Y_teste, pred_test)
print("Accuracy Teste: %.6f" %(acc_test))
