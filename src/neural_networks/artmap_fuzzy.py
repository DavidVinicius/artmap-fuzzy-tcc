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

        for i in range(0, len(self.ArtB.I)):
            
            categoriesA    = self.ArtA.categories()
            categoriesB    = self.ArtB.categories()
            
            champion       = self.valueOfChampion(categoriesB)
            championIndexB = self.indexOfChampion(categoriesB)

            while champion != 0:
                if self.ArtB.hadRessonance(self.ArtB.I[i], self.ArtB.W[championIndexB]):
                    print(championIndexB)
                else:            
                    categoriesB[championIndexB] = 0
                    championIndexB              = self.indexOfChampion(categoriesB)
            

    