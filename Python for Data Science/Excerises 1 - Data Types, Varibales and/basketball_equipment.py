annual_fee = int(input())

basketball_sneakers = annual_fee - (annual_fee * 0.40)
basketball_team =  basketball_sneakers - (basketball_sneakers * 0.20)
basketball =  (basketball_team * 1/4)
basketball_accessories =(basketball * 1/5)

total = annual_fee + basketball_sneakers +basketball_team + basketball + basketball_accessories
print(f"{total:.2f}")
