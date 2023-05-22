from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from assets.webinit_ import initBrowser

class PlaneteMobile():
    def __init__(self, driver):
        self.outputObject = []
        self.driver = driver

    def getData(self, url, name):
        try:
            self.driver.get(url)
            price_element = self.driver.find_element(By.XPATH, '//div[@class="detail_produit__price"]/span[@class="detail_produit__price__final"]')
            price = price_element.text.replace('€', '').replace(',', '.').replace('\xa0', '')  # \xa0 is a non-breaking space
            return [name, float(price)]
        except Exception as e:
            return print('Erreur :', e)