elements = input().split(" ")
search_element = input().split(" ")

result = {}

while len(elements) != 0:
    key = elements.pop(0)
    value = elements.pop(0)
    result[key] = int(value)

for w in search_element:
    if w in result.keys():
        print(f"We have {result[w]} of {w} left")
    else:
        print(f"Sorry, we don't have {w}")

