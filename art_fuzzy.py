import numpy as np
from funcoes import *

v = np.array([
    [7, 4.5],
    [2, 3]
])

valueMax = 10

IC = normalize(v, valueMax)
IC = complement(IC)



print(IC)