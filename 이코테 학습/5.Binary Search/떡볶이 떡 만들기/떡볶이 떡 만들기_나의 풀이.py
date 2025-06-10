# Input
# 4 6
# 19 15 10 17



# N의 범위는  0 <= N <= 1,000,000 (0~100만)
# M의 범위는  0 <= M <= 2,000,000,000 (0~20억)
# 시간 제한 2초
# 아래 알고리즘의 시간 복잡도는 O(NlogN)이므로
# 약 40,000,000번으로 파이썬은 1초당 약 10,000,000번의 연산을 수행하므로 시간초과될 확률이 높음
# 또한 커팅기의 길이는 떡 배열에 존재하지 않는 수로도 가능하니 틀린 풀이이다.

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
