from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser

class Piecetelephone():
    def __init__(self):
        self.outputObject = []

    def getData(self, url, name, driver):
        try:
            driver.get(url)
            price_element = driver.find_element(By.XPATH, '//div[@class="product-price h5 "]/div[@class="current-price"]/span[@itemprop="price"]')
            price = price_element.get_attribute("content")
            return [name, float(price)]
        except Exception as e:
            return print('Erreur :', e)