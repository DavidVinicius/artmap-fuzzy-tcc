import numpy as np
from src.utils.functions import *
from src.neural_networks.artmap_fuzzy import ARTMAPFUZZY

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

INPUT   = layerF0(A, 1)
OUTPUT  = layerF0(B, 1)

ArtMapFuzzy = ARTMAPFUZZY(INPUT, OUTPUT, rhoINPUT=0.5, rhoOUTPUT=0.9, rho=0.6)

ArtMapFuzzy.train()


print("-----------------------RESULT")
print(ArtMapFuzzy.WAB)
print(ArtMapFuzzy.ArtA.W)
print(ArtMapFuzzy.ArtB.W)