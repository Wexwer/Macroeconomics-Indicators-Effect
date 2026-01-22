factor = int(input())
count = int(input())

list = []
factor1 = 0
for i in range(count):
    factor1 += factor
    list.append(factor1)

print(list)