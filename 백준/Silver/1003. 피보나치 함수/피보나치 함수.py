import sys

input = sys.stdin.readline

N = int(input())

nums = [int(input()) for _ in range(N)]
max_n = max(2, max(nums) + 1)  # 인덱스 에러 방지

zero_dp = [0] * max_n
one_dp = [0] * max_n

zero_dp[0] = 1
one_dp[1] = 1

for i in range(2, max_n):
    zero_dp[i] = zero_dp[i - 1] + zero_dp[i - 2]
    one_dp[i] = one_dp[i - 1] + one_dp[i - 2]

for n in nums:
    print(zero_dp[n], one_dp[n])