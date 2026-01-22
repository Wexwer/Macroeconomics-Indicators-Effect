product = input()
quantity = int(input())

def order(product_name: str, quantity_amount: int) -> float:
    price = 0
    if product_name == "coffee":
        price = 1.50
    elif product_name == "water":
        price = 1.00
    elif product_name == "coke":
        price = 1.40
    elif product_name == "snacks":
        price = 2.00
    return price * quantity_amount

print(f"{order(product, quantity):.2f}")