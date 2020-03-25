from PIL import Image, ImageOps, ImageDraw

'''image = Image.new('RGB', (100, 100))
draw  = ImageDraw.Draw(image)
draw.ellipse((0, 0, 100, 100), fill=255)

#size = (128, 128)
#mask = Image.new('L', size, 0)
#draw = ImageDraw.Draw(mask) 
#draw.ellipse((0, 0) + size, fill=255)

#im = Image.open('./imgs/Circulo10x10/01.bmp')

#output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
#output.putalpha(mask)

image.save('output.png')'''

import math 
import uuid
from random import *
from PIL import Image, ImageDraw 

w, h = 512, 512
  
for i in range(0, 100):
    x = randrange(1, 256)
    y = randrange(1, 256)
    xx = randrange(100, 256)
    yy = randrange(256, 300)

    shape = [(x, y), (w - xx, h - xx)] 

    # creating new Image object 
    img = Image.new("RGB", (w, h), (255, 255, 255)) 

    # create rectangle image 
    img1 = ImageDraw.Draw(img)   
    img1.ellipse(shape, fill ="black", outline ="black") 
    filename = str(uuid.uuid4())
    img.save("./imgs/Elipse/"+filename+".png")     