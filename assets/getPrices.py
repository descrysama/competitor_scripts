from urllib.parse import urlparse
from fetch_data import fetch_items
from assets.webinit_ import initBrowser

## Classes des sites
from classes.planetemobile import PlaneteMobile
from classes.tout_pour_phone import toutPourPhone
from classes.brico_phone import BricoPhone
from classes.yodoit import Yodoit
from classes.gsm55 import Gsm55
from classes.macway import macWay
from classes.sosav import Sosav
from classes.lapommediscount import laPommeDiscount
from classes.all4iphone import All4iphone
from classes.best_price_market import Best_price_market
from classes.compo_phone import Compo_phone
from classes.cpix import Cpix
from classes.ebay import Ebay
from classes.ecrans_telephone import Ecrans_telephone
from classes.empetel import Empetel
from classes.global_stock import Global_stock
from classes.hightechplace import Hightechplace
from classes.ibuy import Ibuy
from classes.icasse import iCasse
from classes.kabiloo import Kabiloo
from classes.lcdstore import Lcdstore
from classes.mobile24 import Mobile24
from classes.phonexpert78 import Phonexpert78
from classes.piecetelephone import Piecetelephone
from classes.world_itech import World_itech
from classes.zanphone import Zanphone
from classes.ifixit import Ifixit

binding_array = {
    'www.tout-pour-phone.com': 'tout_pour_phone',
    'store.ifixit.fr': 'ifixit',
    'www.gsm55.com': 'gsm55',
    'www.brico-phone.com': 'brico_phone',
    'www.yodoit.com': 'yodoit',
    'www.macway.com': 'macway',
    'www.sosav.fr': 'sosav',
    'www.lapommediscount.com': 'lapommediscount',
    'www.all4iphone.fr': 'all4iphone',
    'www.best-price-market.com' : 'best_price_market',
    'www.compo-phone.com': 'compo_phone',
    'cpix.fr': 'cpix',
    'www.ebay.fr': 'ebay',
    'ecrans-telephone.com' : 'ecrans_telephone',
    'www.empetel.net' : 'empetel',
    'global-stock.fr' : 'global_stock',
    'www.hightechplace.com' : 'hightechplace',
    'ibuy.fr': 'ibuy',
    'empetel.net': 'empetel',
    'icasse.fr': 'icasse',
    'www.kabiloo.fr': 'kabiloo',
    'lcdstore.fr': 'lcdstore',
    'www.mobile24.fr': 'mobile24',
    'www.phonexpert78.com' : 'phonexpert78',
    'www.piecetelephone.fr' : 'piecetelephone',
    'www.planetemobile.fr': 'planetemobile',
    'www.world-itech.com': 'world_itech',
    'zanphone.com' : 'zanphone'
}

tout_pour_phone = toutPourPhone()
ifixit = Ifixit()
gsm55 = Gsm55()
brico_phone = BricoPhone()
yodoit = Yodoit()
macway = macWay()
sosav = Sosav()
lapommediscount = laPommeDiscount()
all4iphone = All4iphone()
best_price_market = Best_price_market()
compo_phone = Compo_phone()
cpix = Cpix()
ebay = Ebay()
ecrans_telephone = Ecrans_telephone()
empetel = Empetel()
global_stock = Global_stock()
hightechplace = Hightechplace()
ibuy = Ibuy()
icasse = iCasse()
kabiloo = Kabiloo()
lcdstore = Lcdstore()
mobile24 = Mobile24()
phonexpert78 = Phonexpert78()
piecetelephone = Piecetelephone()
world_itech = World_itech()
zanphone = Zanphone()
planetemobile = PlaneteMobile()

def checkAllReferences() :
    ## Item fetch à partir de l'API (la meme que sur le site http://79.137.87.52:5000/sku/get)
    items = fetch_items()
    sku_array = {}
    try:
        for index, item in enumerate(items[::-1]) :
            if index < 2:
                print(index + 1, ' / ', len(items))
                for index_link, link in enumerate(item['urls']): 
                    print('Link', index + 1, ':', index_link ,'/ ', len(item['urls']))
                    domain = urlparse(link['url']).netloc
                    if domain in binding_array :
                        result = globals()[binding_array[domain]].getData(link['url'], item['name'])
                        if result :
                            if str(result[0]).strip() in str(sku_array).strip() :
                                oldvalue = sku_array[str(result[0]).strip()]
                                if oldvalue > result[1] : 
                                    sku_array[str(result[0]).strip()] = result[1]
                            else :
                                sku_array[str(result[0]).strip()] = result[1]
                    else :
                        print("Ce domaine n'est pas dans la liste : ", domain)
    except Exception as e:
        print('The run has been canceled or crashed :', e)
        
    return sku_array
