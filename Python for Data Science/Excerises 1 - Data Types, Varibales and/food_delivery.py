# * CONSTANTS
CHICKEN_MENU = 10.35
FISh_MENU = 12.40
VEGGIE_MENU = 8.15
DESERT = 0.20 # * 20% from the total bill excluding delivery
DELIVERY_PRICE = 2.5

# * INPUT DATA
number_of_chicken_menu = int(input())
number_of_fish_menu = int(input())
number_of_veggie_menu = int(input())

# * LOGIC
total_price_menus = ((number_of_chicken_menu * CHICKEN_MENU) + (number_of_fish_menu * FISh_MENU) +
                     (number_of_veggie_menu * VEGGIE_MENU))
desert_price = total_price_menus * DESERT

final_order_value = total_price_menus + desert_price + DELIVERY_PRICE

print(f"{final_order_value}")