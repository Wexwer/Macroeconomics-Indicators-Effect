def even_numbers(numbers):
   return list(filter(lambda x: x % 2 == 0, numbers))

num_input = list(map(int, input().split()))
print(even_numbers(num_input))

