from src.neural_networks.art_fuzzy import ARTFUZZY
from src.utils.functions import *
import numpy as np
import pytest


@pytest.fixture()
def resource():
    print("setup")
    yield "resource"
    print("teardown")

def test_if_values_is_valids():
    v = np.array([
        [0.2, 0.1, 0.1],
        [0.3, 0.2, 0.1],    
        [0.3, 0.3, 0.2],
        [0.2, 0.3, 0.3],
        [0.1, 0.2, 0.3],
    ])
    
    valueMax = 1
    IC       = layerF0(v, valueMax)

    A = ARTFUZZY(IC)   
    A.train()
    actual      = [0.1, 0.1, 0.1, 0.7, 0.7, 0.7]
    assert all([a == b for a, b in zip(actual, A.W[0])])
    