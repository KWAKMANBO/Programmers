import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
arr.sort()
answer = 0
for i in range(len(arr)):
    target = arr[i]
    left = 0
    right = len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s < target:
            left += 1
        elif s > target:
            right -= 1
        else:
            if i == left:
                left += 1
            elif i == right:
                right -= 1
            else:
                answer += 1
                break
print(answer)
