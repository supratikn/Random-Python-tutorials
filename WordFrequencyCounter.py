import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    wordList =[]
    sourceCode = requests.get(url).text
    soup = BeautifulSoup(sourceCode)
    for postText in soup.findAll('a',{'class': 'index_singleListingTitles'}):
        content = postText.string
        words = content.lower().split()
        for w in words:
            print(w)
            wordList.append(w)


start('https://buckysroom.org/tops.php?type=text&period=this-month')