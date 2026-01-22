user_input = input().split()

nums = [int(x) for x in user_input]

for i in range(len(nums)):
    nums[i] = -nums[i]

print(nums)