import numpy as np
from PIL import Image
from src.neural_networks.art_fuzzy import ARTFUZZY

img = Image.open(r"C:/Users/ht3000052/Documents/artmap-fuzzy-tcc/samples/circ.png").convert('RGBA')
im  = img.convert("L")
arr = np.array(list(im.getdata()))
arr = np.divide(arr, 255)


r = ARTFUZZY(arr)

print()
print(arr.size)

# arr = np.fromiter(iter(im.getdata()), np.uint8)
# arr.resize(im.height, im.width)

# arr ^= 0xFF  # invert
# inverted_im = Image.fromarray(arr, mode='L')
# inverted_im.show()

quit()