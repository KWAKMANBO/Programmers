import sys

B, N = map(str, sys.stdin.readline().rstrip().split())
N = int(N)

answer = 0

for i in range(len(B)):
    if ord(B[i]) >= 65:
        answer += (ord(B[i]) - 55) * N ** (len(B) - 1 - i)
    else:
        answer += int(B[i]) * N ** (len(B) - 1 - i)
print(answer)
