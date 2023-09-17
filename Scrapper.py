import requests
from bs4 import BeautifulSoup


class Scrapper:

    def __init__(self, url):
        self.url = url

    def getPageTxt(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        result = soup.find(id="mw-content-text")
        r = result.find(class_="mw-parser-output")
        c=0
        tabResult = []
        for balise in r :
            c+= 1
            if c > 6 :
                tabResult.append(balise.text)

        return "".join(tabResult)
    
    def saveTextInFile(self):
        text = self.getPageTxt()
        
        #TODO recup le titre de la page pour le nom du fichier
        fileName = "data/abc.txt"
        
        with open(fileName, "w", encoding="utf-8") as file:
            # Write the text to the file
            file.write(text)