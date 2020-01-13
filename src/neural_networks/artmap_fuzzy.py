import numpy as np
from src.neural_networks.art_fuzzy import ARTFUZZY
from src.neural_networks.art import ART

class ARTMAPFUZZY(ART):
    ArtA  = []
    ArtB  = []
    rho   = 0
    WAB   = []

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

            while championA != 0:                
                print("Vigilance Art A: ", self.vigilanceValue(self.ArtA.I[i], self.ArtA.W[championIndexA]), self.rho)
                if self.ArtA.hadRessonance(self.ArtA.I[i], self.ArtA.W[championIndexA]):
                    
                    self.ArtA.activate(championIndexA)
                    self.ArtA.Js.append([i, championIndexA])

                    print("Vigilance Match: ", self.vigilanceValue(self.ArtB.Y[championIndexB], self.WAB[championIndexA]))
                        
                    if self.hadRessonance(self.ArtB.Y[championIndexB], self.WAB[championIndexA], self.rho):
                        self.ArtA.W[championIndexA] = self.ArtA.learn(self.ArtA.I[i], self.ArtA.W[championIndexA])
                        
                        print("Ressonance")
                        print("Ativacao", self.ArtB.Y[championIndexB], self.WAB[championIndexA], championIndexB)
                        print("Peso ArtA\n", self.ArtA.W, championIndexA)
                        print("Peso ArtB\n", self.ArtB.W)
                        print("learning Match", self.activate(self.WAB[championIndexA], championIndexB))
                        
                        self.WAB[championIndexA]  = self.activate(self.WAB[championIndexA], championIndexB)
                        print("MAtch\n", self.WAB)
                        print()
                        break

                    else:
                        categories[championIndexA] = 0                
                        championA                  = self.valueOfChampion(categories)
                        championIndexA             = self.indexOfChampion(categories)

                        x                          = self.AND(self.ArtA.I[i], self.ArtA.W[championIndexA])
                        newRho                     = (sum(x) / sum(self.ArtA.I[i]))
                        print(newRho, "NOVO", x, self.ArtA.I[i])

                        self.ArtA._rho            = newRho + 0.05

                    
                else:                    
                    print("NAO PASSOU", championIndexA, championA)
                    categories[championIndexA] = 0                
                    championA                  = self.valueOfChampion(categories)
                    championIndexA             = self.indexOfChampion(categories)


            
            print()
    
    
    def activate(self, W, i):
        temp    = np.zeros(len(W))
        temp[i] = 1
        return list(temp)

    def matchTracking(self):
        pass
            

    