import numpy as np
from PIL import Image
from src.neural_networks.art_fuzzy import ARTFUZZY
from src.utils.functions import *

import os

path             = os.getcwd()
circ_imgs_paths  = path+"/imgs/Retangulo100x100/"
rect_imgs_paths  = path+"/imgs/Circulo100x100/"

list_circ_imgs   = os.listdir(circ_imgs_paths)
list_rect_imgs   = os.listdir(rect_imgs_paths)

imgs = list_circ_imgs + list_rect_imgs

imgs_paths = [circ_imgs_paths, rect_imgs_paths]

x = []
for img_path in imgs_paths:
    for i in imgs:    
        img = Image.open(img_path+str(i))
        im  = img.convert("L")
        x.append(list(im.getdata()))

arr = np.array(x)

valueMax = 255
IC       = layerF0(arr, valueMax)

print(IC)

r = ARTFUZZY(IC, rho = 0.95)
r.train()

print()
#print(r.W)
print(r.Js)

circ_pesos = []
rect_pesos = []

for i in r.Js:
    if i[0] < 40 and i[1] not in circ_pesos:
        circ_pesos.append(i[1])
    elif i[0] > 40 and i[1] not in rect_pesos:
        rect_pesos.append(i[1])

print(circ_pesos)
print(rect_pesos)

P  = 0
FN = 0
FP = 0
N  = 0

for i in r.Js:
    if i[0] < 40:
        if i[1] in circ_pesos:
            P += 1
        else:
            FN += 1
    else:
        if i[1] in rect_pesos:
            FP += 1
        else:
            N += 1

print('Positivo: '+str(P)+'\nNegativo: '+str(N)+'\nFalso Positivo: '+str(FP)+'\nFalso Negativo: '+str(FN))
print('Taxa de acerto: ', ((P+N)/40)*100)

 