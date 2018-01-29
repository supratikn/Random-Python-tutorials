import random
import urllib.request

def downloadWebImage(url):
    name =random.randrange(1,1000)
    fullName = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullName)


downloadWebImage("https://img-9gag-fun.9cache.com/photo/aDz072B_700b.jpg")