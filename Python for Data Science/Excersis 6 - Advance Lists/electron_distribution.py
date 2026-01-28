
num = int(input())

result = []
shell = 1

while num > 0:
    capacity = 2 * shell ** 2

    if num >= capacity:
        result.append(capacity)
        num -= capacity
    else:
        result.append(num)
        num = 0

    shell += 1

print(result)