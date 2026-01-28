phonebook_data = {}

while True:
    line = input()

    if line.isdigit():
        number = int(line)
        break

    name, number = line.split("-")
    phonebook_data[name] = number

for i in range(number):
    search_name = input()
    if search_name in phonebook_data:
        print(f"{search_name} -> {phonebook_data[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")