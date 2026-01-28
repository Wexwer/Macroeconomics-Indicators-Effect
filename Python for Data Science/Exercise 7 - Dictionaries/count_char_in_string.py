text_input = input().split()
dictionary = {}
for char in text_input:
    for c in char:
        if c not in dictionary:
            dictionary[c] = 0
        dictionary[c] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")