from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser

class World_itech():
    def __init__(self):
        self.outputObject = []

    def getData(self, url, name):
        try:
            driver = initBrowser(True)
            driver.get(url)
            price_element = driver.find_element(By.ID, 'our_price_display')
            price = price_element.get_attribute("content")
            driver.quit()
            return [name, float(price)]
        except Exception as e:
            return print('Erreur :', e)
