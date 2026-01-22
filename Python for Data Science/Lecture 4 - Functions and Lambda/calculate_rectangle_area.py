rectangle_width = int(input())
rectangle_height = int(input())

def calculate_rectangle_area(rectangle_width1: int, rectangle_height1: int) -> int:
    return rectangle_width1 * rectangle_height1

print(calculate_rectangle_area(rectangle_width, rectangle_height))