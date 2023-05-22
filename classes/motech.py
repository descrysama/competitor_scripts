from selenium.webdriver.common.by import By
import html
from assets.webinit_ import initBrowser

class Motech():
    def __init__(self):
        self.outputObject = []

    def getData(self, url, name):
        try:
            driver = initBrowser(True)
            driver.get(url)
            price_element = driver.find_element(By.XPATH, '//span[@itemprop="price"]')
            price_text = price_element.get_attribute("innerHTML")
            price_text = html.unescape(price_text)  # Supprimer l'entité HTML
            price = float(price_text.replace(",", ".").replace("€", "").strip())
            driver.quit()
            return [name, price]
        except Exception as e:
            return print('Erreur :', e)