import sys

input = sys.stdin.readline

N = int(input())

city = list(map(int, input().split()))
money = int(input())

start = 1
end = max(city)
result = 0
idx = 1
while start <= end:
    mid = (start + end) // 2
    tmp = []
    for c in city:
        tmp.append(mid if c >= mid else c)

    if sum(tmp) > money:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
    idx += 1
print(result)
