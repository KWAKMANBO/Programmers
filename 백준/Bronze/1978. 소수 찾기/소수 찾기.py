import sys

n = int(sys.stdin.readline().rstrip())

nums = [int(i) for i in sys.stdin.readline().rstrip().split()]

answer = 0

for i in nums:
    tmp = 0
    for j in range(1, (i // 2) + 1):
        if i % j == 0:
            tmp += 1
    tmp += 1
    if tmp == 2:
        answer += 1

print(answer)
