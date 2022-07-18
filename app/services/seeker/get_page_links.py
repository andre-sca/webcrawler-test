from bs4 import BeautifulSoup
import urllib.request
import re
from services import utils

def getPageLinks(url, linkList, index):

    if len(linkList) < 100:

        try:
            page = urllib.request.urlopen(url)

            BSoup = BeautifulSoup(page, "html.parser", from_encoding = "iso-8859-1")

            auxList = []

            for link in (BSoup.findAll('a', attrs={'href': re.compile("^http://")}) or BSoup.findAll('a', attrs={'href': re.compile("^https://")})):
                nextLink = link.get('href')

                if nextLink not in linkList:
                    linkList.append(nextLink)
                    auxList.append(nextLink)
            utils.addLinks(auxList)
            if index is None:
                index = 0
            else:
                index = index + 1

            getPageLinks(linkList[index], linkList, index)

        except Exception as e:
            print(e)
    else:
        return linkList

    return linkList
    
