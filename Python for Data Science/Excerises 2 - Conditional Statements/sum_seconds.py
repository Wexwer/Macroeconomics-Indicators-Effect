num1 = int(input())
num2 = int(input())
num3 = int(input())

total_time = num1 + num2 + num3

total_time_in_minutes = total_time // 60

total_time_in_seconds = total_time % 60

print(f"{total_time_in_minutes}:{total_time_in_seconds:02d}")