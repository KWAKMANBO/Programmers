import sys

input = sys.stdin.readline

A, K = map(int, input().split())

dp = [0] * (K + 1)

for i in range(A + 1, K + 1):
    if i < A * 2:
        dp[i] = dp[i - 1] + 1
    elif i == 2 * A:
        dp[i] = 1
    else:
        if i % 2 == 0:
            dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)
        else:
            dp[i] = dp[i - 1] + 1


print(dp[K])
