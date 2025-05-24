# Input 1
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

#Input 2
# 2 4
# 7 3 1 8
# 3 3 3 4

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

result = 0
# 한 줄 씩 입력받아서 확인하기
for i in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result,min_value)

print(result)
