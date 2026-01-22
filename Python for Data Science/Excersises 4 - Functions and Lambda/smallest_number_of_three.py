input_num1 = int(input())
input_num2 = int(input())
input_num3 = int(input())

def smallest(num1: int, num2: int, num3: int) -> int:
   return min(num1, num2, num3)

print(smallest(input_num1, input_num2, input_num3))