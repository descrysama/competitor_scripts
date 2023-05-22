from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser

class Repar_smartphone():
    def __init__(self, driver):
        self.outputObject = []
        self.driver = driver

    def getData(self, url, name):
        try:
            self.driver.get(url)
            price_element = self.driver.find_element(By.XPATH, '//span[@class="woocommerce-Price-amount amount"]/bdi')
            price = price_element.text.replace('€', '').replace(',', '.').strip()
            return [name, float(price)]
        except Exception as e:
            return print('Erreur :', e)
