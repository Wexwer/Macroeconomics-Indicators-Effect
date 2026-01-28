n = int(input())
synonyms = {}

for i in range(n):
    word = input()
    s = input()

    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(s)

for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")