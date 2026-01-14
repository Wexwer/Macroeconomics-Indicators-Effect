def dis(price, discount):
    discount1 = discount / 100
    discount_price = price - (price * discount1)
    print(round(discount_price,2))
    return discount_price

dis(1693,80)