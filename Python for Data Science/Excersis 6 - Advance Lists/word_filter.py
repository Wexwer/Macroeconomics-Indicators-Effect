user_input = input().split()

result = [w for w in user_input if len(w) % 2 == 0]

for word in result:
    print(word)
