import numpy as np
from src.utils.functions import *
from src.neural_networks.art_fuzzy import ARTFUZZY

A = np.array([
    [0.25, 0.25],
    [0.25, 0.75],
    [0.75, 0.25],
    [0.75, 0.75]
])

B = np.array([
    [0.25],
    [0.75],
    [0.75],
    [0.25]
])

AC   = layerF0(A, 1)
BC   = layerF0(B, 1)


WAB   = np.ones([AC.shape[0], BC.shape[0]])

rhoA  = 0.5
rhoB  = 0.9
rhoAB = 0.6

ArtA = ARTFUZZY(AC, rho=rhoA)
ArtB = ARTFUZZY(BC, rho=rhoB)

categoriesA    = ArtA.categories()
categoriesB    = ArtB.categories()

for i in range(0, len(ArtB.I)):

    
    
    championB      = max(categoriesB)
    championIndexB = categoriesB.index(championB)

    
    print()

    
    if ArtB.hadRessonance(ArtB.I[i], ArtB.W[championIndexB]):
        
        ArtB.W[championIndexB] = ArtB.learn(ArtB.I[i], ArtB.W[championIndexB])
                        
        ArtB.activate(championIndexB)
        ArtB.Js.append([i, championIndexB])

        championA       = max(categoriesA)
        championIndexA  = categoriesA.index(championA)

        for j in range(0, len(ArtA.I)):
            print(i,j)
            if ArtA.hadRessonance(ArtA.I[j], ArtA.W[championIndexA]):        
                
                ArtA.activate(championIndexA)
                ArtA.Js.append([j, championIndexA])
                
                
                if hadRessonance(ArtB.Y[championIndexB], WAB[championIndexB], rhoAB):        
                    print()
                    ArtA.W[championIndexA] = ArtA.learn(ArtA.I[j], ArtA.W[championIndexA])                    
                    
                    WAB[championIndexA]    = activate(WAB, championIndexB)
                    print(activate(WAB, championIndexB), championIndexA)
                    print(WAB)
                    break
                else:
                    categoriesA[championIndexA] = 0
                    championA                   = max(categoriesA)
                    championIndexA              = categoriesA.index(championA)

                    x                           = AND(ArtB.Y[championIndexB], WAB[championIndexB])
                    temp                        = (sum(x) / sum(ArtB.Y[championIndexB]))

                    ArtA._rho                   += 0.01
                    print(ArtA._rho)
            else:
                categoriesA[championIndex]  = 0
                champion                    = max(categoriesA)
                championIndex               = categoriesA.index(champion)

    else:
        categoriesB[championIndexB] = 0



