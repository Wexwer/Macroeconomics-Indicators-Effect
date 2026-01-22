grade_input = float(input())

def in_range(n:float, low_limit: float, high_limit: float) -> bool:
    return low_limit <= n <= high_limit

def grade(num: float):
    if in_range(num, 2, 2.99):
        print("Fail")
    elif in_range(num, 3, 3.49):
        print("Poor")
    elif in_range(num, 3.50, 4.49):
        print("Good")
    elif in_range(num, 4.50, 5.49):
        print("Very Good")
    elif in_range(num, 5.50, 6.00):
        print("Excellent")

grade(grade_input)