import sys

input = sys.stdin.readline

N = int(input())

# 포도주를 선택하면 무조건 마셔야함
# 연속으로 놓여 있는 3잔을 모두 먹을 수 없음

wines = [0]
dp = [0] * 10001

for _ in range(N):
    wines.append(int(input()))

if N >= 1:
    dp[1] = wines[1]
if N >= 2:
    dp[2] = wines[1] + wines[2]

for i in range(3, N + 1):
    # 1. i번째 와인을 마시지 않는 경우 그냥 그전의 최고값을 쓰기
    # 2. dp[i-3] + wines[i-1] + wines[i] 즉 연속으로 두잔을 선택하는 경우의수
    # 3. dp[i-2] + wines[i] 한잔 을 뛰어넘어서 선택하는 경우의수
    dp[i] = max(dp[i - 1], dp[i - 3] + wines[i - 1] + wines[i], dp[i - 2] + wines[i])

print(max(dp))
