from selenium.webdriver.common.by import By
import html
from assets.webinit_ import initBrowser

class Mainhattan_mobile():
    def __init__(self, driver):
        self.outputObject = []
        self.driver = driver

    def getData(self, url, name):
        try:
            self.driver.get(url)
            price_element = self.driver.find_element(By.XPATH, '//div[@class="price h1 "]/span')
            price_text = price_element.get_attribute("innerHTML")
            price_text = html.unescape(price_text)  # Supprimer l'entité HTML
            price = float(price_text.replace(",", ".").replace("€", "").strip())
            return [name, price]
        except Exception as e:
            return print('Erreur :', e)
