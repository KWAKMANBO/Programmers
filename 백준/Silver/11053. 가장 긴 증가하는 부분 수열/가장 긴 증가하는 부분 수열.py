import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))


def bs(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] >= target:
            r = mid - 1
        else:
            l = mid + 1
    return l


answer = [nums[0]]
for i in range(1, N):
    if nums[i] > answer[-1]:
        answer.append(nums[i])
    else:
        idx = bs(answer, nums[i])
        answer[idx] = nums[i]
print(len(answer))
