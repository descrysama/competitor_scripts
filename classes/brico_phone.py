from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser
class BricoPhone():
    def __init__(self):
        self.outputObject = []

    
    def getData(self, url, name, driver):
        try:
          driver.get(url)
          price = driver.find_element(By.XPATH, '//span[@class="price_total"]').text.replace('€', '').replace(',', '.').strip()
          return [name, float(price)]
        except:
          return
        