from bs4 import BeautifulSoup
import urllib.request
import re

def getPageLinks(url, linkList):
    try:
        page = urllib.request.urlopen(url)

        BSoup = BeautifulSoup(page, "html.parser", from_encoding="iso-8859-1")

        for x in (BSoup.findAll('a', attrs={'href': re.compile("^http://")}) or BSoup.findAll('a', attrs={'href': re.compile("^https://")})):
            nextLink = x.get('href')

            if nextLink not in linkList:
                linkList.append(nextLink)
            else:
                break
    except:
        print("error")



