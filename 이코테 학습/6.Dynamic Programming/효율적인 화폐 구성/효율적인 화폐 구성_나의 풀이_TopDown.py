# Input 1
# 2 15
# 2
# 3

# Input 2
# 3 4
# 3
# 5
# 7

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

coins = [int(input()) for _ in range(N)]

dp = [0] + [10001] * 10000


def solve(n):
    if n < 0:
        return 10001

    if dp[n] != 10001:
        return dp[n]

    for c in coins:
        dp[n] = min(dp[n], solve(n - c) + 1)

    return dp[n]


result = solve(M)

print(result if result != 10001 else -1)
