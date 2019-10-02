import numpy as np
from PIL import Image
from src.neural_networks.art_fuzzy import ARTFUZZY
from src.utils.functions import *

from os import listdir

path = "C:/Users/ht3000052/Documents/artmap-fuzzy-tcc/imgs/Circulo/"

imgs_paths = listdir(path)
x = []
for i in imgs_paths:
    img = Image.open(r"C:/Users/ht3000052/Documents/artmap-fuzzy-tcc/imgs/Circulo/"+i)
    im  = img.convert("L")
    x.append(list(im.getdata()))

arr = np.array(x)

valueMax = 255
IC       = layerF0(arr, valueMax)

print(IC)

r = ARTFUZZY(IC, rho=0.8)
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