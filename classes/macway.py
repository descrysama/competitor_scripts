from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser

class macWay():
    def __init__(self, driver):
        self.outputObject = []
        self.driver = driver

    def getData(self, url, name):
        try:
            self.driver.get(url)
            price = self.driver.find_element(By.XPATH, '//span[@class="price"]').text.replace('€', '.')
            return [name, float(price)]
        except Exception as e:
            return print('Erreur :', e)