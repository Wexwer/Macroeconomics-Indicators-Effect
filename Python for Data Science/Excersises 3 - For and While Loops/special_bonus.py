break_number = int(input())
output_number = 1

while True:
    numbers = int(input())
    if numbers == break_number:
        break
    else:
        output_number = numbers + ( numbers * 0.20)

print(f"{output_number:.0f}")
