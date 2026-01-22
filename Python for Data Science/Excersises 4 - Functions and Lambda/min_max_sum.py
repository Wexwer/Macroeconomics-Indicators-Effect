def min_max_sum(nums):
    minimum =  min(nums)
    maximum = max(nums)
    subtract = sum(nums)

    print(f"The minimum number is {minimum}")
    print(f"The maximum number is {maximum}")
    print(f"The sum number is: {subtract}")




user_input = list(map(int, input().split()))

min_max_sum(user_input)