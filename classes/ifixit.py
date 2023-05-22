from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser

class Ifixit():
    def __init__(self):
        self.outputObject = []

    def getData(self, url, name, driver):
        try:
            driver.get(url)
            price_element = driver.find_element(By.XPATH, '//div[@class="product__price"]//span[@data-product-price]')
            price_text = price_element.get_attribute("innerHTML")
            price = float(price_text.replace(",", ".").replace("€", "").strip())
            return [name, price]
        except Exception as e:
            return print('Erreur :', e)
