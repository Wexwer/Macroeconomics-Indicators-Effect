
all_goods_sold = 0
stock = {}
while True:
    input_text = input().split()
    command = input_text[0]

    if command == "Complete":
        break

    if command == "Receive":
        quantity = int(input_text[1])
        food = input_text[2]

        if food not in stock:
            stock[food] = quantity
        else:
            stock[food] += quantity

    if command == "Sell":
        quantity = int(input_text[1])
        food = input_text[2]

        if food not in stock:
            print(f"You do not have any {food}.")
        else:
            if stock[food] < quantity:
                sold = stock[food]
                all_goods_sold += sold
                print(f"There aren't enough {food}. You sold the last {sold} of them.")
                del stock[food]
            else:
                all_goods_sold += quantity
                stock[food] -= quantity
                print(f"You sold {quantity} {food}.")

                if stock[food] <= 0:
                    del stock[food]



for key, value in stock.items():
    print(f"{key}: {value}")
print(f"All sold: {all_goods_sold} goods")