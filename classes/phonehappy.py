from selenium import webdriver
from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser

class Phonehappy():
    def __init__(self, driver):
        self.outputObject = []
        self.driver = driver

    def getData(self, url, name):
        try:
            self.driver.get(url)
            price_main = self.driver.find_element(By.XPATH, '//span[@id="ajaxPriceTTC"]/span[not(@class)]').text
            price_cents = self.driver.find_element(By.XPATH, '//span[@id="ajaxPriceTTC"]/span[@class="cents"]').text
            price = f"{price_main}{price_cents}"  # Concatenation of the main price and cents
            return [name, float(price)]
        except Exception as e:
            return print('Erreur :', e)
