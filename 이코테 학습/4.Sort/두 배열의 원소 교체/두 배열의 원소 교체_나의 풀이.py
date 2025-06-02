import sys

# Input1
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5


input = sys.stdin.readline

N, K = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort(reverse=True)
i, j = 0, 0

for _ in range(K):
    if arr1[i] < arr2[j]:
        arr1[i], arr2[j] = arr2[j], arr1[i]
        i += 1
        j += 1
    elif arr1[i] > arr2[j]:
        j += 1

print(sum(arr1))
