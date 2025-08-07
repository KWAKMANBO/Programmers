import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
camps = [0] + list(map(int, input().split()))
dp[1] = camps[1]
dp[2] = camps[2]


def solve(n):
    if dp[n] != 0:
        return dp[n]

    dp[n] = max(solve(n - 1), solve(n - 2) + camps[n])
    return dp[n]
print(solve(N))