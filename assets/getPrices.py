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
from classes.mainhattan_mobile import Mainhattan_mobile
from classes.mobile24 import Mobile24
from classes.phonexpert78 import Phonexpert78
from classes.pieces2mobile import Pieces2mobile
from classes.piecetelephone import Piecetelephone
from classes.repar_smartphone import Repar_smartphone
from classes.world_itech import World_itech
from classes.zanphone import Zanphone
from assets.edit_final_output import editFinalOutput

binding_array = {
    'www.tout-pour-phone.com': 'tout_pour_phone',
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
    'www.global-stock.fr' : 'global_stock',
    'www.hightechplace.com' : 'hightechplace',
    'ibuy.fr': 'ibuy',
    'icasse.fr': 'icasse',
    'www.kabiloo.fr': 'kabiloo',
    'lcdstore.fr': 'lcdstore',
    'mainhattan-mobile.de': 'mainhattan_mobile',
    'www.mobile24.fr': 'mobile24',
    'www.phonexpert78.com' : 'phonexpert78',
    'www.pieces2mobile.com' : 'pieces2mobile',
    'www.piecetelephone.fr' : 'piecetelephone',
    'www.planetemobile.fr': 'planetemobile',
    'www.repar-smartphone.fr' : 'repar_smartphone',
    'www.world-itech.com': 'world_itech',
    'www.zanphone.com' : 'zanphone'
}

tout_pour_phone = toutPourPhone()
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
mainhattan_mobile = Mainhattan_mobile()
mobile24 = Mobile24()
phonexpert78 = Phonexpert78()
pieces2mobile = Pieces2mobile()
piecetelephone = Piecetelephone()
repar_smartphone = Repar_smartphone()
world_itech = World_itech()
zanphone = Zanphone()
planetemobile = PlaneteMobile()

def checkAllReferences() :
    driver = initBrowser(True)
    ## Item fetch à partir de l'API (la meme que sur le site http://79.137.87.52:5000/sku/get)
    items = fetch_items()
    count = 0

    sku_array = {}
    for index, item in enumerate(items) :
        print(index + 1, ' / ', len(items))
        for index_link, link in enumerate(item['urls']): 
            if(count >= 10) :
                driver.quit()
                driver = initBrowser(True)
                count = 0
            print('Link', index + 1, ':', index_link ,'/ ', len(item['urls']))
            domain = urlparse(link['url']).netloc
            if domain in binding_array :
                count += 1
                result = globals()[binding_array[domain]].getData(link['url'], item['name'], driver)
                if result :
                    if str(result[0]).strip() in str(sku_array).strip() :
                        oldvalue = sku_array[result[0]]
                        if oldvalue > result[1] : 
                            sku_array[result[0]] = result[1]
                    else :
                        sku_array[result[0]] = result[1]
            else :
                print("Ce domaine n'est pas dans la liste : ", domain)
        editFinalOutput(sku_array)
    return sku_array