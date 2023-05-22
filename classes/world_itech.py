from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser

class World_itech():
    def __init__(self, driver):
        self.outputObject = []
        self.driver = driver

    def getData(self, url, name):
        try:
            self.driver.get(url)
            price_element = self.driver.find_element(By.ID, 'our_price_display')
            price = price_element.get_attribute("content")
            return [name, float(price)]
        except Exception as e:
            return print('Erreur :', e)
