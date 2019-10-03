import numpy as np
from PIL import Image

im = Image.open(r"C:/Users/ht3000052/Documents/artmap-fuzzy-tcc/samples/circ.png")

#im=im.rotate(1)

im2= im.convert("L")
threshold = 100
im = im2.point(lambda p: p < threshold and 255)
im.save("d.jpg")