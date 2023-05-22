from selenium import webdriver
from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser

class Pieces2mobile():
    def __init__(self, driver):
        self.outputObject = []
        self.driver = driver

    def getData(self, url, name):
        try:
            driver = initBrowser(True)
            driver.get(url)
            price_element = driver.find_element(By.XPATH, '//span[@class="price"]')
            price = price_element.text.replace('€', '').replace(',', '.')
            driver.quit()
            return [name, float(price)]
        except Exception as e:
            return print('Erreur :', e)