from assets.webinit_ import initBrowser
from assets.getPrices import checkAllReferences
from assets.fetchFinalOutput import fetchFinalOutput
from assets.checkPriceMargin import checkPriceMargin
from assets.edit_final_output import editFinalOutput

lowest_price = checkAllReferences() 
final_output = fetchFinalOutput() 

final_checked_prices = checkPriceMargin(lowest_price, final_output)
editFinalOutput(final_checked_prices)