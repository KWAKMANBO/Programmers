# N은 0 <= N <= 1,000,000
# M은 0 <= M <= 100,000
# 순챁탐색하면 1,000,000,000,00 => 순차 탐색은 사용X


# Input
# 5
# 8 3 7 9 2
# 3
# 5 7 9
import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
M = int(input())
targets = list(map(int, input().split()))
for t in targets:
    start, end = 0, len(nums) - 1
    flag = False
    while start <= end:
        mid = (start + end) // 2
        if t < nums[mid]:
            end = mid - 1
        elif t > nums[mid]:
            start = mid + 1
        else:
            flag = True
            break
    if flag:
        print("yes", end=" ")
    else:
        print("no", end=" ")
