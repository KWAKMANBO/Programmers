import sys

input = sys.stdin.readline

tc = int(input())


def binary_search(arr, target, length):
    start = 0
    end = length - 1
    result = -1
    while start <= end:
        mid = (start + end) // 2

        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            result = mid
            break

    return 1 if result != -1 else 0


for _ in range(tc):
    n1 = int(input())

    note1 = list(map(int, input().split()))

    n2 = int(input())

    note2 = list(map(int, input().split()))

    note1.sort()

    for i in note2:
        print(binary_search(note1, i, n1))
