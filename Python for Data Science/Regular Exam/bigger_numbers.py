# USER INPUT
user_input = list(map(int, input().split()))
control_num = int(input())

# LOGIC
result = []

for i in user_input:

    if control_num < i:
        result.append(i)

# OUTPUT
result = " ".join(map(str, result))
print(result)

