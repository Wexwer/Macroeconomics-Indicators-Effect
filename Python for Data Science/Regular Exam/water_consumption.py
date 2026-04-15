count_of_days = int(input())

total_consumption = 0

if count_of_days <= 0:
    print(0)
else:

    for i in range(count_of_days):

        water_consumption = int(input())


        total_consumption += water_consumption
        print(total_consumption)

