from selenium.webdriver.common.by import By
import html
from assets.webinit_ import initBrowser

class Hightechplace():
    def __init__(self):
        self.outputObject = []

    def getData(self, url, name, driver):
        try:
            driver.get(url)
            price_element = driver.find_element(By.XPATH, '//span[@class="price"]')
            price_text = price_element.get_attribute("innerHTML")
            price_text = html.unescape(price_text)  # Supprimer l'entité HTML
            price = float(price_text.replace(",", ".").replace("€", "").strip())
            return [name, price]
        except Exception as e:
            return print('Erreur :', e)