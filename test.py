import numpy as np
from PIL import Image
from src.neural_networks.art_fuzzy import ARTFUZZY
from src.utils.functions import *

import os

path             = os.getcwd()
circ_imgs_paths  = path+"/imgs/Retangulo5x5/"
rect_imgs_paths  = path+"/imgs/Circulo5x5/"

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


r = ARTFUZZY(IC, rho = 0.99)
r.train()

print()
print(r.W)
print(r.Js)

# arr = np.fromiter(iter(im.getdata()), np.uint8)
# arr.resize(im.height, im.width)

# arr ^= 0xFF  # invert
# inverted_im = Image.fromarray(arr, mode='L')
# inverted_im.show()

quit()