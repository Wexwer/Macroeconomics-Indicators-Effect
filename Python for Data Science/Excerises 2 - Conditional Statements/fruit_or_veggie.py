product = input()

fruits = ["banana","apple","kiwi", "cherry", "lemon"]
vegetables = ["cucumber", "pepper", "carrot"]

if product in fruits:
    print("fruit")
elif product in vegetables:
    print("vegetable")
else:
    print("unknown")