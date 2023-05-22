from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser

class toutPourPhone():
    def __init__(self, driver):
      self.outputObject = []
      driver = driver
    
    def getData(self, url, name, driver):
       
       try: 
         driver.get(url)
         price = driver.find_element(By.XPATH, '//span[@id="our_price_display"]').text.replace('€', '').replace(',', '.').strip()
         return([name, float(price)])
       except:
          return
       