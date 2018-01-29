import requests
from bs4 import BeautifulSoup


def spider1(max_pages):
    page=1
    while page<=max_pages:
        url ='https://buckysroom.org/trade/search.php?page=' + str(page)
        source =requests.get(url)
        plainText =source.text
        soup =BeautifulSoup(plainText)
        for link in soup.findAll('a', {'class': 'item-name'}):
            href = "https://buckysroom.org" +link.get('href')
            print(href)

        page+=1


spider1(1)

