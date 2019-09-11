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

AC = layerF0(A, 1)
BC = layerF0(B, 1)

ArtA = ARTFUZZY(AC)
ArtB = ARTFUZZY(BC)

'''print("Art A")
print("Pesos: \n", ArtA.W," \n Matriz: \n", AC)
print("\n Artb")
print(ArtB.W, BC)'''

categoriesA = ArtA.categories()
categoriesB = ArtB.categories()

championA    = ArtA.chooseChampion()
championB    = ArtB.chooseChampion()


print(champion.get("value"))
print()
