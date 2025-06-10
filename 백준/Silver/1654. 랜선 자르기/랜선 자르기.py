import sys

input = sys.stdin.readline

K, N = map(int, input().split())

lans = [int(input()) for _ in range(K)]

start = 1
end = max(lans)
answer = 0
while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for lan in lans:
        cnt += lan // mid
    if cnt < N:
        # 줄의 개수가 적음 -> 잘게 조갬 -> 단위 길이를 높이기
        end = mid - 1
    else:
        # 줄의 개수가 많음
        answer = mid
        start = mid + 1


print(answer)

