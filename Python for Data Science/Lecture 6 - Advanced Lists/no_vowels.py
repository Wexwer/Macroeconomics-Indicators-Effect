data = input()

vowels = ['a', 'e', 'i', 'o', 'u']

result = [d for d in data if d.lower() not in vowels]

result1 = "".join(result)
print(result1)