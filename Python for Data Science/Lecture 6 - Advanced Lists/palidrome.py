from os.path import join

words = input().split(" ")
searched_word = input()

list = [w for w in words if ''.join(reversed(w)) == w]

print(list)
print(f"Found palindrome {list.count(searched_word)} times")