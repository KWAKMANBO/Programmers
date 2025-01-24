import sys


def sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left_arr = sort(arr[:mid])
    right_arr = sort(arr[mid:])

    return merge(left_arr, right_arr)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


n = int(sys.stdin.readline())

lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))

lst = sort(lst)

for l in lst:
    print(l)
