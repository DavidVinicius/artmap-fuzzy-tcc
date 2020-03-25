from PIL import Image
import os    



path       =  os.getcwd()
imgs_paths = path+"/imgs/Elipse/"
imgs       = os.listdir(imgs_paths)

for i in imgs:
    img = Image.open(imgs_paths+i)
    im  = img.convert("L")
    im.thumbnail((10, 10), Image.ANTIALIAS)    
    #img = im.point(lambda p: p < 100 and 255)
    im.save(path+"/imgs/Elipse10x10/"+str(i)) 


quit()
#print(imagem)
#quit()
