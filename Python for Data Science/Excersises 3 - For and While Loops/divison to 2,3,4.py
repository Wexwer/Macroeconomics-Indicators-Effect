n = int(input())

count2 = 0
count3 = 0
count4 = 0

for _ in range(n):
    num = int(input())

    if num % 2 == 0:
        count2 += 1
    if num % 3 == 0:
        count3 += 1
    if num % 4 == 0:
        count4 += 1

p2 = count2 / n * 100
p3 = count3 / n * 100
p4 = count4 / n * 100

print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
