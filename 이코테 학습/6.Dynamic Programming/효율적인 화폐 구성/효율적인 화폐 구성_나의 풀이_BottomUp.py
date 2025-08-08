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

# 최대 10000원까지만 가능하므로 불가능한 값인 10001로 초기화
# 인덱스를 1부터 시작하기위해서 길이는 10001로 설정
dp = [0] + [10001] * 10000

for c in coins:
    # 작은 코인부터 순회하기
    for i in range(c, M + 1):
        if dp[i - c] != 10001:
            dp[i] = min(dp[i], dp[i - c] + 1)

print(dp[M] if dp[M] != 10001 else -1)
