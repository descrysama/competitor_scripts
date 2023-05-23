from bs4 import BeautifulSoup
from assets.webinit_ import initBrowser

class Lcdstore():
    def __init__(self):
        self.outputObject = []
        self.driver = initBrowser(True)

    def getData(self, url, name):
        try:
            self.driver.get(url)
            html = self.driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            
            # Extraction du prix avec le premier schéma
            price_element_1 = soup.find('div', class_='product__price')
            if price_element_1:
                price_element_1 = price_element_1.find('span', recursive=False)
                if price_element_1:
                    price_text_1 = price_element_1.get_text(strip=True)
                    price_1 = float(price_text_1.replace(",", ".").replace("€", ""))
                    return [name, price_1]
            
            # Extraction du prix avec le deuxième schéma
            price_element_2 = soup.find('p', class_='price')
            if price_element_2:
                del_element = price_element_2.find('del')
                if del_element:
                    price_text_2 = del_element.find('bdi').get_text(strip=True)
                else:
                    price_text_2 = price_element_2.find('span', class_='woocommerce-Price-amount').get_text(strip=True)
                price_2 = float(price_text_2.replace(",", ".").replace("€", ""))
                return [name, price_2]
                
        except Exception as e:
            return print('Erreur :', e)
        
        # Si aucun schéma ne renvoie de prix, renvoyer None
        return None