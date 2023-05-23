
def checkPriceMargin(lowest_price, final_output):
    final_checked_prices = []
    for key in lowest_price :
        print(str(key).strip())
        if str(key).strip() in final_output:
            price_ttc = float(final_output[key].replace(',', '.')) * 1.2
            lowest_competitor_price = float(lowest_price[str(key).strip()])
            potential_new_price = lowest_competitor_price - 1
            if potential_new_price >= (price_ttc * 1.16) :
                final_checked_prices.append([str(key).strip(), potential_new_price])
            else:
                final_checked_prices.append([str(key).strip(), price_ttc * 1.15])
    return final_checked_prices