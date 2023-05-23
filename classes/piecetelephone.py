import requests
from bs4 import BeautifulSoup

class Piecetelephone():
    def __init__(self):
        self.outputObject = []

    def getData(self, url, name):
        try:
            response = requests.get(url)
            html_content = response.content
            soup = BeautifulSoup(html_content, "html.parser")
            price_element = soup.find('div', class_='product-price').find('div', class_='current-price').find('span', itemprop='price')
            price = price_element.get_text().replace('€', '').replace(',', '.').strip()
            return [str(name).strip(), float(price)]
        except Exception as e:
            return print('Erreur :', e)