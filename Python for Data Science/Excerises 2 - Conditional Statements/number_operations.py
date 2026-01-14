num1 = int(input())
num2 = int(input())
math_operator = input()

# if math_operator == "+":
#     print(f"{num1} {math_operator} {num2} = {num1 + num2:.2f}")
# elif math_operator == "-":
#     print(f"{num1} {math_operator} {num2} = {num1 - num2:.2f}")
# elif math_operator == "*":
#     print(f"{num1} {math_operator} {num2} = {num1 * num2:.2f}")
# elif math_operator == "/":
#     print(f"{num1} {math_operator} {num2} = {num1 / num2:.2f}")


operations = {
    "+": num1 + num2,
    "-": num1 - num2,
    "*": num1 * num2,
    "/": num1 / num2 if num2 != 0 else "error"
}

result = operations[math_operator]

print(result)