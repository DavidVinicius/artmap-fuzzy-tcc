import numpy as np
from src.utils.functions import *
from src.neural_networks.art import ART

class ARTFUZZY(ART):
    
    def __init__(self, I, alpha = 0.001, rho = 0.5, beta = 1):
        super().__init__(I, alpha = 0.001, rho = 0.5, beta = 1)
                      
    def learn(self, IC, W, beta):
        temp1   = beta * AND(IC, W)
        temp2   = (1 - beta) * IC
        return temp1 + temp2

    def activate(self, i):
        temp    = np.zeros(len(self.W))
        temp[i] = 1
        self.Y.append(list(temp))
    
    def categories(self, alpha = 0.0001):
        categories  = []
        for i in range(0, len(self.I)):
            a       = np.sum(AND(self.I[i], self.W[i]))
            temp    = round(a / (alpha + np.sum(self.W[i])), 5)
            categories.append(temp)
        return categories
    
    def hadRessonance(self, IC, W):
        x   = AND(IC, W)
        return ((sum(x) / sum(IC)) >= self._rho)
    
    def chooseChampion(self):
        categories      = self.categories(self._alpha)
        champion        = max(categories)
        championIndex   = categories.index(champion)

        return {
            "value": champion,
            "index": championIndex
        }

    def train(self):        
        
        for i in range(0, len(self.I)):
                
            categories      = self.categories(self._alpha)
            champion        = max(categories)
            championIndex   = categories.index(champion)
    
            while champion != 0:                
                if self.hadRessonance(self.I[i], self.W[championIndex]):
                    self.W[championIndex]    = self.learn(self.I[i], self.W[championIndex], self._beta)
                    
                    self.activate(championIndex)
                    self.Js.append([i, championIndex])
                    
                    break
                else:                    
                    categories[championIndex] = 0
                    champion                  = max(categories)
                    championIndex             = categories.index(champion)
