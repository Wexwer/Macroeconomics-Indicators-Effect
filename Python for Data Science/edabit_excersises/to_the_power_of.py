def calculate_exponent(num, exp):
    final_number = 1
    for _ in range(exp):
        final_number *= num
    print(final_number)
    return final_number

calculate_exponent(5, 5)
