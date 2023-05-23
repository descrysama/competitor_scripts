import requests
from bs4 import BeautifulSoup

class Ecrans_telephone():
    def __init__(self):
        self.outputObject = []

    def getData(self, url, name):
        try:
            response = requests.get(url)
            html_content = response.content
            soup = BeautifulSoup(html_content, "html.parser")
            price_element = soup.select_one('span[id="pretaxe_price_display"]')
            price = float(price_element.get("content").strip()) * 1.2
            return [str(name).strip(), float(price)]
        except Exception as e:
            return print('Erreur :', e)
