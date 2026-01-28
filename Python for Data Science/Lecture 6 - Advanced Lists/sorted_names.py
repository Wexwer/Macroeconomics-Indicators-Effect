names_input = input().split(", ")

list = sorted(names_input, key=lambda s: (-len(s), s))

print(list)