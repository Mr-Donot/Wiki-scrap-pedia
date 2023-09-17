import requests
from bs4 import BeautifulSoup


class Scrapper:

    def __init__(self, url=None):
        self.url = url

    def getPageTxt(self, url=None):
        if url is None :
            if self.url is None :
                print("Need an URL to scrap.")
                return False
            page = requests.get(self.url)
        else:
            page = requests.get(url)
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
    
    def saveTextInFile(self, url=None, outputFileName = None):
        text = self.getPageTxt(url)
        if not text : return
        #TODO recup le titre de la page pour le nom du fichier

        if outputFileName is None : 
            fileName = "data/abc.txt"
        else :
            fileName = "data/" + outputFileName + ".txt"
        with open(fileName, "w", encoding="utf-8") as file:
            # Write the text to the file
            file.write(text)

    
    def saveListOfArticleInFile(self, listFileName, outputFileName):
        with open(listFileName, "r", encoding="utf-8") as file:
            text = file.read().split("\n")
        
        globalOutput = ""
        for url in text:
            text = self.getPageTxt(url)
            if text : globalOutput += text

        fileName = "data/" + outputFileName + ".txt"
        
        with open(fileName, "w", encoding="utf-8") as file:
            # Write the text to the file
            file.write(globalOutput)
