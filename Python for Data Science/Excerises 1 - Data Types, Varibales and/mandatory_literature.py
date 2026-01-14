number_of_pages = int(input())
page_per_hour = int(input())
number_of_days = int(input())

total_hours = number_of_pages // page_per_hour

total_hours_per_day = total_hours // number_of_days

print(f"{total_hours_per_day}")