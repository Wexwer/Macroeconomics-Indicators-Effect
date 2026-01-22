cards = input().split()
shuffles = int(input())

for _ in range(shuffles):
    half = len(cards) // 2
    first_half = cards[:half]
    second_half = cards[half:]

    shuffled = []

    for i in range(half):
        shuffled.append(first_half[i])
        shuffled.append(second_half[i])

    cards = shuffled

print(cards)