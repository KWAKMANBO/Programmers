import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

nums = [int(i) for i in sys.stdin.readline().rstrip().split()]

answer = []

for i in nums:
    if i < k:
        answer.append(i)

print(*answer)
