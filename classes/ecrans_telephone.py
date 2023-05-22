from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser

class Ecrans_telephone():
    def __init__(self):
        self.outputObject = []

    def getData(self, url, name, driver):
        try:
            driver.get(url)
            price_element = driver.find_element(By.XPATH, '//div[@class="our_price_display"]/span[@id="pretaxe_price"]/span[@itemprop="price"]')
            price = float(price_element.get_attribute("content"))
            increased_price = price * 1.20
            return [name, increased_price]
        except Exception as e:
            return print('Erreur :', e)
