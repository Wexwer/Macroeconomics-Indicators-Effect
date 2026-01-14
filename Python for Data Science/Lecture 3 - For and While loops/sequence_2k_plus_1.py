end_number = int(input())
numbers = 1

while True:
    print(numbers)
    numbers = (numbers * 2) + 1
    if numbers > end_number:
        break