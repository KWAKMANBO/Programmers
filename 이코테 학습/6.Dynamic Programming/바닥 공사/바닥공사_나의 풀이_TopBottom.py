import sys

input = sys.stdin.readline

N = int(input())
blocks = [0] * 1001
dp = [0] * 1001
dp[1] = 1
dp[2] = 3


def solve(n):
    if dp[n] != 0:
        return dp[n]

    dp[n] = (solve(n - 2) * 2 + solve(n - 1)) % 796796
    return dp[n]


print(solve(N))
