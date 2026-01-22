numbers = list(map(int, input().split()))
removed = int(input())


for i in range(removed):
    numbers.remove(min(numbers))

numbers = (map(str, numbers))

print(", ".join(numbers))


