wagons = int(input())

train = [0 for x in range(wagons)]

while True:
    user_input = input()
    if user_input == "End":
        break
    command = user_input.split(" ")
    if command[0] == "add":
        count = int(command[1])
        last_index = len(train) -1
        train[last_index] += count
    elif command[0] == "insert":
        idx = int(command[1])
        count = int(command[2])
        train[idx] += count
    elif command[0] == "leave":
        idx = int(command[1])
        count = int(command[2])
        train[idx] -= count

print(train)