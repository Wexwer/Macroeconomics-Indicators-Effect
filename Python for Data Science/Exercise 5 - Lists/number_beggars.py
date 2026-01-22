items = input().split(", ")
items = [int(x) for x in items]
beggars = int(input())




beggars_list = [0] * beggars

for index in range(len(items)):
    current_number = items[index]
    beggar_index = index % beggars
    beggars_list[beggar_index] += current_number

print(beggars_list)