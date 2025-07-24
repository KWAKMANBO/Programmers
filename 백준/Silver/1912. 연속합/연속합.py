import sys

input = sys.stdin.readline

N = int(input())

nums = [0] +  list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = max(nums[i], dp[i - 1] + nums[i])

print(max(dp[1:]))
