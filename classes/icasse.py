from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser

class iCasse:
    def __init__(self, driver):
        self.outputObject = []
        self.driver = driver

    def getData(self, url, name):
        try:
            self.driver.get(url)
            price = self.driver.find_element(By.XPATH, '//span[@id="our_price_display"]').text.replace('€', '').strip()
            price = price.replace('.', '') # new line of code
            return [name, float(price)]
        except Exception as e:
            return print('Erreur :', e)
