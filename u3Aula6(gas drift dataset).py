import torch # para Deep Learning
import torch.autograd as autograd # para autodiferenciação
import torch.nn as nn # para montar redes neurais
import torch.nn.functional as F # funções do Torch
import torch.optim as optim # para otimização com GDE
from torchvision import datasets, transforms
import numpy as np

import random
import copy


import os
import pandas as pd
import torch.utils.data as data_utils
import time

from sklearn.model_selection import KFold, train_test_split
from sklearn.preprocessing import minmax_scale # normalizar os dados

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using PyTorch version:', torch.__version__, ' Device:', device)

def seed_everything(seed=1062):
  np.random.seed(seed)
  np.random.seed(seed)
  torch.manual_seed(seed)
  torch.cuda.manual_seed(seed)
  torch.backends.cudnn.deterministic = True


data = pd.read_csv(os.path.join('gas_drift.csv'))

print("Data")
print(data.shape)
print(data)

# Converter pra array numpy:
data = data.to_numpy()
# print(data.shape)

# Separação dos Dados em Treino, Validação e Teste
xtrain = data[:, 0:128]
ytrain = data[:, 128]
ytrain = ytrain.astype('int')
ytrain = ytrain-1

xtrain = minmax_scale(xtrain)

X_train, X_test, y_train, y_test = train_test_split(xtrain, ytrain, test_size=.10, random_state=42)

print("TRAIN")
print(X_train.shape)
#print(X_train)
print(y_train.shape)
#print(y_train)

print("\nTEST")
print(X_test.shape)
#print(X_test)
print(y_test.shape)
#print(y_test)

dataset_train = data_utils.TensorDataset(torch.FloatTensor(X_train), torch.LongTensor(y_train)) # Convertendo para Tensor
dataset_test = data_utils.TensorDataset(torch.FloatTensor(X_test), torch.LongTensor(y_test)) # Convertendo para Tensor



