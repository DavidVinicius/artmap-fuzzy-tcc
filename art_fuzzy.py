import numpy as np
from funcoes import *

v = np.array([
    [7, 4.5, 6],
    [2, 3, 9]
])

Y     = []

alpha = 0.0001
p     = 0.5
beta  = 1

valueMax = 10

IC = normalize(v, valueMax)
IC = complement(IC)

W  = np.ones(IC.shape)
T  = []

for i in range(0, len(IC)):
    a = np.sum(AND(IC[i], W[i]))
    T.append(a / (alpha + np.sum(W[i])))

champion      = np.amax(T)
championIndex = np.argmin(T)

teste = np.sum(AND(IC[championIndex], W[championIndex])) / np.sum(IC[championIndex])

if teste > p:
    print("OCORREU RECORRÊNCIA", teste)
    Y.append(np.zeros(len(IC)))
    #Y[championIndex] = 1

print("I choose my champion:", champion ,championIndex)

print(Y)
'''
print(IC)
print("-----")
print("-----")
print(W)
'''