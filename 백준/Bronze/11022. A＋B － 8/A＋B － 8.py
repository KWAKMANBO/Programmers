import sys

n = int(sys.stdin.readline().rstrip())

answer = []
A = []
B = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    A.append(a)
    B.append(b)
    answer.append(a + b)

for i in range(n):
    print("Case #{}: {} + {} = {}".format(i + 1, A[i], B[i], answer[i]))
