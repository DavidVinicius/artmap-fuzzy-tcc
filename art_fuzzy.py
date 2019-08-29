import numpy as np
from funcoes import *

v = np.array([
    [0.2, 0.1, 0.1],
    [0.3, 0.2, 0.1],    
    [0.3, 0.3, 0.2],
    [0.9, 0.9, 0.9],
    [0.2, 0.3, 0.3],
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

#quit()

print("Input values\n", IC, "\n")
print("Weight\n", W, "\n")


for i in range(0, len(IC)):
    
    categories    = groupCategories(IC, W, alpha)

    champion      = max(categories)
    championIndex = categories.index(champion)
    
    print("categories i=", i, "\n ", categories)
    print("Champion:", champion)

    while champion != 0:        
        if hadRessonance(IC[championIndex], W[championIndex], rho):
            print("Recorrência!")
            print("Index:", championIndex)
            print("Pesos antes da atualizacao: ", W[championIndex])
            print("Entrada", IC[championIndex])
            print()
            W[championIndex]    = learn(IC[championIndex], W[championIndex], beta)
            
            temp                = np.zeros(len(W))
            temp[championIndex] = 1
            Y.append(list(temp))

            print("Atualizado!")
            print("IC", IC[championIndex])
            print("W", W[championIndex])            
            print("----------------------")
            break
        else:
            categories[champion] = 0
            champion             = np.amax(categories)
            championIndex        = np.argmin(categories)
    
    '''categories    = groupCategories(IC, W, alpha)
    champion      = max(categories)
    championIndex = categories.index(champion)'''

#print("Categories", categories)
print("")
print("I choose my champion:", champion, "Champion Index", championIndex)

#print(categories)
print("-----")
print("Pesos finais")
print(W)
print("-----")
print(Y)