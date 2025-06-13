import sys

input = sys.stdin.readline

x, y = map(int, input().split())

start = 1
end = x
rate = y * 100 // x
result = -1
while start <= end:
    mid = (start + end) // 2

    new_x = x + mid
    new_y = (y + mid) * 100
    new_rate = new_y // new_x
    if new_rate > rate:
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)
