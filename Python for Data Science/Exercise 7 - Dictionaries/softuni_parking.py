number_of_commands = int(input())
registered = {}
for i in range(number_of_commands):
    parts = input().split()
    command = parts[0]

    if command == "register":
        username = parts[1]
        platform = parts[2]

        if username not in registered:
            registered[username] = platform
            print(f"{username} registered {platform} successfully")
        else:
            print(f"ERROR: already registered with plate number {registered[username]}")
    elif command == "unregister":
        username = parts[1]
        if username in registered:
            del registered[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"{username} not registered")

for key, value in registered.items():
    print(f"{key} -> {value}")

