import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser

class Cpix():
    def __init__(self):
        self.outputObject = []

    def getData(self, url, name):
        try:
            driver = initBrowser(True)
            driver.get(url)
            price_html = driver.page_source
            soup = BeautifulSoup(price_html, "html.parser")
            
            # getting the price detail div
            price_detail_div = soup.find('div', {'class': 'prix_detail'})
            # getting the text after 'Prix Dégressifs :'
            price_degressifs_text = price_detail_div.get_text(strip=True)
            # find the first price in this text
            match = re.search(r'\d+,\d+', price_degressifs_text)
            price = float(match.group().replace(",", "."))
            driver.quit()
            return [name, price]
        except Exception as e:
            return print('Erreur :', e)
        