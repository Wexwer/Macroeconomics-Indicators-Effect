n = int(input())
biggest = int(input()) # * we can use biggest_number = float('-inf') so we
# * can start with - inf # as everything is bigger than it

for _ in range(n - 1):
    num = int(input())
    if num > biggest:
        biggest = num

print(biggest)
