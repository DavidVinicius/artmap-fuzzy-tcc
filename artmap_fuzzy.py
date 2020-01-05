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

categoriesB  = ArtB.categories()
championB    = ArtB.chooseChampion()

print(championB.get("value"))
print()

championIndex = championB.get("index")

if ArtB.hadRessonance(ArtB.I[0], ArtB.W[championIndex]):
    ArtB.W[championIndex] = ArtB.learn(ArtB.I[0], ArtB.W[championIndex])
                    
    ArtB.activate(championIndex)
    ArtB.Js.append([0, championIndex])
    print(ArtB.Js, ArtB.Y)
    print(ArtB.W)
    
    categoriesA   = ArtA.categories()
    championA     = ArtA.chooseChampion()
    championIndex = championA.get("index")

    if ArtA.hadRessonance(ArtA.I[0], ArtA.W[championIndex]):
        ArtA.W[championIndex] = ArtA.learn(ArtA.I[0], ArtA.W[championIndex])
                    
        ArtA.activate(championIndex)
        ArtA.Js.append([0, championIndex])
        print()
        print(ArtA.Js, ArtA.Y)
        print(ArtA.W)


