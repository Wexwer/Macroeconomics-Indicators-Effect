def stutter(word):
    first = word[:2]
    print(f"{first}... {first}... {word}?")
    return word

stutter("incredible")