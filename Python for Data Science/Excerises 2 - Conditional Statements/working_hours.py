hour_of_day = int(input())
day_of_week = input()

if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday" or day_of_week == "Saturday":
    if hour_of_day == 10 or hour_of_day == 11 or hour_of_day == 12 or hour_of_day == 13 or hour_of_day == 14 or hour_of_day == 15 or hour_of_day == 16 or hour_of_day == 17 or hour_of_day == 18:
        print("open")
    else:
        print("closed")
else:
    print("closed")