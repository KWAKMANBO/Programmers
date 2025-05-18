import sys

N = int(input())

nums = set(input().strip().split())
M = int(input())
lst = list(input().strip().split())

for l in lst:
    if l in nums:
        print(1)
    else:
        print(0)