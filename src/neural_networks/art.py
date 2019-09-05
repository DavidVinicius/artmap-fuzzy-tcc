import numpy as np

class ART():
    Y   = []
    _W  = []
    
    def __init__(self, I, alpha = 0.001, rho = 0.5, beta = 1):
        self._alpha = alpha
        self._rho   = rho
        self._beta  = beta
        self.setI(I)  
        self.setW(np.ones(self.I.shape))
    
    @property
    def I(self):
        return self._I
    
    
    def setI(self, I):
        if isinstance(I, np.ndarray):
            self._I = I
        else:
            self._I = np.array(I)
    
    @property
    def W(self):
        return self._W
    
    
    def setW(self, W):
        if isinstance(W, np.ndarray):
            self._W = W
        else:
            self._W = np.array(W)