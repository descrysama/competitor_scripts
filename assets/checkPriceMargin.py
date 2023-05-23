def checkPriceMargin(lowest_price, final_output):
    final_checked_prices = final_output.copy()

    for index, item in enumerate(final_output):
        for low_price in lowest_price:
            if item[0] == low_price[0]:
                price_ttc = float(item[1].replace(',', '.')) * 1.2
                lowest_competitor_price = float(low_price[1])
                potential_new_price = lowest_competitor_price - 1

                if potential_new_price >= (price_ttc * 1.16):
                    print(low_price[0])
                    final_checked_prices[index].append(str(potential_new_price))
                else:
                    final_checked_prices[index].append(str(price_ttc * 1.15))

    return final_checked_prices