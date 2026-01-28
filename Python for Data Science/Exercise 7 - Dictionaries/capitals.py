country = input().split(", ")
capital = input().split(", ")

result = zip(country, capital)

for key, value in result:
    print(f"{key} -> {value}")