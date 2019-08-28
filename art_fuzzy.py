import numpy as np
from funcoes import *

v = np.array([
    [0.3, 0.2, 0.1],
    [0.2, 0.1, 0.1],
    [0.3, 0.3, 0.2],
    [0.2, 0.3, 0.3],
    [0.1, 0.2, 0.3],
])

Y     = []

alpha = 0.0001
rho   = 0.5
beta  = 1

valueMax = 1

IC = normalize(v, valueMax)
IC = complement(IC)

W  = np.ones(IC.shape)
Y  = []

print("Input values\n", IC, "\n")
print("Weight\n", W, "\n")

for i in range(0, len(IC)):

    categories    = groupCategories(IC, W, alpha)
    champion      = np.amax(categories)
    championIndex = np.argmin(categories)
 
    while champion != 0:        
        if hadRessonance(IC[championIndex], W[championIndex], rho):
            W[championIndex] = learn(IC[championIndex], W[championIndex], beta)
            temp                = np.zeros(len(W))
            temp[championIndex] = 1
            Y.append(list(temp))

            print("Recorrência em:", championIndex)
            print(learn(IC[championIndex], W[championIndex], beta))
            break
        else:
            categories[champion] = 0
            champion             = np.amax(categories)
            championIndex = np.argmin(categories)

print("Categories", categories)
print("I choose my champion:", champion, "Champion Index", championIndex)

#print(categories)
print("-----")
print("-----")
print(W)
print(Y)