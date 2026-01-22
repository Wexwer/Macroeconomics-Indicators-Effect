numbers = int(input())

list = []

for i in range(numbers):
    number = int(input())
    list.append(number)

command = input()

result = []

for e in list:
    if command == "positive":
        if e >= 0:
            result.append(e)
    if command == "negative":
        if e < 0:
            result.append(e)
    if command == "even":
        if e % 2 == 0:
            result.append(e)
    if command == "odd":
        if e % 2 != 0:
            result.append(e)

print(result)