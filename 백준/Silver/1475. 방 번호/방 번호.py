import math
import sys

input = sys.stdin.readline

nums = [0] * 10

for i in input().strip():
    if i == '6' or i == '9':
        nums[6] += 1
    else:
        nums[int(i)] += 1
nums[6] = math.ceil((nums[6] + nums[9]) / 2)
nums[9] = 0
print(max(nums))
