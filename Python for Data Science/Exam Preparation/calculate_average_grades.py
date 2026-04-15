
students = int(input())

total_grades = 0


for i in range(students):
    grades = float(input())
    total_grades += grades

average = total_grades / students

print(f"{average:.2f}")