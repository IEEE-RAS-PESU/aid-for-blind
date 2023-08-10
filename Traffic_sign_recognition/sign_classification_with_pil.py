from PIL import Image
import os

path = "C:\\Users\\namit\\Downloads\\traffic-signs-classification\\myData"

i=0

for root , directories, files in os.walk(path):
    for file in files:
        if file.endswith('.png'):
            pat=os.path.join(root, file)
            with Image.open(pat) as im:
                if im.size!=(32, 32):
                    im=im.resize((32, 32),Image.LANCZOS)
                im.save(pat.replace(".png",".jpg"))
            os.remove(pat)
            i+=1
            print(i,end='\r')
        elif file.endswith('.jpg'):
            pat=os.path.join(root, file)
            with Image.open(pat) as im:
                if im.size!=(32, 32):
                    im=im.resize((32, 32),Image.LANCZOS)
                    im.save(pat)
                    i+=1
                    print(i,end='\r')

