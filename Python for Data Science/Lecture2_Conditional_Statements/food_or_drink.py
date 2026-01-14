food = ["curry", "noodles", "sushi", "spaghetti", "bread"]
drink = ["tea", "water", "coffee", "juice"]

entry = input()

if entry in food:
    print(f"food")
elif entry in drink:
    print(f"drink")
else:
    print(f"unknown")