def characters_in_range(char1, char2):
    start = ord(char1)
    end = ord(char2)

    result = []

    for i in range(start + 1 , end):
        result.append(chr(i))

    return ' '.join(result)

char1_input = input()
char2_input = input()

print(characters_in_range(char1_input, char2_input))