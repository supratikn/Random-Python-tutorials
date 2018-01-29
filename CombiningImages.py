from PIL import Image

s = Image.open("Supratik.jpg")
g = Image.open("Dank Meme.jpg")

area=(100,100,300,300)
cropped = s.crop(area)

g.paste(cropped)
g.show()