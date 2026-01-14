balance = 0
while True:
    entry = input()
    if entry == "End":
        break
    else:
        entry = float(entry)
        if entry >= 1:
            print(f"Increase: {entry:.2f}")
            balance += entry
        elif entry < 1:
            print(f"Decrease: {abs(entry):.2f}")
            balance += entry
print(f"Balance: {balance:.2f}")