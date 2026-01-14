# * CONSTANTS
PROTECTIVE_NYLON = 1.5
PAINT = 14.50
PAINT_THINNER = 5

ADDITION_OF_PAINT = 0.10
ADDITION_OF_NYLON = 2
ADDITION_OF_BAGS = 0.40

ONE_HOUR_PRICE = 0.30 # * 30% from the sum is the labor pricing

# * INPUT DATA
required_nylon = int(input())
required_paint = int(input())
required_thinner = int(input())
hours_needed_for_crafting = int(input())

# * LOGIC
total_nylon = (required_nylon + ADDITION_OF_NYLON) * PROTECTIVE_NYLON
total_paint = (required_paint * PAINT) + ((required_paint * PAINT)*ADDITION_OF_PAINT)
total_paint_thinner = (required_thinner * PAINT_THINNER)

total_materials = total_paint + total_nylon +  total_paint_thinner + ADDITION_OF_BAGS
price_per_hour = (total_materials*ONE_HOUR_PRICE)
total_labor_cost = price_per_hour * hours_needed_for_crafting

total_pricing = total_materials + total_labor_cost

print(f"{total_pricing}")