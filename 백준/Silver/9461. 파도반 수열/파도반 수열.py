import sys

input = sys.stdin.readline

N = int(input())

nums = [int(input()) for _ in range(N)]

dp = [0] * 101

dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(3, max(nums) + 1):
    dp[i] = dp[i - 2] + dp[i - 3]

for n in nums:
    print(dp[n])
