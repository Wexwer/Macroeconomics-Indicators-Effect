PRICE_PER_SQ_METER = 7.61

DISCOUNT = 0.18

squre_meters_to_landscaped = float(input())

final_price = (PRICE_PER_SQ_METER * squre_meters_to_landscaped) * 0.18
final_discount = (PRICE_PER_SQ_METER * squre_meters_to_landscaped) - final_price

print(f"The final price is: {final_discount} lv.")
print(f"The discount is: {final_price} lv.")


