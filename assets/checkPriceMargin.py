
def checkPriceMargin(lowest_price, final_output):
    final_checked_prices = []
    for key in lowest_price :
        if key in final_output:
            price_ttc = float(final_output[key].replace(',', '.')) * 1.2
            lowest_competitor_price = float(lowest_price[key])
            potential_new_price = lowest_competitor_price - 1
            if potential_new_price >= (price_ttc * 1.16) :
                final_checked_prices.append([key, potential_new_price])
    return final_checked_prices