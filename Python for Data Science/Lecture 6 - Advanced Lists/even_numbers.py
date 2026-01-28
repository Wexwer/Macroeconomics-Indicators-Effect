# * User input
numbers = list(map(int, input().split(", ")))

# * Logic
fount = list(map(lambda x: x if numbers[x] % 2 == 0 else '', range(len(numbers))))

filtered = list(filter(lambda x: x != '', fount))

print(filtered)