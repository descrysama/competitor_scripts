from selenium import webdriver
from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser

class Kabiloo():
    def __init__(self):
        self.outputObject = []

    def getData(self, url, name):
        try:
            driver = initBrowser(True)
            driver.get(url)
            price_element = driver.find_element(By.XPATH, '//div[@class="price"]/span[@itemprop="price"]')
            price = price_element.text.replace('€', '').replace(',', '.')
            driver.quit()
            return [name, float(price)]
        except Exception as e:
            return print('Erreur :', e)