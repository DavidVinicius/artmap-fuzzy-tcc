import numpy as np
from PIL import Image
from src.neural_networks.artmap_fuzzy import ARTMAPFUZZY
from src.utils.functions import *

import os

path             = os.getcwd()
circ_imgs_paths  = path+"/imgs/Retangulo10x10/"
rect_imgs_paths  = path+"/imgs/Circulo10x10/"

list_circ_imgs   = os.listdir(circ_imgs_paths)
list_rect_imgs   = os.listdir(rect_imgs_paths)

imgs             = list_circ_imgs + list_rect_imgs

imgs_paths       = [circ_imgs_paths, rect_imgs_paths]

x = []
y = []

for img_path in imgs_paths:
    for i in imgs:    
        img = Image.open(img_path+str(i))
        im  = img.convert("L")
        x.append(list(im.getdata()))

        if "Circ" in img_path:
            y.append([1])
        else:
            y.append([0])

x     = np.array(x)

INPUT            = layerF0(x, 255)
OUTPUT           = layerF0(y, 1)

#print(OUTPUT)
#quit()

rhoInput         = 0.5
rhoOutput        = 0.99999
rhoMatchTracking = 0.6

ArtMapFuzzy = ARTMAPFUZZY(INPUT, OUTPUT, rhoINPUT=rhoInput, rhoOUTPUT=rhoOutput, rho=rhoMatchTracking)
ArtMapFuzzy.train()


print("-----------------------RESULT")
print("MATCH TRACKING:\n", ArtMapFuzzy.WAB, "\n")
print("ART A:\n", ArtMapFuzzy.ArtA.W, "\n")
print("ART B:\n", ArtMapFuzzy.ArtB.W)



print("TESTE", ArtMapFuzzy.test(INPUT[0], 0.7))
print("TESTE", ArtMapFuzzy.testMapped(INPUT[0], 0.7))



