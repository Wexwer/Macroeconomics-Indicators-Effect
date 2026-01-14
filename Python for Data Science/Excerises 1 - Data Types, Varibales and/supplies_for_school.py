PACKEGE_OF_PENS = 5.8
PACKEGE_OF_MARKETS = 7.20
BOARD_CLEANER_PER_LITER  = 1.20


number_of_pens = int(input())
number_of_markets = int(input())
liters_board_cleaner = int(input())
discount_percentange = int(input()) / 100


total = ((number_of_pens * PACKEGE_OF_PENS) + (number_of_markets * PACKEGE_OF_MARKETS) +
         (liters_board_cleaner * BOARD_CLEANER_PER_LITER))

total_after_discount = total - (total * discount_percentange)

print(f"{total_after_discount}")



