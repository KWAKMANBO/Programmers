import sys

a = -1
b = -1

answer = []

while True:
    try:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        answer.append(a + b)
    except:
        break

for i in answer:
    print(i)
