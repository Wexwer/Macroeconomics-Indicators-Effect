input_number1 = int(input())
input_number2 = int(input())
input_number3 = int(input())

def sum_numbers(num1: int, num2: int) -> int:
    return num1 + num2

def subtract_numbers(s: int, num3: int) -> int:
    return s - num3

print(subtract_numbers(sum_numbers(input_number1, input_number2), input_number3))