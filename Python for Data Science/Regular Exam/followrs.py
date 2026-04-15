followers = {}

while True:
    user_input = input()

    if user_input == "Log out":
        break

    parts = user_input.split(": ")

    if parts[0] == "New follower":
        username = parts[1]
        if username not in followers:
            followers[username] = {"likes": 0, "comments": 0}

    if parts[0] == "Like":
        username = parts[1]
        likes = int(parts[2])
        if username not in followers:
            followers[username] = {"likes": 0, "comments": 0}
            followers[username]["likes"] += likes
        elif username in followers:
            followers[username]["likes"] += likes

    if parts[0] == "Comment":
        username = parts[1]
        if username not in followers:
            followers[username] = {"likes": 0, "comments": 0}
            followers[username]["comments"] += 1
        elif username in followers:
            followers[username]["comments"] += 1

    if parts[0] == "Blocked":
        username = parts[1]
        if username not in followers:
            print(f"{username} doesn't exist.")
        if username in followers:
            del followers[username]

print(f"{len(followers)} followers")
for username in followers:
    total = followers[username]["likes"] + followers[username]["comments"]
    print(f"{username}: {total}")