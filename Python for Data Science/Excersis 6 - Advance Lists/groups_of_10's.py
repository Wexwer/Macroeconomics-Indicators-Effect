user_list = list(map(int, input().split(", ")))

max_num = max(user_list)

for i in range(10, max_num +10, 10):
    current = [n for n in user_list if i >= n > i -10]
    print(f"Group of {i}\'s: {current}")