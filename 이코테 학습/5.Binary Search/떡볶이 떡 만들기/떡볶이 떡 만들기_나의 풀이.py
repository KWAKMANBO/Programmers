# Input
# 4 6
# 19 15 10 17

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

rices = list(map(int, input().split()))
rices.sort()

start = 0
end = len(rices) - 1
answer = 0

while start <= end:
    mid = (start + end) // 2
    cut_length = rices[mid]
    length = 0
    for r in rices:
        if r > cut_length:
            length += r - cut_length

    # 길이의 합이 목표보다 작다면
    # 길이의 합을 더 늘려야 하므로 작은 범위로 이동
    if length < M:
        end = mid - 1
    elif length > M:
        start = mid + 1
    else:
        answer = cut_length
        break
print(answer)
