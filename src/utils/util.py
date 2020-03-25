import os
from PIL import Image

def getFolderItens(path):    
    return list(map(lambda x: path+x, os.listdir(path)))

def convertImageToLine(path):
    img = Image.open(path)
    im  = img.convert("L")
    return list(im.getdata())