from src.neural_networks.art_fuzzy import ARTFUZZY
import numpy as np


def test_If_I_isintance_numpy():
    A = ARTFUZZY([1.0, 2.0])    
    assert isinstance(A.I, np.ndarray)

def test_If_W_isintance_numpy():
    A = ARTFUZZY([1.0, 2.0])    
    assert isinstance(A.I, np.ndarray)