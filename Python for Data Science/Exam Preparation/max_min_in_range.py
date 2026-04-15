# from math import inf
# index_numbers = list(map(int, input().split()))
# start_index = int(input())
# end_index = int(input())
# max_number = 0
# min_number = 0
# for i in range(start_index, end_index + 1):
#     if i < min_number:
#         min_control = i
#     if i > max_number:
#         max_number = i
#
#
# # print(f"{index_numbers[start_index]} {index_numbers[end_index]}")

index_numbers = list(map(int, input().split()))
start_index = int(input())
end_index = int(input())

min_number = index_numbers[start_index]
max_number = index_numbers[start_index]

for i in range(start_index, end_index + 1):  # +1 if you want inclusive
    if index_numbers[i] < min_number:
        min_number = index_numbers[i]
    if index_numbers[i] > max_number:
        max_number = index_numbers[i]

print(f"{min_number + max_number}")
