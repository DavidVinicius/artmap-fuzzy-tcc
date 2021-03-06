import numpy as np
from src.neural_networks.art import ART

class ARTFUZZY(ART):
    
    championIndex      = 0
    championValue      = 0    
    categoriesArray    = []

    def __init__(self, I, alpha = 0.001, rho = 0.5, beta = 1):
        super().__init__(I, alpha, rho, beta)
                      
    def learn(self, IC, W):
        temp1   = self._beta * self.AND(IC, W)
        temp2   = (1 - self._beta) * IC
        return temp1 + temp2

    def activate(self, i):
        temp    = np.zeros(len(self.W))
        temp[i] = 1
        self.Y.append(list(temp))
    
    def categories(self, alpha = 0.001):
        categories  = []        
        for i in range(0, len(self.I)):                                    
            a       = np.sum(self.AND(self.I[i], self.W[i]))
            temp    = round(a / (alpha + np.sum(self.W[i])), 5)
            categories.append(temp)
        return categories
    
    def hadRessonance(self, IC, W):
        x   = self.AND(IC, W)
        return ((sum(x) / sum(IC)) >= self._rho)
    
    def chooseChampion(self):
        categories      = self.categories(self._alpha)
        champion        = max(categories)
        championIndex   = categories.index(champion)

        return {
            "value": champion,
            "index": championIndex
        }
    
    def getIndexOfChampion(self):
        return self.championIndex
    
    def getValueOfChampion(self):
        return self.championValue

    def train(self):                
        for i in range(0, len(self.I)):                                
            self.match(i)
    
    def match(self, indexOfInput):
        categories      = self.categories(self._alpha)
        champion        = max(categories)
        championIndex   = categories.index(champion)

        while champion != 0:
            if self.hadRessonance(self.I[indexOfInput], self.W[championIndex]):
                self.W[championIndex]    = self.learn(self.I[indexOfInput], self.W[championIndex])
                
                self.activate(championIndex)
                self.Js.append([indexOfInput, championIndex])

                self.championIndex = championIndex
                self.championValue = champion
                
                break
            else:                    
                categories[championIndex] = 0
                champion                  = self.valueOfChampion(categories)
                championIndex             = self.indexOfChampion(categories)

    def searchForChampions(self, indexOfInput):
        self.categoriesArray  = self.categories(self._alpha)
        champion              = max(self.categoriesArray)
        championIndex         = self.categoriesArray.index(champion)

        while champion != 0:                
            if self.hadRessonance(self.I[indexOfInput], self.W[championIndex]):

                self.championIndex = championIndex
                self.championValue = champion

                break
            else:                    
                self.categoriesArray[championIndex] = 0
                champion                  = self.valueOfChampion(self.categoriesArray)
                championIndex             = self.indexOfChampion(self.categoriesArray)
