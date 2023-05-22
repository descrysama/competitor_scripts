from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser

class Yodoit():
    def __init__(self, driver):
        self.outputObject = []
        self.driver = driver

    def getData(self, url, name):
        try:
            self.driver.get(url)
            price_element = self.driver.find_element(By.XPATH, '//span[@class="ProductMeta__Price Price Text--subdued u-h4"]')
            price = price_element.text.replace('€', '').replace(',', '.')
            return [name, float(price)]
        except Exception as e:
            return print('Erreur :', e)