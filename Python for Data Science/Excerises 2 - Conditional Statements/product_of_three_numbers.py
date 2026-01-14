num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 == 0 or num2 == 0 or num3 == 0:
    print("zero")
else:
    negative_count = 0
    if num1 < 0:
        negative_count += 1
    if num2 < 0:
        negative_count += 1
    if num3 < 0:
        negative_count += 1
    if negative_count % 2 == 0:
        print("positive")
    else:
        print("negative")