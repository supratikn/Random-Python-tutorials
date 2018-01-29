from PIL import Image

img = Image.open("Supratik.jpg")
print(img.size)
print(img.format)
area =(100,100, 300,375)
cropped = img.crop(area)

cropped.show()



