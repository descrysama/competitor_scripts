from selenium import webdriver
from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser

class Phonehappy():
    def __init__(self):
        self.outputObject = []

    def getData(self, url, name):
        try:
            driver = initBrowser(True)
            driver.get(url)
            price_main = driver.find_element(By.XPATH, '//span[@id="ajaxPriceTTC"]/span[not(@class)]').text
            price_cents = driver.find_element(By.XPATH, '//span[@id="ajaxPriceTTC"]/span[@class="cents"]').text
            price = f"{price_main}{price_cents}"  # Concatenation of the main price and cents
            driver.quit()
            return [name, float(price)]
        except Exception as e:
            return print('Erreur :', e)
