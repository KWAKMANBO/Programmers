import sys
input = sys.stdin.readline

N, M = map(int, input().split())

trees = list(map(int, input().split()))

start = 0
end = max(trees)
result = 0
while start <= end:
    mid = (start + end) // 2
    length = sum([t - mid for t in trees if t > mid])
    # print(mid, length)
    if length < M:
        end = mid -1
    else:
        result = mid
        start = mid + 1
        if length == M:
            break

print(result)
