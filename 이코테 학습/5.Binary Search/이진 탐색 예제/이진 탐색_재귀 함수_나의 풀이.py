# Input1
# 10 7
# 1 3 5 7 9 11 13 15 17 19
# Input2
# 10 6
# 1 3 5 7 9 11 13 15 17 19

import sys

input = sys.stdin.readline


def binary_search(array, target, start, end):
    mid = (start + end) // 2

    if start > end:
        return None

    # array[mid]와 비교하므로 그다음 binary_serach를 실행할때 미드 인덱스는 포함 X
    if target < array[mid]:
        return binary_search(array, target, start, mid - 1)
    elif target > array[mid]:
        return binary_search(array, target, mid + 1, end)
    else:
        return mid


N, target = map(int, input().split())

arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, N - 1)
print(result if result else "원소가 존재하지 않습니다.")
