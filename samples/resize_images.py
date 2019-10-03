from PIL import Image
import os    



path       =  os.getcwd()
imgs_paths = path+"/imgs/Circulo/"
imgs       = os.listdir(imgs_paths)

for i in imgs:
    img = Image.open(imgs_paths+i)
    im  = img.convert("L")
    im.thumbnail((50, 50), Image.ANTIALIAS)    
    img = im.point(lambda p: p < 100 and 255)
    img.save(path+"/imgs/CirculoB50x50/"+str(i)) 


quit()
print(imagem)
#quit()
