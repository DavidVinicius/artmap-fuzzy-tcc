import numpy as np
from PIL import Image
from src.neural_networks.artmap_fuzzy import ARTMAPFUZZY
from src.utils.util import *
from random import *

import os

path             = os.getcwd()
list_circ_imgs   = getFolderItens(path+"/imgs/Elipse10x10/")
list_rect_imgs   = getFolderItens(path+"/imgs/Retangulo10x10/")
imgs_paths       = list_circ_imgs + list_rect_imgs

x = []
y = []

for img_path in imgs_paths:    
    img       = convertImageToLine(img_path)
    x.append(img)

    if "Elipse" in img_path:
        y.append([0])            
    else:
        y.append([1])            

x     = np.array(x)

print(len(x))

INPUT            = ARTMAPFUZZY.layerF0(x, 255)
OUTPUT           = ARTMAPFUZZY.layerF0(y, 1)

#print(OUTPUT)
#quit()

rhoInput         = 0.9999
rhoOutput        = 0.99999
rhoMatchTracking = 0.9999

ArtMapFuzzy = ARTMAPFUZZY(INPUT, OUTPUT, rhoINPUT=rhoInput, rhoOUTPUT=rhoOutput, rho=rhoMatchTracking)
ArtMapFuzzy.train()

Map = {
    "00001010": "Círculo",
    "10100000": "Retângulo",
    "00101000": "Estrela",
    "10000010": "Quadrado"
}

print("-----------------------RESULT")
print("INTER ART:\n", ArtMapFuzzy.WAB, "\n")
print("ART A:\n", ArtMapFuzzy.ArtA.W, "\n")
print("ART B:\n", ArtMapFuzzy.ArtB.W)

#print("TESTE", ArtMapFuzzy.testMapped(INPUT[0], 0.997))
#print("TESTE", ArtMapFuzzy.testMapped(INPUT[50], 0.9999))
t         = []
imgs      = getFolderItens("./imgs/Teste_Retangulo10x10/")
for i in imgs:
    img       = convertImageToLine(i)
    t.append(img)

INPUT_TESTE  = ARTMAPFUZZY.layerF0(t, 255)

for i in range(0, 20):
    output    = ArtMapFuzzy.testMapped(INPUT_TESTE[i], 0.99999)
    print(output)
#print(ARTMAPFUZZY.normalize(img, 255))

'''for i in range(0, 20):
    x = randrange(0, 80)    
    output = ArtMapFuzzy.testMapped(INPUT[x], 0.99999)
    print(x, Map.get(output.get("id")))
    #print(x, output)
'''


