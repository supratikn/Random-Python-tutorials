from PIL import Image

img = Image.open("Supratik.jpg")
square=img.resize((250,250))
flip=img.transpose(Image.FLIP_LEFT_RIGHT)
spin=img.transpose(Image.ROTATE_90)
