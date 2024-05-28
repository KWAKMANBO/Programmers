import sys

n = int(sys.stdin.readline().rstrip())

answer = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    answer.append(a + b)

for i in range(n):
    print("Case #{}: {}".format(i + 1, answer[i]))
