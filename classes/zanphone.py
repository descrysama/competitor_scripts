import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from assets.webinit_ import initBrowser

class Zanphone():
    def __init__(self):
        self.outputObject = []

    def getData(self, url, name, driver):
        try:
            driver.get(url)
            # Extraire le contenu du script JSON
            json_script = driver.find_element(By.XPATH, '//script[@type="application/ld+json" and @class="rank-math-schema"]').get_attribute('innerHTML')
            # Parser le contenu JSON
            data = json.loads(json_script)
            # Extraire le prix
            for graph_element in data["@graph"]:
                if graph_element["@type"] == "Product":
                    price = graph_element["offers"]["price"]
                    return [name, float(price)]
        except Exception as e:
            return print('Erreur :', e)
