from PIL import Image
import os    



path       =  os.getcwd()
imgs_paths = path+"/imgs/Estrela/"
imgs       = os.listdir(imgs_paths)

for i in imgs:
    img = Image.open(imgs_paths+i)
    im  = img.convert("L")
    im.thumbnail((50, 50), Image.ANTIALIAS)
    im.save(path+"/imgs/Estrela50x50/"+str(i)) 


quit()
print(imagem)
#quit()
