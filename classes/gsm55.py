from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from assets.webinit_ import initBrowser

class Gsm55():
    def __init__(self) :
      self.outputObject = []
      self.driver = initBrowser(True)
    
    def getData(self, url, name):
      try:
         self.driver.get(url)
         self.loopOnWait(self.driver)
         price = self.driver.find_element(By.XPATH, '//span[starts-with(@class, "productPrice-module__price")]').text.replace('€', '').replace(',', '.').strip()
         return [name, float(price)]
      except:
         return


    def loopOnWait(self, driver):
        try: 
           WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//span[starts-with(@class, "productPrice-module__price")]')))
        except:
           self.loopOnWait(driver)