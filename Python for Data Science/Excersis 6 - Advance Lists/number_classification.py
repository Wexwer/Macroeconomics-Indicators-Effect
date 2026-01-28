
user_list = input().split(", ")

positive = []
negative = []
even = []
odd = []

nums = list((map(int, user_list)))
for n in nums:
    positive.append(n) if n >= 0 else None
    negative.append(n) if n < 0 else None
    even.append(n) if n % 2 == 0 else None
    odd.append(n) if n % 2 != 0 else None

positive = list(map(str, positive))
negative = list(map(str, negative))
even = list(map(str, even))
odd = list(map(str, odd))

postive_joint = ", ".join(positive)
negative_join = ", ".join(negative)
even_joint = ", ".join(even)
odd_joint = ", ".join(odd)

print(f"Positive: {postive_joint}")
print(f"Negative: {negative_join}")
print(f"Even: {even_joint}")
print(f"Odd: {odd_joint}")