import sys

input = sys.stdin.readline

N, C = map(int, input().split())

home = [int(input()) for _ in range(N)]
home.sort()

start = 1
end = home[-1] - home[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    current_home = home[0]
    cnt = 1

    for i in range(1, len(home)):
        if home[i] >= current_home + mid:
            cnt += 1
            current_home = home[i]

    if cnt >= C:
        start = mid + 1
        answer = mid
    elif cnt < C:
        end = mid - 1

print(answer)
