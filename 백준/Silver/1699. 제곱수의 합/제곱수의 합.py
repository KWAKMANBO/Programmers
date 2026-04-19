import sys

input = sys.stdin.readline

N = int(input())
dp = [i for i in range(N + 1)]

for i in range(1, N + 1):
    if int(i ** 0.5) == i ** 0.5:
        dp[i] = 1
    else:
        tmp = 1000000
        for j in range(1,int(i**0.5) + 1):
            tmp = min(tmp, dp[i-j**2])
        dp[i] = tmp + 1

print(dp[N])