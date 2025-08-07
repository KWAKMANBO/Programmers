import sys

input = sys.stdin.readline

N = int(input())

camps = [0] + list(map(int, input().split()))

# N >=3 이므로
dp = [0] * (N + 1)

dp[1] = camps[1]
dp[2] = max(camps[2], dp[1])

for i in range(3, N + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + camps[i])

print(max(dp))
