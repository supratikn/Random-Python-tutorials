from PIL import Image
from PIL import ImageFilter
img = Image.open("Supratik.jpg")
bw = img.convert("L")
blur = img.filter(ImageFilter.BLUR)
detail = img.filter(ImageFilter.DETAIL)
edges= img.filter(ImageFilter.FIND_EDGES)
edges.show()

