import sys

input = sys.stdin.readline

N = int(input())

blocks = [0] * 1001
dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2)% 796796

print(dp[N])
