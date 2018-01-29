from PIL import Image

img = Image.open("Supratik.jpg")
area=(100,100,300,300)
c=img.crop(area)
img2 = Image.open("Dank Meme.jpg")
c1 = img2.crop(area)

r,g,b=c.split()
r1,g2,b2=c1.split()
newimg = Image.merge(img.mode, (r,g2,b2))
newimg.show()
