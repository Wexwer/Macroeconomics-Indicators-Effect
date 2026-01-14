season = input()
accommodation = input()
days= int(input())

# # * Season accommodation prices
# seasons = {
#     "Spring": {"Hotel":30, "Camping": 10},
#     "Summer": {"Hotel":50, "Camping": 30},
#     "Autumn": {"Hotel":20, "Camping": 15},
#     "Winter": {"Hotel":40, "Camping": 10}
# }
#
# # * Season discounts
# discount = {
#     "Spring": 0.20,
#     "Summer": 0.00,
#     "Autumn": 0.30,
#     "Winter": 0.10
# }
#
# price_per_day = seasons[season][accommodation]
# disc = discount[season]
# total = (price_per_day* (1 - disc)) * days
# print(f"{total:.2f}")

price_per_day = 0
discount = 0

if season == "Spring":
    discount = 0.20
    if accommodation == "Camping":
        price_per_day = 10
    elif accommodation == "Hotel":
        price_per_day = 30
elif season == "Summer":
    discount = 0.00
    if accommodation == "Camping":
        price_per_day = 30
    elif accommodation == "Hotel":
        price_per_day = 50
elif season == "Winter":
    discount = 0.10
    if accommodation == "Camping":
        price_per_day = 10
    elif accommodation == "Hotel":
        price_per_day = 40
elif season == "Autumn":
    discount = 0.30
    if accommodation == "Camping":
        price_per_day = 15
    elif accommodation == "Hotel":
        price_per_day = 20

price_before_discount = price_per_day * days
price_after_discount = price_before_discount - (price_before_discount * discount)
print(f"{price_after_discount:.2f}")
