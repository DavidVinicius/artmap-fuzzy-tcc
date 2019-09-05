import numpy as np
from src.utils.functions import *

v = np.array([
    [0.2, 0.1, 0.1],
    [0.3, 0.2, 0.1],    
    [0.3, 0.3, 0.2],
    [0.2, 0.3, 0.3],
    [0.1, 0.2, 0.3],
])

valueMax = 1
IC       = layerF0(v, valueMax)

Y     = []

alpha = 0.0001
rho   = 0.5
beta  = 1


W  = np.ones(IC.shape)
Y  = []

print("Input values\n", IC, "\n")
print("Weight\n", W, "\n")


for i in range(0, len(IC)):
    
    categories    = groupCategories(IC, W, alpha)

    champion      = max(categories)
    championIndex = categories.index(champion)
    
    print("Loop: i =", i, "\n ")
    print("Categories:", categories)
    print("Champion:", champion)

    while champion != 0:                
        if hadRessonance(IC[i], W[championIndex], rho):
            print("Teve Ressonância!")
            print("Index:", championIndex)
            print("Pesos antes da atualizacao: ", W[championIndex])
            print("Entrada", IC[i])
            print()
            W[championIndex]    = learn(IC[i], W[championIndex], beta)
            
            temp                = np.zeros(len(W))
            temp[championIndex] = 1
            Y.append(list(temp))

            print("Atualizado!")
            print("IC", IC[i])
            print("W", W[championIndex])            
            print("----------------------")
            break
        else:
            print("Não teve ressonância")
            categories[championIndex] = 0
            champion                  = max(categories)
            championIndex             = categories.index(champion)
    
#print("Categories", categories)
print("")
#print(categories)
print("-----")
print("Pesos finais")
print(W)
print("-----")
print(Y)