import sys

input = sys.stdin.readline

N, K = map(int, input().split())
count = 0
while N >= K:
    if N == 1:
        break

    if N % K != 0:
        count += N - (N // K) * K
        N = (N // K) * K
    else:
        N //= K
        count += 1

if N > 1:
    count += (N -1)
    N = 1
print(count)
