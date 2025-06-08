# Input1
# 10 7
# 1 3 5 7 9 11 13 15 17 19
# Input2
# 10 6
# 1 3 5 7 9 11 13 15 17 19
import sys

input = sys.stdin.readline

N, target = map(int, input().split())

arr = list(map(int, input().split()))
start = 0
end = N - 1
result = None
# mid가 바로 target일 수 있는  조건을 <=로 해줘야함
while start <= end:
    mid = (start + end) // 2
    if arr[mid] < target:
        start = mid + 1
    elif arr[mid] > target:
        end = mid - 1
    elif arr[mid] == target:
        result = mid
        break

print(result if result else "원소가 존재하지 않습니다.")
