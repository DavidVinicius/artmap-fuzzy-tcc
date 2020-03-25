import numpy as np

class ART():
    Y          = []
    Js         = []
    _W         = []
    categories = []
    
    def __init__(self, I, alpha = 0.001, rho = 0.5, beta = 1):
        self._alpha = alpha
        self._rho   = rho
        self._beta  = beta
        self.setI(I)  
        self.setW(np.ones(self.I.shape))

    @staticmethod
    def layerF0(I, valueMax = 0):
        IC = ART.normalize(I, valueMax)
        IC = ART.complement(IC)    
        return IC
    
    @staticmethod
    def normalize(arr, valueMax = 0):
        if valueMax == 0:
            valueMax = arr.max()

        I  = np.divide(arr, valueMax)
        return I
    
    @staticmethod
    def complement(I):
        IC = np.subtract(1, I)
        A  = []

        for i in range(0, len(I)):            
            A.append( np.concatenate((I[i], IC[i])) )
        
        return np.array(A)
        

    def AND(self, arr1, arr2):
        I = []
        for i in range(0, len(arr1)):
            I.append(min(arr1[i], arr2[i]))
        return I
    
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

    def hadRessonance(self, IC, W, rho):
        x   = self.AND(IC, W)
        return ((sum(x) / sum(IC)) >= rho)
    
    def vigilanceValue(self, IC, W):
        x   = self.AND(IC, W)
        return (sum(x) / sum(IC))
    
    def groupCategories(self, IC, W, alpha = 0.0001):
        categories  = []
        for i in range(0, len(IC)):
            a       = np.sum(self.AND(IC[i], W[i]))
            temp    = round(a / (alpha + np.sum(W[i])), 5)
            categories.append(temp)
        return categories
    
    def indexOfChampion(self, categories):
        championB      = max(categories)
        
        return categories.index(championB)
    
    def valueOfChampion(self, categories):
        return max(categories)