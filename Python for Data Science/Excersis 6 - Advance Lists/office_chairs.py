rooms = int(input())

free_chairs = 0
need_chairs = 0

for room in range(1, rooms + 1):
    chairs, visitors = input().split()
    visitors = int(visitors)

    diff = len(chairs) - visitors

    if diff >= 0:
        free_chairs += diff
    else:
        need_chairs += abs(diff)
        print(f"{abs(diff)} more chairs needed in room {room}")

if need_chairs == 0:
    print(f"Game On, {free_chairs} free chairs left")
