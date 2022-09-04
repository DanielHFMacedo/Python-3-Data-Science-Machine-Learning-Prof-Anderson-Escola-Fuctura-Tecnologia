import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("pima-data.csv")
print(df)

#verificando se existem valores missing

print(df.isnull().values.any())

print(df.corr())

import sklearn as sk
