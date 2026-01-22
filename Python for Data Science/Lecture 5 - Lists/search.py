count = int(input())

filter_word = input()

first_list = []

for i in range(count):
    word = input()
    first_list.append(word)
print(first_list)


filter_list = []

for e in first_list:
    if filter_word in e:
        filter_list.append(e)

print(filter_list)