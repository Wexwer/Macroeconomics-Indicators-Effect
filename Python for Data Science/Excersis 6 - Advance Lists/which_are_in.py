first_string = input().split(', ')
second_string =input().split(', ')

result = [w for w in first_string if any(w in target for target in second_string)]
# for i in first_string:
#     for target in second_string:
#         if i in target:
#             result.append(i)
#             break
print(result)