from src.neural_networks.art_fuzzy import ARTFUZZY
from src.utils.functions import *
import numpy as np

v = np.array([
    [0.2, 0.1, 0.1],
    [0.3, 0.2, 0.1],    
    [0.3, 0.3, 0.2],
    [0.2, 0.3, 0.3],
    [0.1, 0.2, 0.3],
])

valueMax = 1
IC       = layerF0(v, valueMax)

r = ARTFUZZY(IC)
r.train()
print(r.W)
print(r.Js)