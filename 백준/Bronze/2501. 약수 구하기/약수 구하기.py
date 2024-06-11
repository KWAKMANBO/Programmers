import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

answer = []
for i in range(1, n // 2 + 1):
    if n % i == 0:
        answer.append(i)

answer.append(n)
if k > len(answer):
    print(0)
else:
    print(answer[k - 1])
