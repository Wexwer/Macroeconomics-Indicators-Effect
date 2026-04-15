USD_TO_BGN = 1.57

cpu_price = float(input())
video_card_price = float(input())
ram_price = float(input())
ram_count = int(input())
discount = float(input())


video_card_price = video_card_price - ( video_card_price * discount )
cpu_price = cpu_price - ( cpu_price * discount )

total_price = cpu_price + video_card_price + (ram_price * ram_count)

total_price = total_price * USD_TO_BGN

print(f"Money needed - {total_price:.2f} leva.")