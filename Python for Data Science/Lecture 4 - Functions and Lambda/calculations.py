# * User input
operator = input()
num1 = int(input())
num2 = int(input())

# * Logic

def calculation(operation: str, number1: int, number2: int) -> int:
    if operation == "multiply":
        return number1 * number2
    elif operation == "divide":
        return number1 // number2
    elif operation == "add":
        return number1 + number2
    elif operation == "subtract":
        return number1 - number2

# * Print output
print(calculation(operator, num1, num2))