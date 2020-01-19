import numpy as np
from src.neural_networks.art_fuzzy import ARTFUZZY
from src.neural_networks.art import ART

class ARTMAPFUZZY(ART):
    ArtA       = []
    ArtB       = []
    rho        = 0
    WAB        = []
    championsA =[]

    def __init__(self, INPUT, OUTPUT, rhoINPUT=0.5, rhoOUTPUT=0.5, rho=0.5):
        self.ArtA = ARTFUZZY(INPUT, rho=rhoINPUT)
        self.ArtB = ARTFUZZY(OUTPUT, rho=rhoOUTPUT)
        self.rho  = rho        
        self.WAB  = np.ones([INPUT.shape[0], OUTPUT.shape[0]])
    

    def train(self):
        print("Treinando ...")

        for i in range(0, len(self.WAB)):            
            self.ArtB.match(i)
            
            
            championIndexB  = self.ArtB.getIndexOfChampion()            

            print("-------", i)
            print(championIndexB, self.ArtB.getValueOfChampion())

            categories      = self.ArtA.categories()            
            championA       = self.valueOfChampion(categories)
            championIndexA  = self.indexOfChampion(categories)

            while championIndexA in self.championsA:
                categories[championIndexA] = 0
                championA                  = self.valueOfChampion(categories)
                championIndexA             = self.indexOfChampion(categories)
            else:
                self.championsA.append(championIndexA)

            print("Champion A:", championIndexA, championA)

            while championA != 0:                
                print("Vigilance test Art A: ", self.vigilanceValue(self.ArtA.I[i], self.ArtA.W[championIndexA]), self.rho)
                if self.ArtA.hadRessonance(self.ArtA.I[i], self.ArtA.W[championIndexA]):
                    

                    print("Vigilance test Match tracking: ", self.vigilanceValue(self.ArtB.Y[championIndexB], self.WAB[championIndexA]))
                        
                    if self.hadRessonance(self.ArtB.Y[championIndexB], self.WAB[championIndexA], self.rho):
                        self.ArtA.W[championIndexA]    = self.ArtA.learn(self.ArtA.I[i], self.ArtA.W[championIndexA])
                        self.ArtA.activate(championIndexA)
                        self.ArtA.Js.append([i, championIndexA])
                        
                        print("Ressonance!")
                        print("Ativacao", self.ArtB.Y[championIndexB], self.WAB[championIndexA], championIndexB)                                                
                        
                        self.WAB[championIndexA]  = self.activate(self.WAB[championIndexA], championIndexB)                        
                        print()
                        break

                    else:
                        categories[championIndexA] = 0                
                        championA                  = self.valueOfChampion(categories)
                        championIndexA             = self.indexOfChampion(categories)

                        x                          = self.AND(self.ArtA.I[i], self.ArtA.W[championIndexA])
                        newRho                     = (sum(x) / sum(self.ArtA.I[i]))
                        print(newRho, "NOVO", x, self.ArtA.I[i])

                        self.ArtA._rho            = newRho

                    
                else:                    
                    print("NAO PASSOU", championIndexA, championA)
                    categories[championIndexA] = 0                
                    championA                  = self.valueOfChampion(categories)
                    championIndexA             = self.indexOfChampion(categories)
    
    
    def train2(self):
        for i in range(0, len(self.WAB)):
            self.ArtB.searchForChampions(i)
            self.ArtA.searchForChampions(i)

            championIndexB = self.ArtB.getIndexOfChampion()
            championIndexA = self.ArtA.getIndexOfChampion()

            champion       = self.ArtA.getValueOfChampion()

            self.ArtB.activate(championIndexB)
            self.ArtA.activate(championIndexA)

            while champion != 0:
                if self.hadRessonance(self.ArtB.Y[championIndexB], self.WAB[championIndexA], self.rho):
                    
                    self.ArtA.W[championIndexA] = self.ArtA.learn(self.ArtA.I[i], self.ArtA.W[championIndexA])                        
                    self.ArtB.W[championIndexB] = self.ArtB.learn(self.ArtB.I[i], self.ArtB.W[championIndexB])                        
                    
                    self.WAB[championIndexA]    = self.activate(self.WAB[championIndexA], championIndexB)            
                    break
                else:
                    self.ArtA.categoriesArray[championIndexA] = 0                
                    champion                  = self.valueOfChampion(self.ArtA.categoriesArray)
                    championIndexA            = self.indexOfChampion(self.ArtA.categoriesArray)                

                    x                          = self.AND(self.ArtA.I[i], self.ArtA.W[championIndexA])
                    newRho                     = (sum(x) / sum(self.ArtA.I[i]))
                    print(newRho, "NOVO", x, self.ArtA.I[i])

                    self.ArtA._rho            += 0.01


    def activate(self, W, i):
        temp    = np.zeros(len(W))
        temp[i] = 1
        return list(temp)

    def matchTracking(self):
        pass
            

    