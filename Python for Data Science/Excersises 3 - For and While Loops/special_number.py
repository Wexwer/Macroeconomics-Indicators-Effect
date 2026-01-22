num = int(input())
temp = num
is_special = True

while True:
    digit = temp % 10
    if num % digit != 0:
        is_special = False
        break

    temp //= 10
    if  temp == 0:
        break
if is_special:
    print(f"{num} is special")
else:
    print(f"{num} is not special")