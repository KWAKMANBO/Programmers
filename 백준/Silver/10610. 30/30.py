import sys


input = sys.stdin.readline

nums = list(input().strip())
nums.sort(reverse=True)

if '0' not in nums:
    print(-1)
else:
    s = sum(map(int, nums))
    if s % 3 == 0:
        print("".join(nums))
    else:
        print(-1)
