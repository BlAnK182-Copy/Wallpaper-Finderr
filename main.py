from Assets import constants as consts 
from Assets import webScraper as ws 

if __name__ == "__main__":
    wsObj = ws.WebScraper()
    wsObj.downloadWebpage()