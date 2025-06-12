import sys

input = sys.stdin.readline

# N과 M 입력받기
N, M = map(int, input().split())

videos = list(map(int, input().split()))

start = max(videos)
end = sum(videos)

answer = 0

while start <= end:
    mid = (start + end) // 2

    cnt = 1
    tmp = 0

    for v in videos:
        if tmp + v > mid:
            tmp = 0
            cnt += 1
        tmp += v

    if cnt <= M:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)
