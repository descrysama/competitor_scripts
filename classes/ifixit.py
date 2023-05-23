import requests
from bs4 import BeautifulSoup

class Ifixit():
    def __init__(self):
        self.outputObject = []

    def getData(self, url, name):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            price_element = soup.select_one('div.product__price span[data-product-price]')
            price_text = price_element.text
            price = float(price_text.replace(",", ".").replace("€", "").strip())
            return [str(name).strip(), float(price)]
        except Exception as e:
            return print('Erreur :', e)
