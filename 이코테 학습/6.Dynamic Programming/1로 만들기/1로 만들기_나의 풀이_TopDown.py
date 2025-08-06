import sys

N = int(input())

dp = [0] * 30001


def solve(n):
    # 이미 계산 됐다면
    if dp[n] != 0:
        return dp[n]
    if n == 1:
        return dp[1]
    # 1을 빼는 연산은 기본연산
    dp[n] = solve(n - 1) + 1
    if n % 2 == 0:
        dp[n] = min(dp[n], solve(n // 2) + 1)
    if n % 3 == 0:
        dp[n] = min(dp[n], solve(n // 3) + 1)
    if n % 5 == 0:
        dp[n] = min(dp[n], solve(n // 5) + 1)

    return dp[n]


solve(N)
print(dp[N])
