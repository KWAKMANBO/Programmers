# Input1
# 10 7
# 1 3 5 7 9 11 13 15 17 19
# Input2
# 10 6
# 1 3 5 7 9 11 13 15 17 19

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


N, target = map(int, input().split())

arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, N - 1)
print(result + 1 if result else "원소가 존재하지 않습니다.")
