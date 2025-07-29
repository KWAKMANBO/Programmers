import sys

input = sys.stdin.readline

mod = 1000000000

N = int(input())


dp = [[0] * 101 for _ in range(101)]

for i in range(1, N + 1):
    dp[i][0] = 1

dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][0] = dp[i - 1][1]
        elif j == 9:
            dp[i][9] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[N])%mod)
