import requests
from bs4 import BeautifulSoup

class toutPourPhone():
    def __init__(self):
      self.outputObject = []
    
    def getData(self, url, name):
       
       try: 
            response = requests.get(url)
            html_content = response.content
            soup = BeautifulSoup(html_content, "html.parser")
            price_element = soup.select_one('span[id="our_price_display"]')
            price = price_element.get_text().replace('€', '').replace(',', '.').strip()
            return [str(name).strip(), float(price)]
       except:
          return
       