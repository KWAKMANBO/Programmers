import sys

input = sys.stdin.readline

T = int(input())

dp = [[0] * 14 for _ in range(14)]

for i in range(1, 15):
    dp[0][i - 1] = sum([j for j in range(1, i + 1)])
    dp[i - 1][0] = 1

for i in range(1, 14):
    for j in range(1, 14):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]


for _ in range(T):
    a = int(input())
    b = int(input())
    print(dp[a-1][b-1])
