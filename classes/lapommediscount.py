from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser

class laPommeDiscount():
    def __init__(self):
        self.outputObject = []

    def getData(self, url, name, driver):
        try:
            driver.get(url)
            price_element = driver.find_element(By.XPATH, '//span[@id="ajaxPriceTTC"]')
            price = price_element.text.replace('€', '').replace(',', '.')
            return [name, float(price)]
        except Exception as e:
            return print('Erreur :', e)