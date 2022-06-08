import os 
import Assets.constants as c

class WebScraper:

    def __init__(self):
        self.moduleCheck()
        self.getSearchTerm(c.COLORS, c.TAGS)

    def moduleCheck(self):
        try: 
            import bs4
        except ModuleNotFoundError:
            os.system("pip install bs4")

        try:
            import requests
        except ModuleNotFoundError:
            os.system("pip install bs4")

    def getSearchTerm(self, colors, tags):
        #making search term for entering into url
        self.sTerm = ""
        terms = tags + colors 
        
        for term in terms:
            if len(term.split()) > 1:
                for word in term.split():
                    self.sTerm+=word + "+"
            else:
                self.sTerm+=term + "+"
            
        self.sTerm+="wallpaper"
        # print(self.sTerm)
    
    def downloadWebpage(self):
        import requests
        self.url = f"https://www.google.com/search?q={self.sTerm}&tbm=isch&sxsrf=ALiCzsZjMo54L-3oeSu3vp0lZe-EVsJdzw%3A1654679608916&source=hp&biw=1536&bih=750&ei=OGigYqf-NZHFhwOAk5TAAw&iflsig=AJiK0e8AAAAAYqB2SLOSG3BX0gtVDeVFKlFGKWQNbbw0&ved=0ahUKEwin-rfywZ34AhWR4mEKHYAJBTgQ4dUDCAc&uact=5&oq=dark+souls&gs_lcp=CgNpbWcQAzIECCMQJzIECCMQJzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgsIABCABBCxAxCDAToICAAQgAQQsQM6CAgAELEDEIMBUABYpgtg8QtoAHAAeACAAfgBiAHFB5IBBTguMC4xmAEAoAEBqgELZ3dzLXdpei1pbWc&sclient=img"
        r = requests.get(self.url, allow_redirects = True)
        open("raw.html","wb").write(r.content)
