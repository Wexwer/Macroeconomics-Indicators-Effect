lenght_in_cm = int(input())
width_in_cm = int(input())
hight_in_cm = int(input())
percentange = float(input()) / 100

total_dimensions_in_liter = (lenght_in_cm * width_in_cm * hight_in_cm) / 1000
total_needed = total_dimensions_in_liter - (total_dimensions_in_liter * percentange)

print(f"{total_needed:.2f}")