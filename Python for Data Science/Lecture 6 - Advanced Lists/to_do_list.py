to_do_list = ['' for i in range(10)]

while True:
    user_input = input()

    if user_input == "End":
        break

    importance,  task = user_input.split("-")
    importance = int(importance) - 1
    to_do_list.pop(importance)
    to_do_list.insert(importance, task)
    # * to_do_list[importance] = task # * is an option


result = [x for x in to_do_list if x != ""]
print(result)