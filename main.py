from assets.webinit_ import initBrowser
from assets.getPrices import checkAllReferences
from assets.fetchFinalOutput import fetchFinalOutput
from assets.checkPriceMargin import checkPriceMargin
from assets.edit_final_output import editFinalOutput
## Driver initial (le navigateur tu t'en sers sur toute les classes qui vont arrivés ensuite )


lowest_price = checkAllReferences() ## format : {"PP0290" : '6,56',  'IP13-ECSOFT', '108,50'} 
final_output = fetchFinalOutput() ## format : {"PP0290" : '6,56',  'IP13-ECSOFT', '108,50'} les deux ont le même format oui

final_checked_prices = checkPriceMargin(lowest_price, final_output)
editFinalOutput(final_checked_prices)

