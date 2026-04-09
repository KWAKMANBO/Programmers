import sys

input = sys.stdin.readline

K = int(input())

MAX_K = 46
dp = [[0, 0] for _ in range(MAX_K)]
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, K+1):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

print(*dp[K])
