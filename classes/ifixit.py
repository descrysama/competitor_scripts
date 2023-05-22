from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser

class Ifixit():
    def __init__(self, driver):
        self.outputObject = []
        self.driver = driver

    def getData(self, url, name):
        try:
            self.driver.get(url)
            price_element = self.driver.find_element(By.XPATH, '//div[@class="product__price"]//span[@data-product-price]')
            price_text = price_element.get_attribute("innerHTML")
            price = float(price_text.replace(",", ".").replace("€", "").strip())
            return [name, price]
        except Exception as e:
            return print('Erreur :', e)
