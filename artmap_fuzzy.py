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

for i in range(0, len(ArtB.I)):

    categoriesB  = ArtB.categories()
    championB    = ArtB.chooseChampion()

    print(championB.get("value"))
    print()

    championIndexB = championB.get("index")

    if ArtB.hadRessonance(ArtB.I[i], ArtB.W[championIndexB]):
        ArtB.W[championIndexB] = ArtB.learn(ArtB.I[i], ArtB.W[championIndexB])
                        
        ArtB.activate(championIndexB)
        ArtB.Js.append([i, championIndexB])
        #print(ArtB.Js, ArtB.Y)
        #print(ArtB.W)
        for j in range(0, len(ArtA.I)):
        
            categoriesA   = ArtA.categories()
            championA     = ArtA.chooseChampion()
            championIndex = championA.get("index")
            

            if ArtA.hadRessonance(ArtA.I[j], ArtA.W[championIndex]):        
                ArtA.activate(championIndex)
                ArtA.Js.append([j, championIndex])
                
                
                if hadRessonance(ArtB.Y[championIndexB], WAB[championIndexB], rhoAB):        
                    
                    ArtA.W[championIndex] = ArtA.learn(ArtA.I[j], ArtA.W[championIndex])                    
                    WAB[championIndexB] = activate(WAB, championIndex)
                    print()
                    print(WAB)
                else:
                    categoriesA[championIndex]  = 0
                    champion                    = max(categoriesA)
                    championIndex               = categoriesA.index(champion)
                    x                           = AND(ArtB.Y[championIndexB], WAB[championIndexB])
                    temp                        = (sum(x) / sum(ArtB.Y[championIndexB]))

                    ArtA._rho                   += 0.01
            else:
                categoriesA[championIndex]  = 0
                champion                    = max(categoriesA)
                championIndex               = categoriesA.index(champion)

    else:
        categoriesB[championIndexB] = 0
        champion                    = max(categoriesB)
        championIndexB              = categoriesB.index(champion)



