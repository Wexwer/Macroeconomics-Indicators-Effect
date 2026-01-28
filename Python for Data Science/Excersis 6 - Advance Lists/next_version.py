input_version = list(map(int, input().split(".")))

input_version[2] += 1

if input_version[2] >= 10:
    input_version[2] = 0
    input_version[1] += 1
    if input_version[1] >= 10:
        input_version[1] = 0
        input_version[0] += 1

# * Mario Zahariev Answer
# * for i in range(2, 0, -1)
# *     if input_version[i] > 9:
#*          input_version[i] = 0
#*          input_version[i - 1 ] += 1

input_version = list(map(str, input_version))
result = ".".join(input_version)
print(result)