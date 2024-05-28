import sys

a = -1
b = -1

answer = []

while a != 0 and b != 0:
    a, b = map(int, sys.stdin.readline().rstrip().split())
    answer.append(a + b)

for i in answer[:-1]:
    print(i)
