import sys

input = sys.stdin.readline

N, K = map(int, input().split())
count = 0
while True:
    if N == 1:
        break

    if K != 1 and N % K == 0:
        N //= K
    else:
        N -= 1

    count += 1

print(count)
