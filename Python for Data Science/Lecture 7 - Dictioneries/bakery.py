user_input = input().split(" ")

result = {}

while len(user_input) != 0:
    key = user_input.pop(0)
    value = user_input.pop(0)
    result[key] = int(value)

print(result)