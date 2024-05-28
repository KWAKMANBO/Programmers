import sys

n = int(sys.stdin.readline().rstrip())

A = [int(i) for i in sys.stdin.readline().rstrip().split()]
B = [int(i) for i in sys.stdin.readline().rstrip().split()]

A.sort()
B.sort(reverse=True)

answer = 0

for i, j in zip(A, B):
    answer += i * j
print(answer)
