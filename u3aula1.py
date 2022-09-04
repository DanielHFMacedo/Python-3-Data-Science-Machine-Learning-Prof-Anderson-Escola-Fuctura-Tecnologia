import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Aula 23/04/2022 Assunto Numpy

a=np.array([1,2,3])
print(a)

#help(np.array)

lst=[0,1,2,3,4,5,6]
print("lst:\n",lst)
print(type(lst))
vetor1=np.array(lst)
print("vetor1:\n",vetor1)
print(type(vetor1))

# Podemos criar uma lista e passar ela para o array, ou criar uma lista dentro do np.array()

vetor1[3]=10 # Alteramos valores do array como alteramos listas
print(vetor1)
print("np.shape(vetor1):",np.shape(vetor1))
print(vetor1.dtype)

# arange
vetor2=np.arange(0.,5,0.5)
print("Vetor2:\n",vetor2) # Observe que o valor final 5 não entra no array
print("np.shape(vetor2):\n",np.shape(vetor2))
print(vetor2.dtype)

nulo=np.zeros((5,2))
print("Array nulo:\n",nulo)
nulo=np.zeros((2,5))
print("Array nulo:\n",nulo)
nulo=np.zeros((2,3,4))
print("Array nulo:\n",nulo)
diagonal=np.eye(3)
print("Array identidade:\n",diagonal)
diagonal=np.diag([1,2,3,4])
print("Array diagonal:\n",diagonal)
b=np.array([True,False,True])
print("Array boleano:\n",b)
b=np.diag([True,False,True])
print("Array boleano:\n",b)

array2=np.array([1,2,0,4,5], dtype=bool)
print(array2)
array2=np.array([1,2,0,4,5], dtype=str)
print(array2)
array2=np.array([1,2,0,4,5], dtype=float)
print(array2)
array2=np.array([1,2,0,4,5], dtype=int)
print(array2)

print("Usando linspace:\n",np.linspace(0,5,5))

print("Elemento 2x1:\n",diagonal[2,2])

#numero aleatorios

print("Aleatorios :\n",np.random.rand(10)) # Cria matriz de 10 termos com valores entre 0 e 1 normalmente distribuidos
print("Aleatorios Poisson:\n",np.random.poisson(10,5))
print("Aleatorios inteiros:\n",np.random.randint(0,10, 5)) # 5 inteiros entre 0 e 10
print("Aleatorios inteiros:\n",np.random.randint(-10,10, 5)) # 5 inteiros entre 0 e 10

print("Media vetor 1",np.mean(vetor1))
print("desvio padrao vetor 1",np.std(vetor1))
print("variancia vetor 1",np.var(vetor1))
v3=np.arange(1,10)
print("v3:",v3)
print(np.sum(v3))
print(np.cumsum(v3))
print(np.prod(v3))
print(np.cumprod(v3))

# coomparação de arrays
a=np.array([1,2,3,4,5])
b=np.array([4,2,2,4,6])
x= a==b
print(x)

print(a.max())

print(np.array([1,2,3])+1.5)
print(np.array([1,2,3])*3)
print(np.around([1.2,5.3,4.2,6.8]))

# concat
c=np.concatenate(((a,b)), axis=0)
print(c)

#copiando arrays
d=np.copy(a)
print("a",a)
print("d",d)
