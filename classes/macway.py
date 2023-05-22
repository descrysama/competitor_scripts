from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser

class macWay():
    def __init__(self):
        self.outputObject = []

    def getData(self, url, name):
        try:
            driver = initBrowser(True)
            driver.get(url)
            price = driver.find_element(By.XPATH, '//span[@class="price"]').text.replace('€', '.')
            driver.quit()
            return [name, float(price)]
        except Exception as e:
            return print('Erreur :', e)