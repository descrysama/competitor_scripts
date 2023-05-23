from bs4 import BeautifulSoup
import requests
import re

class Cpix():
    def __init__(self):
        self.outputObject = []

    def getData(self, url, name):
        try:
            response = requests.get(url)
            html_content = response.content
            soup = BeautifulSoup(html_content, "html.parser")
            price_detail_div = soup.find('div', {'class': 'prix_detail'})
            price_degressifs_text = price_detail_div.get_text(strip=True)
            match = re.search(r'\d+,\d+', price_degressifs_text)
            price = float(match.group().replace(",", ".")) * 1.2
            return [str(name).strip(), float(price)]
        except Exception as e:
            return print('Erreur :', e)
        