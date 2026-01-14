n = int(input())
biggest = int(input())

for _ in range(n - 1):
    num = int(input())
    if num > biggest:
        biggest = num

print(biggest)
