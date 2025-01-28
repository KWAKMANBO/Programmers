import sys

lst = []

n = int(sys.stdin.readline())

for i in range(n):
    age, name = sys.stdin.readline().strip().split()
    age = int(age)
    lst.append([age, name, i])

lst.sort(key=lambda x: (x[0], x[2]))

for i in lst:
    print(i[0], i[1])
