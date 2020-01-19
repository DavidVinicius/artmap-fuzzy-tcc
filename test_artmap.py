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

A = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

B = np.array([
    [0],
    [0],
    [0],
    [1]
])

INPUT            = layerF0(A, 1)
OUTPUT           = layerF0(B, 1)
rhoInput         = 0.5
rhoOutput        = 0.9
rhoMatchTracking = 0.6

ArtMapFuzzy = ARTMAPFUZZY(INPUT, OUTPUT, rhoINPUT=0.5, rhoOUTPUT=0.9, rho=0.6)

ArtMapFuzzy.train()
print()
print("-----------------------INPUT")
print("Match tracking rho:",rhoMatchTracking, "\n")
print("Art A --> rho:",rhoInput,"\n", INPUT,"\n")
print("Art B --> rho:",rhoOutput,"\n", OUTPUT,"\n")


print("-----------------------RESULT")
print("MATCH TRACKING:\n", ArtMapFuzzy.WAB, "\n")
print("ART A:\n", ArtMapFuzzy.ArtA.W, "\n")
print("ART B:\n", ArtMapFuzzy.ArtB.W)