from math import ceil, floor
# CONSTANTS
PRICE_PAINT = 21.50
PRICE_WALLPAPER = 5.20

# USER INPUT
count_cans_paint = int(input())
count_wallpaper_rolls = int(input())
pirce_for_one_pair_gloves = float(input())
price_for_one_brush = float(input())
required_gloves = ceil((count_wallpaper_rolls * 0.35))
required_brushes = floor(count_cans_paint * 0.48)

# LOGIC
total_price = ((count_cans_paint * PRICE_PAINT) + (count_wallpaper_rolls * PRICE_WALLPAPER) +
               (pirce_for_one_pair_gloves * required_gloves) + (price_for_one_brush * required_brushes))

delivery_price = total_price * (1/15)
print(f"This delivery will cost {delivery_price:.2f} lv.")
