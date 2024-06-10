import sys

n = int(sys.stdin.readline().rstrip())

answer = 1
tmp = 1
while tmp < n:
    tmp += answer * 6
    answer += 1

print(answer)
