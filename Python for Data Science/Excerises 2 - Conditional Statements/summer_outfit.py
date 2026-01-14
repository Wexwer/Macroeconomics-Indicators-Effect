temperature = int(input())
time_of_day = input()

clothing = ""
shoes = ""

if time_of_day == "Morning":
    if 10 <= temperature <= 18:
        clothing = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < temperature <= 24:
        clothing = "Shirt"
        shoes = "Moccasins"
    else:
        clothing = "T-Shirt"
        shoes = "Sandals"

if time_of_day == "Afternoon":
    if 10 <= temperature <= 18:
        clothing = "Shirt"
        shoes = "Moccasins"
    elif 18 < temperature <= 24:
        clothing = "T-Shirt"
        shoes = "Sandals"
    else:
        clothing = "Swim Suit"
        shoes = "Barefoot"

if time_of_day == "Evening":
    if 10 <= temperature <= 18:
        clothing = "Shirt"
        shoes = "Moccasins"
    elif 18 < temperature <= 24:
        clothing = "Shirt"
        shoes = "Moccasins"
    else:
        clothing = "Shirt"
        shoes = "Moccasins"

print(f"It's {temperature} degrees, get your {clothing} and {shoes}.")